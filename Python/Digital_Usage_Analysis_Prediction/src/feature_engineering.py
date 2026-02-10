import pandas as pd
import numpy as np

def create_features(df):
    df['activity_frequency'] = df['app_usage_time_min_day'] + df['screen_on_time_hours_day']
    df['average_session_time'] = df['screen_on_time_hours_day'] / (df['app_usage_time_min_day'] + 1)
    df['activity_score'] = (df['activity_frequency']*0.4 +
                            df['battery_drain_mah_day']*0.3 +
                            df['data_usage_mb_day']*0.3)
    return df
