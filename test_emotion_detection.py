from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        self.assertTrue(emotion_detector("I am glad this happened"), "joy")
        self.assertTrue(emotion_detector("I am really mad about this"), "anger")
        self.assertTrue(emotion_detector("I feel disgusted just hearing about this"), "disgust")    
        self.assertTrue(emotion_detector("I am so sad about this"), "sadness")
        self.assertTrue(emotion_detector("I am really afraid that this will happen"), "fear")

if __name__ == "__main__":
    unittest.main()