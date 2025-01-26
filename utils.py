import json
from datetime import datetime


def parse_date(date_str):
    """Convert string date to datetime object."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f%z")
    except ValueError as e:
        raise ValueError(f"Invalid date format: {date_str}. Error: {e}")


def calculate_time_difference(start_time, end_time):
    """Calculate the time difference in minutes between two timestamps."""
    try:
        start = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
        end = datetime.fromisoformat(end_time.replace("Z", "+00:00"))
        return (end - start).total_seconds() / 60  # Convert to minutes
    except Exception as e:
        raise ValueError(f"Invalid timestamp format: {start_time} or {end_time}. Error: {e}")


def calculate_accuracy(correct, incorrect):
    """Calculate accuracy percentage."""
    total_attempted = correct + incorrect
    return round((correct / total_attempted) * 100, 2) if total_attempted > 0 else 0


def calculate_performance_metrics(data):
    """Calculate performance metrics from the data."""
    started_at = data.get("started_at")
    ended_at = data.get("ended_at")

    if not started_at or not ended_at:
        print("Warning: Missing 'started_at' or 'ended_at' in the data.")
        duration_minutes = None
    else:
        duration_minutes = calculate_time_difference(started_at, ended_at)

    # Parse accuracy and final score as floats
    accuracy = float(data.get("accuracy", "0%").strip('%'))
    final_score = float(data.get("final_score", 0))

    performance = {
        "quiz_id": data.get("quiz_id", "N/A"),
        "score": data.get("score", 0),
        "accuracy": accuracy,
        "final_score": final_score,
        "duration_minutes": duration_minutes,
        "topic": data.get("topic", "Unknown")  # Default to "Unknown" if the topic is missing
    }
    return performance


def load_data(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return data if isinstance(data, list) else [data]
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON in file {file_path}: {e}")


def summarize_performance(data):
    """Summarize the performance of the user."""
    performance = calculate_performance_metrics(data)

    summary = {
        "Quiz ID": performance["quiz_id"],
        "Score": performance["score"],
        "Accuracy": f"{performance['accuracy']}%",
        "Final Score": performance["final_score"],
        "Duration (minutes)": (
            round(performance["duration_minutes"], 2) if performance["duration_minutes"] is not None else "N/A"
        ),
        "Topic": performance["topic"]
    }
    return summary


# Example Usage
if __name__ == "__main__":
    # Sample data for testing
    sample_data = {
        "quiz_id": "123",
        "score": 85,
        "accuracy": "90%",
        "final_score": "85.5",
        "started_at": "2023-01-01T12:00:00.000+0000",
        "ended_at": "2023-01-01T12:30:00.000+0000"
    }

    print("Performance Metrics:")
    print(calculate_performance_metrics(sample_data))

    # Complete sample data
    sample_data_complete = {
        "quiz_id": "123",
        "score": 85,
        "accuracy": "90%",
        "final_score": "85.5",
        "started_at": "2023-01-01T12:00:00.000+0000",
        "ended_at": "2023-01-01T12:30:00.000+0000",
        "topic": "Math"
    }

    print("\nPerformance Summary:")
    print(summarize_performance(sample_data_complete))
