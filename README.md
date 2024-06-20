# Band Tour Scraper App

## Overview
The Band Tour Scraper App is a Python-based application designed to monitor a music band's website for new tour announcements. Upon detecting new tours, it sends out email notifications and records the tour details in both a text file and an SQLite database. The app operates continuously to ensure that users are promptly informed of any upcoming events.

## Features
- **Website Monitoring**: Checks the band's official website for updates on new tours.
- **Email Notifications**: Sends an email alert when new tour information is detected.
- **Data Storage**:
  - **Text File**: Stores tour details such as band name, city, and date in a `.txt` file.
  - **SQLite Database**: Records the same information in an SQLite database for robust data management.
- **Continuous Operation**: Runs non-stop to provide real-time updates.

## Prerequisites
- Python 3.x
- SQLite
- Additional Python packages: `requests`, `selectorlib`, `smtplib`, `sqlite3`, `time`, `ssl`, `os`

## Installation
1. Clone the repository:
   ```shell
   git clone https://github.com/Mahdi-Meyghani/Music_Tour_Scraper.git

2. Navigate to the app directory:
   ```shell
   cd Music_Tour_Scraper

3. Install the required packages:
   ```shell
   pip install -r requirements.txt

## Usage
To start the application, run:
   ```shell
   python main.py
```

## Configuration
Before running the app, configure the following settings in `main.py` `send_email` function:
- EMAIL_SETTINGS: Email configuration for sending notifications.
   ```python
  host = "smtp.your_host.com"
  port = "your_port"
  username = "example@email.com"
  password = "your_email_password"
  receiver = "receiver@email.com"

## License
This project is licensed under the Apache-2.0 license - see the `LICENSE.md` file for details.

## Acknowledgments
- The band for their inspiring music and tours.
- Contributors who have helped with the development of this app.

## Contact
- For any queries or further assistance, please contact Your Email.
- Feel free to customize the README file to better fit your application's specifics and your personal preferences. 
If you need further assistance with the code or any other aspect of your project, just let me know! :)
