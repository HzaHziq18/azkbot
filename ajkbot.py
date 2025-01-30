from time import sleep
from mcprotocol import Client

# Minecraft Server Information
SERVER_IP = "katakana.aternos.me"
SERVER_PORT = 33395
USERNAME = "AFK_BOT"

# Connect to the Server
client = Client(SERVER_IP, SERVER_PORT, username=USERNAME)

# Keep the Bot Online
print("AFK Bot is now running...")
while True:
    client.send_chat_message("I'm still here!")  # Sends a message every 5 minutes
    sleep(300)  # Waits for 5 minutes before sending again
