# from Sep import *
# from config import ProductionConfig


# app=create_app(ProductionConfig)

# with app.app_context():
# 	user = Admin.query.first()
# 	print(user.email)
# 	print(user.password)





# import  requests, os
# TRUSTIFI_URL='https://be.trustifi.com'
# TRUSTIFI_KEY='fff6a731534c67910cbe6ce95c1843459234f993cac4ef1c'
# TRUSTIFI_SECRET='3bbec8c80dcfe0bd038a2ba3c3c23c07'
# url = TRUSTIFI_URL+'/api/i/v1/email'

# payload = "{\"recipients\":[{\"email\":\"sepanouir.maroc@gmail.com\"}],\"title\":\"Sepnaouir\",\"html\":\"Hello mester abderafie chairi\"}"
# headers = {
#   'x-trustifi-key': TRUSTIFI_KEY,
#   'x-trustifi-secret':TRUSTIFI_SECRET,
#   'Content-Type': 'application/json'
# }

# response = requests.request('POST', url, headers = headers, data = payload)
# print(response.json())


# import requests


# DJANGO_MAILGUN_SERVER_NAME = ''
# DJANGO_MAILGUN_API_KEY = ''

# recipient_list = ['email@one.com', 'email@two.com']

# for email in recipient_list:
# 	requests.post(
#         DJANGO_MAILGUN_SERVER_NAME + "/messages",
#         auth=("api", DJANGO_MAILGUN_API_KEY),
#         data={"from": "Us <us@email.com>",
#               "to": email,
#               "o:campaign": "", # optional, but it was cool (and creepy) to track opens and clicks.
#               "subject": "Your subject",
#               "text": 'Your alt text for non-html clients',
#               }


# import smtplib

# rec_email ='abderafiechairi02@gmail.com'
# sender_email = 'sepanouir.maroc@gmail.com'
# pwd = 'gexxrmihlbqnhxfn'
# msg ='hello world'

# server = smtplib.SMTP('smtp.gmail.com',587)
# server.starttls()
# server.login(sender_email, pwd)
# print('login seccuful')


# server.sendmail(sender_email, rec_email, msg)
# print('email > ',rec_email)


# api_key='57a4d05d-7095-4a6c-8a35-35fd9c4b4d8f'
# import requests

# email_address = "abderafiechairi01@gmail.com"
# response = requests.get(
#     "https://isitarealemail.com/api/email/validate",
#     params = {'email': email_address},
#      headers = {'Authorization': "Bearer " + api_key })

# status = response.json()['status']
# if status == "valid":
#   print("email is valid")
# elif status == "invalid":
#   print("email is invalid")
# else:
#   print("email was unknown")


# def test():
# 	# raise Exception("hhhhhhh")
# 	print('test')

# try:
# 	test()
# except Exception as e:
# 	print(e)
# else:
# 	print("else")
# finally:
# 	print("finally")