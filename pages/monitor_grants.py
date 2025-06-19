import streamlit as st
import feedparser

st.title("Grant Opportunity Monitor")
feed_url = "https://grants.nih.gov/grants/guide/newsfeed/fundingopps.xml"  # New feed URL
st.write(f"Attempting to fetch feed from: {feed_url}")

try:
    feed = feedparser.parse(feed_url)
    st.write(f"Feed status: {feed.status} | Bozo: {feed.bozo}")  # Debug info
    if feed.entries:
        st.header("Latest NIH Grant Opportunities")
        for entry in feed.entries[:5]:  # Show top 5 entries
            st.write(f"**Title:** {entry.title}")
            st.write(f"**Link:** [{entry.link}]")
            st.write(f"**Published:** {entry.published}")
            st.write("---")
    else:
        st.write("No entries found in the feed. The RSS feed may be empty or inaccessible.")
except Exception as e:
    st.write(f"Error fetching feed: {e}")