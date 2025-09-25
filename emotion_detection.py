''' Detect text emotion
'''

import requests
import json

def emotion_detector(text_to_analyse):
    ''' This method detects text emotion
    '''
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' # pylint: disable=line-too-long
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = {"raw_document": {"text": text_to_analyse}}
    
    try:
        response = requests.post(url, json = input, headers=headers, timeout=10)
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    return response.text
