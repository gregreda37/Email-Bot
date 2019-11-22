import os
import smtplib
import csv
import pandas as pd
from itertools import zip_longest
from Methods import Methods
import sched, time
s = sched.scheduler(time.time, time.sleep)

#List of contractor emails
contractorEmailList = []

#CSV File //Make sure the file is presented in your project folder
with open('drbill_contracting_new_jersey_email.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for line in csv_reader:
        contractorEmailList.append(line[0])

#Breaks up array into chunks to be sent
chunks = [[i for i in t if i is not None] for t in zip_longest(*(contractorEmailList,)*1)]
# print(chunks[2])
points = 0
def do_something(sc): 
    try:
        global points
        print( "Sending Email To..",chunks[points])
        with smtplib.SMTP('smtp.office365.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            #User name and password
            smtp.login('email@example.com', 'password')
    
            subject = 'Follow Up on the Free Marketing'
            body = 'Hey! I just wanted to follow up on the free marketing platform we discussed. Unlike most of our competitors, we are free for life! Just upload a profile and watch the new customers come pouring in. I attached a link to the app below to sign up. Thanks again!\n\n-Greg Reda \n https://apps.apple.com/gb/app/topbox-inc/id1476438064'

            msg = f'Subject: {subject}\n\n{body}'

            smtp.sendmail('contact@ukrainianrestoration.com', chunks[points], msg)

        print(points)
        print(chunks[points])
        points += 1
        # specify time frame you'd like to send the paginated emails
        # Example: Outlook Business allows 10,000 emails a day but only 30 a minuet. So if you paginate and send a bulk of 30 every minuet, you wont be caught
        s.enter(3, 1, do_something, (sc,))

    #Except if index is out of range
    except IndexError:
        print('No more lists')
        


s.enter(3, 1, do_something, (s,))
s.run()



