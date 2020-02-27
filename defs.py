import os
import json
import spreadsheet
import random
import Classes as c

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

def formatStats(stats):
    winp = str(round(float(stats[2])/float(stats[1])*100,3)) + "%"  if stats[1] != 0 else "0.00%"
    fin = "Name: " + stats[0] + "\nGames Played: " + stats[1] + "\nWin: " + winp + "\nDrinks: " + stats[3]
    return fin


def parse_data(data):
    
    txt = data['text'].lower()

    if(txt.find('!stats ') == 0):
        play = c.Player(txt[7:])
        stats = play.getStats()
        msg = formatStats(stats)
        send_message(msg)
    elif(txt.find("!game ") == 0):
        gme = c.Game(txt[6:])
        gme.gameUpdate()
        del gme
        msg = "apex!\ngame logged sucessfully"
        send_message(msg)
    elif(txt.find("!lead") == 0):
        msg = spreadsheet.showLeaderboard()
        send_message(msg)
    elif(txt.find("!racks -f") == 0):
        msg = spreadsheet.showRacks(True)
        send_message(msg)
    elif(txt.find("!racks") == 0):
        if (len(txt) > 6):
            play = c.Player(txt[7:])
            play.setRacks()
            msg = "Updated!\nRacks purchased this season: " + str(play.getRacks())
        else:
            msg = spreadsheet.showRacks()
        send_message(msg)
    elif(txt.find("!compare ") == 0):
        msg = spreadsheet.comparePlayers(txt[9:])
        send_message(msg)
        return 0
    elif(txt.find("!add ") == 0):
        plrname = txt[5:]
        spreadsheet.addPlayer(plrname)
        send_message(plrname + " added!")
    elif(txt.find("!miami") == 0):
        phrase = ["apex!","hookah vibes", "broo"]
        send_message(phrase[random.randint(0,2)])
    elif(txt.find("!jewtax") == 0):
        msg = "It's not a jew tax... You just pay more because you are jewish"
        send_message(msg)
    elif(txt.find("!drinks") == 0):
        msg = spreadsheet.getTotalDrinks()
        send_message(msg)

    else:
        return 0

def send_message(msg):
    url = 'https://api.groupme.com/v3/bots/post'

    data = {
        'bot_id' : os.getenv('BOT_KEY'),
        'text' : msg
        }
    request = Request(url, urlencode(data).encode())
    urlopen(request).read().decode()  
