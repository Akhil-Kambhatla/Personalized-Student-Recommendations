import streamlit as st
from utils import calculate_performance_metrics, load_data, summarize_performance
from main import identify_weak_areas, analyze_trends, analyze_performance
from recommendations import generate_recommendations, define_persona
import numpy as np
import matplotlib.pyplot as plt
import json

# Load data
current_quiz = load_data(r"C:\Users\akhil\OneDrive\Desktop\Student Recommendations\current_quiz_data.json")
historical_quiz = load_data(r"C:\Users\akhil\OneDrive\Desktop\Student Recommendations\hist_quiz_data.json")
historical_quiz = analyze_performance(historical_quiz)

# Analysis
weak_topics, weak_difficulty = identify_weak_areas(historical_quiz)
trends = analyze_trends(historical_quiz)
persona = define_persona(weak_topics, weak_difficulty)

# Dashboard
st.title("NEET Testline - Performance Dashboard")
st.subheader("Student Performance Analysis")

# Weak Areas
st.header("Weak Topics")
if weak_topics.size > 0:
    st.write(weak_topics)  # Display weak topics (if any)
else:
    st.write("No weak topics identified.")
    
# Weak difficulty levels
st.header("Weak Difficulty Levels")
if weak_difficulty.size > 0:
    st.write(weak_difficulty)  # Display weak difficulty levels (if any)
else:
    st.write("No weak difficulty levels identified.")


# Recommendations
st.write("### Recommendations")
recommendations = generate_recommendations(weak_topics, weak_difficulty)
if recommendations:
    st.write(recommendations)
else:
    st.write("No recommendations available.")

# Persona
st.write(f"### Persona: {persona}")
print(persona)

# Main block
if __name__ == "__main__":
    # Replace 'performance_analysis.json' with your actual data file path
    with open(r"C:\Users\akhil\OneDrive\Desktop\Student Recommendations\performance_analysis.json", "r") as perf_file:
        historical_performance = json.load(perf_file)