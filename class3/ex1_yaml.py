import snmp_helper
from datetime import datetime, timedelta
import yaml
# Uptime when running config last changed

ip_addr1 = "184.105.247.70"
ip_addr2 = "184.105.247.71"

port = 161

snmp_user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'

a_user = (snmp_user, auth_key, encrypt_key)

device1 = (ip_addr1, port)
device2 = (ip_addr2, port)


import smtplib

from email.mime.text import MIMEText

recipient1 = "zoomhgtk@gmail.com"

mail_host1 = "smtp.gmail.com:587"
mail_password1 = "lala1atch"
mail_sender1 = "vooomhgtk@gmail.com"

def get_the_current_value(device, user):
    '''
    to get the current value of ccmHistoryRunningLastChanged
    and the value of uptime
    to calculate out how many hundredths of seconds did the change happen before NOW
    '''
     
    ccmHistoryRunningLastChanged = '1.3.6.1.4.1.9.9.43.1.1.1.0'
    sysUptime = '1.3.6.1.2.1.1.3.0'
    output = snmp_helper.snmp_get_oid_v3(device, user, ccmHistoryRunningLastChanged)
    last_change = snmp_helper.snmp_extract(output)
    output = snmp_helper.snmp_get_oid_v3(device, user, sysUptime)
    uptime = snmp_helper.snmp_extract(output)
    dvalue = int(uptime) - int(last_change)
    value = (last_change, uptime, dvalue)

    return value


def save_status(filename, value):
    '''
    save the current value of ccmHistoryRunningLastChanged
    '''

    status = []
    status.append({})
    status[-1]['time_stemp'] = str(datetime.now())
    status[-1]['value'] = value
    with open(filename, "a") as stream:
        stream.write(yaml.dump(status, default_flow_style = False))

def read_status(filename):
    '''
    read the value of ccmHistoryRunningLastChanged from yaml file
    '''
    try:
        with open(filename, "r") as stream:
            current = yaml.load(stream)
            return current[-1]["value"]
    except IOError:
        return "NULL"
    '''
    do not use print, it will cause the equaty between
    this func and get_the_current_value to be False,
    even when you see it by eye, they look equal to each other
    '''

def no_need_to_save_new(filename, current_value):
    '''
    determin whether to write a new status to yaml file
    '''
    return read_status(filename) == current_value


def send_email(recipient, subject, message, mail_sender, mail_host, mail_password):
    '''
    use smtplib to send email via gmail server, the conn.starttls() is indispensable
    '''
    try:
        smtp_conn = smtplib.SMTP(mail_host)
        smtp_conn.ehlo()
        smtp_conn.starttls()
        smtp_conn.login(mail_sender, mail_password)

        message = MIMEText(message)
        message['To'] = recipient
        message['Subject'] = subject
        message['From'] = mail_sender
        smtp_conn.sendmail(mail_sender, recipient, message.as_string())
        smtp_conn.close()
        print "The email has been sent."
        return True
    except:
        "Email sending is failed"

def config_change_detector(device, user, filename):
    '''
    call no_need_to_save_new to determin if there is a new change
    if there is a new change, call send_email to send email
    '''
    value = get_the_current_value(device, user)
    last_change = value[0]
    uptime = value[1]
    dvalue = value[2]
    if device == device1:
        device_name = "rtr1"
    else:
        device_name = "rtr2"

    if no_need_to_save_new(filename, last_change):
        print "Nothing changed on %s" % device_name
        print "****************************", "\n"
    else:
        save_status(filename, last_change)
        print "Change detected on %s" % device_name

        dvalue_in_seconds = dvalue/100
        change_was_at = datetime.now() - timedelta(seconds=dvalue_in_seconds)
        change_was_at = str(change_was_at)

        if device == device1:
            subject = "rtr1 has been changed"
        else:
            subject = "rtr2 has been changed"

        message = "the change happend at %s PDT" % change_was_at

        send_email(recipient1, subject, message, mail_sender1, mail_host1, mail_password1)
        print "****************************", "\n"
#config_change_detector(device1, a_user, "device1_status.yml")

def main():
    '''
    use for loop to run for two devices
    '''

    for device in (device1, device2):
        if device == device1:
            dest_filename = "device1_status.yml"
        else:
            dest_filename = "device2_status.yml"
            
        config_change_detector(device, a_user, dest_filename)

if __name__ == "__main__":
    main()
