
# TCDD Train Seat Finder (TCDD Bilet Bulucu)

## Overview
<em>For Turkish see `README_TR.md`. | Türkçe anlatım için `README_TR.md`dosyasını inceleyin.</em>

The TCDD Train Seat Finder is a Python-based tool designed to help users find available seats on Turkish State Railways (TCDD) trains. It automates the process of checking seat availability for specified routes, dates, and, optionally, times. When an available seat is found, the tool notifies the user via email, providing details such as the train name, journey date, wagon number, and seat number.

## Features
- **Automated Seat Checking**: Automatically checks for available seats on specified train routes.
- **Email Notifications**: Sends email alerts when available seats are found, with detailed information.
- **Configurable Searches**: You can specify departure and arrival stations, journey dates, and optionally, preferred departure times.

## Installation

### Prerequisites
- Python 3.x
- Pip (Python package installer)

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


## Configuration
Before using the tool, you must configure it by editing the `config.py` file located in the `src` directory. Set the following parameters according to your preferences:

- `binis_istasyon_adi`: Name of the departure station.
- `inis_istasyon_adi`: Name of the arrival station.
- `date`: Date of the journey (format: YYYY-MM-DD).
- `check_specific_hour`: Set to `True` if you want to check for trains at a specific hour, otherwise `False`.
- `hour`: Preferred hour for departure (format: HH:MM), required if `check_specific_hour` is `True`.
- `email_address`: Your email address from which the notification will be sent.
- `email_password`: Password for the email account above.
- `destination_address`: Email address to receive the notification.

**Note:**  `binis_istasyon_adi` and `inis_istasyon_adi` must be valid station names. See `stations.json` file for available station names.

## Usage
To start the seat finder, run the `main.py` file:
```sh
python3 main.py
```

The tool will periodically check for available seats according to the specified configuration and send an email notification when a seat is found.

## Structure
The project is organized as follows:
- `src/`: Contains the source code files.
  - `config.py`: Configuration file for setting up the tool.
  - `email_notifications.py`: Handles sending email notifications.
  - `seat_checker.py`: Core logic for checking seat availability.
  - `utils.py`: Utility functions for date formatting and other common tasks.
- `main.py`: The entry point of the application.
- `stations.json`: JSON file containing station names and their corresponding IDs.
- `requirements.txt`: Lists the required Python packages.

## Disclaimer
This tool is intended only for educational purposes and is not affiliated with TCDD in any way. Please use responsibly and in accordance with TCDD's terms of service.
