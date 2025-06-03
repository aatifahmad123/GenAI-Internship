import json
import os

# Path to the folder containing the JSON files
folder_path = 'Gemini Responses'
output_file = 'output.json'

# Prepare a list to hold data from all files
all_data = []

# Loop through files response01.json to response50.json
for i in range(1, 51):
    filename = f'response{i:02d}.json'
    file_path = os.path.join(folder_path, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        all_data.append(data)

# Write all data to output.json as a JSON array
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(all_data, f, indent=4)
