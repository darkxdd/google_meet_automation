
## Join Google Meet automatically with camera and microphone turned off using a Python script

This Python script uses Selenium to log into your Gmail account and then join a Google Meet meeting with the camera and microphone turned off.

## Prerequisites
- Python 3
- pip
- Google Chrome
- ChromeDriver (compatible with your Google Chrome version)

## Installation
1. Install the required packages:
   ```fish
   pip install selenium pytz
   ```
2. Install ChromeDriver:

   For Windows:
   ```fish
   winget install -e --id Chromium.ChromeDriver
   ```
   For Mac OS:
   ```fish
   brew install --cask chromedriver
   ```
4. Clone the repository:
   ```fish
   git clone https://github.com/darkxdd/google_meet_automation.git
   ```
5. Navigate to the project directory:
   ```fish
   cd google_meet_automation
   ```

## Usage
1. Run the script:
   ```fish
   python main.py
   ```
2. The script will prompt you for the following inputs:
   - **Email Address**: Your Gmail email address
   - **Password**: Your Gmail password (entered securely)
   - **Meeting Link**: The Google Meet meeting link
   - **Start Time**: The time to join the meeting in the format `HH:MM:SS` (IST)
   - **End Time**: The time to leave the meeting in the format `HH:MM:SS` (IST)
3. The script will log into your Gmail account, join the meeting, turn off the microphone and camera, and then exit the meeting at the specified end time.

## How it works
1. The script uses the Selenium WebDriver to automate the browser interactions.
2. The `Glogin` function logs into your Gmail account by entering the email and password.
3. The `turnOffMicCam` function finds and clicks the microphone and camera buttons to turn them off before joining the meeting.
4. The `joinNow` function calculates the wait time before joining and exiting the meeting, and then performs the actual joining and exiting actions.
5. The script uses the `pytz` library to handle time zone conversions between the user's local time (IST) and UTC.
