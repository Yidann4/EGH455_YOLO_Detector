"""
predict - YOLO object detection to find gauges and valves in images


"""

from ultralytics import YOLO
from annotater import Annotater
import cv2


class Predictor(Annotater):
    """Predictor class for YOLO object detection to find gauges and valves in images."""
    
    def __init__(self, model_location: str):
        super().__init__()
        self.model = YOLO(model_location)
        self.predicted_classes = []
        
        
    def predict(self, image):
        boxes = self.model.predict(image, verbose=False)[0].boxes
        return [
            (self.class_names[int(cls)], tuple(xywhn))
            for cls, xywhn in zip(boxes.cls.tolist(), boxes.xywhn.tolist())
        ]
        
    
    def demonstrate(self, image):
        results = self.predict(image)
        annotated_image = self.annotate_image(image, results)
        cv2.imshow(annotated_image)
        
    def rough_test(self):
        return 5
        
