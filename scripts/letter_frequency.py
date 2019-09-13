#A program that reads a file
#and prints the letters in decreasing order of frequency.
#Program converts all the input to lower case
#and only counts the letters a-z. The program does not count
#spaces, digits, punctuation, or anything other than the letters a-z.

import string

file_name = input("Enter a file name: ")

try:
    file = open(file_name)
except:
    print("Can't open file with that name.")
    quit()

letters = dict()

#goes through each line and coverts each letter to lowercase
for line in file:
    line = line.lower()
    #checks if letter is whitespace or punctuation or a digit and doesn't count those
    for letter in line:
        if letter is '\n' or letter is ' ' or letter is 't' or letter.isdigit():
            continue
        elif letter in string.punctuation:
            continue
        else:
            letters[letter] = letters.get(letter, 0) + 1

frequency = list()
sum = 0

#orders the letters by frequency and adds the total amount of letters in the file
for key, value in letters.items():
    frequency.append((value, key))
    sum = sum + value

#sorts frequency in descending order
frequency.sort(reverse=True)

#prints the freqyency, letter and average percent used in the file
for item in frequency:
    average = (item[0]/sum) * 100
    print(item[0], item[1], average)
