# employee-salary-predictot-by-ankam-tulasi-maha-lakshmi
# Employee Salary Predictor

A simple machine learning project to predict employee salary based on experience, education, and job title.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Train the model:
   ```bash
   python train_model.py
   ```

3. Run the API:
   ```bash
   python predictor_api.py
   ```

4. Make a prediction (example using curl):
   ```bash
   curl -X POST http://127.0.0.1:5000/predict \
     -H 'Content-Type: application/json' \
     -d '{"years_experience": 2, "education_level": "Master", "job_title": "Data Scientist"}'
   ``` 
