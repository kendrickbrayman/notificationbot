import gspread
import defs

from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("BD statslog").sheet1

 

def addPlayer(player):
    sheet.append_row([player,0,0,0,0])
    return 0

def sortElem(elem):
    return elem[0]

def showRacks(full = False):
    rows = len(sheet.col_values(1)) - 1
    out = "Rack Purchase Leaderboard: "
    data = []
    for i in list(range(2,rows)):
        data.append((int(sheet.cell(i,5).value),sheet.cell(i,1).value))
    data.sort(reverse = True, key = sortElem)
    if full:
        places = len(data)
    else:
        places = 7
    for i in range(0,places):
        out += "\n" + str(data[i][0]) + " -- " + data[i][1]
    return out

def getTotalDrinks():
    dvals = sheet.col_values(4)[1:]
    total = sum(int(i) for i in dvals )
    out = "Total beers condumed: " + str(total) + "\nThat's " + str(round(float(total/30),1)) + " racks worth $" + str(round(float(total*0.05),2)) + " in deposits"
    return out

def showLeaderboard(full = False):
    rows = len(sheet.col_values(1)) - 1
    out = "Win Rate Leaderboard: "
    data = []
    minGames = 5
    for i in list(range(2,rows)):
        if(int(sheet.cell(i,2).value) > minGames):
            data.append((round(int(sheet.cell(i,3).value)/int(sheet.cell(i,2).value),2),sheet.cell(i,1).value))
    data.sort(reverse = True, key = sortElem)
    if full:
        places = len(data)
    else:
        places = 3
    for i in range(0,places):
        out += "\n" + str(data[i][1]) + " -- " + str(data[i][0]) + "%"
    return out

def comparePlayers(pstring):
    import Classes as c
    players = pstring.split(" ")
    p1 = c.Player(players[0])
    p2 = c.Player(players[1])
    out = "Player Comparison: \n\n"
    out += p1.name + ":\n" + str(p1.getWinPercent()) + "% winrate\n" + str(p1.getDrinks()) + " drinks\n" + str(p1.getRacks()) + " racks purchased\n\n"
    out += p2.name + ":\n" + str(p2.getWinPercent()) + "% winrate\n" + str(p2.getDrinks()) + " drinks\n" + str(p2.getRacks()) + " racks purchased"
    return out