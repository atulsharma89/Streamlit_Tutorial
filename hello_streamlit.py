'''
Day 1: Introduction to Streamlit - The Basics

Goal: Understand the core concepts of Streamlit and build a simple "Hello, World!" application.
Topics:
What is Streamlit? (Purpose, advantages, use cases)
Installation: pip install streamlit
Basic Streamlit commands:
st.write(): Display text, data, and more.
st.title(), st.header(), st.subheader():  Text formatting.
st.markdown(): Using Markdown for formatting.
st.code(): Displaying code snippets.

Running your first Streamlit app: streamlit run your_app.py
Understanding Streamlit's execution model (how it re-runs the script on every interaction).

Activities:
Follow the official Streamlit "Hello, World!" tutorial: https://streamlit.io/ (Look for "Get Started" or "Build your first app")
Create a simple app that displays:
A title and a welcome message.
A short paragraph of text with some Markdown formatting (e.g., bold, italics, a link).
A code snippet (e.g., a simple Python function).
'''

import streamlit as st

# Title
st.title("Hello Streamlit")
# Header
st.header("This is a header")

# Subheader

st.subheader("This is a subheader")

# Text  : to display raw text in your app, essentially writing a string of text to the page.

st.text("### This is a text")

# Text with Markdown
st.text("This is a **text** with Markdown")

# Markdown
st.markdown("### This is a markdown")
st.markdown("This is a paragraph with some **bold text**, *italicized text*, and a [link to Google](https://www.google.com). Isn't that neat?")

# Code
st.code("import streamlit as st")
# Success
st.success("This is a success")
# Info
st.info("This is a info")
# Warning
st.warning("This is a warning")
# Error
st.error("This is a error")
# Exception
st.exception("NameError('name is not defined')")
# Displaying Data   