from machine import I2S, Pin  # Import I2S and Pin modules for audio input and pin control
import time  # Import time module for managing recording duration

# Function to record audio using I2S and save it to a file
def record_audio(file_path, sck_pin_number=18, ws_pin_number=19, sd_pin_number=5, record_duration_ms=3000, buffer_size=2048, mode=I2S.RX, bits=16, format=I2S.MONO, rate=16000, ibuf=8096):
    """Record audio from the I2S microphone and save it to a file."""
    
    # Setup I2S pins for audio input
    sck_pin = Pin(sck_pin_number)  # Serial Clock pin
    ws_pin = Pin(ws_pin_number)    # Word Select pin
    sd_pin = Pin(sd_pin_number)    # Serial Data input pin
    
    # Configure the I2S interface for receiving audio data
    audio_in = I2S(
        0,  # I2S peripheral number
        sck=sck_pin,
        ws=ws_pin,
        sd=sd_pin,
        mode=mode,  # Set mode to receive (input)
        bits=bits,  # Data bit width
        format=format,  # Audio format (mono)
        rate=rate,  # Sampling rate
        ibuf=ibuf  # Internal buffer size
    )
    
    print(f"Recording for {record_duration_ms / 1000} seconds")

    # Create a buffer for audio data
    samples = bytearray(buffer_size)  # Buffer size of 2048 bytes
    start_time = time.ticks_ms()  # Record the start time

    # Open the specified file to write the recorded audio data
    with open(file_path, "wb") as file:
        while time.ticks_diff(time.ticks_ms(), start_time) < record_duration_ms:
            # Read audio data into the buffer
            read_bytes = audio_in.readinto(samples)
            # Write the read data to the file
            file.write(samples[:read_bytes])
    
    print("Finished Recording")

if __name__ == "__main__":
    record_audio("test.raw")  # Record audio and save it as "test.raw"
