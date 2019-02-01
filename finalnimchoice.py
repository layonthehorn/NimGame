#!/usr/bin/env python3

# By LayOnTheHorn 
#
#
# God the bot was a pain in the ass to make functional.
# the bot will almost always win though

import string, random, sys

def liststicksleft(removesticks,listtosticks):

    # this section takes a list of sticks and removes the ones that the player chose
    for i in removesticks:
        i = int(i)
        i = i - 1
        listtosticks[i] = "*"

# Don't ask me to explain this mess here.

def aithatremovessticks(liststicks):

    # this is a list that is filled with the index locations of any sticks left
    listofsticks = []
    # this varible is the storage for the index point of the sticks
    numberinlist = -1
    # This is the point in the list of sticks that we are removing from
    pointoflist = 0

    # this section checks which parts of the list are still | and can be replaced
    for i in liststicks:
        numberinlist = numberinlist + 1
        if i == "|":
            listofsticks.append(numberinlist)
    #print(listofsticks)

    # this calculates how many sticks the bot should take
    botremove = (liststicks.count("|") % 3)
    #print("botremove:",botremove)

    #
    for i in range(botremove):

        # this iterates through the list of sticks and removes what the bot chooses
        for inum in listofsticks:
            pointoflist = pointoflist + 1
            # if the list has not itterated more then the amount of sticks the bot took
            # it will continue to remove sticks
            # this allows me to not care about stoping the itteration because it will only remove sticks if
            # the bot wants to remove them
            if pointoflist <= botremove:
                liststicks[inum] = "*"


    print("Bot took: {0} sticks".format(botremove))


# this is the same as above but pick randomly
def aithatremovessticksrandom(liststicks):
    listofsticks = []
    numberinlist = -1
    pointoflist = 0

    # this section checks which parts of the list are still | and can be replaced
    for i in liststicks:
        numberinlist = numberinlist + 1
        if i == "|":
            listofsticks.append(numberinlist)
    #print(listofsticks)

    # this calculates how many sticks the bot should take
    botremove = random.randrange(0,3)
    #print("botremove:",botremove)

    #
    for i in range(botremove):

        #print(pointoflist)
        for inum in listofsticks:
            pointoflist = pointoflist + 1
            if pointoflist <= botremove:
                liststicks[inum] = "*"


    print("Bot took: {0} sticks".format(botremove))


def playerremovesticks(listosticks):

    playertakelist = []
    print ("\nSticks: {0} {1} {2} {3} {4} {5} {6}\n".format(listosticks[0],listosticks[1],listosticks[2],listosticks[3],listosticks[4],listosticks[5],listosticks[6]))

    # asks for user input until either the user does not enter anything or they enter 2 numbers.
    while 1:
        print("\nWhich sticks to remove? (1 - 7)\nYou can take 0 - 2 enter nothing to stop taking sticks\n")

        if len(playertakelist) == 2:
            break
        playerremoves = input("Enter which sticks to remove. ")
        if playerremoves == "":
            break
        if playerremoves in string.ascii_letters+ string.punctuation:
            print("\nPlease enter only numbers.\n")
            continue
        if int(playerremoves) < 1 or int(playerremoves) > 7:
            print("\nthe value must be 1 through 7.\n")
            continue
        playertakelist.append(playerremoves)


    #print(playerremoves)
    liststicksleft(playertakelist,listosticks)
    print("\nSticks left: {0} {1} {2} {3} {4} {5} {6}\n".format(listosticks[0], listosticks[1], listosticks[2], listosticks[3],listosticks[4], listosticks[5], listosticks[6]))

# if the user does not chose a type of bot the program quits and prints a usage statment
if len(sys.argv) < 2:
    print("Usage:\n\t./finalnimchoice [random]|[always]\n\n\tRandom picks randomly\n\n\tAlways picks by an algorithm\n")
    sys.exit(0)

# grabs the type of bot the user choose
typebot = sys.argv[1]

if typebot != "random" and typebot != "always":
    print("\n\t./finalnimchoice [random]|[always]\n\n\tRandom picks randomly\n\n\tAlways picks by an algorithm\n")
    sys.exit(0)



liststicks = ["|","|","|","|","|","|","|"]


if typebot == "random":
    while 1:



        playerremovesticks(liststicks)
        if not "|" in liststicks:
            print("\nPlayer wins congrats. ")
            break

        aithatremovessticksrandom(liststicks)
        if not "|" in liststicks:
            print("\nBot wins sorry. ")
            break


if typebot == "always":
    while 1:



        playerremovesticks(liststicks)
        if not "|" in liststicks:
            print("\nPlayer wins congrats. ")
            break

        aithatremovessticks(liststicks)
        if not "|" in liststicks:
            print("\nBot wins sorry. ")
            break


# 
#
#
#
#
