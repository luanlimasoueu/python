import pandas as pd
import numpy as np
from datetime import datetime
import streamlit as st


# Set random seed for reproducibility
np.random.seed(42)

# Generate dates for 5 years (to match the original date range)
start_date = datetime(2019, 8, 1)
end_date = datetime(2024, 9, 30)
date_range = pd.date_range(start=start_date, end=end_date, freq='ME')

# Initialize data with zeros
n_months = len(date_range)
data = {
    'DATE': date_range.strftime('%Y-%m'),  # Format date as YYYY-MM
    'SUBSCRIBERS_GAINED': np.zeros(n_months, dtype=int),
    'SUBSCRIBERS_LOST': np.zeros(n_months, dtype=int),
    'VIEWS': np.zeros(n_months, dtype=int),
    'WATCH_HOURS': np.zeros(n_months, dtype=int),
    'LIKES': np.zeros(n_months, dtype=int),
    'SHARES': np.zeros(n_months, dtype=int),
    'COMMENTS': np.zeros(n_months, dtype=int)
}

# Create DataFrame
df = pd.DataFrame(data)

# Function to generate growth
def generate_growth(start, end, months):
    return np.linspace(start, end, months)

# Generate growth patterns
subscribers_gained = generate_growth(30, 6000, n_months)
subscribers_lost = generate_growth(0, 1500, n_months)
views = generate_growth(300, 300000, n_months)
watch_hours = generate_growth(30, 30000, n_months)
likes = generate_growth(0, 15000, n_months)
shares = generate_growth(0, 3000, n_months)
comments = generate_growth(0, 1500, n_months)

# Add randomness and ensure integer values
for i, col in enumerate(['SUBSCRIBERS_GAINED', 'SUBSCRIBERS_LOST', 'VIEWS', 'WATCH_HOURS', 'LIKES', 'SHARES', 'COMMENTS']):
    random_factor = np.random.normal(1, 0.1, n_months)  # Mean of 1, standard deviation of 0.1
    df[col] = np.maximum(0, (eval(col.lower()) * random_factor).astype(int))

# Seasonal variation (higher in summer)
summer_boost = np.sin(np.linspace(0, 2*np.pi, 12))
df['VIEWS'] = df['VIEWS'] * (1 + 0.2 * np.tile(summer_boost, n_months // 12 + 1)[:n_months])

# Occasional viral videos (once every 6 months on average)
viral_months = np.random.choice(range(1, n_months), size=n_months // 6, replace=False)
df.loc[viral_months, ['VIEWS', 'LIKES', 'SHARES', 'COMMENTS']] = df.loc[viral_months, ['VIEWS', 'LIKES', 'SHARES', 'COMMENTS']] * 5

# Ensure integer values
for col in df.columns:
    if col != 'DATE':
        df[col] = df[col].astype(int)

# Calculate cumulative subscribers
df['NET_SUBSCRIBERS'] = (df['SUBSCRIBERS_GAINED'] - df['SUBSCRIBERS_LOST'])

# Ensure no negative values
df[df.select_dtypes(include=[np.number]).columns] = df.select_dtypes(include=[np.number]).clip(lower=0)

# Convert DATE column to datetime
df['DATE'] = pd.to_datetime(df['DATE'])

# Display DataFrame
df
