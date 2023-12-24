<h1> Automated Email Sender with Google Sheets Integration </h1>

</h2><ins>Overview </ins></h2><br/>
<br/>

This project consists of two main components: a Python script for extracting data from a specific column in a Google Sheets document, and another Python script that uses smtplib to send out an email notification, potentially with the extracted data.

This [google_sheets_extractors.py](#Setup) script is useful for automating the process of data extraction from Google Sheets. This Python script is designed to extract data from a specific column in a Google Sheets document using the Google Sheets API. It automates the process of accessing, authenticating, and retrieving data from a user's spreadsheet. The script first checks for the presence of a `token.json` file, which holds the user's access and refresh tokens, essential for authentication. If this file is absent or contains invalid credentials, the script initiates a new authorization process using a `credentials.json` file. This file should be obtained from the Google Developer Console and is necessary for the script's initial setup and authorization.

Once authenticated, the script creates a service object for the Google Sheets API. It then specifies the `SPREADSHEET_ID` and the target range, which in this case is column C of the first sheet. The script fetches the data from this column, excluding the first row, usually a header.

The script is robust in handling HTTP errors that might occur during the API request, such as network issues or invalid spreadsheet IDs. It is particularly useful for applications requiring regular data extraction from Google Sheets for purposes like data analysis, reporting, or integration with other data processing tools. This makes it a valuable tool for automating and streamlining workflows that involve Google Sheets data.

Your [email_notifier.py](#Setup) script is designed to send emails with an attachment to a list of recipients obtained from a Google Sheets document. This Python script is designed to send emails with an attachment to multiple recipients using Gmail's SMTP server. It operates using the `smtplib` library and is structured to provide a secure and efficient way of handling email communication. The script requires the sender's Gmail credentials and uses port 587, adhering to the standard for secure SMTP communication.

The core functionality is encapsulated in the `send_emails` function, which accepts a list of recipients, a subject line, the email body, and the path of the attachment. The script establishes a secure TLS connection with the SMTP server and iterates over each recipient to send personalized emails. For the attachment, it reads the file in binary, encodes it with Base64, and attaches it to the email. The file name for the attachment is extracted using `os.path.basename`, ensuring that only the file name, not the full path, is displayed in the email.

The script includes robust error handling, gracefully managing issues like file access errors or problems in sending emails. It ensures that an issue with one recipient does not halt the entire process, allowing the script to attempt sending emails to all recipients in the list. This makes the script practical and reliable for bulk email sending tasks, particularly when distributing similar content, such as newsletters or notifications, to multiple individuals.
<br/>
</h2><ins>Prerequisites </ins></h2>
<br/>
<br/>
Before using this tool, ensure you have the following prerequisites installed:              

- Python 3.x
- Google account with access to Google Sheets
- Google Cloud Platform project with the Google Sheets API enabled
- google-auth, google-auth-oauthlib, and google-auth-httplib2 packages
- smtplib (standard library in Python) for sending emails

</h2><ins>Installation </ins></h2>
<br/>
<br/>
Make sure you have the following packages installed before executing the files in this repository

- Python 3.x: If you don't have Python 3.x installed, download and install it from the official Python website.
- Install required Python packages:

```bash
   pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
   pip install secure-smtplib
   pip install email
```

</h2><ins>Setup </ins></h2>
<br/>
<br/>

**Google Sheets API Credentials:**

- Go to the Google Developers Console.
- Create a new project or select an existing one.
- Enable the Google Sheets API for your project.
- Create credentials (OAuth client ID) and download the JSON file.
- Rename the downloaded file to credentials.json and place it in the project folder.

**OAuth Token:**

- Run the Google Sheets data extraction script for the first time.
- Follow the instructions to authenticate and authorize access to your Google Sheets.
- A file named token.json will be generated in your project folder.
- Google Sheets Data Extraction (google_sheets_extractor.py)
- This script extracts data from a specified column in a Google Sheets document.

**Google Sheets Data Extraction (google_sheets_extractor.py)**

This script extracts data from a specified column in a Google Sheets document. To use this script: 
- Update the SPREADSHEET_ID variable with your specific Google Sheets ID.
- Set the desired column in the range (e.g., "Sheet1!C:C" for column C).

**Email Notification System (email_notifier.py)**

This script sends an email using smtplib. To use this script:
- Configure your email settings (sender, receiver, SMTP server, etc.).
- If using Gmail, ensure that "Less secure app access" is enabled or use an App Password.

</h2><ins>Usage </ins></h2>
<br/>
<br/>

**Extract Data from Google Sheets:** 

- Run google_sheets_extractor.py.
- The script will output the data from the specified column.

**Send Email Notification:** 

- Use email_notifier.py to send an email. It can send mails to multiple recipients and can add attachments according to the specific need.
- Integrate it with google_sheets_extractor.py to send the extracted data via email, if needed.

</h2><ins>Example </ins></h2>
<br/>
<br/>


To send an email with data extracted from Google Sheets:

```python
   # In your main script
   import google_sheets_extractor
   import email_notifier
   
   data = google_sheets_extractor.get_column_data()
   test_recipient = data
   subject = "Test Subject"
   body = "Test Body"
   attachment_file = r'Your Path'
   email_notifier.send_emails(test_recipient, subject, body, attachment_file)
```

To use the program just call the following command in the terminal

```bash
   python main.py
```

</h2><ins>Additional Resources </ins></h2>
<br/>
<br/>
For more information and troubleshooting, refer to the following resources:

- Getting Started with Google Sheets API
- Python smtplib Documentation
- Setting Up OAuth 2.0

</h2><ins>Troubleshooting </ins></h2>
<br/>
<br/>

Common issues and solutions:

- Issue: Error when generating OAuth Token.
- Solution: Ensure you have followed all steps in the Google Cloud Console, and your credentials.json is correctly configured.
- Issue: Email not sending through smtplib.
- Solution: Check your email provider's settings, and if using Gmail, make sure you have allowed less secure apps or set up an App Password.

</h2><ins>Output </ins></h2>
<br/>
<br/>
The output of google_sheets_extractor.py will be a list of data extracted from the specified column in your Google Sheets document. This data can then be used as part of the email body in email_notifier.py, enabling you to send this information via email.
<br/>
<br/>
</h2><ins>Notes </ins></h2>
<br/>
<br/>

- Adhere to Google's Sheets API usage limits and quotas.
- Handle email credentials securely, especially when using Gmail's "Less secure app access."

</h2><ins>Disclaimer </ins></h2>
<br/>
<br/> 
This tool is for educational and informational purposes only. Use it responsibly and ensure compliance with all relevant laws and regulations.
<br/>
<br/>
</h2><ins>Contributions </ins></h2>
<br/>
<br/>
karthikram781@gmail.com
Feel free to contribute to this project by submitting issues or pull requests.
