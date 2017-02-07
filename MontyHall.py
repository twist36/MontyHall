"""
Monty Hall simulation
Chris Whitling
Created: 10/5/2016
LE:2/7/2017

MIT License

Copyright (c) [2017] [Christopher John Whitling]

Permission is hereby granted, free of charge, to any person obtaining a 
copy
of this software and associated documentation files (the "Software"), to 
deal
in the Software without restriction, including without limitation the 
rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or 
sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included 
in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS 
OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
IN THE
SOFTWARE.
"""

#Import Block
import random
import datetime
from statistics import mean

#Function Block
def empty_door(choice_door, prize_door):
    switch_door = 0
    while switch_door == 0 or switch_door == choice_door or switch_door == prize_door:
        switch_door = random.randint(1, 3)
    return switch_door

def guess_check(choice_door, prize_door):
    if choice_door == prize_door:
        temp_guess_list.append(1)
    else:
        temp_guess_list.append(0)

def switch_check(choice_door, prize_door, switch_door):
    placeholder_door = choice_door
    while choice_door == placeholder_door or choice_door == switch_door:
        choice_door = random.randint(1, 3)
    if choice_door == prize_door:
        temp_switch_list.append(1)
    else:
        temp_switch_list.append(0)
    
#Global Variable Decleration
temp_guess_list = [] #The list of values for first guess acuracy on each runthrough
temp_switch_list = [] #The list of values for change guess on each runthrough

master_guess_list = [] #The list of values for all of the runthroughs
master_switch_list = [] #The list of values for all of the runthroughs

temp_number_itterations = 1000000 #Some number of times to run through the temp, this is the number of values stored in the temp listss

master_number_itterations = 1000000 #Some number of times to run the temp, keep this low if there are memory issues

number_itterations_out = ("Number of trials: "  + str(temp_number_itterations * master_number_itterations) + "\n")

#Main
if __name__ == '__main__':
    for i in range(master_number_itterations):
        temp_guess_list = []
        temp_switch_list = []
        
        print ((i / master_number_itterations) * 100)
        
        for j in range(temp_number_itterations):
            choice_door = random.randint(1, 3)
            prize_door = random.randint(1, 3)
            switch_door = empty_door(choice_door, prize_door)
            guess_check(choice_door, prize_door)
            switch_check(choice_door, prize_door, switch_door)
        
        master_guess_list.append(mean(temp_guess_list))
        master_switch_list.append(mean(temp_switch_list))
        
    first_out = ("First guess percentage: " + str(mean(master_guess_list) * 100) + "%\n")
    second_out = ("Switching percentage: " + str(mean(master_switch_list) * 100) + "%\n")
    
    filename = ("MH_output_" + str(master_number_itterations) + ".txt")
    
    with open(filename, "w+") as output:
        output.write("Monty Hall Simulation Output")
        output.write("\n")
        
        output.write(number_itterations_out)
        output.write("\n")
        
        output.write(first_out)
        output.write(second_out)




