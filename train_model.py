 sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# Load dataimport pandas as pd
from
df = pd.read_csv('sample_data.csv')

# Features and target
X = df.drop('salary', axis=1)
y = df['salary']

# Preprocessing for categorical features
categorical_features = ['education_level', 'job_title']
numeric_features = ['years_experience']

preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(), categorical_features),
    ('num', 'passthrough', numeric_features)
])

# Create pipeline
model = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Train model
model.fit(X, y)

# Save model
joblib.dump(model, 'model.joblib')
print('Model trained and saved as model.joblib') 
