import hashlib
import json
import os

def my_json_add(hashed, user):
    fd = open('mdp.json')
    nw_dict = json.load(fd)
    nw_dict[user] = hashed
    fd.close()
    fd = open('mdp.json', 'w')
    json.dump(nw_dict, fd, indent=4)
    fd.close

def my_json_starter(hashed, user):

    try :
        open('mdp.json')
    except:
        nw_dict = {user : hashed}
        open_file = open("mdp.json", 'w')
        json.dump(nw_dict, open_file, indent=4)
        open_file.close()
    else:
        my_json_add(hashed, user)

def my_print_error(list):
    
    ret = 0

    if list[0] == 1:
        print('Le mot de passe doit faire au moins 8 caractères')
        ret = 1
    if list[1] == 1:
        print('le mot de passe doit contenir au moins une lettre majuscule')
        ret = 1
    if list[2] == 1:
        print('le mot de passe doit contenir au moins une lettre minuscule')
        ret = 1
    if list[3] == 1:
        print('le mot de passe doit contenir au moins un chiffre')
        ret = 1
    if list[4] == 1:
        print('le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *)')
        ret = 1
    if list[5] == 1:
        print('le mot de passe contient au moins un caractère non géré')
        ret = 1
    return (ret)
    
def my_verif(test):
    
    list_error = [0, 1, 1, 1, 1, 0]

    if (len(test) < 8):
        list_error[0] = 1
    for char in test:
        if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            list_error[1] = 0
        elif char in 'abcdefghijklmnopqrstuvwxyz':
            list_error[2] = 0
        elif char in '0123456789':
            list_error[3] = 0
        elif char in '!@#$%^&*':
            list_error[4] = 0
        else:
            list_error[5] = 1
    return(my_print_error(list_error))

def my_check_data_mdp(password):
    try: 
       fd = open('mdp.json')
    except:
        return(True)
    test = hashlib.sha256(password.encode()).hexdigest()
    data = json.load(fd)
    fd.close()
    for key in data:
        if (test == data[key]):
            return(False)
    return(True)


def my_get_password():

    password = input('Veuillez entrer votre mot de passe : ')
    confirm_check = False
    while(confirm_check == False):
        if (my_verif(password) == 0):
            if (my_check_data_mdp(password) == True):
                verif_pswrd = input('Veuillez confirmer votre mot de passe : ')
                if(verif_pswrd == password):
                    confirm_check = True
                else:
                    print('Les deux mots de passe doivent être identiques')
            else:
                print('Désolé mais ce mot de passe est déja pris')
        if (confirm_check == False):
            password = input('Veuillez entrer un nouveau mot de passe : ')
    return(password)

def my_get_user():
    user = input("Veuillez définir un nom d'utilisateur ")
    if (len(user) == 0):
        return(my_get_user())
    try :
        fd = open('mdp.json', 'r')
    except:
        return(user)
    data = json.load(fd)
    for key in data:
        if user == key:
            print("Ce nom d'utilisateur est deja pris")
            return(my_get_user())
    return(user)

def my_password_handler():
    user = my_get_user()
    password = my_get_password()
    hashed = hashlib.sha256(password.encode()).hexdigest()
    my_json_starter(hashed , user)

def my_data_reader():
    try:
        fd = open('mdp.json')
    except:
        print('pas de données enregistrées')
        return()
    data = json.load(fd)
    for key in data:
        print("le mot de passe (crypté) associé à l'utilisateur", key, 'est :', data[key])
    
def my_del_json():
    try:
        open('mdp.json')
    except:
        print("Il n'y a pas de base de donées a supprimer")
    else:
        os.remove('mdp.json')

def my_menu():
    i = 0
    print("-Tapez 1 pour enregistrer un mot de passe")
    print("-Tapez 2 pour afficher les mots de passe")
    print("-Tapez 3 pour supprimer la base données")
    print("-Tapez 4 pour sortir du programme")
    while (i != 4):
        try :
            i = int(input("Selection : "))
        except ValueError:
            i = 0
        if (i == 1):
            my_password_handler()
        if (i == 2):
            my_data_reader()
        if (i == 3):
            my_del_json()
        elif ( i <= 0 or i > 4):
            print("La saisie est invalide")


my_menu()