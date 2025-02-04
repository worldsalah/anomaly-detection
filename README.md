# Anomaly Detection System

## Overview
This project is a simple anomaly detection system with a graphical user interface (GUI) built using Python and Tkinter. It uses the Isolation Forest algorithm to detect anomalies in numerical data from a CSV file.

## Features
- Upload a CSV file
- Automatically detect numerical columns for processing
- Detect anomalies using Isolation Forest
- Display results in a scatter plot

## Requirements
Ensure you have the following Python libraries installed:

```bash
pip install pandas numpy scikit-learn matplotlib
```

## How to Use
1. Run the script:
   ```bash
   python anomaly_detection_ui.py
   ```
2. Click the **Upload File** button and select a CSV file.
3. Click **Detect Anomalies** to process the data.
4. A scatter plot will display the anomalies detected.

## Notes
- Only numerical columns are considered for anomaly detection.
- Missing values in numerical columns are replaced with the column mean.
- The contamination rate is set to 5% by default.

## License
This project is open-source and free to use.

