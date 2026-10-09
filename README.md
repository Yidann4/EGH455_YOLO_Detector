### Pixi Usage

- pixi install
- pixi run python3 file.py

### Downloading dataset (for PyTests)
- pixi run python assets/download_dataset.py

### PyTest Usage

- Note: Before doing this you must have downloaded the dataset

- pixi run pytest -q tests/<file_name>

- pixi run pytest -q -rP tests/<file_name> -- for logging prints to terminal

### PyTest Implementation

- classes must begin with Test
- child methods must begin with test

### Integrating with system
- All detections are done in the Predictor class inside src/predict.py
1. from src/predict.py import initialise_predictor
2. get the instance of predictor by calling initialise_predictor()
3. cleaned_prediction = predictor.predict(raw_image)

Note: cleaned_prediction will be in the form [(detection_class, (x_centre, y_centre, width, height))]
where each of the floats are percentages of image

4. latest_gauge_crop = predictor.get_latest_gauge_crop()

Note: latest_gauge_crop = image of the latest gauge crop. Returns `None` if no gauge has been spotted in the last 30 seconds
