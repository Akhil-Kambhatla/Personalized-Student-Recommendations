import json
import pandas as pd

# Function to generate recommendations based on historical performance
def generate_recommendations(historical_performance, current_quiz):
    recommendations = []
    
    # Ensure 'quiz' and 'topic' exist in current_quiz
    topic = current_quiz.get("quiz", {}).get("topic", "general knowledge")

    for performance in historical_performance:
        # Check accuracy and recommend improvement
        if performance["accuracy"] < 0.8:
            recommendations.append({
                "user_id": performance["user_id"],
                "message": "Focus on improving accuracy for better results in future quizzes.",
                "suggested_topic": topic
            })

        # Check speed and suggest improvement
        if performance["speed"] < 80:
            recommendations.append({
                "user_id": performance["user_id"],
                "message": "Try to increase your speed to answer more questions within the given time.",
                "suggested_topic": topic
            })

        # Check incorrect answers and recommend topic revision
        if performance["incorrect_answers"] > 5:
            recommendations.append({
                "user_id": performance["user_id"],
                "message": f"Revise concepts from {topic} to reduce mistakes.",
                "suggested_topic": topic
            })
    
    return recommendations

# Enhanced function to define student persona with creative labels
def define_persona(accuracy_by_time, accuracy_by_difficulty):
    """
    Define student persona based on accuracy patterns with creative labels for strengths and weaknesses.
    """
    persona = {}

    # Debugging print statements
    print("Accuracy by Difficulty:", accuracy_by_difficulty)
    print("Accuracy by Time:", accuracy_by_time)

    # Define creative labels for strengths and weaknesses
    if accuracy_by_difficulty.get('hard', 0) > 0.8 and accuracy_by_difficulty.get('medium', 0) < 0.6:
        persona = "Confident Explorer - Mastering Hard Challenges, Struggling with Medium Difficulty."
    elif accuracy_by_time.max() > 0.9 and accuracy_by_time.min() < 0.5:
        persona = "Topic Specialist - Mastering Easy Topics, But Needs to Work on Time Management."
    elif accuracy_by_difficulty.get('easy', 0) > 0.85 and accuracy_by_difficulty.get('medium', 0) < 0.6:
        persona = "Speed Demon - Quick on Easy Questions, Needs More Focus on Medium Difficulty."
    elif accuracy_by_time.min() > 0.7:
        persona = "Steady Performer - Consistently Performing Well, Needs to Boost Speed."
    else:
        persona = "Balanced Learner - Strong Across All Areas, But Needs to Fine-Tune Speed."

    # Return the persona along with the performance strengths and weaknesses
    strengths, weaknesses = categorize_strengths_weaknesses(accuracy_by_time, accuracy_by_difficulty)
    
    return persona, strengths, weaknesses

# Function to categorize strengths and weaknesses based on data
def categorize_strengths_weaknesses(accuracy_by_time, accuracy_by_difficulty):
    strengths = []
    weaknesses = []
    
    # Strengths based on accuracy and time management
    if accuracy_by_difficulty.get('hard', 0) > 0.8:
        strengths.append("Hard Topic Specialist")
    if accuracy_by_time.max() > 0.9:
        strengths.append("Time Management Master")
    
    # Weaknesses based on performance trends
    if accuracy_by_difficulty.get('medium', 0) < 0.6:
        weaknesses.append("Medium Difficulty Struggler")
    if accuracy_by_difficulty.get('easy', 0) < 0.85:
        weaknesses.append("Need Improvement on Easy Topics")
    
    return strengths, weaknesses


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

# Example usage
if __name__ == "__main__":
    # Sample historical performance data
    historical_performance = [
        {
            "user_id": "student_1",
            "accuracy": 0.75,
            "speed": 70,
            "incorrect_answers": 8
        },
        {
            "user_id": "student_2",
            "accuracy": 0.85,
            "speed": 85,
            "incorrect_answers": 3
        }
    ]
    current_quiz = {
        "quiz": {
            "topic": "Math"
        }
    }

    # Generate recommendations
    recommendations = generate_recommendations(historical_performance, current_quiz)
    for rec in recommendations:
        print(f"Recommendation for {rec['user_id']}: {rec['message']} on {rec['suggested_topic']}")

    # Define persona for a student
    persona, strengths, weaknesses = define_persona(accuracy_by_time, accuracy_by_difficulty)
    print(f"Persona: {persona}")
    print(f"Strengths: {', '.join(strengths)}")
    print(f"Weaknesses: {', '.join(weaknesses)}")
