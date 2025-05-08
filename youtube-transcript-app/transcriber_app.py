import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi

def get_youtube_id(url):
    if "watch?v=" in url:
        return url.split("watch?v=")[-1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[-1].split("?")[0]
    return None

def fetch_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return "\n".join([entry["text"] for entry in transcript])
    except Exception as e:
        return f"❌ Could not fetch transcript: {e}"

st.title("📄 YouTube Transcript Extractor")

url = st.text_input("Paste a YouTube URL:")

if st.button("Get Transcript"):
    if not url:
        st.warning("Please enter a YouTube URL.")
    else:
        video_id = get_youtube_id(url)
        if video_id:
            st.info("🔎 Fetching transcript...")
            result = fetch_transcript(video_id)
            st.text_area("Transcript", result, height=300)
        else:
            st.error("❌ Invalid YouTube URL.")
