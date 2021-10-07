import random
from random import choice


def generatePost():
    player_post = random.choice(post_list)
    pop_post = post_list.index(player_post)
    post_list.pop(pop_post)
    return player_post

# To set marks if Police Finds the Thief


def postPlayer1():
    if player1_post == "King":
        player1_marks = int(3000)
    elif player1_post == "Queen":
        player1_marks = int(2500)
    elif player1_post == "Minister":
        player1_marks = int(200)
    elif player1_post == "Police":
        player1_marks = int(1500)
    elif player1_post == "Cook":
        player1_marks = int(1000)
    elif player1_post == "Thief":
        player1_marks = int(0)
    return player1_marks


def postPlayer2():
    if player2_post == "King":
        player2_marks = int(3000)
    elif player2_post == "Queen":
        player2_marks = int(2500)
    elif player2_post == "Minister":
        player2_marks = int(200)
    elif player2_post == "Police":
        player2_marks = int(1500)
    elif player2_post == "Cook":
        player2_marks = int(1000)
    elif player2_post == "Thief":
        player2_marks = int(0)
    return player2_marks


def postPlayer3():
    if player3_post == "King":
        player3_marks = int(3000)
    elif player3_post == "Queen":
        player3_marks = int(2500)
    elif player3_post == "Minister":
        player3_marks = int(200)
    elif player3_post == "Police":
        player3_marks = int(1500)
    elif player3_post == "Cook":
        player3_marks = int(1000)
    elif player3_post == "Thief":
        player3_marks = int(0)
    return player3_marks


def postPlayer4():
    if player4_post == "King":
        player4_marks = int(3000)
    elif player4_post == "Queen":
        player4_marks = int(2500)
    elif player4_post == "Minister":
        player4_marks = int(200)
    elif player4_post == "Police":
        player4_marks = int(1500)
    elif player4_post == "Cook":
        player4_marks = int(1000)
    elif player4_post == "Thief":
        player4_marks = int(0)
    return player4_marks


def postPlayer5():
    if player5_post == "King":
        player5_marks = int(3000)
    elif player5_post == "Queen":
        player5_marks = int(2500)
    elif player5_post == "Minister":
        player5_marks = int(200)
    elif player5_post == "Police":
        player5_marks = int(1500)
    elif player5_post == "Cook":
        player5_marks = int(1000)
    elif player5_post == "Thief":
        player5_marks = int(0)
    return player5_marks


def postPlayer6():
    if player6_post == "King":
        player6_marks = int(3000)
    elif player6_post == "Queen":
        player6_marks = int(2500)
    elif player6_post == "Minister":
        player6_marks = int(200)
    elif player6_post == "Police":
        player6_marks = int(1500)
    elif player6_post == "Cook":
        player6_marks = int(1000)
    elif player6_post == "Thief":
        player6_marks = int(0)
    return player6_marks

#  If police don't find the thief


def thiefEscaped():
    if player1_post == "Thief":
        player1_marks = int(1500)
        return player1_marks
    elif player2_post == "Thief":
        player2_marks = int(1500)
        return player2_marks
    elif player3_post == "Thief":
        player3_marks = int(1500)
        return player3_marks
    elif player4_post == "Thief":
        player4_marks = int(1500)
        return player4_marks
    elif player5_post == "Thief":
        player5_marks = int(1500)
        return player5_marks
    elif player6_post == "Thief":
        player6_marks = int(1500)
        return player6_marks


def whoIsThief():
    if player1_post == "Thief":
        print(f"{your_name} is thief")
    elif player2_post == "Thief":
        print("Player 2 is thief")
    elif player3_post == "Thief":
        print("Player 3 is thief")
    elif player4_post == "Thief":
        print("Player 4 is thief")
    elif player5_post == "Thief":
        print("Player 5 is thief")
    elif player6_post == "Thief":
        print("Player 6 is thief")
    print("\n")


your_name = input("Enter your name: ")
player_list = [
    your_name, "player 1", "player 2", "player 3", "player 4", "player 5"
]
post_list = [
    "King", "Queen", "Minister", "Police", "Cook", "Thief"
]


shuffleCount = int(input("How many times you want to play :"))
count = int(0)
while count < shuffleCount:
    marks = int(0)
    player1_post = generatePost()
    player2_post = generatePost()
    player3_post = generatePost()
    player4_post = generatePost()
    player5_post = generatePost()
    player6_post = generatePost()
    print(f"\nRound {count+1}")
    print(f"You are {player1_post}")
    post_list = [
        "King", "Queen", "Minister", "Police", "Cook", "Thief"
    ]
    if player1_post == "Police":
        # Find Thief
        theifFind = int(input("Who is thief ? Player 2, 3, 4, 5 : "))
        if theifFind == 2 and player2_post == "Thief" or theifFind == 3 and player3_post == "Thief" or theifFind == 4 and player4_post == "Thief" or theifFind == 5 and player5_post == "Thief" or theifFind == 6 and player6_post == "Theif":
            # If Police find theif
            postPlayer2()  # To check 2nd Player Post and assign them their marks
            postPlayer3()  # To check 3rd Player Post and assign them their marks
            postPlayer4()  # To check 4th Player Post and assign them their marks
            postPlayer5()  # To check 5th Player Post and assign them their marks
            postPlayer6()  # To check 6th Player Post and assign them their marks
            print(f"{your_name} found the thief")
            whoIsThief()
        else:
            # If thief escaped
            player1_marks = int(0)
            thiefEscaped()
            print("You couldn't find the thief")
            whoIsThief()  # Check who is thief
    elif player2_post == "Police":
        theifFind = choice([i for i in range(1, 7) if i not in [2]])
        if theifFind == 1 and player1_post == "Thief" or theifFind == 3 and player3_post == "Thief" or theifFind == 4 and player4_post == "Thief" or theifFind == 5 and player5_post == "Thief" or theifFind == 6 and player6_post == "Theif":
            # If Police find theif
            postPlayer1()  # To check 1st Player Post and assign them their marks
            postPlayer3()  # To check 3rd Player Post and assign them their marks
            postPlayer4()  # To check 4th Player Post and assign them their marks
            postPlayer5()  # To check 5th Player Post and assign them their marks
            postPlayer6()  # To check 6th Player Post and assign them their marks
            print("Player 2 found the thief")
            whoIsThief()   # Display the name of thief
        else:
            # If thief escaped
            player2_marks = int(0)
            thiefEscaped()  # Assign marks when theif escaped
            print("Player 2 couldn't find the thief")
            whoIsThief()  # Display the name of thief
    elif player3_post == "Police":
        theifFind = choice([i for i in range(1, 7) if i not in [3]])
        if theifFind == 1 and player1_post == "Thief" or theifFind == 2 and player2_post == "Thief" or theifFind == 4 and player4_post == "Thief" or theifFind == 5 and player5_post == "Thief" or theifFind == 6 and player6_post == "Theif":
            # If Police find theif
            postPlayer1()
            postPlayer2()  # To check 2nd Player Post and assign them their marks
            postPlayer4()  # To check 4th Player Post and assign them their marks
            postPlayer5()  # To check 5th Player Post and assign them their marks
            postPlayer6()  # To check 6th Player Post and assign them their marks
            print("Player 3 found the thief")
            whoIsThief()   # Display the name of thief
        else:
            # If thief escaped
            player3_marks = int(0)
            thiefEscaped()  # Assign marks when theif escaped
            print("Player 3 couldn't find the thief")
            whoIsThief()  # Display the name of thief
    elif player4_post == "Police":
        theifFind = choice([i for i in range(1, 7) if i not in [4]])
        if theifFind == 1 and player1_post == "Thief" or theifFind == 2 and player2_post == "Thief" or theifFind == 3 and player3_post == "Thief" or theifFind == 5 and player5_post == "Thief" or theifFind == 6 and player6_post == "Theif":
            # If Police find theif
            postPlayer1()
            postPlayer2()  # To check 2nd Player Post and assign them their marks
            postPlayer3()  # To check 3rd Player Post and assign them their marks
            postPlayer5()  # To check 5th Player Post and assign them their marks
            postPlayer6()  # To check 6th Player Post and assign them their marks
            print("Player 4 found the thief")
            whoIsThief()   # Display the name of thief
        else:
            # If thief escaped
            player4_marks = int(0)
            thiefEscaped()  # Assign marks when theif escaped
            print("Player 4 couldn't find the thief")
            whoIsThief()  # Display the name of thief
    elif player5_post == "Police":
        theifFind = choice([i for i in range(1, 7) if i not in [5]])
        if theifFind == 1 and player1_post == "Thief" or theifFind == 2 and player2_post == "Thief" or theifFind == 3 and player3_post == "Thief" or theifFind == 4 and player4_post == "Thief" or theifFind == 6 and player6_post == "Theif":
            # If Police find theif
            postPlayer1()
            postPlayer2()  # To check 2nd Player Post and assign them their marks
            postPlayer3()  # To check 3rd Player Post and assign them their marks
            postPlayer4()  # To check 4th Player Post and assign them their marks
            postPlayer6()  # To check 6th Player Post and assign them their marks
            print("Player 5 found the thief")
            whoIsThief()   # Display the name of thief
        else:
            # If thief escaped
            player5_marks = int(0)
            thiefEscaped()  # Assign marks when theif escaped
            print("Player 5 couldn't find the thief")
            whoIsThief()  # Display the name of thief
    elif player6_post == "Police":
        theifFind = choice([i for i in range(1, 7) if i not in [6]])
        if theifFind == 1 and player1_post == "Thief" or theifFind == 2 and player2_post == "Thief" or theifFind == 3 and player3_post == "Thief" or theifFind == 4 and player4_post == "Thief" or theifFind == 5 and player5_post == "Theif":
            # If Police find theif
            postPlayer1()
            postPlayer2()  # To check 2nd Player Post and assign them their marks
            postPlayer3()  # To check 3rd Player Post and assign them their marks
            postPlayer4()  # To check 4th Player Post and assign them their marks
            postPlayer5()  # To check 6th Player Post and assign them their marks
            print("Player 6 found the thief")
            whoIsThief()   # Display the name of thief
        else:
            # If thief escaped
            player6_marks = int(0)
            thiefEscaped()  # Assign marks when theif escaped
            print("Player 6 couldn't find the thief")
            whoIsThief()  # Display the name of thief

    count += 1
