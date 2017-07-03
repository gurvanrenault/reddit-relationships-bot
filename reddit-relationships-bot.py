
import praw
from  social_analysis import *  
reddit = praw.Reddit(client_id=SETTINGS['REDDIT_CLIENT_ID'],
                     client_secret=SETTINGS['REDDIT_CLIENT_SECRET'],
                     user_agent=SETTINGS['REDDIT_USER_AGENT'])

subreddit = reddit.subreddit('relationships')


submissions = subreddit.hot(limit=SETTINGS["SUBMISSIONS_TO_ANALYSE"])
submissions_analysed = 0
comments_analysed = 0
men=0
women=0
gender_analysed=0;
print submissions
for submission in submissions:
    for comment in submission.comments.list():
        analyse_comment(comment)
        comments_analysed += 1
        display_information(comments_analysed, submissions_analysed );
    men,women,gender_analysed=analyse_gender_OP(submission.title,men,women,gender_analysed)
    display_analyse_gender_OP(men,women,gender_analysed);
    submissions_analysed += 1

print "\nComplete."
