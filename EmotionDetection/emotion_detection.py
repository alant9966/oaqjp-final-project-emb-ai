# Import the requests library to handle HTTP requests
import requests
import json

def emotion_detector(text_to_analyze):
    # URL of the emotion prediction service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Create a request payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Send a POST request to the emotion detector API
    response = requests.post(url, json=myobj, headers=header)  
    
    # Parse the JSON response from the API
    formatted_response = json.loads(response.text)
    
    # If the response status code is 200, extract the emotions and corresponding scores
    if response.status_code == 200:
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    # If the response status code is 400, set all entries to None
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None
        
    # Format the results and determine the dominant emotion
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    if response.status_code == 200:
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    emotion_scores['dominant_emotion'] = dominant_emotion
    
    # Return the emotion detector results
    return emotion_scores



# from emotion_detection import emotion_detector
# from EmotionDetection.emotion_detection import emotion_detector
