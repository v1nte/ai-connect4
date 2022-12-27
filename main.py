import subprocess

print('Hello')
print('\n')
print('Press 1 if you want to play against AI')
print('Press 2 if you want to play against player')
a = int(input("Select 1 or 2:"))
print(a)

if a==1:
    print('Playing agains AI')
    exec(open('minimax_game2.py').read())
else:
    print('Playing against player')
    exec(open('2_player.py').read())