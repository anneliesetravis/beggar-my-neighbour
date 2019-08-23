from random import shuffle

def finished(players):
    """
    Function that returns True if one player has all the
    cards and the others have none

    Arguments:

    :param players: the list of lists of the players' cards
    :return: True iff all players except one have run out of cards
    """
    
    if players.count([]) == len(players)-1:
        return True
    else:
        return False
    

def take_turn(player, pile):
    """
    plays a single turn of the game and returns the player's cards after the
    turn, the new pile and the reward cards to be given to the previous player,
    if any

    Arguments:

    :param player: the cards of the current player at the start of the turn
    :param pile: the pile at the start of the turn
    :return: the player's cards after the turn, the new pile and the reward
    cards to be given to the previous player
    
    """
    
    last_player_pickup = False
    reward = []
    newplayer = []
    newpile = []
    penalties = [14, 13, 12, 11]
    
    if pile != [] and player != []:
        if pile[-1] in penalties:
            penalty = pile[-1] - 10
            
            #current player to pay penalties until the penalty is 
            # complete, they run out of cards, or they play a court card
            while penalty > 0:
                last_player_pickup = False
                pile.append(player.pop(0))
                penalty = penalty - 1
                
                if pile[-1] not in penalties:
                    last_player_pickup = True
                
                if player == []:
                    last_player_pickup == True
                    break
                
                if pile[-1] in penalties:
                    last_player_pickup = False
                    break
        else:
            #penalty-free (regular) turn taking 
            pile.append(player.pop(0))
            newpile = pile
            newplayer = player
            
    elif player == []:
        #if the current player has no cards, skip this player 
        last_player_pickup = False
        newpile = pile
        newplayer = player
        reward = []
        
    else:
        pile.append(player.pop(0))
        newpile = pile
        newplayer = player
           
    if last_player_pickup == True:
        reward = pile
        newpile = []
        newplayer = player
        return newplayer, newpile, reward
    
    else:
        reward = []
        newpile = pile
        newplayer = player
        return newplayer, newpile, reward
            

def beggar(Nplayers, deck, talkative = False):
    """
    Function to play a single game of Beggar my Neighbour

    Arguments:

    :param Nplayers: the number of players in the game
    :param deck: the deck with whick to play the game
    :param talkative: whether to print out a transcript of the game being played
    :return: the number of turns taken to finish the game
    """
    
    #checking that the number of players is legal
    assert Nplayers <= len(deck), "Too many players!"
    
    shuffle(deck)
    turn = 0
    pile = []
    current_player = 0
    player_list = list(range(Nplayers))

    #creating a list to match up the previous player with
    #the current player for dealing out rewards (iterable)
    previous_player_list = player_list[0:-1]
    previous_player_list.insert(0, player_list[-1])

    #separate list of lists for the players' cards
    players = [[] for n in range(Nplayers)]
    
    #dealing the deck to the players
    while len(deck) > 0:
        for n in player_list:
            if len(deck) != 0:
                players[n].insert(0,deck[0])
                deck.remove(deck[0])
        
    while finished(players) == False:
        for m, n in zip(previous_player_list, player_list):            
            if finished(players) == True:
                break

            current_player = n
            player = players[n]
            
            #if a player is out of cards, this removes 
            # them from the turn iteration
            if players[n] == []:
                player_list.remove(n)
                previous_player_list.remove(n)
                newplayer = player
                newpile = pile
                reward = []
                continue
            else:
                newplayer, newpile, reward = take_turn(player, pile)
        
            pile = newpile
            players[n] = newplayer
            players[m] = players[m] + reward

            turn = turn + 1
            
            if talkative == True:
                print("After Turn", turn, ":")
                print("Pile:", pile)

                for x in range(Nplayers):
                    if x == current_player:
                        print("*", x, players[x])
                    else:
                        print(" ", x, players[x])
            
    return turn
    
if __name__ =='__main__':
    number_of_players = input((("""How many players?
    """)))
    print(beggar(int(number_of_players), 4 * list(range(2,15)), talkative = True))

    
