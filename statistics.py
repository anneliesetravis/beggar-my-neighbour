import beggar

def statistics(Nplayers, games):
    """
	Function using my imported beggar function to find the shortest,
    average and longest of (games) number of games with (Nplayers) players
	
	Arguments:
	
	:param Nplayers: the number of players in the game
	:param games: the number of games to be played
	:return: the shortest, average and longest game in the set of games
    """
	
	#creating a list of game length with the standard 52 card deck
    game_lengths = [beggar.beggar(Nplayers, 4 * list(range(2,15))) for x in range(games)]

    average = round(sum(game_lengths)/len(game_lengths))
    shortest = min(game_lengths)
    longest = max(game_lengths)

    return shortest, average, longest

if __name__ == " __main__ " :	
	for x in range(2,11):
		print("For", x, "players, shortest, average and longest game lengths are:", statistics(x,100))

    

