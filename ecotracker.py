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

    def notification(self):
        # Fetch companies from the Company table
        company_data = requests.get(base_url + 'Company?limit_page_length=100&fields=["*"]', headers=headers).json()
        
        recipients = []
        # Loop through the company table to find matching category
        for company in company_data["data"]:
            if company["category"].lower() == self.category.lower():  # Case-insensitive comparison
                recipients.append(company["email"])

        # If no matching companies found, notify the user
        if not recipients:
            print("No matching companies found for the given category.")

        # Send notification to the recipient
        for email in recipients:
            subject = "Waste Collection Notification"
            message = f"A new waste item has been logged:\n- Name: {self.waste}\n- Category: {self.category}\n- Quantity(kg): {self.quantity}\n- Location: {self.area}\n- Date: {self.date}"
            self.send_email(email, subject, message)

    def send_email(self, to, subject, message):
        smtp_server = "smtp.gmail.com"  # Gmail SMTP server
        smtp_port = 587  # port
        smtp_user = "onuigbokelvin2003@gmail.com"  # Gmail address
        smtp_password = "huis fvly yrsz coii"  # Use app password or Gmail password

        # Create email
        msg = MIMEMultipart()
        msg["From"] = smtp_user
        msg["To"] = to
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain"))

        try:
            # Connect and send email
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_user, smtp_password)
                server.send_message(msg)
            print(f"\nNotification successfully sent")
        except Exception:
            print(f"Failed to send email")

    def waste_history(self):
        # Prompt user to input location to filter waste records
        location_input = input("Enter the location to filter waste records: ")

        # Get waste data from the waste table
        waste_data = requests.get(base_url + 'Waste?limit_page_length=100&fields=["*"]', headers=headers).json()

        # Filter waste records that match the input location (case-insensitive)
        for entry in waste_data["data"]:
            if entry["location"].lower() == location_input.lower():
                for key, value in entry.items():
                    if key not in {"name", "owner", "creation", "modified", "modified_by", "docstatus", "idx"}: # Exclude unnecessary keys
                        print(f"{key}: {value}")
                print("-" * 30)  # Separator for clarity


# Main menu
waste = Waste()
while True:
    print("\n1. Add Waste")
    print("2. View Waste History")
    print("3. Exit")

    choice = input("Please choose an option: ")

    if choice == "1":
        waste.add_waste()  # Add waste data and send notifications if applicable
    elif choice == "2":
        waste.waste_history()  # View waste history filtered by location
    elif choice == "3":
        print("Exiting the program.")
        break  # Exit the loop and the program
    else:
        print("Invalid option. Please try again.")
