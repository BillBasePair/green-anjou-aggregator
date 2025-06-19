import feedparser
import streamlit as st

st.title("Grant Opportunity Monitor")
feed_url = "https://grants.nih.gov/grants/guide/rss_updates.xml"
feed = feedparser.parse(feed_url)

st.header("Latest NIH Grant Opportunities")
for entry in feed.entries[:5]:  # Show top 5 entries
    st.write(f"**Title:** {entry.title}")
    st.write(f"**Link:** [{entry.link}]")
    st.write(f"**Published:** {entry.published}")
    st.write("---")