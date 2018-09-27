import requests
from flask import Flask
app = Flask(__name__)

# Fetch events from NUDLS
EVENTS = requests.get('https://dinoparks.net/nudls/feed').json()
