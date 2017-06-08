from random import randint

suites = ["Spades", "Hearts", "Diamonds", "Clubs"]
''' Card class contains the cards suite and value'''
class card:
    def __init__(self, suite, value):
        ''' Suites is passed into card as an int and card assigns the suite from the suites array using the int '''
        self.__suite = suites[suite]
        self.__value = value
    '''Getters and Setters'''
    def __getSuite__(self):
        return self.__suite

    def __setSuite__(self, suite):
        self.__suite = suite

    def __getValue__(self):
        return self.__value

    def __setValue__(self,value):
        self.__value = value

def defeat():
    print("Your cards add up to " + str(playerScore))
    print("Your cards where:")
    for each_card in playerHand:
        print(str(each_card.__getValue__()) + " of " + each_card.__getSuite__())
    print("Sorry, you lost!")

def compareScores(playerScore):
    enemyScore = randint(2,30)
    print("Your Score Was : " + str(playerScore))
    print("Enemy Score Was : " + str(enemyScore))
    if enemyScore < 22:
        if enemyScore - 21 > playerScore:
           print("You Won!")
        else:
            print("You Lost!")
    else:
        print("You Won!")

''' List of all cards '''
deck = []
''' List of the cards the player has '''
playerHand = []

''' Creates cards by passing an int 0-3 for suite and 1-13 for value'''
for suite in range(0,4):
    for value in range(1,14):
        ''' Creates card with suite and value'''
        a = card(suite, value)
        ''' Appends card to the deck list '''
        deck.append(a)

''' Removes 2 random cards from the deck and places them in the playerHand list '''
playerHand.append(deck.pop(randint(0,len(deck))))
playerHand.append(deck.pop(randint(0,len(deck)-1)))
''' Caculates Score '''
playerScore = playerHand[0].__getValue__() + playerHand[1].__getValue__()
''' Sets turnFinished to false so while loop runs'''
turnFinished = False
''' Logic to handle if player losses straight away '''
if playerScore > 22:
    defeat()
    ''' Sets turnFinished to true so while loop dosen't run'''
    turnFinished = True
else:
    ''' Shows the user their cards'''
    print("Your 2 cards are:")
    for each_card in playerHand:
        print(str(each_card.__getValue__()) + " of " + each_card.__getSuite__())

''' Runs while player is playing'''
while turnFinished == False:
    ''' User gets to stick or twist'''
    choice = input("stick or twist (s/t)")
    ''' If user sticks then the while loop stops and compareScore() is ran'''
    ''' If user twist they get a new card added to their deck'''
    if choice == "s":
        turnFinished = True
        compareScores(playerScore)
    elif choice == 't':
        ''' Appends a random card to playerHand '''
        playerHand.append(deck.pop(randint(0, len(deck) - 1)))
        ''' Calculates score '''
        playerScore = 0
        for each_card in playerHand:
            playerScore += each_card.__getValue__()
        if playerScore < 22:
            ''' If the score is less than 21 the user is shown their cards'''
            print("Your cards are:")
            for each_card in playerHand:
                print(str(each_card.__getValue__()) + " of " + each_card.__getSuite__())
        else:
            ''' If not defeat() ir ran and while loop stops'''
            defeat()
            turnFinished = True
    else:
        print("Wrong answer, We'll presume you chose stick")
        turnFinished = True