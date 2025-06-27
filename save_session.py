from instagrapi import Client
import os
from dotenv import load_dotenv
from pathlib import Path

def create_session(client, username, password, session_path):
    client.login(username, password)
    client.get_timeline_feed()  # Simulate human behaviour
    client.dump_settings(session_path)
    print("✅ Logged in and session saved.")

def load_session(client, username, password, session_path):
    if Path(session_path).exists():
        client.load_settings(session_path)
        client.login(username, password) # this doesn't actually login using username/password but uses the session
        client.get_timeline_feed()  # Simulate human behaviour
        print("✅ Loaded session.")
    else:
        raise FileNotFoundError(f"Session file {session_path} not found.")
    
def main():
    load_dotenv()
    USERNAME = os.getenv("INSTAGRAM_USERNAME")
    PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
    session_path = "insta_session.json"
    print(USERNAME)
    print(PASSWORD)
    client = Client()
    # if you want to create a new session
    create_session(client, USERNAME, PASSWORD, session_path)
    
    # if you want to load a session 
    #load_session(client, USERNAME, PASSWORD, session_path)

if __name__ == "__main__":
    main()
