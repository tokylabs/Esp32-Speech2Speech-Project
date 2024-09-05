import network
import utime
from config import credentials

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)
    wlan.active(True)
    if not wlan.isconnected():
        print(f'Connecting to network...{ssid}')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print(wlan.isconnected())
    print('network config:', wlan.ifconfig())

if __name__=="__main__":
    # Replace with your Wi-Fi credentials
    ssid = credentials.get("ssid")
    password = credentials.get("password")
    connect_to_wifi(ssid, password)