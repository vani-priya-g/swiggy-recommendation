# 🍽️ Swiggy Restaurant Recommendation System

This project is a restaurant recommender system inspired by Swiggy. Users can select their city, preferred cuisine, budget, and rating to get personalized restaurant recommendations.

## 🚀 Features
- Filter by city, cuisine, rating, and cost
- Restaurant recommendations using K-Means clustering
- User-friendly web interface built with Streamlit
- Animated UI and custom styling
- Cleaned and encoded data using One-Hot Encoding

## 📁 Files
- `swiggy.py` – Main Streamlit app
- `clean.ipynb` – Data preprocessing notebook
- `cleaned_data.csv` – Cleaned restaurant data
- `encoded_data.csv` – One-Hot encoded dataset
- `encoder.pkl` – Pickled encoder object
- `requirements.txt` – Libraries needed to run the app

## 🧠 Technologies Used
- Python
- Pandas
- Scikit-learn
- Streamlit

## 📦 Installation

```bash
pip install -r requirements.txt
streamlit run swiggy.py
