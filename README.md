# Tokymakers ESP32 Voice-Controlled Assistant

This project demonstrates how to create a voice-controlled assistant using the ESP32 microcontroller. The assistant captures audio, converts it to text, generates a response using an AI language model, converts the response back to speech, and plays the synthesized audio. The functionality is similar to that of smart assistants like Alexa.

## Table of Contents

- [Overview](#overview)
- [File Structure](#file-structure)
- [Requirements](#requirements)
- [Setup and Configuration](#setup-and-configuration)
- [Usage](#usage)
- [Additional Notes](#additional-notes)
- [License](#license)

## Overview

The project consists of the following steps:

1. **Record Audio**: Captures audio from a microphone and saves it as a raw audio file.
2. **Speech-to-Text**: Converts the recorded audio to text using a speech-to-text API.
3. **Text Generation**: Generates a response based on the converted text using a language model API.
4. **Text-to-Speech**: Converts the generated response to speech and saves it as a WAV file.
5. **Play Audio**: Outputs the synthesized audio through a speaker.

## File Structure

- **`record_audio_final.py`**: Handles recording audio from a microphone.
- **`play_audio_final.py`**: Manages playback of audio files using the I2S interface.
- **`speech_to_text.py`**: Converts audio input to text using a speech-to-text API.
- **`llm.py`**: Generates responses using the Groq API or another language model API.
- **`text_to_speech.py`**: Converts the generated text responses into speech.
- **`app.py`**: Orchestrates the overall process from recording to response.
- **`config.py`**: Stores API keys and configuration settings.

## Requirements

### Hardware
- **ESP32**: Microcontroller with at least 2MB flash memory for smooth operation.
- **MAX98357A**: Digital-to-analog audio amplifier.
- **INMP441**: I2S digital microphone.

### Software
- **MicroPython**: Installed on the ESP32.
- **Python Dependencies**: `requests` library for API calls.

## Setup and Configuration

1. **Flash/Reset ESP32**: Factory Reset Your ESP32 BOARD.
   - Connect your ESP32 with your computer
   - Step 1: Go to [Flash/Reset ESP32](https://espressif.github.io/esptool-js/)
   <img src="./StepsForConfiguration/Step 1.PNG">
   - Step 2: Select 115200 in Program Baudrate and click on connect
   <img src="./StepsForConfiguration/Step 2.PNG">
   - Step 3: Select your USB connected port and click on connect
   <img src="./StepsForConfiguration/Step 3.PNG">
   - Step 4: You can see the connection process on the terminal
   <img src="./StepsForConfiguration/Step 4.PNG">
   - Step 5: Now press and hold the boot button of ESP32, press and release the EN/Reset Button of ESP32, Now release the boot button. Now ESP32 will be connected
   <img src="./StepsForConfiguration/Step 5.PNG">
   - Step 6: Now click on Erase Flash Button
   <img src="./StepsForConfiguration/Step 6.PNG">
   - Step 7: Now it will take a while to Flash it so wait for it
   <img src="./StepsForConfiguration/Step 7.PNG">
   - Step 8: Now go to [Download Reset File](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbnQ1T0pmalFPamxpY2xZdnVPNE9QX3JiQzNrZ3xBQ3Jtc0trMkJUOE1JQTJhcllFMUNfVU5hRmJBTUZxVV9mTHhBeFhKbkt5SEJvMVBOV2RMc1RaYlB6N1JHaTRkY2oyWDUwNjFXUG9rNF9JcXUzZGg2RjR1VGdjdlpjb1B3UUNKdWRoSmYzRVk3WEstcXJuS05pOA&q=https%3A%2F%2Fgithub.com%2Fitsbhupendrasingh%2FESP32-Factory-Reset-S2-and-bootloader%2Fraw%2FMaster%2FFactory_Reset_And_Bootloader_Repair.bin&v=3oEvXhgHZHo) and download it.
   - Step 9: Now in Falash Adress make it 0x0000 and upload the downloaded file and click on Program
   <img src="./StepsForConfiguration/Step 8.PNG">
   - Step 10: Now it will take a while to factory reset the ESP32
   - Congratulation your ESP32 is now Factory Reset Now you can disconnect your ESP32 with Your Computer.
   <img src="./StepsForConfiguration/Step 9.PNG">

1. **Install MicroPython**: Flash MicroPython onto your ESP32.
   - You can follow [this guide](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html) for installation instructions.

2. **Install Python Dependencies**: Install the `requests` library on the ESP32 using `upip`:
   ```bash
   upip install requests

3. **Connect Hardware**

   - **MAX98357A**: Connect to the ESP32 for audio output.
   - **INMP441**: Connect to the ESP32 for audio input.

5. **Configure API Keys**: Open config.py and insert your API keys for the speech-to-text and text generation services.

6. **Upload Files to ESP32**: Transfer all Python scripts to your ESP32 using an IDE like Thonny or ampy.

## Usage
1. **Run the Application**: Execute app.py to start the voice-controlled assistant.
    - The assistant will listen for your voice command, process it, and respond accordingly.

2. **Troubleshooting**:

    - Ensure all hardware components are correctly connected.
    - Verify API key configurations in config.py.
    - Test each script individually to isolate any issues.


## Contributing
We welcome contributions from the community! If you'd like to contribute, feel free to submit a pull request or report any issues. We're happy to work with you to improve the project.
