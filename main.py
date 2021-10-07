import random
from random import choice


def generateStatus():
    player_status = random.choice(status_list)
    pop_status = status_list.index(player_status)
    status_list.pop(pop_status)
    return player_status

# To set marks if Police Finds the Thief


def statusPlayer1():
    if player1_status == "King":
        player1_marks = int(3000)
    elif player1_status == "Queen":
        player1_marks = int(2500)
    elif player1_status == "Minister":
        player1_marks = int(200)
    elif player1_status == "Police":
        player1_marks = int(1500)
    elif player1_status == "Cook":
        player1_marks = int(1000)
    elif player1_status == "Thief":
        player1_marks = int(0)
    return player1_marks


def statusPlayer2():
    if player2_status == "King":
        player2_marks = int(3000)
    elif player2_status == "Queen":
        player2_marks = int(2500)
    elif player2_status == "Minister":
        player2_marks = int(200)
    elif player2_status == "Police":
        player2_marks = int(1500)
    elif player2_status == "Cook":
        player2_marks = int(1000)
    elif player2_status == "Thief":
        player2_marks = int(0)
    return player2_marks


def statusPlayer3():
    if player3_status == "King":
        player3_marks = int(3000)
    elif player3_status == "Queen":
        player3_marks = int(2500)
    elif player3_status == "Minister":
        player3_marks = int(200)
    elif player3_status == "Police":
        player3_marks = int(1500)
    elif player3_status == "Cook":
        player3_marks = int(1000)
    elif player3_status == "Thief":
        player3_marks = int(0)
    return player3_marks


def statusPlayer4():
    if player4_status == "King":
        player4_marks = int(3000)
    elif player4_status == "Queen":
        player4_marks = int(2500)
    elif player4_status == "Minister":
        player4_marks = int(200)
    elif player4_status == "Police":
        player4_marks = int(1500)
    elif player4_status == "Cook":
        player4_marks = int(1000)
    elif player4_status == "Thief":
        player4_marks = int(0)
    return player4_marks


def statusPlayer5():
    if player5_status == "King":
        player5_marks = int(3000)
    elif player5_status == "Queen":
        player5_marks = int(2500)
    elif player5_status == "Minister":
        player5_marks = int(200)
    elif player5_status == "Police":
        player5_marks = int(1500)
    elif player5_status == "Cook":
        player5_marks = int(1000)
    elif player5_status == "Thief":
        player5_marks = int(0)
    return player5_marks


def statusPlayer6():
    if player6_status == "King":
        player6_marks = int(3000)
    elif player6_status == "Queen":
        player6_marks = int(2500)
    elif player6_status == "Minister":
        player6_marks = int(200)
    elif player6_status == "Police":
        player6_marks = int(1500)
    elif player6_status == "Cook":
        player6_marks = int(1000)
    elif player6_status == "Thief":
        player6_marks = int(0)
    return player6_marks

#  If police don't find the thief


def thiefEscaped():
    if player1_status == "Thief":
        player1_marks = int(1500)
        return player1_marks
    elif player2_status == "Thief":
        player2_marks = int(1500)
        return player2_marks
    elif player3_status == "Thief":
        player3_marks = int(1500)
        return player3_marks
    elif player4_status == "Thief":
        player4_marks = int(1500)
        return player4_marks
    elif player5_status == "Thief":
        player5_marks = int(1500)
        return player5_marks
    elif player6_status == "Thief":
        player6_marks = int(1500)
        return player6_marks


def whoIsThief():
    if player1_status == "Thief":
        print(f"{your_name} is thief")
    elif player2_status == "Thief":
        print("Player 2 is thief")
    elif player3_status == "Thief":
        print("Player 3 is thief")
    elif player4_status == "Thief":
        print("Player 4 is thief")
    elif player5_status == "Thief":
        print("Player 5 is thief")
    elif player6_status == "Thief":
        print("Player 6 is thief")
    print("\n")


your_name = input("Enter your name: ")
player_list = [
    your_name, "player 1", "player 2", "player 3", "player 4", "player 5"
]
status_list = [
    "King", "Queen", "Minister", "Police", "Cook", "Thief"
]


shuffleCount = int(input("How many times you want to play :"))
count = int(0)
while count < shuffleCount:
    marks = int(0)
    player1_status = generateStatus()
    player2_status = generateStatus()
    player3_status = generateStatus()
    player4_status = generateStatus()
    player5_status = generateStatus()
    player6_status = generateStatus()
    print(f"\nRound {count+1}")
    print(f"You are {player1_status}")
    status_list = [
        "King", "Queen", "Minister", "Police", "Cook", "Thief"
    ]
    if player1_status == "Police":
        # Find Thief
        theifFind = int(input("Who is thief ? Player 2, 3, 4, 5 : "))
        if theifFind == 2 and player2_status == "Thief" or theifFind == 3 and player3_status == "Thief" or theifFind == 4 and player4_status == "Thief" or theifFind == 5 and player5_status == "Thief" or theifFind == 6 and player6_status == "Theif":
            # If Police find theif
            statusPlayer2()  # To check 2nd Player status and assign them their marks
            statusPlayer3()  # To check 3rd Player status and assign them their marks
            statusPlayer4()  # To check 4th Player status and assign them their marks
            statusPlayer5()  # To check 5th Player status and assign them their marks
            statusPlayer6()  # To check 6th Player status and assign them their marks
            print(f"{your_name} found the thief")
            whoIsThief()
        else:
            # If thief escaped
            player1_marks = int(0)
            thiefEscaped()
            print("You couldn't find the thief")
            whoIsThief()  # Check who is thief
    elif player2_status == "Police":
        theifFind = choice([i for i in range(1, 7) if i not in [2]])
        if theifFind == 1 and player1_status == "Thief" or theifFind == 3 and player3_status == "Thief" or theifFind == 4 and player4_status == "Thief" or theifFind == 5 and player5_status == "Thief" or theifFind == 6 and player6_status == "Theif":
            # If Police find theif
            statusPlayer1()  # To check 1st Player status and assign them their marks
            statusPlayer3()  # To check 3rd Player status and assign them their marks
            statusPlayer4()  # To check 4th Player status and assign them their marks
            statusPlayer5()  # To check 5th Player status and assign them their marks
            statusPlayer6()  # To check 6th Player status and assign them their marks
            print("Player 2 found the thief")
            whoIsThief()   # Display the name of thief
        else:
            # If thief escaped
            player2_marks = int(0)
            thiefEscaped()  # Assign marks when theif escaped
            print("Player 2 couldn't find the thief")
            whoIsThief()  # Display the name of thief
    elif player3_status == "Police":
        theifFind = choice([i for i in range(1, 7) if i not in [3]])
        if theifFind == 1 and player1_status == "Thief" or theifFind == 2 and player2_status == "Thief" or theifFind == 4 and player4_status == "Thief" or theifFind == 5 and player5_status == "Thief" or theifFind == 6 and player6_status == "Theif":
            # If Police find theif
            statusPlayer1()
            statusPlayer2()  # To check 2nd Player status and assign them their marks
            statusPlayer4()  # To check 4th Player status and assign them their marks
            statusPlayer5()  # To check 5th Player status and assign them their marks
            statusPlayer6()  # To check 6th Player status and assign them their marks
            print("Player 3 found the thief")
            whoIsThief()   # Display the name of thief
        else:
            # If thief escaped
            player3_marks = int(0)
            thiefEscaped()  # Assign marks when theif escaped
            print("Player 3 couldn't find the thief")
            whoIsThief()  # Display the name of thief
    elif player4_status == "Police":
        theifFind = choice([i for i in range(1, 7) if i not in [4]])
        if theifFind == 1 and player1_status == "Thief" or theifFind == 2 and player2_status == "Thief" or theifFind == 3 and player3_status == "Thief" or theifFind == 5 and player5_status == "Thief" or theifFind == 6 and player6_status == "Theif":
            # If Police find theif
            statusPlayer1()
            statusPlayer2()  # To check 2nd Player status and assign them their marks
            statusPlayer3()  # To check 3rd Player status and assign them their marks
            statusPlayer5()  # To check 5th Player status and assign them their marks
            statusPlayer6()  # To check 6th Player status and assign them their marks
            print("Player 4 found the thief")
            whoIsThief()   # Display the name of thief
        else:
            # If thief escaped
            player4_marks = int(0)
            thiefEscaped()  # Assign marks when theif escaped
            print("Player 4 couldn't find the thief")
            whoIsThief()  # Display the name of thief
    elif player5_status == "Police":
        theifFind = choice([i for i in range(1, 7) if i not in [5]])
        if theifFind == 1 and player1_status == "Thief" or theifFind == 2 and player2_status == "Thief" or theifFind == 3 and player3_status == "Thief" or theifFind == 4 and player4_status == "Thief" or theifFind == 6 and player6_status == "Theif":
            # If Police find theif
            statusPlayer1()
            statusPlayer2()  # To check 2nd Player status and assign them their marks
            statusPlayer3()  # To check 3rd Player status and assign them their marks
            statusPlayer4()  # To check 4th Player status and assign them their marks
            statusPlayer6()  # To check 6th Player status and assign them their marks
            print("Player 5 found the thief")
            whoIsThief()   # Display the name of thief
        else:
            # If thief escaped
            player5_marks = int(0)
            thiefEscaped()  # Assign marks when theif escaped
            print("Player 5 couldn't find the thief")
            whoIsThief()  # Display the name of thief
    elif player6_status == "Police":
        theifFind = choice([i for i in range(1, 7) if i not in [6]])
        if theifFind == 1 and player1_status == "Thief" or theifFind == 2 and player2_status == "Thief" or theifFind == 3 and player3_status == "Thief" or theifFind == 4 and player4_status == "Thief" or theifFind == 5 and player5_status == "Theif":
            # If Police find theif
            statusPlayer1()
            statusPlayer2()  # To check 2nd Player status and assign them their marks
            statusPlayer3()  # To check 3rd Player status and assign them their marks
            statusPlayer4()  # To check 4th Player status and assign them their marks
            statusPlayer5()  # To check 6th Player status and assign them their marks
            print("Player 6 found the thief")
            whoIsThief()   # Display the name of thief
        else:
            # If thief escaped
            player6_marks = int(0)
            thiefEscaped()  # Assign marks when theif escaped
            print("Player 6 couldn't find the thief")
            whoIsThief()  # Display the name of thief

    count += 1
