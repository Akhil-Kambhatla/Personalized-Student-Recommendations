import json
import pandas as pd

# File paths (use raw strings to handle Windows paths correctly)
performance_analysis_path = r'C:\Users\akhil\OneDrive\Desktop\Student Recommendations\performance_analysis.json'
current_quiz_path = r'C:\Users\akhil\OneDrive\Desktop\Student Recommendations\current_quiz_data.json'

def generate_recommendations(historical_performance, current_quiz):
    recommendations = []
    
    # Ensure 'quiz' and 'topic' exist in current_quiz
    topic = current_quiz.get("quiz", {}).get("topic", "general knowledge")

    for performance in historical_performance:
        if isinstance(performance, dict):
            print(f"Analyzing performance for user: {performance.get('user_id', 'Unknown')}")

            # Debug prints for conditions
            accuracy = performance.get("accuracy", 0)
            speed = performance.get("speed", 0)
            incorrect_answers = performance.get("incorrect_answers", 0)
            
            print(f"Accuracy: {accuracy}, Speed: {speed}, Incorrect Answers: {incorrect_answers}")
            
            # Accuracy condition
            if accuracy < 0.8:
                print(f"Adding accuracy recommendation for {performance.get('user_id')}")
                recommendations.append({
                    "user_id": performance["user_id"],
                    "message": "Focus on improving accuracy for better results in future quizzes.",
                    "suggested_topic": topic
                })

            # Speed condition
            if speed < 80:
                print(f"Adding speed recommendation for {performance.get('user_id')}")
                recommendations.append({
                    "user_id": performance["user_id"],
                    "message": "Try to increase your speed to answer more questions within the given time.",
                    "suggested_topic": topic
                })

            # Incorrect answers condition
            if incorrect_answers > 5:
                print(f"Adding incorrect answers recommendation for {performance.get('user_id')}")
                recommendations.append({
                    "user_id": performance["user_id"],
                    "message": f"Revise concepts from {topic} to reduce mistakes.",
                    "suggested_topic": topic
                })
        else:
            print(f"Skipping invalid performance entry: {performance}")

    return recommendations


# Sample accuracy series for persona definition
accuracy_by_difficulty = pd.Series({
    'easy': 0.9,
    'medium': 0.55,
    'hard': 0.85
})
accuracy_by_time = pd.Series({
    'easy': 0.9,
    'medium': 0.55,
    'hard': 0.85
})

# Function to define student persona
def define_persona(accuracy_by_time, accuracy_by_difficulty):
    """
    Define student persona based on accuracy patterns.
    """
    # Debugging print statements
    print("Accuracy by Difficulty:", accuracy_by_difficulty)
    print("Accuracy by Time:", accuracy_by_time)

    persona = {}
    if accuracy_by_difficulty.get('hard', 0) > 0.8 and accuracy_by_difficulty.get('medium', 0) < 0.6:
        persona = "Confident Explorer"
    elif accuracy_by_time.max() > 0.9 and accuracy_by_time.min() < 0.5:
        persona = "Topic Specialist"
    else:
        persona = "Balanced Learner"
    return persona

# Main execution block
if __name__ == "__main__":
    # Load the performance analysis data
    with open(performance_analysis_path, 'r') as perf_file:
        historical_performance = json.load(perf_file)
    
    # Load the current quiz data
    with open(current_quiz_path, 'r') as curr_file:
        current_quiz = json.load(curr_file)
    
    # Generate recommendations
    recommendations = generate_recommendations(historical_performance, current_quiz)
    print("Generated Recommendations:")
    print(json.dumps(recommendations, indent=2))
    
    # Define student persona based on accuracy
    persona = define_persona(accuracy_by_time, accuracy_by_difficulty)
    print("\nStudent Persona:")
    print(persona)
