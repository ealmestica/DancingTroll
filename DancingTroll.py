import time
import os


# Prints a troll in ACSII ART 
def print_troll(hair_char):
    print('       ',hair_char * 5) # Hair
    print('        |_ _|') # Head
    print('       <(o.o)> ___...TROLOLO LOLO TROLOLO!!!') # Face, ears, eyes, nose and troll song
    print('__     __\\"/__/   \__') # Mouth
    print('  \___/  |  |      ')# Arms
    print('        |  /') # Body
    print('        /  |')
    print('        |  /')
    print('        ||||')
    print('        ||||') # Legs
    print('      __||||')
    print('     |___|(_)') # Feet 
    return
 
 
 # Prints troll 2 in different position
def print_troll_2(hair_char):

    print('       ',hair_char * 5) # Hair
    print('        |_ _|') # Head
    print('       <(-.-)> ...TROLOLO LOLO TROLOLO!!!') # Face, ears, eyes, nose and troll song
    print('__     __\o/__     __') # Mouth
    print('  \___/  |  | \___/')# Arms
    print('         |  |') # Body
    print('         |  |')
    print('         \  /')
    print('         ||||')
    print('         ||||') # Legs
    print('       __||||__')
    print('      |___||___|') # Feet 
    return
 
 
 # Prints troll 3 in different position
def print_troll_3(hair_char):

    print('       ',hair_char * 5) # Hair
    print('        |_ _|') # Head
    print('   ___ <(o.o)> ...TROLOLO LOLO TROLOLO!!!') # Face, ears, eyes, nose and troll song
    print('__/   \__\\"/__     __') # Mouth
    print('        |  |  \___/')# Arms
    print('         \  |') # Body
    print('         |  /')
    print('         \  |')
    print('         ||||')
    print('         ||||') # Legs
    print('         ||||__')
    print('        (_)|___|') # Feet 
    return
 
 
 
 # prompts for input to see a troll and change troll's  hair style
print('Would you like to see a troll? \n')

troll = input('Enter any key to see a troll or "no" if you do not wish to see troll: ')
if troll != 'no':
    print_troll('m')
else: 
    print('\nLooks like you are not in a troll mood today.\n')
troll_hair = ((input('\nEnter a single character to change the troll\'s hair style and make troll dance: ')))
print_troll(troll_hair)
# Loop to print troll in various positions
for i in range(0, 20):
    os.system('cls')
    print_troll(troll_hair)
    time.sleep(0.25)
    os.system('cls')
    print_troll_2(troll_hair)
    time.sleep(0.25)
    os.system('cls')
    print_troll_3(troll_hair)
    time.sleep(0.25)
    os.system('cls')
    print_troll_2(troll_hair)
    time.sleep(0.25)








