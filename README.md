# 🌍 Real-Time Disaster Misinformation Tracker

A real-time NLP-powered system that monitors Reddit for disaster-related content, detects potential misinformation, extracts location data, and visualizes verified vs. false posts on an interactive world map.

> 🛠 Built with Python, PRAW, MongoDB, Hugging Face Transformers, spaCy, and Streamlit.

---

## 🚀 Features

- ✅ Real-time Reddit stream of posts from disaster-related subreddits
- 🧠 NLP pipeline for location extraction and fake/real classification using BERT
- 🌐 Interactive map dashboard with location pins, labels, and confidence scores
- 📦 MongoDB integration for persistence and enrichment tracking
- 🔁 Automated classification of unprocessed posts
- 🔍 Focused on disaster-related keywords like earthquakes, floods, wildfires

---

## 🎯 Use Case

During natural disasters or geopolitical events, misinformation spreads rapidly. This tool helps:
- First responders monitor credible alerts
- Journalists detect emerging rumors
- Governments visualize threat propagation
- Researchers study false information trends

---

## 🧩 Tech Stack

| Layer           | Tools/Libs                                |
|----------------|--------------------------------------------|
| **Streaming**   | `praw` (Reddit API)                        |
| **Storage**     | `MongoDB`                                  |
| **NLP**         | `spaCy`, `transformers`, `BERT`            |
| **Geolocation** | `geopy`, `Nominatim`                       |
| **Dashboard**   | `Streamlit`, `Folium`, `streamlit-folium` |

---

## 📁 Folder Structure

disaster_tracker/
├── reddit_stream.py # Streams live posts to MongoDB
├── nlp_classify.py # Processes, classifies, and tags locations
├── map_dashboard.py # Interactive map of results
├── .env # Reddit API keys
└── README.md # You're here!


---

## ⚙️ How to Run

### 1. Clone Repo and Install Dependencies

```bash
git clone https://github.com/your-username/disaster-tracker.git
cd disaster-tracker
pip install -r requirements.txt
