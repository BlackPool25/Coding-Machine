import pandas as pd
import math
import Python.Practise_Files.General.numpy_test as np

# Constants
mu_0 = 4 * math.pi * 1e-7  # T·m/A
n = 50  # number of turns
a = 0.082  # radius in meters

# Create the base DataFrame with the given data
data = {
    'S-No': range(1, 9),
    'Current I in A': [0.3, 0.3, 0.3, 0.3, 0.4, 0.4, 0.4, 0.4],
    'X in M': [0, 0.05, 0.10, 0.15, 0, 0.05, 0.10, 0.15],
    'Deflections in degrees (θ1, θ2, θ3, θ4)': [
        "75°, 76°, 70°, 73°",
        "60°, 61°, 60°, 62°",
        "43°, 44°, 31°, 33°",
        "21°, 22°, 23°, 22°",
        "78°, 79°, 72°, 75°",
        "65°, 66°, 70°, 71°",
        "53°, 52°, 45°, 46°",
        "30°, 31°, 25°, 26°"
    ],
    'Average θ in degrees': [73.5, 60.7, 37.7, 22.0, 76.0, 68.0, 49.0, 28.0]
}

df = pd.DataFrame(data)

# Calculate B
df['B in T'] = df.apply(lambda row: 
    (mu_0 * n * row['Current I in A'] * (a**2)) / 
    (2 * ((a**2 + row['X in M']**2)**(3/2))), 
    axis=1
)

# Calculate BH
df['BH = B/tan θ'] = df.apply(lambda row: 
    row['B in T'] / math.tan(math.radians(row['Average θ in degrees'])),
    axis=1
)

# Format the scientific notation for B and BH columns
df['B in T'] = df['B in T'].apply(lambda x: '{:.3e}'.format(x))
df['BH = B/tan θ'] = df['BH = B/tan θ'].apply(lambda x: '{:.3e}'.format(x))

# Calculate mean BH
mean_bh = df['BH = B/tan θ'].apply(lambda x: float(x)).mean()

# Export to CSV
df.to_csv('magnetic_field_calculations.csv', index=False)

# Display the DataFrame
print("\nMagnetic Field Calculations:")
print(df.to_string())
print(f"\nMean BH = {mean_bh:.3e} T")