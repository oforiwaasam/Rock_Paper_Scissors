#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:40:00 2021

@author: lilsam
"""

import random

another = "y"
while another == "y":
    # Step 1: Read in user choice
    
    user_move = input("Please choose (r)ock, (p)aper, or (s)cissors:")
    
    # Step 2: Randomly select computer move
    computer_move = random.choice(['r','p','s'])
    
    # Step 3: Select winner
    
    if user_move == computer_move:
        print("Draw.")
        
    if (user_move == 'r' and computer_move == "p") or \
       (user_move == 'p' and computer_move == "s") or \
       (user_move == 's' and computer_move == "r"):
           print("Computer wins.")
        
    elif (user_move == "r" and computer_move == "s") or \
        (user_move == "s" and computer_move == "p") or \
        (user_move == "p" and computer_move == "r"):
        print("Player wins.")
        
    else:
        print("Draw")
        
    another = input("Do you want another game? (y/n)")