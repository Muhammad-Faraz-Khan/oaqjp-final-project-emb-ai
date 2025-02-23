from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] == "Error":
        return "Invalid input! Try again."
    else:
        return f"""{{
"anger": {response['anger']},
"disgust": {response['disgust']},
"fear": {response['fear']},
"joy": {response['joy']},
"sadness": {response['sadness']},
"dominant_emotion":"{response['dominant_emotion']}"
}}"""

@app.route("/")
def render_index_page():
    return render_template('index 1.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)