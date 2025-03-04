import json
import csv


def revisar_bases():    
    with open('bases.json', 'r', encoding='utf-8') as json_file:
        bases = json.load(json_file)
    for base in bases:        
        procesa_revalidacion(base['email_owner'], base['name'], base['clasificacion'])
        

def revisa_usuarios(owner):
    with open('users.csv', newline='') as csvfile:
        usuarios = csv.DictReader(csvfile)
        for user in usuarios:
            if (user['user_id']==owner):
                return user
            

def valida_clasificacion(clasificacion):
    if(clasificacion == 'high' or clasificacion==""):
        return True
    else:
        return False

def procesa_revalidacion(usuario_owner, db, clasificacion):
    user=revisa_usuarios(usuario_owner)
    destinatario=''
    if(user['user_state']=="active"):
        destinatario= user['user_id']
    else:
        destinatario= user['user_manager']
    if (valida_clasificacion(clasificacion)): enviar_email(destinatario, db, clasificacion)
    registra_depuracion(db, usuario_owner, user['user_manager'], clasificacion )


def enviar_email(destinatario, db, clasificacion):
    print("Estimado "+destinatario+": Favor de confirmar si la base de datos "+db+" conserva la clasificación asignada de: "+clasificacion)

def registra_depuracion(db, owner, manager, clasificacion):
    
    with open('resultados.csv', 'a', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        if(csv_file.tell() == 0): 
            fieldnames = ["Nombre base", "Email owner", "Email manager", "Clasificacion"]
            writer.writerow(fieldnames)
        writer.writerow([db, owner, manager, clasificacion])



revisar_bases()