import spreadsheet as sh
import defs
import re
import math

sheet = sh.client.open("BD statslog").sheet1

class Player:
    name = ""
    row = 0
    games = 0
    wins = 0
    drinks = 0
    racks = 0
    args = None

    #defaul constructor
    def __init__(self,playerinit):
        if(isinstance(playerinit,str)):
            self.name = playerinit
        else:
            self.args = playerinit
            self.name = self.args[0]
        self.row = self.getPlayerRow(self.name)
        self.games = int(sheet.cell(self.row,2).value)
        self.wins = int(sheet.cell(self.row,3).value)
        self.drinks = int(sheet.cell(self.row,4).value)
        self.racks = int(sheet.cell(self.row,5).value)

        
    def getPlayerArgs(self,argstring):
        args = argstring.split(" ")
        return args
    
    def getPlayerRow(self,player):
        rnum = sheet.col_values(1).index(player)
        return rnum + 1

    def getRow(self):
        return self.row

    def getStats(self):
        return sheet.row_values(self.row)

    def updateStat(self,col,val):
        sheet.update_cell(self.row,col,val)
        return 0

    def getGames(self):
        return self.games
    
    def setGames(self,games = 1):
        self.games += games
        self.updateStat(2,self.games)
        return 0

    def getWins(self):
        return self.wins

    def setWins(self,wins = 1):
        self.setGames()
        self.wins += wins
        self.updateStat(3,self.wins)
        return 0
    
    def getDrinks(self):
        return self.drinks

    def setDrinks(self,drinks):
        self.drinks += drinks
        self.updateStat(4,self.drinks)
        return 0
    
    def getRacks(self):
        return self.racks

    def setRacks(self,racks = 1):
        self.racks += racks
        self.updateStat(5,self.racks)
        return 0

    def PostGame(self,drinks,win = False):
        if(win):
            self.setWins()
        else:
            self.setGames()
        self.setDrinks(drinks)
        return 0
    
    def getWinPercent(self):
        return round(float(self.getWins())/float(self.getGames()),2)

class Game:
    winner = []
    loser = []
    drinks = None

    def __init__(self,initstring):
        args = initstring.split(" ")
        team1 = [args[0],args[1]]
        team2 = [args[3],args[4]]
        for play in team1:
            self.winner.append(Player(play))
        for play in team2:
            self.loser.append(Player(play))
        self.drinks = [args[2],args[5]]

    def gameUpdate(self):
        for player in self.winner:
            player.PostGame(int(self.drinks[0]),True)
        for player in self.loser:
            player.PostGame(int(self.drinks[1]))
        return 0

class Roster:
    players = []

    def __init__(self):
        pnames = sheet.col_values(1)
        for play in pnames:
            self.players.append(Player(play))
