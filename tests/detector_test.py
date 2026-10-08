# tests/test_predict.py


import cv2
import pytest

from src.predict import Predictor

# from predict import Predictor  # matches pythonpath=["src"] config



class TestPredictor:
    # @pytest.fixture
    # def random_test_sample(self):
        

    # def test_rough_test(self):
    #     predictor = Predictor("models/50_epoch_best.pt")
    #     result = predictor.rough_test()
    #     assert result == 5

    # def test_predictor_runs_on_random_image(self):
    #     predictor = Predictor("models/50_epoch_best.pt")
    #     raw_image, annotated_image, ground_labels = predictor.get_test_sample()
        
    #     assert 1+1 == 2
        
    #     cv2.imshow(f"{ground_labels}", annotated_image)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()
        
    #     prediction = predictor.predict(raw_image)
        
    #     predicted_image = predictor.annotate_image(raw_image, prediction)
        
    #     cv2.imshow("Prediction", predicted_image)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()
        
    def test_spam_a_bunch(self):
        predictor = Predictor("models/50_epoch_best.pt")
        
        LOOP_TIMES = 3
        loop_count = 0
        while loop_count < LOOP_TIMES:
            raw_image, annotated_image, ground_labels = predictor.get_test_sample()
            
            prediction = predictor.predict(raw_image)
            predicted_image = predictor.annotate_image(raw_image, prediction)
            
            cv2.imshow("Spam Prediction", predicted_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            loop_count +=1
        
        assert 1 + 1 ==2
        
    def test_spam_gauge(self):
        predictor = Predictor("models/50_epoch_best.pt")
        
        MAX_GAUGE_COUNT = 3
        gauge_count = 0
        
        while gauge_count < MAX_GAUGE_COUNT:
            found_gauge = False
            while not found_gauge:
                raw_image, annotated_image, ground_labels = predictor.get_test_sample()
                if any(name == "gauge" for name, _ in ground_labels):
                    found_gauge = True
                    
            cv2.imshow("Raw image Gauge", raw_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
            prediction = predictor.predict(raw_image)
            predicted_image = predictor.annotate_image(raw_image, prediction)
            
            cv2.imshow("Raw image Post Prediction Gauge", raw_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
            cv2.imshow("Gauge Prediction", predicted_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            gauge_count += 1

            
            
            
            
            