def send():
    import smtplib
    gmail_user = 'projectRF.test@gmail.com'
    gmail_password = 'projectRF.test1234'

    sent_from = gmail_user
    to = ['michiel_pieters@student.uhasselt.be']
    subject = 'somebody is by your door'
    #body = 'http://127.0.0.1:4554/deur'
    body = 'http://34.77.237.235/deur'

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print('Email sent!')
    except:
        print('Something went wrong...')
