import smtplib

sender = input("wie verstuurder:  ")
receivers = input("who are the reciepents:  ")
message = input("wat is het bericht:  ")

filterReceipients = receivers.replace ("" , "")
listreceipents = filterReceipients.split(",")

try: 
    server = smtplib.SMTP_SSL('mail.pandoraproducties.nl', 465)
    server.login("kaan", "39m9UeZb")

    for i in listreceipents: 
      server.sendmail(sender, i , message)

      print("the message worked!")

except:
  print("oops")
