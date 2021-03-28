import praw
import pandas as pd

# path to csv with api keys                                                                              
api_path = '../../api_keys/project1.csv'

# capture api oauth                                                                                      
reddit_oauth = pd.read_csv(api_path)

# authenticate & use api oauth items                                                                     
reddit = praw.Reddit(client_id=reddit_oauth['client_id'][0],
                     client_secret=reddit_oauth['secret'][0],
                     user_agent=reddit_oauth['agent_id'][0])

sub = "politics"

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
for submission in reddit.subreddit(sub).hot(limit = 5):
    counter += 1
    print("\nPost #" + str(counter) + ":\n")
    print(submission.title)
    print("ID: " + str(submission.id) + "\n")
    print(submission.selftext + "\n")
    print("Posted by: u/" + str(submission.author) + (" (Moderator)" * (str(submission.author) in modlist)))        
    print(submission.created_utc)
    print(submission.score)
    print(str(submission.upvote_ratio * 100) + "% of users upvoted. \n\n\n")

