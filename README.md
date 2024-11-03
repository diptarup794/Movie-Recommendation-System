

# Movie Recommendation System User Guide

Welcome to the Movie Recommendation System! This app recommends movies similar to your favorite movies using machine learning.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Using the App](#using-the-app)
- [Troubleshooting](#troubleshooting)
- [Acknowledgments](#acknowledgments)

## Overview

The Movie Recommendation System is built with Streamlit, using a pre-trained machine learning model to suggest movies similar to a selected title. With a few clicks, you can find new movies that match your interests.

## Features

- **Select a Movie**: Choose a movie from the dropdown menu.
- **Get Recommendations**: Find similar movies instantly with a single click.
- **Simple Interface**: Clean and easy-to-navigate interface.

## Getting Started

To run the app, make sure you have the following:

1. **Requirements**: 
    - Python 3.x
    - Required libraries (install using `pip install -r requirements.txt`)
    - Pre-trained model files: `movie_list.pkl` and `similarity.pkl`.

2. **Installation**: Clone or download the app files, and ensure you have the model files in the correct location:
    ```shell
    git clone <repository-link>
    cd <repository-folder>
    ```
3. **Run the App**: Start the app with Streamlit.
    ```shell
    streamlit run app.py
    ```

## Using the App

1. **Select a Movie**: 
    - Navigate to the dropdown menu, start typing, or select a movie title you like.
    
2. **Show Recommendations**:
    - Click the **Show Recommendations** button. The app will list five similar movies.

3. **Reading Recommendations**:
    - Recommended movies will appear in a simple list under the movie title you selected.

## Troubleshooting

- **Error: 'No recommendations found'**: If the app cannot find recommendations, try selecting a different movie. This may happen if the selected movie has limited similarity data.
- **File Not Found Error**: Ensure `movie_list.pkl` and `similarity.pkl` files are in the correct directory as specified in the code (`/path/to/movie_list.pkl` and `/path/to/similarity.pkl`).

## Acknowledgments

This recommendation system uses similarity data and a pre-trained machine learning model to deliver recommendations. Thank you for using the Movie Recommendation System, and happy watching!

---

This guide provides a clear outline for users on how to get started and use the app effectively.
