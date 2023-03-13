password = input('Veuillez entrer votre mot de passe : ')

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
    if list[5] == 1:
        print('le mot de passe contient au moins un caractère non géré')
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

def my_get_password(password):

    confirm_check = False
    while(confirm_check == False):
        if (my_verif(password) == 0):
            verif_pswrd = input('Veuillez confirmer votre mot de passe : ')
            if(verif_pswrd == password):
                confirm_check = True
            else:
                print('Les deux mots de passe doivent être identiques')
        if (confirm_check == False):
            password = input('Veuillez entrer un nouveau mot de passe : ')
    return(password)

print(my_get_password(password))