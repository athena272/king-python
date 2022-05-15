def emailValido(email):
    status = 'certo'
    if(email.index('@') == 0):
        status = 'errado'

    elif(email.count('@') > 1):
        status = 'errado'

    elif((email.index('@') +1) == email.index('.') ):
        status = 'errado'

    email = email.split('.')
    if(len(email) < 3):
        status = 'errado'
    
    elif(email[0] == '' or email[1] == '' or email[2] == ''): 
        status = 'errado' 

    return status

while True:
    email = input()
    if (email == 'sair') : break

    print(emailValido(email))
    

