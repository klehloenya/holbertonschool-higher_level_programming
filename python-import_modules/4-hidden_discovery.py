#!/usr/bin/python3
import hidden_4

def disc():
    name = dir(hidden_4)
    for i in name:
        if i[:2] != '__':
            print('{:s}'.format(i))

            if __name__ == "__main__":
                disc()
                