import pandas as pd
import numpy as np

# Function to calculate vj for a single color triplet
def calculate_vj(color_triplet):
    vj = 0
    for i in range(len(color_triplet)):
        for j in range(i + 1, len(color_triplet)):
            # Calculate the absolute differences for each color component
            diff = abs(color_triplet[i] - color_triplet[j])
            vj += diff
    return vj

# Function to normalize RGB values to the range [0, 1]
def normalize_rgb(rgb):
    return [comp / 255.0 for comp in rgb]

# Read the CSV file containing color data
csv_file_path = 'subject001_visual.csv' 
df = pd.read_csv(csv_file_path)

# Normalize RGB values and store them in new columns 'R_norm', 'G_norm', and 'B_norm'
df['R_norm'], df['G_norm'], df['B_norm'] = zip(*df.apply(lambda row: normalize_rgb([row['r'], row['g'], row['b']]), axis=1))

# Calculate vj for each row using normalized RGB values and add it as a new column 'vj' to the DataFrame
df['vj'] = df.apply(lambda row: calculate_vj([row['R_norm'], row['G_norm'], row['B_norm']]), axis=1)

# Calculate the sum of vj values
vj_sum = df['vj'].sum()

# Define the value of 'N' (you should replace this with your actual value)
N = 36  # Example: Replace with your 'N' value

# Calculate the final 'V' value
V = vj_sum / N

print("Final Value V:", V)
