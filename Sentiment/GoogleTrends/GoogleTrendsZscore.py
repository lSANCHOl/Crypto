import csv
import numpy as np

def read_csv(file_path):
    """
    Read a CSV file and return data as a list of dictionaries.
    Each dictionary represents a row with column names as keys.
    """
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def extract_values(data):
    """
    Extract 'value' from each row of data and return as a list.
    """
    values = [int(row[None][0]) if row[None][0].isdigit() else 0 for row in data]

    # Find the index of the first non-zero element
    first_non_zero_index = next((i for i, x in enumerate(values) if x != 0), None)

    # Slice the array from the first non-zero element to the end
    values = values[first_non_zero_index:]

    return values

def calculate_zscore(values):
    """
    Calculate the z-score of the last value in the array.
    """
    last_value = values[-1]
    mean = np.mean(values)
    std_dev = np.std(values)
    z_score = (last_value - mean) / std_dev
    return z_score

def main():
    # Path to your CSV file
    csv_file = 'multiTimeline.csv'

    # Read CSV file
    btc_data = read_csv(csv_file)

    # Extract values
    btc_values = extract_values(btc_data)

    # Calculate z-score of the last value
    zscore = calculate_zscore(btc_values)
    print("Z-score of the last value:", zscore)

if __name__ == "__main__":
    main()
