import streamlit as st
import pandas as pd
from transformers import pipeline

# Page config
st.set_page_config(page_title="Call Transcript Summarizer")
st.title("📞 Call Transcript Summarizer")

# Load model once
@st.cache_resource
def load_model():
    return pipeline("summarization", model="t5-small")

summarizer = load_model()

# File uploader (supports CSV and Excel)
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    # Load file
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file, engine="openpyxl")
    except Exception as e:
        st.error(f"❌ Error reading file: {e}")
        st.stop()

    # Check for Call_Transcript column
    if "Review Text" not in df.columns:
        st.error("❌ 'Review Text' column not found in the uploaded file.")
        st.stop()

    st.success(f"✅ File loaded: {uploaded_file.name} | Rows: {len(df)}")

    if st.button("Summarize Transcripts"):
        with st.spinner("🔄 Summarizing call transcripts..."):
            def summarize_text(text):
                if pd.isna(text) or len(str(text).strip()) < 30:
                    return ""
                try:
                    result = summarizer(text, max_length=60, min_length=10, do_sample=False)
                    return result[0]["summary_text"]
                except Exception as e:
                    return f"[Summary Error: {e}]"

            df["Summary"] = df["Review Text"].apply(summarize_text)

        st.success("✅ Summarization complete!")
        st.dataframe(df[["Review Text", "Summary"]])

        # Download buttons
        csv_download = df.to_csv(index=False)
        st.download_button("📥 Download CSV", csv_download, file_name="summarized_calls.csv", mime="text/csv")

        excel_download = df.to_excel("temp_summary.xlsx", index=False, engine="openpyxl")
        with open("temp_summary.xlsx", "rb") as f:
            st.download_button("📥 Download Excel", f, file_name="summarized_calls.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
