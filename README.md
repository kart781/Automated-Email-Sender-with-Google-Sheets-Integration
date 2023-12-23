<h1>Mail Automation </h1>

</h2><ins>Overview </ins></h2><br/>
<br/>

This project consists of two main components: a Python script for extracting data from a specific column in a Google Sheets document, and another Python script that uses smtplib to send out an email notification, potentially with the extracted data.

This google_sheets_extractors.py script is useful for automating the process of data extraction from Google Sheets, and it can be integrated into larger Python applications where data from a spreadsheet needs to be processed or analyzed. Remember, for the script to work, you need to have credentials.json from the Google Developer Console, and you must have access to the specified Google Sheets document.


Your email_notifier.py script is designed to send emails with an attachment to a list of recipients obtained from a Google Sheets document. The script uses the smtplib and email libraries for creating and sending emails. 
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

- Use email_notifier.py to send an email.
- Integrate it with google_sheets_extractor.py to send the extracted data via email, if needed.

</h2><ins>Example </ins></h2>
<br/>
<br/>
To send an email with data extracted from Google Sheets:

```python
   # In your main script
   import google_sheets_extractor
   import email_notifier
   data = google_sheets_extractor.get_column_data()  # Ensure this function is defined to return data
   email_notifier.send_email("Subject: Data Extracted", f"Extracted Data:\n{data}")
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
