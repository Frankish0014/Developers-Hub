EcoTracker

Project Overview
EcoTracker is a waste management and recycling system developed as a dedicated service to promote environmental sustainability. Designed for seamless operation, EcoTracker efficiently tracks and manages waste collection, sends automated notifications to companies for waste pickup, and encourages eco-friendly recycling practices.

Features
Log waste data including name, category, quantity, location, and timestamp.
Automatically sends email notifications to relevant companies based on waste category.
View waste collection history filtered by location.

Prerequisites
Python 3.7+
Gmail account with SMTP enabled and an app password.

Installation
Clone the repository:
git clone https://github.com/Frankish0014/Developers-Hub.git
cd ecotracker
Install dependencies:
pip install requests

Configuration
All configurations, including the base_url and API token, are constants in the script. The service is designed for a controlled environment, where these values remain fixed.

Usage
Run the script:
python ecotracker.py
Follow the on-screen prompts:
Option 1 (Add Waste): Prompts for waste name, category, quantity, location, and logs the data. Sends email notifications to relevant companies based on the waste category.
Option 2 (View Waste History): Prompts for a location and displays all waste records logged for that location, showing details like name, category, quantity, and date.
Option 3 (Exit): Safely exits the program.

License
EcoTracker is licensed under the MIT License.

Contribution
As this service is designed for dedicated use, contributions are limited to internal developers. For suggestions or enhancements, please reach out directly.

 
