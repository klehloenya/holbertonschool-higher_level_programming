#!/usr/bin/python3
"""Module: 1-my_list
"""
class MyList(list):
    """Class MyList that inherits from list"""
    
    def print_sorted(self):
        """Print the list in ascending sorted order"""
        print(sorted(self))
