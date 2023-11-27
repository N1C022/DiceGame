import AthenasChallenge
import random
player1score=0
player2score=0
P1Inventory: dict = { "Shield": 0, "Sword": 0, "Gambles":0, "Turns":0}
P2Inventory: dict = { "Shield": 0, "Sword": 0, "Gambles":0, "Turns":0}
#GODS
# MARS:  IF NO DOUBLE OR PASS 10 IN A ROW; x2 points until double or pass
#        IF PASS OR DOUBLE 10 TIMES IN A ROW; /2 points until 5 in a row without pass or double
# HEPHAESTUS: IF YOU LOSE 49 POINTS IN ONE TURN; HEPHAESTUS GIVES YOU A SWORD AND A SHIELD
#            IF YOU ANGER HEPHAESTUS (1/100 CHANCE) MEGA-SWORD TAKES AWAY ALL YOUR POINTS
# ATHENA: IF YOU COMPLETE ATHENAS CHALLENGE ATHENA SHOWS YOU YOUR NEXT 3 ROLES BEFORE YOU ROLE
#         IF YOU FAIL ATHENAS CHALLENGE ATHENA FORCES YOU TO MAKE BAD STRATEGIC CHOICES FOR THE NEXT 3 ROUNDS
# POSEIDON: IF YOU ... HIS HUGE WAVE WILL TAKE YOU TO NEXT CHECKPOINT
#           IF YOU ... HIS HUGE WAVE WILL TAKE YOU TO PREVIOUS CHECKPOINT
# THIEF
#
# LOKI IF YOU ... HE WILL GET YOU TO 400 POINTS FOR 5 ROUNDS (GO BACK TO PREVIOUS POINTS AFTER)
#      IF YOU ... HE WILL FORCE YOU TO ROLL DOUBLES FOR THE NEXT 5 TURNS

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",#2
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "
def AthenasChallenge2():
    chance=random.randint(1,20)
    if chance==1:
        print( " ATHENAS CHALLENGE ".center(50, "~"))
        print("ATHENA has taken an interest in you. She gives you a challenge to prove yourself worthy")
        return AthenasChallenge.main()
        
def HephaestusBlessing(player):
    print( " HEPHAESTUS' BLESSING ".center(50, "~"))
    print("HEPHESTUS has taken pity on you. He gifts you a Sword and Shield")
    if player==P1:
        P1Inventory["Sword"] +=1
        P1Inventory["Shield"] +=1
    elif player==P2:
        P2Inventory["Sword"] +=1
        P2Inventory["Shield"] +=1
def HephaestusAnger():
    a=0
    chance=random.randint(1,100)
    if chance==1:
        print( " HEPHAESTUS' PUNISHMENT ".center(50, "~"))
        print("HEPHESTUS has taken offence by you. HE SMITES YOU WITH HIS GODLY-SWORD")
        a+=1
    return a
def useSword(player):
    a=0
    ask=str(input("Do you want to use a sword?, answer Yes or No"))
    while ask != "Yes" and ask != "No":
        print("Please answer Yes or No")
        ask=str(input("Do you want to use a sword?, answer Yes or No"))
    if ask=="Yes":
        if player==P2:
            if P1Inventory["Shield"]>0:
                ask=str(input(P1+" has a shield, are you sure you want to attack?"))
                while ask!= "Yes" and ask!= "No":
                    print("Please answer Yes or No")
                    ask=str(input("Do you want to use a sword?, answer Yes or No"))
                while ask=="Yes" and P2Inventory["Sword"]>0:
                    P2Inventory["Sword"]-=1
                    if P1Inventory["Shield"]>0:
                        P1Inventory["Shield"]-=1
                        print("YOU BROKE THEIR SHIELD")
                    else:
                        a+=1
                        print("YOU DID 50 DAMAGE!")
                        P2Inventory["Sword"]-=1
                    if P2Inventory["Sword"]>0:
                        ask=str(input("Do you want to attack again?, answer Yes or No"))
                        while ask!= "Yes"  and ask!= "No":
                            print("Please answer Yes or No")
                            ask=str(input("Do you want to attack again?, answer Yes or No"))



            else:
                while ask=="Yes" and P2Inventory["Sword"]>0:
                    a+=1
                    print("YOU DID 50 DAMAGE!")
                    P2Inventory["Sword"]-=1
                    if P2Inventory["Sword"]>0:
                        ask=str(input("Do you want to attack again?, answer Yes or No"))
                        while ask!= "Yes"  and ask!= "No":
                            print("Please answer Yes or No")
                            ask=str(input("Do you want to attack again?, answer Yes or No"))
        if player==P1:
            if P2Inventory["Shield"]>0:
                ask=str(input(P2+" has a shield, are you sure you want to attack?"))
                while ask!= "Yes" and ask!= "No":
                    print("Please answer Yes or No")
                    ask=str(input("Do you want to use a sword?, answer Yes or No"))
                while ask=="Yes" and P1Inventory["Sword"]>0:
                    P1Inventory["Sword"]-=1
                    if P2Inventory["Shield"]>0:
                        P2Inventory["Shield"]-=1
                        print("YOU BROKE THEIR SHIELD")
                    else:
                        a+=1
                        print("YOU DID 50 DAMAGE!")
                    if P1Inventory["Sword"]>0:
                        ask=str(input("Do you want to attack again?, answer Yes or No"))
                        while ask!= "Yes"  and ask!= "No":
                            print("Please answer Yes or No")
                            ask=str(input("Do you want to attack again?, answer Yes or No"))



            else:
                while ask=="Yes" and P1Inventory["Sword"]>0:
                    a+=1
                    print("YOU DID 50 DAMAGE!")
                    P1Inventory["Sword"]-=1
                    if P1Inventory["Sword"]>0:
                        ask=str(input("Do you want to attack again?, answer Yes or No"))
                        while ask!= "Yes"  and ask!= "No":
                            print("Please answer Yes or No")
                            ask=str(input("Do you want to attack again?, answer Yes or No"))

    return(a)

def random_prize(player):
    prize = random.randint(1, 30)
    if prize==1:
        print( " RANDOM PRIZE ".center(50, "~"))
        print("WOW!! You won a Random Prize! Now you have a SHIELD that can stop you losing once!!")
        if player==P1:
            print("P1 won a prize")
            P1Inventory["Shield"] +=1
        else:
            print("P2 won a prize")
            P2Inventory["Shield"] +=1
    if prize==2:
        print( " RANDOM PRIZE ".center(50, "~"))
        print("WOW!! You won a Random Prize! Now you have a SWORD to attack your opponent's points!!")
        if player==P1:
            print("P1 won a prize")
            P1Inventory["Sword"] +=1
        else:
            print("P2 won a prize")
            P2Inventory["Sword"] +=1

def parse_input(input_string):

    if input_string.strip() in {"2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Please enter a number from 2 to 6.")
        num_dice_input = input("How many dice do you want to roll? [2-6] ")
        while num_dice_input not in {"2", "3", "4", "5", "6"}:
            num_dice_input = input("How many dice do you want to roll? [2-6] ")
        return int(num_dice_input)


def roll_dice(num_dice):

    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results


def generate_dice_faces_diagram(dice_values):

    dice_faces = _get_dice_faces(dice_values)
    dice_faces_rows = _generate_dice_faces_rows(dice_faces)


    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram


def _get_dice_faces(dice_values):
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])
    return dice_faces


def _generate_dice_faces_rows(dice_faces):
    dice_faces_rows = []
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)
    return dice_faces_rows
def gamble(player1score,player2score):
    win=False
    print( " GAMBLE MODE ".center(50, "~"))
    print("YOU HAVE ACCEPTED THE CHALLENGE!!!")
    print("The Rules for Gamble Mode are different to normal mode, you get to roll 2 dice, if you get a double YOU WIN, otherwise YOU LOSE. Good Luck!!")
    gamblerol=roll_dice(2)
    dice_face_diagram = generate_dice_faces_diagram(gamblerol)
    print(f"\n{dice_face_diagram}")
    if gamblerol[0]==gamblerol[1]:
        win=True
        print("YOU WON!!!!")
        if player2score>player1score:
            player1score=player2score
        elif player1score>player2score:
            player2score=player1score
    else:
        print("YOU LOST :(")
        if player2score>player1score:
            player1score=0-player1score
            print("You have "+str(player1score)+" points")
        else:
            player2score=0-player2score
            print("You have "+str(player2score)+" points")
    return win



print("RULES: you pick how many dice you roll (2-6) and then they roll, your points is the sum of what you rolled but if any two sides are the same you lose all your points and its the other players turn to continue, after each turn you can choose to continue or pass, first to 500 wins! ")
P1=input("enter name of Player 1")
P2=input("enter name of Player 2")
while True:
    win=None
    if player2score>=500 or player1score>=500:
        break
    if P1Inventory["Turns"]>P2Inventory["Turns"]:
        print(P2+"'s turn!, you have "+str(player2score)+" points")
        Athena2 = AthenasChallenge2()
        print(Athena2)
        player2score-=(HephaestusAnger()*400)
        random_prize(P2)
        if P2Inventory["Sword"]>0:
            a=useSword(P2)
            player1score-=(a*50)
        if P2Inventory["Gambles"]==0:
            if player1score-player2score>=200:
                gamblechoice=str(input("YOU ARE LOSING, do you want to gamble double your points to possibly catch up with "+P1+" in one go? Enter Yes or No"))
                while gamblechoice!= "Yes" and gamblechoice!= "No":
                    print("Please answer Yes or No")
                    ask=str(input("Do you want to do GAMBLE MODE?"))
                if gamblechoice=="Yes":
                    P2Inventory["Gambles"]+=1
                    P2Inventory["Turns"]+=1
                    win=gamble(player1score,player2score)

    else:
        print(P1+"'s turn!, you have "+str(player1score)+" points")
        Athena1 = AthenasChallenge2()
        print(Athena1)
        player1score-=(HephaestusAnger()*400)
        random_prize(P1)
        if P1Inventory["Sword"]>0:
            b=useSword(P1)
            player2score-=(b*50)
        if P1Inventory["Gambles"]==0:
            if player2score-player1score>=200:
                gamblechoice=str(input("YOU ARE LOSING, do you want to gamble double your points to possibly catch up with "+P1+" in one go? Enter Yes or No"))
                while gamblechoice!= "Yes" and gamblechoice!= "No":
                    print("Please answer Yes or No")
                    ask=str(input("Do you want to do GAMBLE MODE?"))
                if gamblechoice=="Yes":
                    P1Inventory["Gambles"]+=1
                    P1Inventory["Turns"]+=1
                    win=gamble(player1score,player2score)
    while True:
        if win==False:
            break
        oopsie=0
        if input("Press 'Enter' to continue or type 'pass' to pass: ") == "pass":
            if P1Inventory["Turns"]>P2Inventory["Turns"]: P2Inventory["Turns"]+=1
            else: P1Inventory["Turns"]+=1
            break
        num_dice_input = input("How many dice do you want to roll? [2-6] ")
        num_dice = parse_input(num_dice_input)

        roll_results = roll_dice(num_dice)
        for r in range(len(roll_results)-1):
            for rol in range(r+1, len(roll_results)):
                if roll_results[r]==roll_results[rol]:
                    if P1Inventory["Turns"]>P2Inventory["Turns"]:
                        if P2Inventory["Shield"]>0:
                            print("YOUR SHIELD HAS ACTIVATED")
                            P2Inventory["Shield"]-=1
                        else:
                            print("Double! Score reset :(")
                            oopsie=1
                            break
                    else:
                        if P1Inventory["Shield"]>0:
                            print("YOUR SHIELD HAS ACTIVATED")
                            P1Inventory["Shield"]-=1
                        else:
                            print("Double! Score reset :(")
                            oopsie=1
                            break
        dice_face_diagram = generate_dice_faces_diagram(roll_results)

        print(f"\n{dice_face_diagram}")
        if oopsie == 1:
            if P1Inventory["Turns"]>P2Inventory["Turns"]:
                P2Inventory["Turns"]+=1
                for x in range(450,-450,-50):
                    if player2score>=x:
                        if player2score==x+49:
                            HephaestusBlessing(P2)
                        player2score=x
                        break

            else:
                P1Inventory["Turns"]+=1
                for x in range(450,-450,-50):
                    if player1score>=x:
                        if player1score==x+49:
                            HephaestusBlessing(P1)
                        player1score=x
                        break

            break
        else:
            if P1Inventory["Turns"]>P2Inventory["Turns"]:
                for x in roll_results:
                    player2score += x
                print(P2+"'s score:", player2score)
                if player2score>=500:
                    print(P2+" wins!!!!!!!")
                    break
            else:
                for x in roll_results:
                    player1score += x
                print(P1+"'s score:", player1score)
                if player1score>=500:
                    print(P1+" wins!!!!!!!")
                    break
