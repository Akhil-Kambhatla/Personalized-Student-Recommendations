# **Student Recommendations System**

## **Overview**
The **Student Recommendations System** is a Python-based project designed to analyze student quiz performance and provide personalized recommendations to improve their learning outcomes. It evaluates quiz data, identifies weak areas, and offers targeted suggestions to enhance understanding.

---

## **Features**
- **Performance Analysis**: Evaluates strengths and weaknesses based on quiz attempts.
- **Personalized Recommendations**: Suggests ways to improve in weak topics and difficulty levels.
- **Student Persona Identification**: Analyzes quiz data to define unique student personas for tailored insights.
- **Dashboard**: Displays performance analysis, weak topics, weak difficulty levels, and actionable recommendations.

---

## **Input Files**
### 1. **current_quiz_data.json**
- Stores the latest quiz attempt data for the student.
- Includes quiz details like topics, questions, correct answers, and scores.

### 2. **historical_quiz_data.json**
- Contains aggregated historical data of previous quizzes for comprehensive analysis.

---

## **Key Scripts**
### 1. `main.py`
- Orchestrates the process by loading data, performing analysis, and generating recommendations.

### 2. `recommendations.py`
- Provides logic to generate actionable insights and study plans based on student performance.

### 3. `persona.py`
- Defines the student's persona based on patterns in quiz data, highlighting strengths and weaknesses.

### 4. `dashboard.py`
- Visualizes student performance with a user-friendly display of weak topics, difficulty levels, and recommendations.

### 5. `utils.py`
- Contains helper functions for JSON handling, calculations, and data preprocessing.

---

## **How to Run**
### 1. Clone the repository:
```bash
git clone https://github.com/Akhil-Kambhatla/Personalized-Student-Recommendations.git
cd Student-Recommendations


