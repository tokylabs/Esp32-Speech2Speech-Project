import os
from machine import Pin, SoftSPI
from sdcard import SDCard

# Configure SPI and SD card
spisd = SoftSPI(-1, miso=Pin(13), mosi=Pin(12), sck=Pin(14))
sd = SDCard(spisd, Pin(27))

# Mount SD card
vfs = os.VfsFat(sd)
os.mount(vfs, '/sd')
os.chdir("/sd")
print("Current directory:", os.getcwd())


"""
# Check current directory (should be the root of the ESP32 filesystem)
current_directory = os.getcwd()
print("Current directory on ESP32:", current_directory)

# Dictionary to hold file contents
file_contents = {}
current_list_dir = os.listdir()
print(current_list_dir)
try:
    # Iterate over files in the source directory
    for filename in current_list_dir:
        if filename == "sd" or filename == "lib":
            continue
        # Open the file on ESP32
        with open(filename, 'rb') as esp_file:
            file_content = esp_file.read()
            # Store file content in dictionary
            file_contents[filename] = file_content
        
        print("File '{}' stored in dictionary.".format(filename))

    # Change current directory to SD card
    os.chdir('/sd')
    print("Current directory on SD card:", os.getcwd())

    # Write files from dictionary to SD card
    for filename, content in file_contents.items():
        # sd_file_path = os.path.join('/sd', filename)
        # Write the content to the SD card
        with open(filename, 'wb') as sd_file:
            sd_file.write(content)
        
        print("File '{}' uploaded successfully.".format(filename))

except OSError as e:
    print("OS error:", e)

except Exception as e:
    print("Error:", e)

# Optionally, verify the files on the SD card
print("SD card contents after upload: {}".format(os.listdir()))
"""