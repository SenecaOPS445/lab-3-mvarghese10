#!/usr/bin/env python3
#Author ID: mvarghese10

# Purpose: to create a Python function that can return the free disk space on a Linux system's root directory.

import os

def free_space():
    df_return = os.popen("df -h | grep '/$' | awk '{print $4}'")
    df_contents = df_return.read().strip()
    return df_contents


if __name__ == '__main__':
    print(free_space())
    

