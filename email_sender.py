import smtplib
import config



def send_email(applicant_email, applicant_first_name,application_code, school_location):
    TO = applicant_email
    SUBJECT = 'Your Application'
    TEXT ='\r\n'.join(['Dear %s!' % applicant_first_name, 'Your application code is %d.' % application_code, 'You have to attend your interview in: %s' % school_location])

    # Gmail Sign In
    gmail_sender = config.email_address
    gmail_passwd = config.email_password

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)

    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % gmail_sender,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])

    try:
        server.sendmail(gmail_sender, [TO], BODY)
        print('email sent')
    except:
        print(applicant_email)

    server.quit()

def send_email(applicant_email, applicant_first_name, mentor_name, interview_start):
    TO = applicant_email
    SUBJECT = 'Your Application'
    TEXT ='\r\n'.join(['Dear %s!' % applicant_first_name, 'Your mentor will be %s.' % mentor_name, 'You have to attend your interview at: %s' % interview_start])

    # Gmail Sign In
    gmail_sender = config.email_address
    gmail_passwd = config.email_password

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)

    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % gmail_sender,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])

    try:
        server.sendmail(gmail_sender, [TO], BODY)
        print('email sent')
    except:
        print(applicant_email)

    server.quit()