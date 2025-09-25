''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection App")

@app.route("/emotionDetector")
def sentiment_detector():
    # Récupère le texte
    query = request.args.get("textToAnalyze", "").strip()

    # Appel de ta fonction métier
    response = emotion_detector(query)

    # Si la fonction a renvoyé le default_output
    if response['anger'] == None:
        return "Invalid input! Please try again."

    # Sécurise l'accès aux clés
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response ['dominant_emotion']

    # f-string pour interpoler les valeurs
    message = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is <b>{dominant_emotion}</b>"
    )
    return message, 200

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
