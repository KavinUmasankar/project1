import praw
import numpy as np
import pandas as pd

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

print(mods[:-2] + "\nRules: \n")

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

wordslist = {}

for submission in submissions:
    counter += 1
    
    words = {}
    
    valid = True
    for word in set(submission.selftext.split(" ")):
        string = ""
        for x in range(len(word)):
            if word[x].isalpha() or word[x] == "'":
                string += word[x]
        if string.lower() in words.keys():
            words[string.lower()] += submission.selftext.count(string)
            continue
        if len(string) < 15:
            words[string] = submission.selftext.count(string)
    print(words)
    wordslist[str(submission.id)] = words
print(wordslist)

df = pd.DataFrame(wordslist)
for column in df.columns:
    df[column] = df[column].replace(np.nan, 0)
df = df[(df.T != 0).any()]
df.to_csv("data.csv")
print(df)