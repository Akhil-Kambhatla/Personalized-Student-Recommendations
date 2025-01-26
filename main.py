import json
import pandas as pd

# File paths (use raw strings to avoid escape sequence issues on Windows)
historical_data_path = r'C:\Users\akhil\OneDrive\Desktop\Student Recommendations\hist_quiz_data.json'
current_quiz_data_path = r'C:\Users\akhil\OneDrive\Desktop\Student Recommendations\current_quiz_data.json'

# Function to analyze performance from historical data
def analyze_performance(historical_data):
    results = []
    for entry in historical_data:
        performance = {
            "user_id": entry["user_id"],
            "quiz_id": entry["quiz_id"],
            "score": entry["score"],
            "accuracy": float(entry["accuracy"].strip('%')) / 100,
            "speed": int(entry["speed"]),
            "final_score": float(entry["final_score"]),
            "correct_answers": entry["correct_answers"],
            "incorrect_answers": entry["incorrect_answers"],
            "total_questions": entry["total_questions"],
            "negative_score": float(entry["negative_score"]),
            "duration": entry["duration"],
            "better_than": entry["better_than"],
            "rank_text": entry["rank_text"]
        }
        results.append(performance)
    return results

# Function to calculate accuracy by grouping data
def calculate_accuracy(data, group_by):
    """Calculate the accuracy by grouping data."""
    # Convert the list of dictionaries to a DataFrame if it's a list
    if isinstance(data, list):
        data = pd.DataFrame(data)

    # Ensure the DataFrame contains the necessary columns
    if 'correct_answers' not in data.columns or 'total_questions' not in data.columns:
        raise ValueError("The DataFrame does not contain required columns: 'correct_answers' or 'total_questions'.")

    # Group by the specified column and calculate accuracy
    grouped = data.groupby(group_by).apply(
        lambda x: x['correct_answers'].sum() / x['total_questions'].sum()
    )
    return grouped

# Function to analyze trends in historical data
def analyze_trends(historical_data):
    """Analyze trends in historical data by quiz_id."""
    if isinstance(historical_data, list):
        historical_data = pd.DataFrame(historical_data)

    # Ensure that the DataFrame contains the required columns
    if 'quiz_id' not in historical_data.columns or 'score' not in historical_data.columns:
        raise ValueError("The DataFrame must contain 'quiz_id' and 'score' columns.")

    # Perform the groupby operation
    trends = historical_data.groupby('quiz_id')['score'].mean().reset_index()
    return trends

# Function to identify weak areas based on accuracy
def identify_weak_areas(historical_data):
    """Identify weak topics and difficulty levels."""
    if isinstance(historical_data, list):
        historical_data = pd.DataFrame(historical_data)

    # Ensure required columns are present
    if 'duration' not in historical_data.columns or 'better_than' not in historical_data.columns:
        raise ValueError("The DataFrame does not contain required columns: 'duration' or 'better_than'.")

    # Calculate accuracies
    accuracy_by_time = calculate_accuracy(historical_data, 'duration')
    accuracy_by_difficulty = calculate_accuracy(historical_data, 'better_than')

    # Identify weak topics and difficulty levels (accuracy < 0.6)
    weak_topics = accuracy_by_time[accuracy_by_time < 0.6]
    weak_difficulty = accuracy_by_difficulty[accuracy_by_difficulty < 0.6]

    print("Weak Topics:", weak_topics)  # Debugging
    print("Weak Difficulty Levels:", weak_difficulty)

    return weak_topics, weak_difficulty

# Main execution block
if __name__ == "__main__":
    # Load historical and current quiz data from JSON files
    with open(historical_data_path, 'r') as hist_file:
        historical_data = json.load(hist_file)

    with open(current_quiz_data_path, 'r') as curr_file:
        current_quiz_data = json.load(curr_file)

    # Analyze performance
    performance_analysis = analyze_performance(historical_data)
    print("Performance Analysis:")
    print(json.dumps(performance_analysis, indent=2))

    # Analyze trends
    trends = analyze_trends(historical_data)
    print("\nTrends by Quiz ID:")
    print(trends)

    # Identify weak areas
    weak_topics, weak_difficulty = identify_weak_areas(historical_data)
    print("\nWeak Areas Identified:")
    print("Weak Topics:", weak_topics)
    print("Weak Difficulty Levels:", weak_difficulty)
