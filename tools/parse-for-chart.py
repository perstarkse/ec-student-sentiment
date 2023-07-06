import json
import sys
import os

def parse_data(data, var, color):
    parsed_data = []

    for entry in data:
        new_entry = {
            "x": f'2023-{entry["week"]}',
            "y": entry[var],
            "num_messages": entry["num_messages"]
        }
        parsed_data.append(new_entry)

    output = {
        "label": var,
        "data": parsed_data,
        "fill": False,
        "borderColor": color,
        "tension": 0.5
    }

    return output

# Get the filename from command line arguments
filepath = sys.argv[1]

# Extract the base filename
base_filename = os.path.basename(filepath)
output_filename = os.path.splitext(base_filename)[0]

# Read data from JSON file
with open(filepath, 'r') as f:
    data = json.load(f)

# Print a menu for the user to choose a variable
print("Please choose a variable to parse:")
print("1. num_messages")
print("2. demand")
print("3. control")
print("4. support")
print("5. sentiment")
print("6. engagement")

choice = int(input("Enter the number of your choice: "))

# Define a dictionary to map choices to variable names
variables = {
    1: ("num_messages", "#904C77"),
    2: ("demand", "#E49AB0"),
    3: ("control", "#ECB8A5"),
    4: ("support", "#ECCFC3"),
    5: ("sentiment", "#957D95"),
    6: ("engagement", "#7D5BA6")
}

# Get the chosen variable and its color
chosen_var, chosen_color = variables.get(choice, ("sentiment", "#957D95"))  # Default to "sentiment" and "#957D95" if an invalid choice is made

# Parse the data with the chosen variable
parsed_data = parse_data(data, chosen_var, chosen_color)

# Define the output path
output_path = os.path.join('output', 'parsed-for-chart', chosen_var, output_filename + '_parsed.json')

# Ensure output directory exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Write parsed_data to a new JSON file
with open(output_path, 'w') as f:
    json.dump(parsed_data, f, indent=4)