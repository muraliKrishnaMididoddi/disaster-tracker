# nlp_classify.py
import spacy
from transformers import pipeline
from pymongo import MongoClient

# Load NLP models
nlp = spacy.load("en_core_web_sm")
classifier = pipeline("text-classification", model="lvwerra/distilbert-imdb")

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["rumor_db"]
collection = db["reddit_posts"]

print("🔍 Processing unclassified posts...")

# Fetch unprocessed posts
posts = collection.find({
    "$or": [
        {"processed": False},
        {"processed": {"$exists": False}}
    ]
})


for post in posts:
    text = post["title"] + " " + post.get("body", "")

    # 1. Location Extraction
    doc = nlp(text)
    locations = [ent.text for ent in doc.ents if ent.label_ == "GPE"]

    # 2. Classification
    result = classifier(text[:512])[0]  # Truncate to 512 tokens
    label = result["label"]
    score = round(result["score"], 2)

    # 3. Update MongoDB with location and classification
    collection.update_one(
        {"_id": post["_id"]},
        {
            "$set": {
                "location": locations,
                "label": label,
                "confidence": score,
                "processed": True
            }
        }
    )
    print(f"✅ Processed: {post['title'][:60]}... → {label} ({score}) | Locations: {locations}")
