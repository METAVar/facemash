"""
@author: abhijeet vaidya
@contact: abhijeetavaidya@gmail.com
@license: MIT license
"""
import math
import random
from operator import itemgetter

class Facemash(object):
    #define attributes
    
    k_factor = 0
    random_player_1 = 0
    random_player_2 = 0
    expected = 0
    
    def getExpectedChances(self,scoreOfPlayer2,scoreOfPlayer1):
        
        return 1/(1+math.pow(10,(scoreOfPlayer2-scoreOfPlayer1)/400)) # Elo-Rating system
    
    
    def getWinnerScore(self,score):
        
        return score+ self.k_factor*(1-self.expected)
        
    
    def getLoserScore(self,score):
        
        return score+ self.k_factor*(0-self.expected)
           
    
    def determineKfactor(self,winnerRank):
        
        if winnerRank < 1600:
            self.k_factor = 32
        elif winnerRank >= 1600 and winnerRank < 1800:
            self.k_factor= 24
        else:
            self.k_factor = 16
        return self.k_factor
    
    def generateRandomPlayer(self):
        self.random_player_1 = random.randint(1,10)
        self.random_player_2 = random.randint(1,10)
    
    def testForEquality(self): # check if both the players are same if same re-shuffle untill they aren't same
        # call function
        self.generateRandomPlayer()
        while self.random_player_1 == self.random_player_2: 
            # i want to re-shuffle
            self.generateRandomPlayer()
        pass
    
    def calculate(self):
        # just simulates 10 player result in the tournament
        players = {}
        playerStastistics = {}
        
        
        # creating 10 players
        for init in range(1,11,1):
            play = "players_"+str(init)
            players[init] = play
        
        # see which player has been selected
        
        # for a specific player to create won ,loss and score with default:1600
        for init1 in range(1,11,1):
            stat = {'won':0,'loss':0,'score':1600,'played':0}
            play = "players_"+str(init1)
            playerStastistics[play] = stat       
        
        #game method
        game = 0
        while game!=10:
            self.testForEquality()
            player1 = self.random_player_1
            player2 = self.random_player_2
            # choose random event to win
            test = random.randint(1,2)
            if test % 2 == 0:
                winner = player1
                losser = player2
                
            else:
                winner = player2
                losser = player1        
            
            
            win = players[winner]
            loose = players[losser]
            print "********************Game Tournament"+" "+str(game+1)+"***************************"
            print "The game was between "+str(players[player1])+" and "+str(players[player2])
            first = players[player1]
            second = players[player2]
            print  str(players[player1])+" "+" statistics: "
            print "won:"+str(playerStastistics[first]['won'])
            print "lost:"+str(playerStastistics[first]['loss'])
            print "Score:"+str(round(playerStastistics[first]['score'],0))
            print " "
            print str(players[player2])+" "+" statistics: "
            print "won:"+str(playerStastistics[second]['won'])
            print "lost:"+str(playerStastistics[second]['loss'])
            print "Score:"+str(round(playerStastistics[second]['score'],0))
            print " "
            
            
            
            playerStastistics[win]['won']+=1
            playerStastistics[loose]['loss']+=1
            # update game played
            playerStastistics[win]['played']+=1
            playerStastistics[loose]['played']+=1
            # determine the k-factor
            self.k_factor = self.determineKfactor(playerStastistics[win]['won'])
            # get expected chance
            self.expected =self.getExpectedChances(playerStastistics[loose]['score'], playerStastistics[win]['score'])
            # get winner score update
            playerStastistics[win]['score'] = self.getWinnerScore(playerStastistics[win]['score'])
            # get looser score update
            playerStastistics[loose]['score'] = self.getLoserScore(playerStastistics[loose]['score'])
            
            print win+" "+"has been choosen as winner"
            print "winner updated score: "+ str(round(playerStastistics[win]['score'],0))
            print "looser updated score: "+ str(round(playerStastistics[loose]['score'],0))
            game+=1
            
            print "\n"
        
        # print top rated players:
        # we need simple mathematics to do this
        rate = 1
        ratings = {}
        
        while rate!=11: # just for 10 players 
            temp = players[rate]  # name of the player
            # i want to rate the only player who has played in the game
            if playerStastistics[temp]['played']!= 0: 
                if playerStastistics[temp]['won'] == 0:
                    performance = round(playerStastistics[temp]['score']/(1+(playerStastistics[temp]['loss'])),0) # to avoid division by zero error
                    ratings[temp] = performance
                else:
                    performance = round(playerStastistics[temp]['score']/(1+(playerStastistics[temp]['loss']/playerStastistics[temp]['won'])),0
                    ratings[temp] = performance             
            
            
            rate+=1
        
        
        #now sort out reverse based on performance value
        topRating = ratings.items()
        topRating.sort(key = itemgetter(1),reverse=True)
        
        # now iterate all the values
        temp1 = 1
        print "Top 5 rated players:"
        while temp1!=6:
            j = 0 # name of the player
            k = 1 # performace
            print "No"+" "+str(temp1)+": position is "+" "+str(topRating[temp1][j])+" "+"with overall performance:"+" "+str(topRating[temp1][k])
            temp1+=1

#main method
if __name__ == '__main__':
    start = Facemash() #creating instance
    start.calculate()
    
