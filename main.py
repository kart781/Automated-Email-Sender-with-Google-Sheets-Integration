import os
import google_sheets_extractor
import email_notifier
from file_selector import file_path

data = google_sheets_extractor.get_column_data()
test_recipient = data
subject = "Test Subject"
body = "Test Body"
attachment_file = os.path.normpath(str(file_path))
email_notifier.send_emails(test_recipient, subject, body, attachment_file)