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

Az = [chr(32+i) for i in range(95)]
print(Az)
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

import datetime

# d=[['id', 'nom', 'prenom', 'date_naissance', 'debut_SEP', 'ntel', 'sexe', 'metier', 'loisirs', 'ville_residence', 'grand_ville', 'medecin_traitant', 'traitement', 'couvMed', 'email', 'auth', 'sep', 'active', 'recovery'], [2, 'Boumart', 'Imane', datetime.date(1989, 8, 10), '2014', '0669211655', 'Féminin', 'Cadre en industrie pharmaceutique', 'Danser ', 'Casablanca ', 'Casablanca', 'Mr Iraqi ', 'Aucun', 'Aucun', 'imaneboumart@hotmail.com', True, True, None, None], [3, 'Ben zairh', 'Mustapha ', datetime.date(1997, 4, 12), '2021', '0766555597', 'Masculin', 'Étudiant ', 'Voyage ', 'Nancy', 'Casablanca', 'Colombo', 'Ocrevus', 'Aucun', 'mustapha.benzairh@gmail.com', True, True, None, None], [5, 'Abouzia', 'Chaimaa', datetime.date(1986, 4, 13), '2021', '0661547080/ 0610101027', 'Féminin', 'Responsable administratif Ste informatique ', 'Sport , voyage, music', 'Rabat', 'Rabat', 'Dr ouafaa Mouti', 'Gilenya', 'CNSS', 'Chaimaa.abouzia@gmail.com', True, True, None, None], [6, 'Miss', 'Sb', datetime.date(1992, 3, 19), '2019', '0662248243', 'Féminin', 'Banquière ', 'Sport ', 'Casablanca ', 'Casablanca', 'Dr Midafi Naila ', 'Aubagio', 'Cmim', 'Sbouiri@outlook.com', True, True, None, None], [7, 'Ballouki', 'Adel', datetime.date(1987, 12, 14), '2011', '0667059351', 'Masculin', 'Ingenieur informatique', 'Musiue natation ', 'Casablanca', 'Casablanca', 'Professeur Slassi', 'Tysabri', 'CNSS', 'Adel.ballouki@gmail.com', True, True, None, None], [8, 'Elb', 'Soumaya', datetime.date(1990, 12, 2), '', '0615062164', 'Féminin', 'supply chain', 'Musique', 'Marseille', '', '', '', 'Aucun', 'Soumaya.elb@hotmail.fr', True, False, None, None], [9, 'Louizi ', 'Asmaa ', datetime.date(1990, 11, 29), '2014', '0691719400', 'Féminin', 'Comptable ', 'Voyage,lecture ', 'Casablanca ', 'Casablanca', 'Docteur Adil Iraqi houssaini ', 'Gilenya', 'CNSS', 'louizi.asmaa@gmail.com', True, True, None, None], [10, 'chairi', 'abderafie', datetime.date(2005, 2, 1), '2006', '0754654665', 'Masculin', 'prof', 'sport', 'fnideq', 'Tétouan', 'Zahraoui', 'Aucun', 'CNSS', 'abderafiechairi02@gmail.com', True, True, None, None], [11, 'Gannoune ', 'Aziza', datetime.date(1986, 8, 24), '2009', '', 'Feminin', 'Ingénieur ', 'Yoga / vélo/ couse', 'Agadir', 'Agadir', 'Pr Slassi', 'Autre', 'CFE', 'Aziza.gannoune@gmail.com', True, True, None, None], [12, 'Zian', 'Yousra', datetime.date(1992, 4, 20), '2019', '0666950099', 'Féminin', 'Ingénieur industriel', 'No longer know', 'Tetouan', 'Tétouan', 'Mrani Alia', 'Betaferon', 'Mutuelle privée', 'Yousrazian@gmail.com', False, True, None, None], [13, 'Mokaddem', 'Sofia', datetime.date(1988, 6, 7), '2015', '0620767143', 'Féminin', 'Cadre', 'Tout et rien', 'Casablanca', 'Casablanca', 'Dr naila midafi', 'Aucun', 'Aucun', 'Sofia.mokaddem@gmail.com', True, True, None, None], [14, 'Touahar ', 'Asmae', datetime.date(1991, 5, 14), '2008', '0697825216', 'Féminin', 'Dentiste ', 'Yoga ,coloriage, lecture ', 'Sidi kacem', 'Sidi Kacem', 'Aucun ', 'Aucun', 'CNOPS', 'Asmaetouahar1@gmail.com', True, True, None, None], [15, 'Benriyene', 'Salwa', datetime.date(1986, 9, 11), '2003', '0664887575', 'Féminin', "Ingénieur d'état en informatique", 'Randonnées, voyages', 'Casablanca', 'Casablanca', 'Dr slassi', 'Avonex', 'Atlanta sanad', 'Salwabenriyene@gmail.com', True, True, None, None], [16, 'Houdou', 'Tarik', datetime.date(1981, 6, 13), '2008', '0661858353', 'Masculin', 'Coordinateur', 'La marche', 'Casablanca', 'Casablanca', 'Mouti', 'Avonex', 'CNSS', 'Tarikhoudou@gmail.com', True, True, None, None], [17, 'Korich', 'Mohamed nazih', datetime.date(1991, 12, 22), '2018', '0671245494', 'Masculin', 'Employé ', 'Football', 'Tanger', 'Tanger', 'Docteur fadil hicham', 'Tysabri', 'CNSS', 'Korichnazih@gmail.com', True, True, None, None], [18, 'Bahta ', 'Youssef ', datetime.date(1994, 7, 21), '2013', '0706853737', 'Masculin', 'Commercial ', 'Cinéphile ', 'Casablanca ', 'Casablanca', 'Slassi ', 'Ocrevus', 'CNSS', 'youssefbahta@gmail.com', True, True, None, None], [19, 'Mastour ', 'Abdelmajid ', datetime.date(1990, 6, 24), '2013', '0614883359', 'Masculin', 'Banquier', 'Divers', 'Casablanca ', 'Casablanca', 'Dr. Midafi naila', 'Aucun', 'Mutuelle privée', 'Abdelmajid.mastour@hotmail.com', True, True, None, None], [20, 'YAALAOUI ', 'Fouad', datetime.date(1991, 10, 13), '2018', '0677010784', 'Masculin', 'Sans', 'Pêche', 'Sidi rahal', 'Casablanca', 'Dr bouchra moutawakil', 'Gilenya', 'CNSS', 'Yaalaoui.fouad07@gmail.com', True, True, None, None], [21, 'Baïna', 'Mouna', datetime.date(1985, 11, 21), '2018', '0670287054', 'Féminin', 'Femme au foyer', 'Natation', 'Tamesna', 'Rabat', 'Benaaboud bouchra', 'Rebif', 'CNOPS', 'mounabaina@gmail.com', True, True, None, None], [22, 'Cherkaoui', 'Oumaima', datetime.date(1980, 1, 5), '2011', '0600636021', 'Féminin', 'Mère au foyer', 'Sport', 'Mohammedia ', 'Mohammédia', 'Iraqui Houssaini Adil', 'Ocrevus', 'CNOPS', 'oumaimac80@gmail.com', True, True, None, None], [23, 'Nejjar', 'Oussama', datetime.date(1974, 12, 31), '1975', '0664344344', 'Masculin', 'Employé de banque', '.', 'Casablanca', 'Casablanca', 'Dr Adil laraqui', 'Ocrevus', 'Cmim', 'onejjar@gmail.com', True, True, None, None], [24, 'Mouti', 'Ouafa', datetime.date(1972, 4, 10), '', '0667225471', 'Féminin', 'Médecin neurologue', 'Sport', 'Rabat', '', '', '', 'Aucun', 'ouafamouti@yahoo.fr', False, False, None, None], [25, 'Faroini', 'Wafaa', datetime.date(1995, 5, 18), '2015', '0607639319', 'Féminin', 'Ingenieure genie civil ', 'Sport', 'Casablanca', 'Casablanca', 'Dr. Ilham Slassi', 'Ocrevus', 'CNSS', 'wafaa.faroini1@gmail.com', True, True, None, None], [26, 'chairi', 'abderafie', datetime.date(2002, 2, 1), '2002', '076206106654', 'Masculin', 'Prof', 'Sport', 'Fnideq', 'Rabat', 'Zahraoui', 'Aucun', 'CNSS', 'testToken@gmail.com', True, False, None, None], [27, 'chairi', 'abderafie', datetime.date(2002, 2, 1), '2002', '076206106654', 'Masculin', 'Prof', 'Sport', 'Fnideq', 'Rabat', 'Zahraoui', 'Aucun', 'CNSS', 'testTokenLocalHost@gmail.com', True, False, False, '4BRNBK'], [29, 'chairi', 'abderafie', datetime.date(2002, 1, 1), '', '0765412313', 'Masculin', 'hello', 'world', 'Rabat', '', '', '', 'Aucun', 'Soumiameniam2@gmail.com', False, False, False, 'RFKIG5']]
# dd=[[str(i) for i in row] for row in d ]
# print('\n'.join([','.join(i) for i in dd]))
d='Tetouan'
print(''.join([i if d!='é' else 'e' for i in d]))