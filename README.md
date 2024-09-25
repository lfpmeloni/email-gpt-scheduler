# email-gpt-scheduler

Automate your daily schedule by integrating OpenAI's GPT model with your email workflow. This script reads tasks from an Excel file, generates a customized daily schedule using GPT-3.5, and sends the schedule via email to the recipient of your choice.

## Features
- Input your daily tasks into an Excel file.
- The script retrieves the tasks, processes them, and generates a detailed schedule using OpenAI's GPT-3.5.
- Automatically sends the generated schedule via email.
- Fully configurable with environment variables for email and API integration.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/lfpmeloni/email-gpt-scheduler.git

2. Navigate to the project directory:

cd email-gpt-scheduler

3. Install the required Python packages:

pip install -r requirements.txt
Create a .env file in the root directory and add your email, password, recipient_email, and OpenAI API key:

EMAIL=your_email_address
PASSWORD=your_email_password
RECIPIENT_EMAIL=recipient_email_address
OPENAI_API_KEY=your_openai_key

## Usage

Add your tasks to the activities.xlsx file. The script reads from this file to generate the schedule.

1. Run the script:

The script will automatically generate a daily schedule and send it via email to the specified recipient.

2. Example
Here is an example of tasks you can add to the activities.xlsx file:

Task	Deadline	Effort Required
Walk the dog	2024-09-25	30 minutes
Attend course	2024-09-25	8 hours
Finish project	2024-09-26	4 hours
Prepare dinner	2024-09-25	1 hour

The GPT model will generate a detailed schedule based on these tasks and email it to you.

3. Environment Setup

Create a .env file:

Store sensitive information like your email, password, recipient email, and OpenAI API key in this file to avoid exposing them in the code.

Configure SMTP Access:

The script uses Gmail's SMTP server. Make sure to enable "less secure apps" for your Gmail account or use an app-specific password if you have 2FA enabled.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue.

## License
This project is licensed under the MIT License - see the LICENSE file for details.