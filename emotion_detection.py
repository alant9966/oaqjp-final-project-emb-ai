# Import the requests library to handle HTTP requests
import requests

def emotion_detector(text_to_analyze):
    # URL of the emotion prediction service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Create a request payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Send a POST request to the emotion detector API
    response = requests.post(url, json=myobj, headers=header)  
    
    # Return the emotion detector results
    return response.text