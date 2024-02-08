import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    # my/sender details
    username = "codelearning8055@gmail.com"
    password = "ocoplbxnotvfdnha"

    # receiver details
    receiver = "indraneeljain8@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)




