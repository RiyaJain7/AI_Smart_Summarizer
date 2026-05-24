import streamlit as st
import nltk

# Download tokenizer data
nltk.download('punkt_tab')
nltk.download('punkt')

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Study Assistant Pro",
    page_icon="🧠",
    layout="centered"
)

# ---------------- HEADER ----------------

st.title("🧠 AI Study Assistant Pro")

st.markdown("""
### 📚 Transform Articles into:
- 📌 Smart Summaries
- 📝 Quick Notes
- 🧠 Keyword Mind Maps
- 🌐 English & Hindi Support
""")

# ---------------- LANGUAGE SELECTOR ----------------

language = st.selectbox(
    "🌐 Select Language",
    ["English", "Hindi"]
)

# ---------------- TEXT INPUT ----------------

article = st.text_area(
    "📄 Paste your article or notes here:",
    height=300
)

# ---------------- SUMMARY FUNCTION ----------------

def generate_summary(text, language):

    # ENGLISH SUMMARY

    if language == "English":

        parser = PlaintextParser.from_string(
            text,
            Tokenizer("english")
        )

        summarizer = LsaSummarizer()

        summary = summarizer(
            parser.document,
            3
        )

        final_summary = ""

        for sentence in summary:

            final_summary += str(sentence) + " "

        return final_summary

    # HINDI SUMMARY

    else:

        sentences = text.split("।")

        short_summary = "। ".join(sentences[:3])

        return short_summary

# ---------------- BUTTON ----------------

if st.button("🚀 Generate Smart Notes"):

    # EMPTY INPUT CHECK

    if article.strip() == "":

        st.warning("⚠️ Please paste some text first.")

    else:

        # GENERATE SUMMARY

        final_summary = generate_summary(
            article,
            language
        )

        # ---------------- SUMMARY ----------------

        st.subheader("📌 Smart Summary")

        st.success(final_summary)

        # ---------------- NOTES ----------------

        st.subheader("📝 Quick Notes")

        if language == "English":

            notes = final_summary.split(".")

        else:

            notes = final_summary.split("।")

        for note in notes:

            if note.strip() != "":

                st.write(f"✅ {note}")

        # ---------------- MIND MAP ----------------

        st.subheader("🧠 Keyword Mind Map")

        words = article.split()

        important_words = []

        for word in words:

            clean_word = word.lower()

            if len(clean_word) > 5:

                important_words.append(clean_word)

        unique_words = list(set(important_words))

        for word in unique_words[:10]:

            st.write(f"🔹 {word}")

        # ---------------- ANALYTICS ----------------

        st.subheader("📊 Article Analytics")

        total_words = len(article.split())

        reading_time = round(total_words / 200, 2)

        st.write(f"📄 Total Words: {total_words}")

        st.write(
            f"⏱ Estimated Reading Time: {reading_time} mins"
        )

        # ---------------- DOWNLOAD BUTTON ----------------

        st.download_button(
            label="📥 Download Notes",
            data=final_summary,
            file_name="study_notes.txt",
            mime="text/plain"
        )

# ---------------- FOOTER ----------------

st.markdown("---")

st.caption("✨ Developed using Streamlit + NLP")