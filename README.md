# 📞 Call Transcript Summarizer

This Streamlit app summarizes customer call transcripts using advanced NLP models. Upload a CSV or Excel file with call transcripts, and the app will generate concise summaries for each entry.

---

## ✨ Features

- ✅ Upload `.csv` or `.xlsx` files
- ✅ Automatically detects and summarizes the `Call_Transcript` column
- ✅ Built using Hugging Face's `t5-small` model
- ✅ Download the output as a summarized `.csv` or `.xlsx`
- ✅ Fully web-based – no installation needed after deployment

---

## 🧾 Input Format

The input file must contain a column named `Call_Transcript`. Example:

| Call_Id | Call_Transcript                                        |
|---------|--------------------------------------------------------|
| 1001    | I called because I couldn’t access my payment portal.  |
| 1002    | I need to confirm the amount due for this month.       |

---

## 🚀 How to Use

1. Click "Browse files" to upload your input `.csv` or `.xlsx`
2. Click "Summarize Transcripts"
3. Preview the summaries in the app
4. Click to download the output file

---

## 📦 Tech Stack

- Python
- Streamlit
- Hugging Face Transformers (`t5-small`)
- Pandas
- Openpyxl

---

## 🧠 Future Improvements

- Support for extractive or hybrid summarization
- Model selection dropdown
- Larger transcript handling with chunking

---

## 🤝 Contributing

Feel free to fork this repo and enhance it! Pull requests are welcome.


