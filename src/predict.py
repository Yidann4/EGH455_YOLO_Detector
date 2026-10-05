"""
predict - YOLO object detection to find gauges and valves in images


"""

from ultralytics import YOLO


class Predictor:
    """Predictor class for YOLO object detection to find gauges and valves in images."""
    
    def __init__(self, model_location: str):
        self.model = YOLO(model_location)
        
        
    def predict(self, image):
        return self.model(image)
    
    def demonstrate(self, image):
        results = self.predict(image)
        results.show()
        
    def rough_test(self):
        return 5
        
