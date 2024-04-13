# PPHA 30537
# Spring 2024
# Homework 1

# YOUR CANVAS NAME HERE: Ryan Jia
# YOUR CNET ID NAME HERE: zehuan
# YOUR GITHUB USER NAME HERE: RyanChhhia

# Due date: Sunday April 10th before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.

#############
# Part 1: Introductory Python (to be done without defining functions or classes)

# Question 1.1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.

tested11 = [1,2,"a","b",1.0]
def positionfunctn(input_list): 
    outputtext = []
    index = 1
    for x in input_list: 
        outputtext.append(f"The value at position {index} is {x}")
        index+=1
    return "\n".join(outputtext)  # "\n": print a line feed
print(positionfunctn(tested11))

# Question 1.2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Microsoft" and the phrase "This isn't a palindrome". Print the results of these
# four tests.

def keep_letters_only(text):  # strip text to only contain lower letters
    cleaned_text = [char.lower() for char in text if char.isalpha()]
    cleaned_text = "".join(cleaned_text)
    # complecated version (can simply because "for" sentence only outputs itself): 
    # cleaned_text = ""
    # for char in text: 
    #     if char.isalpha(): 
    #         cleaned_text = cleaned_text + char.lower()
    return cleaned_text

tested12 = ["radar", "A man, a plan, a canal, Panama!", "Microsoft", "This isn't a palindrome"]
tested12_cleaned = [keep_letters_only(text) for text in tested12]

def palindrome_test(text): 
    reversed_text = text[::-1]
    if text == reversed_text: 
        return "This is a palindrome"
    else: 
        return "This isn't a palindrome"

output_12 = [palindrome_test(text) for text in tested12_cleaned]
print("\n".join(output_12))


# Question 1.3: The code below pauses to wait for user input, before assigning the user input to the
# variable. Beginning with the given code, check to see if the answer given is an available
# vegetable. If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again. Repeat until they pick a valid vegetable.

available_vegetables = ['carrot', 'kale', 'broccoli', 'pepper']

while True: 
    choice = input('Please pick a vegetable I have available: ')
    if choice not in available_vegetables: 
        print("You made an invalid choice. Please pick again. ")
    elif choice in available_vegetables: 
        print("You can have the vegetable! ")
        break


# Question 1.4: Write a list comprehension that starts with any list of strings and returns a new
# list that contains each string in all lower-case letters, unless the modified string begins with
# the letter "a" or "b", in which case it should drop it from the result.

tested14 = ["Abandon", "AAPL", "banana", "dog", "Cabbage", 1, 0.5]

def striplist_lower_ab(inputlist): 
    outputlist = []
    for text in inputlist: 
        if type(text) is not str: 
            pass
        else: 
            text = text.lower()
            if text[0] in ["a", "b"]: 
                pass
            else: 
                outputlist.append(text)
    return outputlist

print(striplist_lower_ab(tested14))


# Question 1.5: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'WI':'Wisconsin'}
short_names = ['IL', 'IN', 'MI', 'WI']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Wisconsin']

statedictn = {}
index = 0
for i in short_names: 
    statedictn[i] = long_names[index]
    index+=1
# simplified version: 
# for short_name, long_name in zip(short_names, long_names):
#     statedictn[short_name] = long_name

print(statedictn)


#############
# Part 2: Functions and classes (must be answered using functions\classes)

# Question 2.1: Write a function that takes two numbers as arguments, then
# sums them together. If the sum is greater than 10, return the string 
# "big", if it is equal to 10, return "just right", and if it is less than
# 10, return "small". Apply the function to each tuple of values in the 
# following list, with the end result being another list holding the strings 
# your function generates (e.g. ["big", "big", "small"]).

start_list = [(10, 0), (100, 6), (0, 0), (-15, -100), (5, 4)]

def functnbigsmall(x): 
    sum = x[0] + x[1]
    if sum > 10: 
        return "big"
    elif sum == 10: 
        return "just right"
    else: 
        return "small"
    
print([functnbigsmall(value) for value in start_list])


# Question 2.2: The following code is fully-functional, but uses a global
# variable and a local variable. Re-write it to work the same, but using one
# argument and no global variable. Use no more than two lines of comments to
# explain why this new way is preferable to the old way.

a = 10
def my_func():
    b = 40
    return a + b
x = my_func()

# Revised version: 
a = 10
def my_func_revised(a): 
    b = 40
    return a + b
x = my_func_revised(a)

# Because, now the function can not only can operate "a = 10" ,it can also 
# operate different variables which we substitute into.


# Question 2.3: Write a function that can generate a random password from
# upper-case and lower-case letters, numbers, and special characters 
# (!@#$%^&*). It should have an argument for password length, and should 
# check to make sure the length is between 8 and 16, or else print a 
# warning to the user and exit. Your function should also have a keyword 
# argument named "special_chars" that defaults to True.  If the function 
# is called with the keyword argument set to False instead, then the 
# random values chosen should not include special characters. Create a 
# second similar keyword argument for numbers. Use one of the two 
# libraries below in your solution:
#import random
#from numpy import random

import random

special_chars = True
upperletters = True
lowerletters = True
numbers = True

def functpassword(): 
    pwlen = random.randint(7, 17)
    if pwlen <8 or pwlen >16: 
        return "warning: the password the function generate does not meet the requirement. exit"
    
    charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*"
    if not special_chars: 
        charset = ''.join(char for char in charset if char not in "@#$%^&*")
    if not upperletters: 
        charset = ''.join(char for char in charset if not char.isupper())
    if not lowerletters: 
        charset = ''.join(char for char in charset if not char.islower())
    if not upperletters: 
        charset = ''.join(char for char in charset if not char.isdigit())
    charlist = [char for char in charset]
    
    pw = ""
    for _ in range(pwlen): 
        pw = pw + random.choice(charlist)
    
    return pw

for _ in range(5):  # generate 5 times
    print(functpassword())

# Below is a test function: 
def valid_password(password):
    has_notation = False
    has_upper = False
    has_lower = False
    has_digit = False
    for char in password: 
        if char in "!@#$%^&*": 
            has_notation = True
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
    return ([has_notation, has_upper, has_lower, has_digit], password)

# for _ in range(5):
#     print(valid_password(functpassword()))
  
# Question 2.4: Create a class named MovieDatabase that takes one argument
# when an instance is created which stores the name of the person creating
# the database (in this case, you) as an attribute. Then give it two methods:
#
# The first, named add_movie, that requires three arguments when called: 
# one for the name of a movie, one for the genera of the movie (e.g. comedy, 
# drama), and one for the rating you personally give the movie on a scale 
# from 0 (worst) to 5 (best). Store those the details of the movie in the 
# instance.
#
# The second, named what_to_watch, which randomly picks one movie in the
# instance of the database. Tell the user what to watch tonight,
# courtesy of the name of the name you put in as the creator, using a
# print statement that gives all of the info stored about that movie.
# Make sure it does not crash if called before any movies are in the
# database.
#
# Finally, create one instance of your new class, and add four movies to
# it. Call your what_to_watch method once at the end.

import random  # do not import import random from numpy

class MovieDatabase: 
    def __init__(self, creator): 
        self.creator = creator
        self.moviestore = []

    def add_movie(self, mvname, mvgenera, mvrate): 
        self.moviestore.append((mvname, mvgenera, mvrate))

    def what_to_watch(self): 
        if not self.moviestore:
            print("No movies in the database. Please add four.")
            return

        chosenmovie = random.choice(self.moviestore)
        print(f"Tonight, {self.creator} recommends: \nName: {chosenmovie[0]}\nGenre: {chosenmovie[1]}\nRating: {chosenmovie[2]}")

courtesyJia = MovieDatabase("RyanJia")
courtesyJia.add_movie("Farewell My Concubine", "drama, love, homo", 9.6/2)
courtesyJia.add_movie("Forrest Gump", "drama, love", 9.5/2)
courtesyJia.add_movie("Titanic", "drama, love, disater", 9.4/2)
courtesyJia.add_movie("Leon", "drama, action, crime", 9.4/2)

# print(courtesyJia.moviestore)
courtesyJia.what_to_watch()


