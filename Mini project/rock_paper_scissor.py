import random
game=["Rock","Paper","Scissor"]

manscore=0
compscore=0

def check(a,b):
    global manscore,compscore
    if(a==b):
        manscore+=1
        compscore+=1
        print("MATCH DRAWN ".center(40,' '))
    elif(game[a]=="Rock" and game[b]=="Paper"):
        compscore+=2
        print("COMPUTER WON :-(".center(40,' '))
    elif(game[a]=="Rock" and game[b]=="Scissor"):
        manscore+=2
        print("YOU WON :-)".center(40,' '))
    elif(game[a]=="Paper" and game[b]=="Scissor"):
        compscore+=2
        print("COMPUTER WON :-(".center(40,' '))
    elif(game[b]=="Rock" and game[a]=="Paper"):
        manscore+=2
        print("YOU WON :-)".center(40,' '))
    elif(game[b]=="Rock" and game[a]=="Scissor"):
        compscore+=2
        print("COMPUTER WON :-(".center(40,' '))
    elif(game[b]=="Paper" and game[a]=="Scissor"):
        manscore+=2
        print("YOU WON :-)".center(40,' '))


def score(manscore,compscore):
    print()
    print("YOUR SCORE IS {}".format(manscore).center(40,' '))
    print()
    print("COMPUTER SCORE IS {}".format(compscore).center(40,' '))
    print()
    print('\n')

def final(manscore,compscore):
    print(("-"*60).center(70,' '))
    print()
    if(manscore==compscore):
        print("MATCH DRAW ..".center(70,' '))
    elif(manscore>compscore):
        print("YOU WON THE MATCH :-)".center(70,' '))
    elif(manscore<compscore):
        print("COMPUTER WON THE MATCH :(".center(70,' '))
    print()
    print(("-"*60).center(70,' '))
        
def instruction():
    print("INSTRUCTIONS".center(70,' '))
    print()
    print("Enter 1 for Rock".center(70,' '))
    print("Enter 2 for paper".center(70,' '))
    print("Enter 3 for scissor".center(70,' '))
    print("For WIN - 2 score added to you.".center(70,' '))
    print("For LOSE - 2 score added to computer.".center(70,' '))
    print("For DRAW 1 score added to you and computer.".center(70,' '))
    print()
    print(("*"*50).center(70,' '))

print("\n")    
print(("-"*60).center(70,' '))
print()   #For new line.
s="ROCK PAPER SCISSOR GAME.."
print(s.center(70,' '))
print()
print(("-"*60).center(70,' '))
print()
print("GAME Versus YOU and COMPUTER".center(70,' '))
print(("-"*30).center(70,' '))
print()
print(("~"*60).center(70,' '))
print()
print(("*"*50).center(70,' '))
print()

instruction()   #function call

print('\n')

a="Enter number of times to play :".center(40,' ')
num=int(input(a))
for i in range(num):
    print()
    a="Enter Rock , Paper or Scissor :".center(40,' ')
    choice=int(input(a))
    if(choice>0 and choice<=3):
        print()
        print("You entered {}".format(game[choice-1]).center(40,' '))
        randnum=random.randint(1,3)
        print()
        print("Computer chose {}".format(game[randnum-1]).center(40,' '))
        print()
        check(choice-1,randnum-1)
        score(manscore,compscore)
    else:
        print()
        print("You entered wrong option".center(40,' '))
        print()
        print("Enter correct option..".center(40,' '))
        print()
final(manscore,compscore)    
    

