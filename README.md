
# TCDD Train Seat Finder (TCDD Bilet Bulucu)

## Overview
<em>For Turkish see `README_TR.md`. | Türkçe anlatım için `README_TR.md`dosyasını inceleyin.</em><br>

<em>For the web application version that you can start using in browser immediately, see [TCDD Bilet Bulucu - WEB](https://github.com/rburaksaritas/tcdd-bilet-bulucu-web).</em>


The TCDD Train Seat Finder is a Python-based tool designed to help users find available seats on Turkish State Railways (TCDD) trains by utilizing available API endpoints of TCDD. It automates the process of checking seat availability for specified routes, dates, and, optionally, times. When an available seat is found, the tool notifies the user via email, providing details such as the train name, journey date, wagon number, and seat number.

## Features
- **Automated Seat Checking**: Automatically checks for available seats on specified train routes.
- **Email Notifications**: Sends email alerts when available seats are found, with detailed information.
- **Configurable Searches**: You can specify departure and arrival stations, journey dates, and optionally, preferred departure times.
- **API-Driven Simplicity**: Utilizes direct API calls for lightweight and reliable operations. This approach minimizes dependencies and reduces the potential for issues caused by website changes, setting it apart from tools that depend on web scraping techniques like Selenium.

## Installation

### Prerequisites
- Python 3.x
- Pip (Python package installer)
- Email address (@outlook.com domain is required) & password

### Setup
1. Clone the repository to your local machine:
   ```sh
   git clone https://github.com/rburaksaritas/tcdd-bilet-bulucu
   ```
2. Navigate to the project directory:
   ```sh
   cd tcdd-bilet-bulucu
   ```
3. Install the required dependencies:
   ```sh
   pip3 install -r requirements.txt
   ``` 


## Configuration (`config.py`)
Before using the tool, you must configure it by editing the `config.py` file located in the `src` directory. Set the following parameters according to your preferences:

- `binis_istasyon_adi`: Name of the departure station.
- `inis_istasyon_adi`: Name of the arrival station.
- `date`: Date of the journey (format: YYYY-MM-DD).
- `check_specific_hour`: Set to `True` if you want to check for trains at a specific hour, otherwise `False`.
- `hour`: Preferred hour for departure (format: HH:MM), required if `check_specific_hour` is `True`.
- `email_address`: Your email address from which the notification will be sent.
- `email_password`: Password for the email account above.
- `destination_address`: Email address to receive the notification.

**Note:**  `binis_istasyon_adi` and `inis_istasyon_adi` must be valid station names. See `stations.json` file for available station names. If you want a station that is recently introduced, please update stations.json with the following command:
```sh
python3 util/fetch_stations.py
``` 
Which will update the stations list in `stations.json`.

**Example 1:** Checks all journeys available on Feb 2, 2024. 
```
binis_istasyon_adi = "İstanbul(Söğütlüçeşme)"
inis_istasyon_adi = "Ankara Gar"
date = "2024-02-02"

check_specific_hour = False

email_address = "sender_mail@outlook.com" 
email_password = "sender_password"
destination_address = "receiver@gmail.com"

sleep_time = 10
```
**Example 2:** Checks the specific journey at 08:02 on Feb 2, 2024. 
```
binis_istasyon_adi = "İstanbul(Söğütlüçeşme)"
inis_istasyon_adi = "Ankara Gar"
date = "2024-02-02"

check_specific_hour = True
hour = "08:02"

email_address = "sender_mail@outlook.com" 
email_password = "sender_password"
destination_address = "receiver@gmail.com"

sleep_time = 10
```

## Run
To start the seat finder, run the `main.py` file:
```sh
python3 main.py
```

The tool will periodically check for available seats according to the specified configuration and send an email notification when a seat is found.

## Structure
The project is organized as follows:
- `src/`: Contains the source code files.
  - `api.py`: Handles sending post request with a valid basic authentication header. 
  - `mail.py`: Handles sending email notifications.
  - `functions.py`: Core logic for checking seat availability.
  - `utils.py`: Utility functions for date formatting and other common tasks.
- `config.py`: Configuration file for setting up the tool.
- `main.py`: The entry point of the application.
- `stations.json`: JSON file containing station names and their corresponding IDs.
- `requirements.txt`: Lists the required Python packages.

## Disclaimer
This tool is intended only for educational purposes and is not affiliated with TCDD in any way. Please use responsibly and in accordance with TCDD's terms of service.
