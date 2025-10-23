import streamlit as st
from youtube_downloader_core import download_youtube

st.set_page_config(page_title="YouTube Downloader")
st.title("🎬 YouTube Downloader")

url = st.text_input("Enter YouTube URL:")
audio_only = st.checkbox("Audio Only (MP3)", value=False)
resolution = st.selectbox("Max Resolution", ["1080", "720", "480", "360"])
download_path = st.text_input("Download Folder", value="~/downloads")

if st.button("Download"):
    with st.spinner("Downloading..."):
        msg = download_youtube(url, audio_only=audio_only, resolution=resolution, download_path=download_path)
    st.success(msg) if msg.startswith("✅") else st.error(msg)