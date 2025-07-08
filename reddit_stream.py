# reddit_stream.py
import praw
from dotenv import load_dotenv

import os
from pymongo import MongoClient

# Load Reddit credentials
load_dotenv()

print("Client ID:", os.getenv("REDDIT_CLIENT_ID"))
print("Client Secret:", os.getenv("REDDIT_CLIENT_SECRET"))
print("Username:", os.getenv("REDDIT_USERNAME"))
print("Password:", os.getenv("REDDIT_PASSWORD"))
print("User Agent:", os.getenv("REDDIT_USER_AGENT"))

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["rumor_db"]
collection = db["reddit_posts"]

# Target subreddits
subreddits = reddit.subreddit("news+worldnews+disaster+earthquake+flood+wildfire")

print("✅ Reddit stream started...")

for submission in subreddits.stream.submissions():
    post = {
        "title": submission.title,
        "body": submission.selftext,
        "url": submission.url,
        "created_utc": submission.created_utc,
        "subreddit": submission.subreddit.display_name
    }
    print(f"📝 {post['title']}")
    collection.insert_one(post)
