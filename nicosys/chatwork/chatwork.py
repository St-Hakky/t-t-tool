# -*- encoding: utf-8 -*-

from __future__ import print_function, unicode_literals
import requests
import pprint
import json
import codecs
import random
import os

class Chatwork:
    def __init__(self, APIKEY, ENDPOINT, ROOMID):
        self.api = APIKEY
        self.endpoint = ENDPOINT
        self.roomid = ROOMID
        self.headers = {'X-ChatWorkToken': APIKEY}

    def getRooms(self):
        get_rooms_url = '{}/rooms'.format(self.endpoint)
        resp = requests.get(get_rooms_url,
                            headers=self.headers)
        return(resp.content)

    def getRoomMembers(self):
        get_room_members_url = '{}/rooms/{}/members'.format(self.endpoint, self.roomid)
        resp = requests.get(get_room_members_url,
                            headers=self.headers)
        return(resp.content)

    def getMe(self):
        get_me_url = '{}/me'.format(self.endpoint)
        resp = requests.get(get_me_url,
                            headers=self.headers)
        return(resp.content)

    def sendMessage(self, message):
        post_message_url = '{}/rooms/{}/messages'.format(self.endpoint, self.roomid)
        params = { 'body': message }
        resp = requests.post(post_message_url,
                            headers=self.headers,
                            params=params)
        return(resp.content)

def getText(file_path):
    f = open(file_path, "r")
    lines = []
    for row in f:
        lines.append(row)
    return(lines)

if __name__ == "__main__":

    with open('./key.json') as data_file:
        data = json.load(data_file)
    APIKEY = data["APIKEY"]
    ENDPOINT = data["ENDPOINT"]
    ROOMID = data["ROOMID"]

    chatwork = Chatwork(APIKEY, ENDPOINT, ROOMID)
    room_members = json.loads(chatwork.getRoomMembers().decode("utf-8"))
    me = json.loads(chatwork.getMe().decode("utf-8"))
    message = ""
    for i in room_members:
        if me["account_id"] != i["account_id"]:
            message += "[To:" + str(i["account_id"]) + "] " + i["name"]
            message += os.linesep
    lines = getText("./sample-text/alert_susida.txt")
    message += random.choice(lines).replace("|", os.linesep)
    chatwork.sendMessage(message)
