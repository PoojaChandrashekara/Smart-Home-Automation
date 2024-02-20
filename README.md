# Smart Home Automation

This project implements a machine learning model to predict and control relay states for home automation. It utilizes relay data collected from a Firebase-connected sensor setup and a K-Nearest Neighbors (KNN) classifier for prediction.

## Key Features

- **Real-time Data Collection:** Gathers relay data from live sensors and stores it in a Google Firebase database.
- **Data Integration with Excel:** Transfers data from Firebase to an Excel sheet for accessibility and analysis.
- **Predictive Modeling:** Trains a KNN classifier to predict relay states based on historical patterns.
- **Adafruit IO Integration:** Sends control signals to relays via Adafruit IO for real-world automation.

## Project Structure

- `README.md`: This file provides an overview of the project.
- `main.py`: Contains the Python code for data loading, model training, prediction, and relay control.
- `requirements.txt`: Lists the required Python libraries.

## Usage

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

2. **Set Adafruit IO Credentials:**
Replace MADHUYASHU and 8d7ee5784a5e4989bf04aadb530f3808 in the code with your Adafruit IO username and key.

3. **Run the Script:**
python main.py

4. **Enter Time for Prediction:**
When prompted, enter the time for which you want to predict relay states.
