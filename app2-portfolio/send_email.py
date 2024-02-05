import smtplib, ssl

host = "smtp.gmail.com"
port = 465


username = "codelearning8055@gmail.com"
password = "hgsryolxohuvydmb"

receiver = "indraneeljain8@gmail.com"
context = ssl.create_default_context()

message = """\
subject: Test message
Hi!
How are you?
Bye!
            """

with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)