import requests
import csv
import json
from google.cloud import storage

url = "https://api-nba-v1.p.rapidapi.com/standings"

querystring = {"league":"standard","season":"2021"}

headers = {
	"X-RapidAPI-Key": "71b5843f77msh7cff2de80136b0cp184163jsn250fb5163f36",
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}

try:
    with open('api_response.json', 'r') as file:
        teams_data = json.load(file)
except FileNotFoundError:
    # If the file is not found, make an API call
    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        teams_data = response.json()

        # Save the response to a file
        with open('api_response.json', 'w') as file:
            json.dump(teams_data, file)
    else:
        print("Failed to fetch data:", response.status_code)
        exit()

teams_data = teams_data['response']

if teams_data:
    # Filter teams by conference (East and West)
    east_teams = [team for team in teams_data if team['conference']['name'] == 'east']
    west_teams = [team for team in teams_data if team['conference']['name'] == 'west']

    # Define CSV filenames for East and West
    east_csv_filename = 'nba_rankings_east.csv'
    west_csv_filename = 'nba_rankings_west.csv'

    # Function to write data to CSV file
    def write_to_csv(filename, teams):
        if teams:
            field_names = ['rank', 'name', 'conference', 'division', 'win', 'loss']  # Specify required field names

            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                writer.writeheader()

                sorted_teams = sorted(teams, key=lambda x: x['conference']['rank'])
                for team in sorted_teams:
                    writer.writerow({
                        'rank': team['conference']['rank'],
                        'name': team['team']['name'],
                        'conference': team['conference']['name'],
                        'division': team['division']['name'],
                        'win': team['win']['total'],
                        'loss': team['loss']['total']
                    })

                print(f"Teams in {filename} fetched successfully and written to '{filename}'")

                # Upload the CSV file to GCS
                bucket_name = 'bkt-ranking-data-lr'
                storage_client = storage.Client()
                bucket = storage_client.bucket(bucket_name)
                destination_blob_name = f'{filename}'  # The path to store in GCS

                blob = bucket.blob(destination_blob_name)
                blob.upload_from_filename(filename)

                print(f"File {filename} uploaded to GCS bucket {bucket_name} as {destination_blob_name}")
                
    # Write East teams to CSV
    write_to_csv(east_csv_filename, east_teams)

    # Write West teams to CSV
    write_to_csv(west_csv_filename, west_teams)

else:
    print("No data available from the API.")

