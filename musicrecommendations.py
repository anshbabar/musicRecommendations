# -*- coding: utf-8 -*-
"""musicRecommendations.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IoemerNJkPyAeecX8nSUWwsAlHsKovhD
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Collecting Data
dataset = pd.DataFrame({'song': ['Happier', 'Bohemian Rhapsody', 'Imagine', 'Shape of You', 'Yesterday',
                                 'Don\'t Stop Believin\'', 'Rolling in the Deep', 'Smells Like Teen Spirit', 'Wonderwall', 'Dancing Queen',
                                 'Sweet Child O\' Mine', 'Hotel California', 'Despacito', 'All Star', 'Hey Jude'],
                        'mood': ['happy', 'powerful', 'peaceful', 'energetic', 'nostalgic',
                                 'uplifting', 'soulful', 'rebellious', 'melancholic', 'joyful',
                                 'passionate', 'timeless', 'upbeat', 'fun', 'emotional']})

# Feature Extraction
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(dataset['song'])
y = dataset['mood']

# Training the Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

# Deploying the Model
def recommend_song(mood):
    # Preprocessing user input
    X_user = vectorizer.transform([mood])
    # Predicting the mood based on user input
    predicted_mood = model.predict(X_user)[0]
    # Filtering songs based on predicted mood
    recommended_songs = dataset[dataset['mood'] == predicted_mood]['song']

    return recommended_songs


user_mood = input("Enter your current mood: ")
recommended_songs = recommend_song(user_mood)

if recommended_songs.empty:
    print("Sorry, no songs found for your current mood.")
else:
    print("Recommended songs:")
    for song in recommended_songs:
        print("- " + song)