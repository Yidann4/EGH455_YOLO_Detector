# tests/test_predict.py
from email.mime import image
import random
from pathlib import Path

import cv2
import pytest
import yaml

from src.predict import Predictor

# from predict import Predictor  # matches pythonpath=["src"] config

IMAGE_DIR = Path("data/v2_EGH455-3/test/images")





class TestPredictor:
    @pytest.fixture
    def random_image(self):
        files = [f for f in IMAGE_DIR.iterdir() if f.is_file()]
        random_number = random.randint(0, len(files) - 1)
        image_path = files[random_number]
        image = cv2.imread(str(image_path))
        assert image is not None, f"Failed to load {image_path}"
        
        label = 
        return image, label

    def test_rough_test(self):
        predictor = Predictor("models/50_epoch_best.pt")
        result = predictor.rough_test()
        assert result == 5

    def test_predictor_runs_on_random_image(self, random_test_sample):
        image, label = random_test_sample
        cv2.imshow(f"Random Image: {label}", image)
        predictor = Predictor("models/50_epoch_best.pt")
        result = predictor.predict(image)
        assert result is not None
        cv2.waitKey(0)
        cv2.destroyAllWindows()