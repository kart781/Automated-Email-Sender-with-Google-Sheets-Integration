# In your main script
import google_sheets_extractor
import email_notifier

data = google_sheets_extractor.get_column_data()
test_recipient = data
subject = "Test Subject"
body = "Test Body"
attachment_file = r'Your Path'
email_notifier.send_emails(test_recipient, subject, body, attachment_file)