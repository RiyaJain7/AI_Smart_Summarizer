import streamlit as st
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

st.set_page_config(
    page_title="AI Study Assistant Pro",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 AI Study Assistant Pro")

st.write(
    "Transform long articles into summaries, notes, and mind maps instantly."
)

article = st.text_area(
    "📄 Paste your article here:",
    height=300
)

def generate_summary(text):

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

if st.button("🚀 Generate AI Study Notes"):

    if article.strip() == "":
        st.warning("Please enter article text.")

    else:

        final_summary = generate_summary(article)

        original_words = len(article.split())
        summary_words = len(final_summary.split())

        st.subheader("📌 Smart Summary")

        st.success(final_summary)

        st.subheader("📝 Key Notes")

        notes = final_summary.split(". ")

        for idx, note in enumerate(notes):

            if note.strip() != "":
                st.write(f"✅ {note}")

        st.subheader("🧠 Mind Map Points")

        for idx, note in enumerate(notes):

            if note.strip() != "":
                st.markdown(f"""
- 📍 {note}
""")

        st.subheader("📊 Statistics")

        st.write(f"Original Words: {original_words}")
        st.write(f"Summary Words: {summary_words}")

        reduction = round(
            ((original_words - summary_words)
            / original_words) * 100,
            2
        )

        st.write(f"Content Reduction: {reduction}%")

        st.download_button(
            label="📥 Download Notes",
            data=final_summary,
            file_name="study_notes.txt",
            mime="text/plain"
        )