import json
import requests
from flask import Flask, jsonify
from flask_restful.reqparse import RequestParser
from events import EVENTS
from simulator import Simulator


app = Flask(__name__)


@app.route('/dinopark/state/', methods=['GET'])
def get_park_state():
    """Retrieve current state of park.
    """
    parser = RequestParser()
    parser.add_argument('time', type=str, required=True, location='args')
    args = parser.parse_args()
    # create park simulator to get latest state of park
    simulator = Simulator()
    time = args['time']
    # Fetch events from NUDLS
    for event in EVENTS:
        if event['time'] <= time:
            # mutate state if event relavent
            simulator.handle(event)
    # Get final park state calculated by simulator
    result = json.dumps(simulator.get_park_state(time))
    return result
