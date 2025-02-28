import requests
from datetime import datetime

def get_fixtures():
    # Fetch football fixtures data (replace with real API URL)
    url = 'https://api.football-data.org/v4/matches'  # Example API URL
    headers = {'X-Auth-Token': '2d944ba8c4774be8bb4d1a153980bfae'}  # Add your API key here
    response = requests.get(url, headers=headers)
    fixtures = response.json()['matches']

    return fixtures

def create_epg(fixtures):
    # Create a simple EPG (XML format)
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<tv>\n'
    for fixture in fixtures:
        xml += f'  <programme start="{fixture["utcDate"]}" channel="{fixture["homeTeam"]["name"]} vs {fixture["awayTeam"]["name"]}">\n'
        xml += f'    <title>{fixture["homeTeam"]["name"]} vs {fixture["awayTeam"]["name"]}</title>\n'
        xml += f'    <desc>{fixture["competition"]["name"]}</desc>\n'
        xml += f'  </programme>\n'
    xml += '</tv>\n'

    with open('football_epg.xml', 'w') as file:
        file.write(xml)

def main():
    fixtures = get_fixtures()
    create_epg(fixtures)
    print("EPG generated!")

if __name__ == "__main__":
    main()
