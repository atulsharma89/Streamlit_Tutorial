# Streamlit 10-Day Study Plan

## Overview

This repository provides a structured 10-day study plan to help you learn Streamlit, a powerful Python library for building interactive web applications for data science and machine learning. The plan covers a range of topics from basic concepts to advanced features and culminates in building and deploying a complete Streamlit application.

## Prerequisites

*   Basic understanding of Python programming.
*   A code editor (e.g., VS Code, Sublime Text, Atom).
*   A terminal or command prompt.
*   Git (optional, but recommended for version control).

## Setup

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd streamlit-10-day-study-plan
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    # Activate the virtual environment (Linux/macOS)
    source venv/bin/activate
    # Activate the virtual environment (Windows)
    venv\Scripts\activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    If you don't have a `requirements.txt` file, you can create one by running:

    ```bash
    pip freeze > requirements.txt
    ```

    This will capture your current environment's dependencies.  Make sure you only have the dependencies for this project installed when you run this command.

## Study Plan

The study plan is divided into 10 days, each focusing on specific topics and including practical exercises. Follow the plan in order for the best learning experience.

**Day 1: Introduction to Streamlit - Core Concepts and Setup**

*   Topics: What is Streamlit? Installation, basic commands (`st.write`, `st.title`, `st.markdown`, `st.code`), running your first app, Streamlit's execution model.
*   Exercises: Create a simple "About Me" app.
*   Location: `Day 1/`

**Day 2: User Input Widgets - Mastering Interaction**

*   Topics: `st.button`, `st.checkbox`, `st.radio`, `st.selectbox`, `st.multiselect`, `st.slider`, `st.text_input`, `st.number_input`, `st.date_input`, `st.time_input`, `st.form`.
*   Exercises: Build a "Configuration Panel" app and a simple calculator app.
*   Location: `Day 2/`

**Day 3: Data Loading and Display - Working with DataFrames**

*   Topics: Loading data from CSV, Excel, JSON, databases, and web APIs, data cleaning and preprocessing with Pandas, `st.dataframe`, `st.table`, `st.json`.
*   Exercises: Build a "Data Explorer" app.
*   Location: `Day 3/`

**Day 4: Data Visualization - Charts and Plots**

*   Topics: `st.line_chart`, `st.bar_chart`, `st.area_chart`, `st.scatter_chart`, `st.pyplot`, `st.map`, integration with Matplotlib, Altair, and Plotly, `st.image`.
*   Exercises: Expand the "Data Explorer" app to include visualizations.
*   Location: `Day 4/`

**Day 5: Layout and Structure - Creating a Professional UI**

*   Topics: `st.sidebar`, `st.columns`, `st.expander`, `st.tabs`, `st.container`, `st.empty`, custom CSS.
*   Exercises: Refactor the "Data Explorer" app to improve its UI.
*   Location: `Day 5/`

**Day 6: Caching and Performance Optimization**

*   Topics: `@st.cache_data`, `@st.cache_resource`, cache invalidation, `st.spinner`, `st.progress`, profiling.
*   Exercises: Add a computationally intensive task to the "Data Explorer" app and optimize its performance.
*   Location: `Day 6/`

**Day 7: State Management - Building Interactive Applications**

*   Topics: `st.session_state`, persisting user input, tracking multi-step processes, implementing undo/redo, managing authentication.
*   Exercises: Build a "To-Do List" app and a simple quiz app.
*   Location: `Day 7/`

**Day 8: Advanced Features and Components**

*   Topics: (Choose one or two) Streamlit Components, Streamlit AgGrid, Streamlit Ace Editor, Streamlit PDF Viewer.
*   Exercises: Implement one or two of the advanced features in your existing apps.
*   Location: `Day 8/`

**Day 9: Deployment - Sharing Your Applications**

*   Topics: Deploying to Streamlit Community Cloud, Heroku, AWS, GCP, Docker, setting up environment variables and secrets.
*   Exercises: Deploy your "Data Explorer" or "To-Do List" app to Streamlit Community Cloud.
*   Location: `Day 9/`

**Day 10: Project Day - Building a Complete Application**

*   Topics: Project planning, development, deployment.
*   Exercises: Build a complete Streamlit application from scratch.
*   Location: `Day 10/`

## Running the Example Code

To run the example code for each day, navigate to the corresponding directory in your terminal and use the following command:

```bash
streamlit run <example_file.py>
