import requests
import json

def emotion_detector(text_to_analyse):
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Print the raw response for debugging
    print("Raw Response:", response.text)

    # Check if the response was successful
    if response.status_code == 200:
        # Parse the response from the API
        formatted_response = json.loads(response.text)
        
        # Extract the required emotions and their scores
        emotions = {
            'anger': formatted_response.get('anger', 0),
            'disgust': formatted_response.get('disgust', 0),
            'fear': formatted_response.get('fear', 0),
            'joy': formatted_response.get('joy', 0),
            'sadness': formatted_response.get('sadness', 0),
        }
        
        # Find the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)

        # Return the results in the specified format
        return {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }
    else:
        # Handle error response
        return {'error': 'Unable to reach the emotion detection service.'}
