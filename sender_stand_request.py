import configuration
import requests
import data

#Solicitud para crear un nuevo usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers_user)  # inserta los encabezados

def post_new_client_kit(kit_body, auth_token):
    headers_kit_change = data.headers_kit.copy()
    headers_kit_change["Authorization"] = "Bearer "+auth_token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,  # inserta la dirección URL completa
                         json=kit_body,  # inserta el cuerpo de solicitud
                         headers=headers_kit_change) # inserta los encabezados
                         #auth=auth_token)