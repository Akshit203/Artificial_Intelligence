# src/classification.py
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

def train_classifier(df):
    features = ['activity_frequency', 'average_session_time', 'activity_score', 'age']
    X = df[features]
    y = df['user_behavior_class']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    model = LogisticRegression(max_iter=500)
    model.fit(X_train_scaled, y_train)
    
    return model, scaler, X_test_scaled, y_test
