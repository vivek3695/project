import random
print("Can't make a choice? Then toss a coin")
x=('HEADS')
y=('TAILS')
l=[x,y]
z=''
a=int(input('how many times do you wanna toss: '))
for x in range(a):
    b=input('click enter to toss: ')
    c=random.choice(l)
    if b==z:
        print(c)
print('hope you made the right choice')
