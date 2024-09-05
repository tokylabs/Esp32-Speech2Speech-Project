import usocket
import ssl

# fucction to convert text to speech using api: https://arbazkhan-cs-text-to-speech.hf.space/synthesize
def text_to_speech(text, audio_file_path="synthesized_audio.wav"):
    try:
        headers = (
            "POST /synthesize HTTP/1.1\r\n"
            "Host: arbazkhan-cs-text-to-speech.hf.space\r\n"
            "Content-Type: application/json\r\n"
            "X-Text: {}\r\n"
            "Content-Length: 0\r\n"
            "Connection: close\r\n"
            "\r\n"
        ).format(text)
                
        # Create a socket and connect to the server
        host = "arbazkhan-cs-text-to-speech.hf.space"
        port = 443
        addr = usocket.getaddrinfo(host, port)[0][-1]
        s = usocket.socket()
        s.connect(addr)
        
        # Wrap the socket with SSL for https and send headers
        s = ssl.wrap_socket(s)        
        s.write(headers.encode())
    
        # Receive and discard response headers
        while True:
            line = s.readline().decode()
            if not line or line == '\r\n':  # End of headers
                break
        
        # Receive the audio data in chunks and write to a file
        with open(audio_file_path, "wb") as f:
            while True:
                chunk = s.read(10024)  # Read chunks of fixed size
                if not chunk:
                    break
                f.write(chunk)

        print(f"Wav audio file saved as {audio_file_path}")

        # Close the socket
        s.close()
        return True
    
    except OSError as e:
        print("Network error:", e)
        return False

if __name__ == "__main__":
    print("Text Processing ...")
    text_to_speech("The minimum sampling rate is often called the Nyquist rate. For example, the minimum sampling rate for a telephone speech signal ")
