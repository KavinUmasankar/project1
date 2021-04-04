# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 13:34:52 2021

@author: kavin
"""

def print_utc(num):
    monthref = {1 : "January", 2 : "February", 3 : "March"}
    calculate = num
    years = calculate // 31556926
    calculate -= years * 31556926
    months = calculate // 2629743
    calculate -= months * 2629743
    days = calculate // 86400
    calculate -= days * 86400
    hours = calculate // 3600
    calculate -= hours * 3600
    minutes = calculate // 60
    print("Posted on " + monthref[months + 1] + " " + str(days + 2) + ", " + str(years + 1970) + " at " + str(hours) + ":" + str(minutes + 26))
    
print_utc(1617043692)