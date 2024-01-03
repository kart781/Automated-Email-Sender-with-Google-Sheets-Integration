import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

smtp_port = 587                 # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

# Set up the email lists
email_from = "karthikram781@gmail.com"
password = "etfrddwagddapxiq" # Replace with your actual password

# Define the email function
def send_emails(email_list, subject, body, attachment_path):
    # Connect with the server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(email_from, password)

        for recipient in email_list:
            # Create MIME object
            msg = MIMEMultipart()
            msg['From'] = email_from
            msg['To'] = recipient
            msg['Subject'] = subject

            # Email body
            body = body
            msg.attach(MIMEText(body, 'plain'))

            # Attach file
            try:
                with open(attachment_path, 'rb') as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f"attachment; filename={os.path.basename(attachment_path)}")
                    msg.attach(part)
            except Exception as e:
                print(f"An error occurred: {e}")
                continue

            # Send email
            try:
                server.sendmail(email_from, recipient, msg.as_string())
                print(f"Email sent to: {recipient}")
            except Exception as e:
                print(f"Failed to send email to {recipient}: {e}")