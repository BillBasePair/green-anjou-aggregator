import streamlit as st

st.title("Green Anjou v1.0 - Grant Search Aggregator")
presets = {
    "Aptamer/Bioengineering": "aptamer, biosensor, SELEX",
    "Neuro & Immunology": "neuroinflammation, Parkinson’s, MS",
    "Opioid & Detection": "opioid, fentanyl, detection"
}
preset = st.selectbox("Select Preset", list(presets.keys()), index=0)
keywords = st.text_input("Custom Keywords (comma-separated)", value=presets[preset]).replace(" ", "+").replace(",", "+")

if st.button("Update Searches"):
    st.rerun()

st.header("Search Results")
st.subheader("NIH RePORTER")
nih_url = f"https://reporter.nih.gov/search?terms={keywords}"
st.markdown(f"NIH RePORTER: [View Results]({nih_url})")

st.subheader("SBIR.gov")
sbir_url = f"https://www.sbir.gov/sbirsearch?keywords={keywords}"
st.markdown(f"SBIR.gov: [View Results]({sbir_url})")

st.subheader("Grants.gov")
grants_url = f"https://www.grants.gov/search-grants?keywords={keywords}"
st.markdown(f"Grants.gov: [View Results]({grants_url})")

st.subheader("Gates Foundation")
gates_url = f"https://www.gatesfoundation.org/what-we-do/global-health/grand-challenges?query={keywords}"
st.markdown(f"Gates Foundation: [View Results]({gates_url})")

st.subheader("Wellcome Trust")
wellcome_url = f"https://wellcome.org/grants-funding/funding-schemes?search={keywords}"
st.markdown(f"Wellcome Trust: [View Results]({wellcome_url})")

st.subheader("Michael J. Fox Foundation")
fox_url = f"https://www.michaeljfox.org/funding-opportunities?search={keywords}"
st.markdown(f"Michael J. Fox Foundation: [View Results]({fox_url}) (Note: Manual search may be required)")

st.subheader("CPRIT")
cprit_url = f"https://www.cprit.state.tx.us/funding-opportunities?keywords={keywords}"
st.markdown(f"CPRIT: [View Results]({cprit_url}) (Note: Manual search may be required)")