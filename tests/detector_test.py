# tests/test_predict.py
import random
from pathlib import Path

import cv2
import pytest

from src.predict import Predictor

# from predict import Predictor  # matches pythonpath=["src"] config

IMAGE_DIR = Path("data/v2_EGH455-3/test/images")


@pytest.fixture
def random_image():
    files = [f for f in IMAGE_DIR.iterdir() if f.is_file()]
    image_path = random.choice(files)
    image = cv2.imread(str(image_path))
    assert image is not None, f"Failed to load {image_path}"
    return image


class TestPredictor:
    def test_rough_test(self):
        predictor = Predictor("models/50_epoch_best.pt")
        result = predictor.rough_test()
        assert result == 5

    # def test_predictor_runs_on_random_image(self, random_image):
    #     predictor = Predictor()
    #     result = predictor.predict(random_image)
    #     assert result is not None