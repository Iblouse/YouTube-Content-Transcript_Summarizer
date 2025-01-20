from dotenv import load_dotenv
import streamlit as st 
import os
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai

# Load all environment variables from .env file
load_dotenv()

# Configure the Google Generative AI with the API key from the environment variable
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define the prompt template for summarizing YouTube transcripts
prompt = """
You are an expert YouTube video summarizer. You will take the transcript
text and summarize the entire video and the most important points within
300 words. The transcript text will be appended here: 
"""

def extract_transcript_details(youtube_video_url):
    """
    Extracts the transcript details from a given YouTube video URL.

    Parameters:
    youtube_video_url (str): URL of the YouTube video.

    Returns:
    str: Transcript of the YouTube video.
    """
    try:
        # Extract the video ID from the URL
        video_id = youtube_video_url.split("=")[1]
        
        # Get the transcript using YouTubeTranscriptApi
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Concatenate the transcript text into a single string
        transcript = " ".join([item["text"] for item in transcript_data])
        
        return transcript
    
    except IndexError:
        raise ValueError("Invalid YouTube URL. Please ensure it includes the video ID.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while fetching the transcript: {e}")

def get_gemini_response(transcript_text, prompt):
    """
    Generates a summary response from the transcript using Google Generative AI.

    Parameters:
    transcript_text (str): Transcript text to summarize.
    prompt (str): Prompt template to guide the summary.

    Returns:
    str: Summary of the transcript.
    """
    try:
        # Create an instance of the GenerativeModel | you experiment with other models 
        model = genai.GenerativeModel('gemini-pro')
        
        # Generate content based on the prompt and transcript text
        response = model.generate_content(prompt + transcript_text)
        
        return response.text
    except Exception as e:
        raise RuntimeError(f"An error occurred while generating the summary: {e}")

# Streamlit Application UI
st.title("YouTube Content Transcript Summarizer App")
youtube_url = st.text_input("Enter YouTube Video Link:")

# Display the thumbnail of the YouTube video if a valid URL is entered
if youtube_url:
    try:
        video_id = youtube_url.split("=")[1]
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
    except IndexError:
        st.error("Invalid YouTube URL. Please ensure it includes the video ID.")

# Generate and display the summarized transcript when the button is clicked
if st.button("Get Summarized Video Transcript"):
    try:
        transcript_text = extract_transcript_details(youtube_url)
        
        if transcript_text:
            summary = get_gemini_response(transcript_text, prompt)
            st.markdown("## Contents Summary:")
            st.write(summary)
    except Exception as e:
        st.error(f"An error occurred: {e}")
