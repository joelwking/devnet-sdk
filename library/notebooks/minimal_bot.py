#!/usr/bin/env python3
#
#      Copyright (c) 2020 World Wide Technology, LLC. All rights reserved.
#
#      author: joel.king@wwt.com GitHub/GitLab @joelwking
#      description:  Minimal Webex Bot for DevNet Associate Study Group
#
#      usage: EXPORT BOT_ACCESS_TOKEN=12345678
#             python3 ./minimal_bot.py

import json, os, requests, pprint
from flask import Flask, request

bot_access_token = os.getenv('BOT_ACCESS_TOKEN', '12345')
bot_port = os.getenv('BOT_PORT', 8443)

WEBEX_HOST = 'https://webexapis.com/'
HEADERS = {"Content-Type": "application/json"}
HEADERS['Authorization'] = 'Bearer {}'.format(bot_access_token)      # Add the token to the header
BOT_DOMAIN= '@webex.bot'

def send_message(room, message='Nice talking with you!'):
    " Send a message to a room "
    message_body = dict(roomId=room, text=message)
    return requests.request('POST', '{}/v1/messages'.format(WEBEX_HOST), data=json.dumps(message_body), headers=HEADERS)

def get_message(id):
    " Get a message from a room based on the message ID "
    return requests.request('GET', '{}/v1/messages/{}'.format(WEBEX_HOST, id), headers=HEADERS)

def main():
    " Main Logic "
    app = Flask(__name__)

    @app.route("/", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
    def webhooks():

        if request.method == 'POST':
            pprint.pprint(request.json)                              # Print data provided by webhook
            message = get_message(request.json['data']['id'])        # Get the message which triggered the webhook

            if not BOT_DOMAIN in message.json()['personEmail']:      # Don't talk to yourself
                print(send_message(request.json['data']['roomId']))
            return "ECHO: POST:\n"

        elif request.method == 'GET':
            return "ECHO: GET\n"
        elif request.method == 'PATCH':
            return "ECHO: PATCH\n"
        elif request.method == 'PUT':
            return "ECHO: PUT\n"
        elif request.method == 'DELETE':
            return "ECHO: DELETE"

    app.run(ssl_context='adhoc', host='0.0.0.0', port=bot_port, debug=True)

if __name__ == '__main__':
    main()
