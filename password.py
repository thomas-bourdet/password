import re
import hashlib
import json
import random
import string
import os

# Fonction pour vérifier la complexité d'un mot de passe
def password_check(password):
    return all([
        len(password) >= 8,  # Au moins 8 caractères
        any(char.islower() for char in password),  # Au moins une lettre minuscule
        any(char.isupper() for char in password),  # Au moins une lettre majuscule
        any(char.isdigit() for char in password),  # Au moins un chiffre
        any(char in "!@#$%^&*" for char in password)  # Au moins un caractère spécial parmi ceux listés
    ])

# Fonction pour hacher un mot de passe
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Fonction pour sauvegarder un mot de passe haché dans un fichier JSON
def save_password(hashed_password):
    filename = 'passwords.json'
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, filename)

    # Si le fichier n'existe pas, le créer avec une liste vide de mots de passe
    if not os.path.isfile(file_path):
        with open(file_path, 'w') as file:
            json.dump({"passwords": []}, file)

    # Charger les données existantes depuis le fichier JSON
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Vérifier si le mot de passe existe déjà dans la liste
    if hashed_password in data["passwords"]:
        print("Ce mot de passe existe déjà.")
    else:
        # Ajouter le mot de passe à la liste
        data["passwords"].append(hashed_password)

    # Sauvegarder la liste mise à jour dans le fichier JSON
    with open(file_path, 'w') as file:
        json.dump(data, file)

# Fonction pour générer un mot de passe aléatoire
def generate_password():
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(10))
    return password

# Fonction principale du programme
def main():
    while True:
        # Demander à l'utilisateur de saisir un mot de passe
        password = input("Choisissez un mot de passe d'au moins 8 charactères qui contiendra au moins 1 Majuscule, 1 Minuscule, 1 Chiffre et 1 Caractère Spécial: ")
        
        # Vérifier si le mot de passe satisfait les critères de complexité
        if password_check(password):
            # Hacher le mot de passe
            hashed_password = hash_password(password)
            
            # Sauvegarder le mot de passe haché dans le fichier JSON
            save_password(hashed_password)
            
            print("Votre mot de passe est enregistré.")
            break
        else:
            print("Votre mot de passe ne respecte pas les exigences de sécurité. Veuillez choisir un nouveau mot de passe.")
            
# Fonction pour visualiser les mots de passe existants
def view_passwords():
    filename = 'passwords.json'
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, filename)

    # Vérifier si le fichier existe
    if os.path.isfile(file_path):
        # Charger les données existantes depuis le fichier JSON
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Vérifier s'il y a des mots de passe enregistrés
        if data["passwords"]:
            print("Mots de passe existants :")
            for index, hashed_password in enumerate(data["passwords"], start=1):
                print(f"{index}. {hashed_password}")
        else:
            print("Aucun mot de passe enregistré.")
    else:
        print("Aucun fichier de mots de passe trouvé.")

# Exécuter la fonction principale si le script est exécuté en tant que programme principal
if __name__ == "__main__":
    main()
