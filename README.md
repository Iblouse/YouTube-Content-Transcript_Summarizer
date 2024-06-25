# YouTube Content Transcript Summarizer App

Welcome to the YouTube Content Transcript Summarizer App! This application allows you to extract transcripts from YouTube videos and summarize their content using Google's Generative AI. The app is built using Streamlit and makes use of the YouTube Transcript API and Google Generative AI for content summarization.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Overview

The YouTube Content Transcript Summarizer App is designed to help users quickly get summaries of YouTube video content by extracting and analyzing the transcript. This is particularly useful for getting an overview of lengthy videos without watching them in full.

## Features

- **Transcript Extraction**: Automatically extracts the transcript from a given YouTube video.
- **Content Summarization**: Summarizes the transcript text into a concise overview using Google's Generative AI.
- **Easy to Use**: Simple and intuitive Streamlit interface.
- **Visual Feedback**: Displays video thumbnail and summary results.

## Installation

### Prerequisites

- Python 3.8 or higher
- A Google API key for accessing Generative AI services.

### Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/Iblouse/YouTube-Content-Transcript_Summarizer.git
    cd YouTube-Content-Transcript_Summarizer
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project directory with your Google API key:

    ```bash
    touch .env
    ```

    Add the following line to `.env`:

    ```plaintext
    GOOGLE_API_KEY=your_google_api_key_here
    ```

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run youtube_app.py
    ```

2. Open the app in your browser at `http://localhost:8501`.

3. Enter a YouTube video link in the provided input field and click on "Get Summarized Video Transcript".

4. The app will display the video thumbnail and a summarized version of the video content.

## Project Structure

```
YouTube-Content-Transcript_Summarizer/
│
├── .env                # Environment variables
├── requirements.txt    # Required Python packages
├── youtube_app.py      # Main application code
└── README.md           # Project documentation
```
