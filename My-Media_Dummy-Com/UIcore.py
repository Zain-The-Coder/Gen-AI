import streamlit as st

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

load_dotenv()

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="centered"
)

# -----------------------------
# Prompt Template
# -----------------------------

prompt = ChatPromptTemplate.from_messages([

    (
        "system",
        """
You Are A Professional Movie Information Extraction Assistant.

Your task:

Extract useful structured information from a movie paragraph and present it in a content.

Rules:

- Do not add explanations
- Do not add extra commentary
- Follow the exact format
- If information is missing then write NULL
- Keep summary short (2-3 lines max)
- Do not guess unknown facts

OUTPUT FORMAT:

Movie Title :

Release Year :

Genre :

Director :

Main Cast :

Setting/Location :

Plot :

Themes :

Rating :

Notable Features :

Short Summary :
"""
    ),

    (
        "human",
        """
Extract information from this paragraph:

{paragraph}
"""
    )
])

# -----------------------------
# UI
# -----------------------------

st.title("🎬 Movie Information Extractor")
st.write("Enter a movie paragraph and extract structured information.")

paragraph = st.text_area(
    "Movie Paragraph",
    value="""Phir Hera Pheri is a 2006 Bollywood comedy film directed by Neeraj Vora and starring Akshay Kumar as Raju, Suniel Shetty as Shyam, and Paresh Rawal as Baburao Ganpatrao Apte. The story continues the adventures of the three friends, who are looking for an easy way to become rich. Raju becomes involved in a deal that promises a huge amount of money, convincing Shyam and Baburao to invest their savings. However, their plan quickly goes wrong when they become trapped in a complicated situation involving debt, deception, and dangerous criminals. Much of the story takes place in Mumbai and revolves around the trio's attempts to escape their financial problems. The film is known for its comedy, memorable dialogues, chaotic situations, and the chemistry between its three main characters. Its major themes include friendship, greed, money, deception, and the consequences of trying to get rich quickly.""",
    height=250
)

# -----------------------------
# Extract Button
# -----------------------------

if st.button("Extract Movie Information", use_container_width=True):

    if paragraph.strip():

        final_prompt = prompt.invoke(
            {"paragraph": paragraph}
        )

        model = ChatMistralAI(
            model="mistral-small-2506"
        )

        response = model.invoke(final_prompt)

        st.subheader("Extracted Information")
        st.text(response.content)

    else:
        st.warning("Please enter a movie paragraph.")