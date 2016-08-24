import smtplib

from email.mime.text import MIMEText

recipient1 = "zoomhgtk@gmail.com"
mail_host1 = "smtp.gmail.com:587"
mail_password1 = "lala1atch"
mail_sender1 = "vooomhgtk@gmail.com"



def send_email(recipient, subject, message, mail_sender, mail_host, mail_password):
    try:
        smtp_conn = smtplib.SMTP(mail_host)
        smtp_conn.ehlo()
        smtp_conn.starttls()
        smtp_conn.login(mail_sender, mail_password)
        print "conn created"

        message = MIMEText(message)
        message['To'] = recipient
        message['Subject'] = subject
        message['From'] = mail_sender
        smtp_conn.sendmail(mail_sender, recipient, message.as_string())
        smtp_conn.close()
        print "Your message has been sent"
        return True
    except Exception, e:
        return False
        print "oops something wrong"

send_email(recipient1, "Test", "sent by script", mail_sender1, mail_host1, mail_password1)

