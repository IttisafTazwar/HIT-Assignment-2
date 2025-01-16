import os
import csv
from collections import defaultdict
# Read temperature data from all files in the folder
def read_temperature_data(folder_path):
    data = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):  # Check if the file is a CSV file
            with open(os.path.join(folder_path, filename), mode='r') as file:
                reader = csv.DictReader(file)
                data.extend(list(reader))  # Add rows to the data list
    return data
# Function to calculate seasonal averages
def calculate_seasonal_avg(data):
    # Map seasons to months
    seasons = {
        'Summer': ['12', '01', '02'],
        'Autumn': ['03', '04', '05'],
        'Winter': ['06', '07', '08'],
        'Spring': ['09', '10', '11']
    }

    # Initialize dictionary for seasonal temperatures
    seasonal_data = defaultdict(list)

    # Group temperatures by season
    for row in data:
        date = row['Date']
        temperature = float(row['Temperature'])
        month = date.split('-')[1]

        for season, months in seasons.items():
            if month in months:
                seasonal_data[season].append(temperature)

    # Calculate averages for each season
    season_avg = {}
    for season, temps in seasonal_data.items():
        if temps:
            season_avg[season] = sum(temps) / len(temps)
        else:
            season_avg[season] = 0.0  # Handle cases with no data

    return season_avg

# Function to save seasonal averages to a file
def save_seasonal_avg_to_file(season_avg, filename):
    with open(filename, 'w') as file:
        for season, avg_temp in season_avg.items():
            file.write(f"{season}: {avg_temp:.2f}°C\n")

def save_to_file(filename, seasonal_avg):
    with open(filename, 'w') as file:
        for season, avg_temp in seasonal_avg.items():
            file.write(f"{season}: {avg_temp:.2f}°C\n")

# Main function
def main():
    # Set the folder path where the CSV files are located
    folder_path = "C:/Users/Public/tazwar/HIT-assignment2/temperature_data"  # Update this if needed

    # Read the temperature data from the CSV files
    data = read_temperature_data(folder_path)

    # # Calculate the average temperature for each season across all years
    # seasonal_avg = calculate_seasonal_avg(data)
    #
    # # Save the calculated seasonal averages to a text file
    # save_to_file("average_temp.txt", seasonal_avg)

    print("The seasonal averages have been saved to 'average_temp.txt'")



# Execute the program
if __name__ == "__main__":
    main()
