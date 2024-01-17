import webbrowser
# searching the term in google

user_term = input("Enter the term which you want to search ").replace(" ", "+")

webbrowser.open("https://www.google.com/search?q="+ user_term)
