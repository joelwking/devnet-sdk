#!/usr/bin/env python3
#
#      Copyright (c) 2020 World Wide Technology, LLC.
#      All rights reserved.
#
#      author: joel.king@wwt.com GitHub/GitLab @joelwking
#
#      description: 
#
#        This playbook loads file(s) to AWS S3 buckets
#
#      usage: EXPORT 

import json
import os
import httplib
import requests
import time
from flask import Flask
from flask import request

RATE_LIMIT_RETRY = os.getenv('RATE_LIMIT_RETRY', 5)
VALIDATOR = os.getenv('VALIDATOR','7e91a1a5089a5fcb6f3ac05cbd7d166a6d7ae521')
WEBEX_HOST = os.getenv('WEBEX_HOST', 'https://webexapis.com/')
BOT_EMAIL = os.getenv('BOT_EMAIL', 'joelwking@webex.bot')

class Message(object):

    def __init__(self):

class Connection(object):

    def __init__(self):

        self.HEADERS = {"Content-Type": "application/json"}
        self.RATE_LIMIT_EXCEEDED = (429, )

    def debug(self, msg=""):
        """
        """
        print(f'{time.asctime()} : {msg}')

    def rate_limit(self, verb, url, **kwargs):
        """
        Returns the requests object to the calling method. Calling method to catch ConnectionError exceptions.
        """

        for _ in range(RATE_LIMIT_RETRY):

            try:
                r = requests.requests(verb, url, **kwargs)
            except requests.ConnectionError as e:
                self.debug(msg=str(e))
                return None

            if r.status_code == self.RATE_LIMIT_EXCEEDED:
                time.sleep(int(r.headers.get("Retry-After"), 1))
            else:
                return r
        return r

    

    def list_hooks(self):
        """
            List the Webhooks currently defined
              "items": [
                {
                  "id": "Y2lzY29zcGFyazovL3VzL1dFQkhPT0svM2EzODkzYTQtODJiOC00MTMwLTk4NDAtYWI4ZjkwZjAzYmY0",
                  "name": "Spark Learning Lab WebhookJOELKING",
                  "targetUrl": "http://ec2-52-25-224-165.us-west-2.compute.amazonaws.com:8080",
                  "resource": "messages",
                  "event": "created",
                  "filter": "roomId=Y2lzY29zcGFyazovL3VzL1JPT00vZDkyNmMyYzAtYTc3MC0xMWU1LWE4ZmUtMTFhZDZmODhjZmVj",
                  "orgId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi9udWxs",
                  "createdBy": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS82ZjFkYzk1ZS05MjYwLTQ5ZDMtYThjMS1lZTY4Y2I1MTVjYzQ",
                  "appId": "Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OL251bGw",
                  "status": "active",
                  "created": "2016-01-22T16:41:42.208Z"
                },
        """
        response = self.rate_limit('GET', f'{WEBEX_HOST}/v1/webhooks', headers=self.HEADERS)
        
        if response:
            return response.json().get('items', [])


    def register(self):
        # register
        POSt /v1/webhooks
        {
          "name": "My Awesome Webhook",
          "targetUrl": "https://example.com/mywebhook",
          "resource": null,
          "event": null,
          "filter": "roomId=Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
          "secret": "86dacc007724d8ea666f88fc77d918dad9537a15"
        }





def main():
    """
        https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request
        https://developer.webex.com/docs/api/guides/webhooks
        https://developer.webex.com/blog/spark-bot-demo

    """

    app = Flask(__name__)

    validator = '7e91a1a5089a5fcb6f3ac05cbd7d166a6d7ae521'

    @app.route("/", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
    def api_echo():
        if request.method == 'GET':
            return VALIDATOR

        elif request.method == 'POST':
            return "ECHO: POST\n"

        elif request.method == 'PATCH':
            return "ECHO: PATCH\n"

        elif request.method == 'PUT':
            return "ECHO: PUT\n"

        elif request.method == 'DELETE':
            return "ECHO: DELETE"    


        app.run(ssl_context='adhoc', host='0.0.0.0', port=8443, debug=True)


if __name__ == '__main__':

    main()




