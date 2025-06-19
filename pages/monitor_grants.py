import streamlit as st
import feedparser

st.title("Grant Opportunity Monitor")

# Preset feed options
feed_options = {
    "NIH Funding Opportunities": "https://grants.nih.gov/grants/guide/newsfeed/fundingopps.xml"
    # Add more feeds as discovered (e.g., SBIR.gov if available)
}
selected_feed = st.selectbox("Select Feed Source", list(feed_options.keys()), index=0)
feed_url = feed_options[selected_feed]
st.write(f"Attempting to fetch feed from: {feed_url}")

try:
    feed = feedparser.parse(feed_url)
    st.write(f"Feed status: {feed.status} | Bozo: {feed.bozo}")  # Debug info
    if feed.entries:
        st.header(f"Latest {selected_feed}")
        for entry in feed.entries[:5]:  # Show top 5 entries
            st.write(f"**Title:** {entry.title}")
            st.write(f"**Link:** [{entry.link}]")
            st.write(f"**Published:** {entry.published}")
            st.write("---")
    else:
        st.write(f"No entries found in the {selected_feed} feed. It may be empty or inaccessible.")
except Exception as e:
    st.write(f"Error fetching feed: {e}")