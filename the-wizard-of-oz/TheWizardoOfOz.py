# A small python program using variables to create a custom story based on the user input.
# Some string functions used as well
# Story based on The Wizard of Oz


import os
import textwrap

os.system('mode con: cols=80 lines=40') #resize the comman line window
width = os.get_terminal_size().columns #get window terminal width

#print the title on the middle
def printTitle(): #creating user-defined function
    print(("#"*40).center(width)) #print # 40 times
    print(("The Wizard of [you]").center(width)) #center align
    print(("#"*40).center(width))

printTitle() #call the user-defined function


print('\nFill in the character\'s information below: ')

print('\n\"Dorothy Gale\" Information:')
dorothyFName = input('\tFirst Name: ') #assigning values to a variable
dorothyLName = input('\tLast Name: ')
dorothyEye = input('\tEye Color: ')

print('\n\"Scarecrow\" Information:')
scarecrow = input('\tName: ')

print('\n\"The Tin Woodman\" Information:')
tinWoodman = input('\tName: ')

print('\n\"The Cowardly Lion\" Information:')
cowardlyLion = input('\tName: ')

os.system('cls') #clear screen on windows

printTitle() #print the Title again

#build the story in a multiline
story = '''
    They walked along listening to the singing of the brightly colored birds and looking at the lovely flowers which now became so thick that the ground was carpeted with them. There were big yellow and white and blue and purple blossoms, besides great clusters of scarlet poppies, which were so brilliant in color they almost dazzled '''+dorothyFName.capitalize()+''''s '''+dorothyEye +''' eyes.
    "Aren't they beautiful?" the girl asked, as she breathed in the spicy scent of the bright flowers.
    "I suppose so," answered '''+ scarecrow.capitalize() +''' Scarecrow. "When I have brains, I shall probably like them better."
    "If I only had a heart, I should love them," added '''+tinWoodman.capitalize()+''' the Tin Woodman.
    "I always did like flowers," said '''+cowardlyLion.capitalize()+''' the Cowardly Lion. "They seem so helpless and frail. But there are none in the forest so bright as these."
    They now came upon more and more of the big scarlet poppies, and fewer and fewer of the other flowers; and soon they found themselves in the midst of a great meadow of poppies. Now it is well known that when there are many of these flowers together their odor is so powerful that anyone who breathes it falls asleep, and if the sleeper is not carried away from the scent of the flowers, he sleeps on and on forever. But '''+dorothyFName.capitalize()+''' did not know this, nor could she get away from the bright red flowers that were everywhere about; so presently her eyes grew heavy and she felt she must sit down to rest and to sleep.
    But the Tin Woodman would not let her do this. "We must hurry and get back to the road of yellow brick before dark," he said; and the Scarecrow agreed with him. So they kept walking until '''+dorothyFName.capitalize()+''' could stand no longer. Her eyes closed in spite of herself and she forgot where she was and fell among the poppies, fast asleep.
'''

#print the story in a textwrap
print(textwrap.fill(story, replace_whitespace=False))

#end program




