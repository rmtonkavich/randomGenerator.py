#!/usr/bin/env python3

# Random String Generator
# For Filling Databases
# And Tseting Sorting Methods

import random
import string
import time    # For a Execution Timing Algo


def randString(length):
    letters = string.ascii_lowercase  # 26 ascii_lowercase "letters" 
    return ( ''.join(random.choice(letters) for i in range(length)))


for x in range(60000):
    length = 10  # Use an Input Statement to get UI-Input
    firstname = randString(length)
    secondname = randString(length)
    
    print(x, "{}  {}".format(firstname, secondname) )
  
    
# Robert Tonkavich
# Midland Michigan