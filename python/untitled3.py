# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 12:33:52 2021

@author: kavin
"""
import praw
import pandas as pd

def print_utc(num):
    monthref = {1 : "January", 2 : "February", 3 : "March", 4 : "April", 5 : "May", 6 : "June", 7 : "July", 8 : "August", 9 : "September", 10 : "October", 11 : "November", 12 : "December"}
    calculate = num
    years = int(calculate // 31556926)
    calculate -= years * 31556926
    months = int(calculate // 2629743)
    calculate -= months * 2629743
    days = int(calculate // 86400)
    calculate -= days * 86400
    hours = int(calculate // 3600)
    calculate -= hours * 3600
    minutes = int(calculate // 60)
    print("Posted on " + monthref[months + 1] + " " + str(days + 2) + ", " + str(years + 1970) + " at " + ("12" * (hours == 0)) + (str(hours % 12) * (hours > 0)) + ":" + str((minutes + 26) % 60) + (" AM" * (hours < 13)) + (" PM" * (hours > 12)))

# path to csv with api keys                                                                              
api_path = '../../api_keys/project1.csv'

# capture api oauth                                                                                      
reddit_oauth = pd.read_csv(api_path)

# authenticate & use api oauth items                                                                     
reddit = praw.Reddit(client_id=reddit_oauth['client_id'][0],
                     client_secret=reddit_oauth['secret'][0],
                     user_agent=reddit_oauth['agent_id'][0])

sub = "python"

print("All about the r/" + sub + " subreddit: \n")

mods = "Moderators: "

modlist = []

for moderator in reddit.subreddit(sub).moderator():
    modlist.append(str(moderator))
    mods += ("u/" + str(moderator) + ", ")

print(mods[:-2] + "\n\nRules:")

counter = 0
for rule in reddit.subreddit(sub).rules:
    counter += 1
    print(str(counter) + ". " + str(rule))

counter = 0

submissions = []

for submission in reddit.subreddit(sub).hot():
    if submission.is_self:
        submissions.append(submission)
        counter += 1
    if counter == 10:
        break

counter = 0

for submission in submissions:
    counter += 1
    print("\nPost #" + str(counter) + ":\n")
    print(submission.title.upper() + "\n")
    print("ID: " + str(submission.id) + "\n")
    print(submission.selftext + "\n\n")
    print("Posted by: u/" + str(submission.author) + (" (Moderator)" * (str(submission.author) in modlist)))        
    print_utc(submission.created_utc)
    print("Score: " + str(submission.score))
    if submission.upvote_ratio == 1:
        print(str(round(submission.score)) + " upvotes, 0 downvotes")
        
    else: 
        total = (submission.score) // (submission.upvote_ratio - (1 - submission.upvote_ratio))
        if str(submission.upvote_ratio * total)[-1] == 5:
            print(str(round(submission.upvote_ratio * total)) + " upvotes, " + str(int((1 - submission.upvote_ratio) * total)) + " downvotes")
        else:
            print(str(round(submission.upvote_ratio * total)) + " upvotes, " + str(round((1 - submission.upvote_ratio) * total)) + " downvotes")
    print(str(round(submission.upvote_ratio * 100)) + "% of users upvoted. \n\n\n")
    
    