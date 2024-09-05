import requests

# function for convert speech to text using api: https://arbazkhan-cs-speech-to-text.hf.space/transcribe
def speech_to_text(file_path, url="https://arbazkhan-cs-speech-to-text.hf.space/transcribe", chunk_size=12024):
    # Initial header indicating the upload is ongoing
    headers = {'X-Complete': 'false'} 
    
    with open(file_path, 'rb') as f:
        while True:
            # Read the file in chunks
            chunk = f.read(chunk_size)  
            if not chunk:
                break  # Exit the loop when no more data to read
                
            # Send chunk to the server
            response = requests.post(url, data=chunk, headers=headers)  
            if response.status_code != 200:
                print(f"Error: {response.json()}") 
                return None
            print(response.json())  # Print server's response for each chunk
    
    headers['X-Complete'] = 'true'  # Mark the upload as complete
    response = requests.post(url, data=b'', headers=headers)  # Send final request to complete transcription
    json_response = response.json()
    print(json_response)  # Print the final transcription result
    return json_response['transcript']  # Return the transcript

if __name__ == "__main__":
    audio_file_path = 'recorded_audio.raw'  # Path to the audio file
    speech_to_text(audio_file_path)  # Call the function to process the audio
