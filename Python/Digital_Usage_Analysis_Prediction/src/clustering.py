# src/clustering.py
import pandas as pd
from sklearn.cluster import KMeans

def perform_clustering(df, n_clusters=3):
    # Use activity features for clustering
    X = df[['activity_frequency', 'average_session_time', 'activity_score']]

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['cluster'] = kmeans.fit_predict(X)

    # Map cluster numbers to meaningful names
    cluster_mean_score = df.groupby('cluster')['activity_score'].mean().sort_values(ascending=False)

    cluster_name_mapping = {}
    for i, cluster_id in enumerate(cluster_mean_score.index):
        if i == 0:
            cluster_name_mapping[cluster_id] = 'High Activity'
        elif i == 1:
            cluster_name_mapping[cluster_id] = 'Medium Activity'
        else:
            cluster_name_mapping[cluster_id] = 'Low Activity'

    df['cluster_name'] = df['cluster'].map(cluster_name_mapping)

    return df, kmeans
