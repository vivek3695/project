import random
print("Can't make a choice? Then toss a coin")
x=('HEADS')
y=('TAILS')
l=[y,x]
a=int(input('how many times do you wanna toss: '))
for x in range(a):
    print('1.HEADS')
    print('2.TAILS')
    b=int(input('ENTER YOUR CHOICE: '))
    c=random.choice(l)
    if c==x and b==1:
        print('heads,you won')
    elif c==x and b==2:
        print('heads,you lost')
    elif c==y and b==1:
        print('tails,you lost')
    elif c==y and b==2:
        print('tails,you won')
print('thank you')
              
