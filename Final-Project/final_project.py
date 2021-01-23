import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#parsing file txt untuk digunakan dalam python
file = open('Final-Project/email.txt', 'r').read()
flx = file.split()

#deklarasi inputan untuk mail
sender_email = "sulthan.a2.pilkom@gmail.com"
rec_email = flx
body = "Ini tugas terakhir\ncoba"

#melampirkan suatu file
part = MIMEBase('application', "octet-stream")
part.set_payload(open("Final-Project/pilar.jpg", "rb").read())
encoders.encode_base64(part)

part.add_header('Content-Disposition', 'attachment; filename="Final-Project/pilar.jpg"')

#draf mail
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = ', '.join(flx)
msg['Subject'] = 'Final Project'

#input text dan lampiran ke mail
msg.attach(MIMEText(body, 'plain'))
msg.attach(part)
text = msg.as_string()

#login ke server smtp
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

#login user
password = input(str("Masukan Password :"))
server.login(sender_email, password)
#kirim mail
server.sendmail(sender_email, rec_email, text)
#keluar dari server
server.quit()