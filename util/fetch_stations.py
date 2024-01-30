import requests
import json

# Endpoint URL
url = "https://api-yebsp.tcddtasimacilik.gov.tr/istasyon/istasyonYukle"

# Request body
body = {
    "kanalKodu": "3",
    "dil": 1,
    "tarih": "Nov 10, 2011 12:00:00 AM",
    "satisSorgu": True
}

# Authorization header
headers = {
    'Authorization': 'Basic ZGl0cmF2b3llYnNwOmRpdHJhMzQhdm8u'
}

# Send POST request
response = requests.post(url, json=body, headers=headers)
data = response.json()

# Extract station names and IDs
stations = {station['istasyonAdi']: station['istasyonId'] for station in data['istasyonBilgileriList']}

# Save to JSON file
with open('stations.json', 'w', encoding='utf-8') as f:
    json.dump(stations, f, ensure_ascii=False, indent=4)

print("Station names and IDs have been saved to stations.json")
