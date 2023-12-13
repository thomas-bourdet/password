import re
import hashlib

def validate_password():
  while True:
      password = input("Entrez un mot de passe : ")
      if len(password) < 8:
          print("Assurez-vous que votre mot de passe a au moins 8 lettres")
      elif re.search('[0-9]', password) is None:
          print("Assurez-vous que votre mot de passe contient un chiffre")
      elif re.search('[A-Z]', password) is None: 
          print("Assurez-vous que votre mot de passe contient une lettre majuscule")
      elif re.search('[a-z]', password) is None:
          print("Assurez-vous que votre mot de passe contient une lettre minuscule")
      elif re.search('[@$!%*#?&]', password) is None:
          print("Assurez-vous que votre mot de passe contient un caractère spécial")
      else:
          print("Votre mot de passe semble correct")
          hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
          print("Votre mot de passe crypté est : ", hashed_password)
          break

validate_password()
