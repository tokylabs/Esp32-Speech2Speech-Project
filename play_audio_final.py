from machine import I2S, Pin  # Import I2S and Pin modules for audio output and pin control

# Function to play a WAV audio file using I2S
def play_audio(wav_file, sample_rate_in_hz=7000):
    # Define pins for the I2S interface
    bck_pin = Pin(26)  # Bit clock pin
    ws_pin = Pin(25)   # Word select pin / LRC pin
    sdout_pin = Pin(22)  # Serial data out pin / din pin

    # Configure the I2S interface for audio output
    audio_out = I2S(
        1,  # I2S peripheral number
        sck=bck_pin,
        ws=ws_pin,
        sd=sdout_pin, 
        mode=I2S.TX,  # Set mode to transmit (output)
        bits=16,  # Data bit width
        format=I2S.STEREO,  # Audio format (stereo)
        rate=sample_rate_in_hz,  # Sampling rate
        ibuf=5000  # Internal buffer size
    )

    # Open the WAV file for reading
    wav = open(wav_file, 'rb')

    # Skip the WAV header (first 44 bytes) to reach the audio data
    wav.seek(44)

    # Prepare a buffer to store audio samples
    wav_samples = bytearray(2048)  # Buffer size of 2048 bytes
    wav_samples_mv = memoryview(wav_samples)  # Memory view for efficient slicing

    print('Starting')
    try:
        # Loop to read and play audio data
        while True:
            num_read = wav.readinto(wav_samples_mv)  # Read audio data into buffer
            if num_read == 0:
                break  # Stop when no more data is available
            num_written = 0
            while num_written < num_read:
                # Write audio data to I2S output
                num_written += audio_out.write(wav_samples_mv[num_written:num_read])
    except (KeyboardInterrupt, Exception) as e:
        # Handle interruptions or errors
        print(f'Caught exception {type(e).__name__}: {e}')
    
    # Clean up resources
    wav.close()  # Close the WAV file
    audio_out.deinit()  # Deinitialize the I2S interface
    print('Done')

if __name__ == "__main__":
    # Play the specified audio file
    play_audio("synthesized_audio.wav")
