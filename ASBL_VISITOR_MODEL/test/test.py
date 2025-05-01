import requests
import json

# Path to the JSON file to be tested
json_file_path = r'C:\Users\xelpmoc\Downloads\output (1).json'

# URL of the FastAPI endpoint
url = "http://127.0.0.1:8000/process-data/"  # Default FastAPI URL

# Open the JSON file and send the request
with open(json_file_path, 'rb') as file:
    files = {'file': ('output.json', file, 'application/json')}
    response = requests.post(url, files=files)

# Handle response
if response.status_code == 200:
    print("✅ Successfully processed data.\n")
    try:
        data = response.json()
        print(f"Returned {len(data)} records.\n")
        print("Sample Record:")
        print(json.dumps(data[0], indent=2))
    except json.JSONDecodeError:
        print("⚠️ Response is not valid JSON.")
else:
    print(f"❌ Failed to process data. Status code: {response.status_code}")
    print(f"Error details:\n{response.text}")
