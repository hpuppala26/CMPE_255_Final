# Music Recommendation System using the Million Song Dataset

**Project Report:** https://docs.google.com/document/d/1It3ln8EGJi4BXIC57_BM-1H0mTwemzmmUUIhJL1rQzM/edit?usp=sharing

## Overview

This project leverages the Million Song Dataset (MSD) and the Taste Profile subset to develop an advanced music recommendation system. By utilizing various machine learning algorithms and integrating song metadata, we aim to provide personalized music recommendations. This repository contains the code, datasets, and resources used for the project.

## Installation
Clone the repository.
```bash
git clone https://github.com/hpuppala26/CMPE_255_Final
cd CMPE_255_Final
```

Install Requirements and Run Code
```bash
python -m venv testenv
source testenv/bin/activate
pip install -r requirements.txt
python app.py
```

## Dataset
The Million Song Dataset (MSD) and the Taste Profile subset are used in this project. The data includes user-song interactions, metadata, and song lyrics. It includes detailed audio features and metadata of over a million tracks.

## Data Preprocessing Steps
Efficient data preprocessing is critical for ensuring the quality and usability of our dataset:

**Data Cleaning:** We start by eliminating inaccuracies and redundant information from the dataset. This involves correcting any anomalies in song titles or artist names and removing entries that lack essential data.

**Data Standardization:** We ensure consistency across the dataset by standardizing text formats and other data types. This uniformity is crucial for accurate analysis and algorithm performance.

**Data Filtering:** We selectively filter the dataset to focus on relevant data points. For example, we may exclude songs with very few listens as they do not contribute significantly to pattern recognition or prediction accuracy.

**Data Enrichment:** Finally, we enhance the dataset by incorporating additional relevant information, such as categorizing songs by release periods or adding computed audio features. This step improves the dataset's depth, aiding in more nuanced analysis and recommendations.

These preprocessing steps transform our dataset into a clean, consistent, and comprehensive resource, ready for effective analysis and model building in our music recommendation project.








## Baseline Models
Singular Value Decomposition and a neural network\
Neural Collaborative Filtering\
Hybrid AutoEncoder Model

## Results
Our models have shown significant improvement in recommendation accuracy:

- SVD + Neural Network achieved the lowest RMSE and MAE, proving to be good models.
- AutoEncoders based Neural Network showed considerable effectiveness in managing sparse data.
- Detailed results and comparisons are available in the results section of the project report.

## Future Work
**Algorithm Optimization:** Further tuning and testing of algorithms for better scalability and real-time processing.
**Data Expansion:** Including more diverse data types like real-time user feedback.
**Domain Expansion:** Adapting the methodology for other recommendation systems like movies or books.


## Conclusion
This project successfully developed a sophisticated music recommendation system using the Million Song Dataset. The hybrid SVD and neural network model achieved the best performance, demonstrating the potential of combining classical and modern machine learning techniques.


