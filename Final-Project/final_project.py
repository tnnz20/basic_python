import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#----------Sumber------------
#belajarpython.com "parsing txt"
#realpython.com/python-send-email "penggunaan modul email"
#qastack.id/programming/3362600/how-to-send-email-attachments "attachment"

#parsing file txt untuk penerima mail menggunakan file txt
file = open('Final-Project/receiver_list.txt', 'r').read()
flx = file.split()

#deklarasi inputan untuk mail
sender_email = "sulthan.a2.pilkom@gmail.com"
rec_email = flx
attach = open("Final-Project/pilar.jpg", "rb").read()
body = """\
Ini dikirim melalu SMPT Python
Sebagai Tugas Terakhir


Terimakasih :)
"""
html ="""\
<html>
    <body>
        <h1>----------Pesan Html----------</h1>
        <p style="color:red;">Warna Merah</p>
    </body>
</html>
"""
#melampirkan suatu file
part = MIMEBase('application', "octet-stream")
part.set_payload(attach)
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="pilar.jpg"')

#draf mail
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = ', '.join(flx)
msg['Subject'] = 'Final Project'

#input text dan lampiran ke mail
msg.attach(MIMEText(body, 'plain'))
msg.attach(MIMEText(html,'html'))
msg.attach(part)
text = msg.as_string()

#login ke server smtp
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

#login user
password = input(str("Masukan Password :"))
try:
    server.login(sender_email, password)
    #kirim mail
    server.sendmail(sender_email, rec_email, text)
    print("Mail Berhasil Dikirim")
except:
    print("Mail gagal untuk dikirim coba lagi")
#keluar dari server
server.quit()