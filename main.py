import hashlib
import json
import os
import random

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
    fd.close()
    for key in data:
        if user == key:
            print("Ce nom d'utilisateur est deja pris")
            return(my_get_user())
    return(user)

def my_randomizer():

    l_pwd = []
    pwd = ''
    maxi_list = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz', '1234567890', '!@#$%^&*']
    random.seed()
    l_pwd.append(maxi_list[0][random.randint(0, 25)])
    l_pwd.append(maxi_list[1][random.randint(0, 25)])
    l_pwd.append(maxi_list[2][random.randint(0, 9)])
    l_pwd.append(maxi_list[3][random.randint(0, 7)])
    for i  in range(4):
        j = random.randint(0, 3)
        if j == 0:
            l_pwd.append(maxi_list[j][random.randint(0, 25)])
        if j == 1:
            l_pwd.append(maxi_list[j][random.randint(0, 25)])
        if j == 2:
            l_pwd.append(maxi_list[j][random.randint(0, 9)])
        if j == 3:
            l_pwd.append(maxi_list[j][random.randint(0, 7)])
    random.shuffle(l_pwd)
    for i in l_pwd:
        pwd += i
    print("Votre mot de passe est", pwd, "veillez à le conserver")
    return(pwd)

def my_password_handler():

    user = my_get_user()
    try:
        i = int(input("Tapez '1' pour créer vous meme votre mot de passe ou '2' pour le créer aléatoirement : "))
    except:
        print('Saisie incorrecte')
        return()
    if (i == 1):
        password = my_get_password()
    elif (i == 2):
        password = my_randomizer()
    else:
        print('Saisie incorrecte')
        return()
    hashed = hashlib.sha256(password.encode()).hexdigest()
    my_json_starter(hashed , user)

def my_data_reader():
    try:
        fd = open('mdp.json')
    except:
        print('pas de données enregistrées')
        return()
    data = json.load(fd)
    fd.close()
    for key in data:
        print("le mot de passe (crypté) associé à l'utilisateur", key, 'est :', data[key])
    
def my_del_json():

    try:
        open('mdp.json')
    except:
        print("Il n'y a pas de base de donées a supprimer")
    else:
        os.remove('mdp.json')

def my_connect(data, key):

    test = data[key]
    cpt = 0
    while(cpt != 3):
        attempt = input("Veuillez taper le mot de passe correspondant à l'utilisateur voulu: ")
        attempt = hashlib.sha256(attempt.encode()).hexdigest()
        if (attempt == test):
            print('Opération validée')
            return(True)
        else:
            cpt += 1
            print("Mot de passe incorrect, il vous reste", 3-cpt, ' essais')
    return(False)

        
def my_del_user():

    del_usr = input("Renseigner le nom d'utilisateur a supprimer : ")
    try:
        fd = open('mdp.json')
    except:
        print("Pas de base de données a modifier")
        return()
    data = json.load(fd)
    fd.close
    for key in data:
        if (key == del_usr):
            if (my_connect(data, key) == True):
                data.pop(key)
                fd = open('mdp.json', 'w')
                json.dump(data, fd, indent=4)
                fd.close()
                return()
            else:
                print("Vous n'avez pas les droits sur cet utilisateur")
                return()
    print("Le nom d'utilisateur donné n'existe pas dans la base de données")

def my_modif_mdp():

    try:
        fd = open('mdp.json')
        data = json.load(fd)
        fd.close()
    except:
        print('Pas de base de données à modifier')
        return()
    usr = input("De quel utilisateur souhaitez-vous modifier le mot de passe ? ")
    for key in data:
        if (key == usr):
            if (my_connect(data, key)):
                new_pswrd = my_get_password()
                new_pswrd = hashlib.sha256(new_pswrd.encode()).hexdigest()
                my_json_add(new_pswrd, key)
                return()
            else:
                print("Vous n'avez pas les droits sur cet utilisateur")
                return()
    print("Le nom d'utilisateur donné n'existe pas dans la base de données")

def my_menu():

    i = 0
    method_list = [my_password_handler, my_data_reader, my_del_json, my_del_user, my_modif_mdp]

    print("-Tapez 1 pour enregistrer un mot de passe")
    print("-Tapez 2 pour afficher les mots de passe")
    print("-Tapez 3 pour supprimer la base données")
    print("-Tapez 4 pour supprimer un utilisateur")
    print("-Tapez 5 pour modifier un mot de passe")
    print("-Tapez 6 pour sortir du programme")
    
    while (i != 6):
        try :
            i = int(input("Selection : "))
        except ValueError:
            i = -1
        if (i > 0 and i <= 5):
            method_list[i - 1]()
        elif (i != 6):
            print("Saisie invalide")

my_menu()