import streamlit as st
from scraper import get_links
from email_extractor import extract_email
import pandas as pd

st.title("Smart Lead Generator 🚀")

query = st.text_input("Enter keyword (e.g. AI startups India)")

if st.button("Generate Leads"):
    links = get_links(query)

    data = []

    for link in links:
        email = extract_email(link)

        score = "High" if email != "Not Found" else "Low"

        data.append({
            "Website": link,
            "Email": email,
            "Score": score
        })

    df = pd.DataFrame(data)
    df = df.drop_duplicates()

    st.write(df)

    csv = df.to_csv(index=False)
    st.download_button("Download CSV", csv, "leads.csv")