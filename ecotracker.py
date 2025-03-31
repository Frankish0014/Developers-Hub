from datetime import datetime
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

base_url = "https://dsms.alphazentechnologies.com/api/resource/"

headers = {
    "Authorization": "token add68da305de272:ca36a1953c2edb8"
}

class Waste:
    def __init__(self):
        # No input needed in constructor
        pass

    def add_waste(self):
        # Prompt for waste details
        self.waste = input("Input name of waste: ")
        self.category = input("Input category of waste (Plastic, Metal, Wood, Organic, Chemical, Plastic, Glass): ")
        self.quantity = input("Input the quantity(kg): ")
        self.area = input("Input the area the waste was collected: ")
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Convert to string and correct format

        new_waste = {
            "waste_name": self.waste,
            "category": self.category,
            "weight": self.quantity,
            "location": self.area,
            "date_and_time": self.date
        }

        # Send data to the API
        response = requests.post(base_url + 'Waste', headers=headers, json=new_waste)
        if response.status_code == 200:
            print("\nSuccessfully added waste data.")
        else:
            print("\nFailed to add waste data. Please check your input.")

        # Call notification method when waste is added
        self.notification()

