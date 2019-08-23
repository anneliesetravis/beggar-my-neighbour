import random

def riffle_once(L):
    """
    Function to perform one riffle shuffle of the 
    list L and return the shuffled list
	
    Arguments:
	
    :param L: the list to be shuffled
    :return: the shuffled list (L_shuffled)
    """
	
    L_shuffled = []

    #splitting the list into 2 lists of equalish length
    L1 = L[0:round(len(L)/2)]
    L2 = L[round(len(L)/2):len(L)]
      
    #choose a card from either list 1 or list 2 to add to the shuffled
    #list (depending on the random value of x) until both lists are empty
    while L1 != [] or L2 != []:
		
        x = random.randint(0,1)
		
        if x == 0:
            
            if L1 != []:
                L_shuffled.append(L1[0])
                del L1[0]
            else:
                L_shuffled.append(L2[0])
                del L2[0]
        else:
            
            if L2 != []:
                L_shuffled.append(L2[0])
                del L2[0]
            else:
                L_shuffled.append(L1[0])
                del L1[0]    
                
    return L_shuffled

def riffle(L, N):
    """
    Shuffles a list L thoroughly by performing N successive riffles
	
    Arguments:
	
    :param L: the list to be shuffled
    :param N: the number of riffles to be performed
    :return: the shuffled list
    """
    
    for n in range(N):
        L = riffle_once(L)        
    return L    
    
def check_shuffle():
    """
    Checks that both riffle functions have all the elements in the original list
    in the shuffled list, and that the shuffled and original list lengths are equal
    """
	
    list = [1, 2, 3, 4, 5, 6]
	
    assert len(riffle_once(list)) == len(list), "Shuffled list length != original list length"
    assert len(riffle(list,5)) == len(list), "Shuffled list length != original list length"
    assert sorted(list) == sorted(riffle_once(list)), "Lists do not contain the same elements"
    assert sorted(list) == sorted(riffle(list,5)), "Lists do not contain the same elements"         

def quality(L):
    """
    Function that evaluates how well the list L is shuffled
    based on the given criteria
	
    Arguments:
	
    :param L: The list that has been shuffled
    :return: the shuffle quality
    """
    
    counter = 0
    n=0

    sorted_L = sorted(L)

    #counting the number of times an item in the list is smaller than the next item
    for n in range(len(L)-1):
        n1 = L[n]
        n2 = L[n+1]

        if int(sorted_L.index(n1))<int(sorted_L.index(n2)):
            counter = counter + 1
            
        n = n + 1
     
    return counter/(len(L)-1)

def average_quality(N, trials = 30):
    """
    Evaluates the average quality of a shuffle of the list of 
    integers 1-50 riffled N times.

    Arguments:

    :param N: the number of times to riffle shuffle the list
    :param trials: the number of trials over which to take an average
    :return: the average quality of the shuffle
    """
    
    L = list(range(50))
    qualities = []
    
    for x in range(trials):
        L = riffle(L, N)
        qualities.append(quality(L))
        
    average_quality = sum(qualities)/trials
    
    return average_quality

def average_quality_increasing_N(N):
    """Prints out the average quality of a riffle shuffle
    of a list of length 50 using N = 1, 2, 3, . . . , N

    Arguments:
    
    :param N: quality will be calculated for up to this number of riffle shuffles
    :print: The average riffle quality for N = 1...N
    """
    
    for n in range(1,N+1):
        quality = average_quality(n)
        print("Average quality with", n, "riffles:")
        print(quality)
    
check_shuffle()

#if __name__ == " __main__ ":
    
L = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta",
"theta", "iota", "kappa", "lambda", "mu"]
print(riffle_once(L))
print(" ")
    
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(riffle_once(L))
print(" ")
    
average_quality_increasing_N(15)
