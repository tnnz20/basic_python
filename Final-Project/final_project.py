import smtplib #import library smtplib

sender_email ="sulthan.a2.pilkom@gmail.com" #email pengirim
rec_email = "kaitora200@gmail.com" #email penerima
password = input(str("Masukan Password :")) #input password
message = "Tugas Jarkom MAIL" #pesan yang akan diterima 

server = smtplib.SMTP('smtp.gmail.com', 587) #menkonek ke smtplib dengan email yang tersedia 
server.starttls()
server.login(sender_email, password) #proses login
print("Login Berhasil")
server.sendmail(sender_email, rec_email, message)
print("Email berhasil dikirim", rec_email)

#smtplib adalah simple Mail Transfer Protokol untuk menangani proses pengiriman dan routing email antar mail server