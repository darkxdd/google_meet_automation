
## Join Google Meet automatically with camera and microphone turned off using a Python script

This Python script uses Selenium to log into your Gmail account and then join a Google Meet meeting with the camera and microphone turned off.

## Prerequisites
- Python 3
- pip
- Google Chrome
- ChromeDriver (compatible with your Google Chrome version)

## Installation
1. Install the required packages:
   ```
   pip install selenium
   ```
2. Clone the repository:
   ```
   git clone https://github.com/darkxdd/google_meet_automation.git
   ```
3. Navigate to the project directory:
   ```
   cd google_meet_automation
   ```

## Usage
1. Open the `main.py` file and update the following variables with your information:
   - `mail_address`: Your Gmail email address
   - `password`: Your Gmail password
   - `meeting_link`: The Google Meet meeting link you want to join
2. Run the script:
   ```
   python main.py
   ```
3. The script will prompt you to enter the meeting start and end times in the format `HH:MM:SS`.
4. The script will log into your Gmail account, join the meeting, turn off the microphone and camera, and then exit the meeting at the specified end time.

## How it works
1. The script uses the Selenium WebDriver to automate the browser interactions.
2. The `Glogin` function logs into your Gmail account by entering the email and password.
3. The `turnOffMicCam` function finds and clicks the microphone and camera buttons to turn them off before joining the meeting.
4. The `joinNow` function calculates the wait time before joining and exiting the meeting, and then performs the actual joining and exiting actions.
5. The script uses the `pytz` library to handle time zone conversions between the user's local time (IST) and UTC.
