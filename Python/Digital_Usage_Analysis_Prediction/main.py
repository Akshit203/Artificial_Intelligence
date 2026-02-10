import os
from src.data_preprocessing import preprocess
from src.feature_engineering import create_features
from src.clustering import perform_clustering
from src.classification import train_classifier
from src.model_evaluation import evaluate_model
from src.insights import generate_insights

# Automatically find CSV in data/ folder
DATA_DIR = 'data'
CSV_FILENAME = 'user_behaviour_dataset.csv'
DATA_FILE = os.path.join(DATA_DIR, CSV_FILENAME)

# Check if file exists
if not os.path.exists(DATA_FILE):
    raise FileNotFoundError(
        f"\nERROR: Could not find the dataset.\n"
        f"Expected at: {DATA_FILE}\n"
        f"Make sure your CSV is in the 'data/' folder and named '{CSV_FILENAME}'"
    )

def main():
    # 1️⃣ Load & clean data
    df = preprocess(DATA_FILE)
    
    # 2️⃣ Feature engineering
    df = create_features(df)
    
    # 3️⃣ Clustering
    df, kmeans = perform_clustering(df)
    
    # 4️⃣ Classification
    model, scaler, X_test, y_test = train_classifier(df)
    
    # 5️⃣ Model evaluation
    evaluate_model(model, X_test, y_test)
    
    # 6️⃣ Insights
    generate_insights(df)
    
if __name__ == "__main__":
    main()
