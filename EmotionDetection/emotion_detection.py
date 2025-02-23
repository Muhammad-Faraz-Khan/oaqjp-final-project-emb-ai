
#AI Emotion Detector

#Application created using the Watson NLP library
#Formatted the output of the application using the json library functions. Extracted the required set of emotions, including anger, disgust, fear, joy and sadness, along with their scores. Wrote the code logic to find the dominant emotion, which is the emotion with the highest score.
#Packaged the application
#Ran unit tests on the application
#Performed Web deployment of the application using Flask
#Incorporated Error handling
#Ran static code analysis

import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json=input_json, headers=headers)
    if response.status_code == 200:
        try:
            formatted_response = json.loads(response.text)
            emotion_data = formatted_response['emotionPredictions'][0]['emotion']
            anger_score = emotion_data['anger']
            disgust_score = emotion_data['disgust']
            fear_score = emotion_data['fear']
            joy_score = emotion_data['joy']
            sadness_score = emotion_data['sadness']
            emotion_scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,}
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion,
            }
        except (KeyError, IndexError, json.JSONDecodeError):
            # Handle cases where the JSON response is malformed
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': "Error",
            }

    elif response.status_code == 500:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': "Error",
        }
    else:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': "Error",
        }