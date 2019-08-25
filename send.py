import csv
import smtplib
from email.mime.multipart import MIMEMultipart
import time

line_0 = 'send email to me'
line_1 = 'hi fadhil i just got back from yellowstone and completely fell in love with it.'
line_2 = 'set subject to Yellowstone adventures'
line_3 = 'let me know if next weekend works for dinner so i can tell you all about it.'

def email_form():
    global get_from
    global get_email
    element = 'to'
    to_element = get_list.index(element)
    to_set = to_element + 1 

    # Get 'From' user
    path = './data/'
    lis = list(csv.reader(open(path + 'user_data.csv')))
    some_list = lis[-1]
    get_from = some_list[1]
    print('From: '+get_from)

    # Get 'To' user
    if 'me' in get_list:
        get_email = some_list[1]
        print('To: '+ get_email)
    else:
        get_to = get_list[to_set]
        with open(path +'email.csv') as csvfile:
            database = csv.DictReader(csvfile)
            for row in database:
                name = row['name']
                get_email = row['email']
                if get_to == name:
                    print('To: '+ get_email)
    write_email()

def write_email():
    global subject
    global body
    # Get subject
    if 'set' and 'subject' in line_1.split():
        get_subject = line_1.split()
        body_1 = ''
    else:
        get_body_1 = line_1.split()
        body_1 = ' '.join(str(e) for e in get_body_1)

    if 'set' and 'subject' in line_2.split():
        get_subject = line_2.split()
        body_2 = ''
    else:
        get_body_2 = line_2.split()
        body_2 = ' '.join(str(e) for e in get_body_2)

    if 'set' and 'subject' in line_3.split():
        get_subject = line_3.split()
        body_3 = ''
    else:
        get_body_3 = line_3.split()
        body_3 = ' '.join(str(e) for e in get_body_3)

    if 'set' and 'subject' in get_subject:
        element_0 = 'set'
        element_0 = get_subject.index(element_0)
        del get_subject[element_0]

        element_1 = 'subject' 
        element_1 = get_subject.index(element_1)  
        del get_subject[element_1]

        if 'to' in get_subject:
            element_2 = 'to'
            element_2 = get_subject.index(element_2)
            del get_subject[element_2]

        if 'for' in get_subject:
            element_2 = 'for'
            element_2 = get_subject.index(element_2)
            del get_subject[element_2]
    
        subject = ' '.join(str(e) for e in get_subject)
        print('Subject: '+subject)
    # Get Body
    body = body_1 + '\n' + body_2 + '\n' + body_3
    print('Body: ' +body)
    time.sleep(2)
    send_email()


# send email
def send_email():
    path = './data/'
    lis = list(csv.reader(open(path + 'user_data.csv')))
    some_list = lis[-1]
    get_password = some_list[2]

    msg = 'Subject: {}\n\n{}'.format(subject, body)
    mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
    mailServer.starttls()
    mailServer.login(get_from , get_password)
    mailServer.sendmail(get_from, get_email, msg)
    print("\nSent!")
    mailServer.quit()

get_list = line_0.split()
if 'send' and 'email' in get_list:
    email_form()