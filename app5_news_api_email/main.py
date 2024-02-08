import requests  # this is used to get content from url / brwose an api
from send_email import send_email

# below wo import is to fix smtplib.SMTPDataError: (550, b'5.7.1 This message is not RFC 5322 compliant.
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# To make the url dynamic
topic = "tesla"

api_key = "305cd13bea2348398dadfc5bc316e02d"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2024-01-08&"
       "sortBy=publishedAt&"
       "apiKey=305cd13bea2348398dadfc5bc316e02d&"
       "language=en")

# at the end of the url we added language=en parameter to get only english news
# Make request
request = requests.get(url)

# Get the dictionary with data
content = request.json()  # gets content from that url in json format

body = ""

# Create the container email message.
message = MIMEMultipart()
message['Subject'] = "Today's News"
message['From'] = 'codelearning8055@gmail.com'  # Replace with your email
message['To'] = 'indraneeljain8@gmail.com'  # Replace with recipient's email



# Access the article titles and description

for article in content["articles"][:20]:
    body = body + article["title"] + "\n" \
           + article["description"] \
           + "\n" + article["url"] + 3 * "\n"


# Attach the body to the email message
message.attach(MIMEText(body, 'plain'))

encoded_message = message.as_string().encode("utf-8")  # need to convert the body into this format before we send
# mail, else it throws error
send_email(message=encoded_message)
