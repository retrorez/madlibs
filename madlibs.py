#! python3

# Mad Libs App - Scans a Madlibs text file and prompts user for input based on file

import sys, os

KEY_WORDS = ['NOUN', 'ADJECTIVE', 'VERB', 'ADVERB', 'NOUN(PLURAL)', 'VERB(ING)']

madTemplate = open('madlib1.txt')

madOutput = open('madlib1COMPLETE.txt', 'w')

madParse = madTemplate.read().split()

for word in madParse:
    if word not in KEY_WORDS:
        madOutput.write(word + ' ')
    else:
        print('Please enter a ' + word + ': ')
        madInput = input()
        madOutput.write(madInput + ' ')



madOutput.close()
madOutput = open('madlib1COMPLETE.txt')
print(madOutput.read())

madTemplate.close()


    

    

    
