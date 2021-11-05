import random
def a():
    import cointoss
def b():
    import quizfinal
def c():
    import rockpaperscissors
A=print('welcome to THE GAME where to get to play a random game')
B=input('press enter to begin')
Z=''
if B==Z:
    while True:
        z=random.randint(0,3)
        if z==0:
            a()
            break
        elif z==1:
            b()
            break
        elif z==2:
            c()
            break

