def fetch_data_from_api(url):
    import requests
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error fetching data from API")

def format_data(data):
    # Assuming data is a list of dictionaries
    formatted_data = []
    for item in data:
        formatted_data.append({key: item[key] for key in item if key in ['date', 'price', 'volume']})
    return formatted_data

def calculate_percentage_change(old_value, new_value):
    if old_value == 0:
        return 0
    return ((new_value - old_value) / old_value) * 100

def save_to_csv(data, filename):
    import pandas as pd
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)