#!/usr/bin/env python3.6

# By Thomas P. Dressel
#
#
# God the bot was a pain in the ass to make functional.
# the bot will almost always win though

import string

def liststicksleft(removesticks,listtosticks):

    for i in removesticks:
        i = int(i)
        i = i - 1
        listtosticks[i] = "*"

# Don't ask me to explain this mess here.

def aithatremovessticks(liststicks):
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
    botremove = (liststicks.count("|") % 3)
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
        print("\nWhich sticks to remove? (1 - 7)\nYou can take 0 - 2 enter to stop taking sticks\n")

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


liststicks = ["|","|","|","|","|","|","|"]

while 1:



    playerremovesticks(liststicks)
    if not "|" in liststicks:
        print("\nPlayer wins congrats. ")
        break

    aithatremovessticks(liststicks)
    if not "|" in liststicks:
        print("\nBot wins sorry. ")
        break