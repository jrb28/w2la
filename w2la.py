# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 09:05:53 2023

"""

import mysql.connector as mysql

def get_route():
    """ Return a route in the list route_soln wherein a route is specified by locations
        abbreviations in the order that th elocations are visited starting with LA 
        and ending with W.  Each pair of adjacent abbreviations must correspond to a 
        valid single-link trip.
   """
        
    user_name = "no_name"   # replace string with your username
    nickname = 'nickname'   # if you chose, enter a nickname to appear instead of your username
    route_soln = []        # use this list for the indices of the towers you select
        
    ''' Start your code below this comment '''
    
    
    ''' Finish coding before this comment '''
    
    return user_name, route_soln, nickname
  
if __name__ == '__main__':
  print(get_route())
