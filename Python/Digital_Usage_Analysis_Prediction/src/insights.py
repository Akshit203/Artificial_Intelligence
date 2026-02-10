import pandas as pd

def generate_insights(df):
    print("\n--- Usage Insights ---")

    # Average activity score per cluster
    avg_score = df.groupby('cluster_name')['activity_score'].mean()
    print("\nAverage activity score per cluster:")
    print(avg_score)

    # Map user_behavior_class numbers to descriptive names with meaning
    behavior_class_mapping = {
        '1': 'Very Low Usage (Rarely uses apps)',
        '2': 'Low Usage (Light usage)',
        '3': 'Medium Usage (Moderate usage)',
        '4': 'High Usage (Heavy usage)',
        '5': 'Very High Usage (Extremely active / Power users)'
    }
    df['behavior_class_name'] = df['user_behavior_class'].map(behavior_class_mapping)

    # Number of users per behavior class
    print("\nNumber of users per behavior class:")
    print(df['behavior_class_name'].value_counts())

    # Cluster names with meaning
    cluster_mean_score = df.groupby('cluster_name')['activity_score'].mean().sort_values(ascending=False)
    cluster_meaning_mapping = {
        'High Activity': 'High Activity (very active users)',
        'Medium Activity': 'Medium Activity (moderately active users)',
        'Low Activity': 'Low Activity (rarely active users)'
    }

    print("\nCluster distribution:")
    for cluster in df['cluster_name'].value_counts().index:
        count = df['cluster_name'].value_counts()[cluster]
        print(f"{cluster} - {cluster_meaning_mapping[cluster]} : {count} users")
