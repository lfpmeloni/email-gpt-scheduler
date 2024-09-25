import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import openai
import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key and email credentials from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
email_address = os.getenv("EMAIL_ADDRESS")
email_password = os.getenv("EMAIL_PASSWORD")
recipient_email = os.getenv("RECIPIENT_EMAIL")

# Function to send the email
def send_email(subject, message, recipient):
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = recipient
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        # Connect to Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_address, email_password)

        # Send the email
        server.sendmail(email_address, recipient, msg.as_string())
        server.quit()
        print(f"Email successfully sent to {recipient}!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to generate a daily schedule suggestion using ChatGPT
def generate_schedule_suggestion(activities):
    activities_list = activities.to_dict(orient='records')

    prompt = (
        "Here is a list of activities for the day:\n\n"
        f"{activities_list}\n\n"
        "Based on the pending activities and the daily routine, create a detailed schedule for the day. "
        "Organize activities by time, breaking them into 'Morning', 'Afternoon', and 'Evening' blocks. "
        "For each task, consider the daily effort required and the deadline for completion. "
        "If there are too many tasks or the workload is excessive, suggest adjustments such as redistributing tasks "
        "throughout the week, adding breaks, or changing priorities. "
        "At the end of the schedule, include an analysis of the workload with recommendations for optimization and "
        "improvements in the routine to ensure a balance between productivity and well-being."
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant specializing in daily planning optimization."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1500,
        temperature=0.7
    )

    return response.choices[0].message['content'].strip()

# Main function
def main():
    try:
        # Load the activities spreadsheet
        activities = pd.read_excel("activities.xlsx")
        
        # Generate the daily schedule suggestion
        message = generate_schedule_suggestion(activities)

        # Send the schedule via email
        send_email("Daily Schedule", message, recipient_email)

    except Exception as e:
        print(f"An error occurred while processing the schedule: {e}")

# Execute the main function
if __name__ == "__main__":
    main()
