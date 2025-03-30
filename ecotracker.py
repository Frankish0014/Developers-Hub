from datetime import datetime
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

base_url = "https://dsms.alphazentechnologies.com/api/resource/"

headers = {
    "Authorization": "token add68da305de272:ca36a1953c2edb8"
}
