import sender_stand_request
import data

# esta función cambia el valor del parámetro "name"
def get_kit_body(name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_body = data.kit_body.copy()
    # Se cambia el valor del parámetro name
    current_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor name requerido
    return current_body


# funcion para obtener el token
def get_new_user_token():
    # Creamos el usuario
    # Guardamos una copia del cuerpo de la solicitud para crear el usuario en la variable user_body
    user_body = data.user_body.copy()
    # El resultado de la solicitud para crear un/a nuevo/a usuario/a se guarda en la variable user_response
    user_response = sender_stand_request.post_new_user(user_body)

    authtoken = user_response.json()["authToken"]

    return authtoken

def positive_assert(kit_body):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body_change
    kit_body_change = get_kit_body(kit_body)

    #obtenemos el token
    authtoken = get_new_user_token()

    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(kit_body_change,authtoken)

    # Comprueba si el código de estado es 201
    assert kit_response.status_code == 201

    #comprueba que el campo name del cuerpo de la solicitud coincide campo name del cuerpo de la respuesta
    assert kit_body_change["name"] == kit_response.json()["name"]


def negative_assert_code_400(kit_body):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body_change
    kit_body_change = get_kit_body(kit_body)

    # obtenemos el token
    authtoken = get_new_user_token()

    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(kit_body_change, authtoken)

    # Comprueba si el código de estado es 400
    assert kit_response.status_code == 400

def negative_assert_no_name_code_400(kit_body):
    # obtenemos el token
    authtoken = get_new_user_token()

    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable kit_response
    kit_response = sender_stand_request.post_new_client_kit(kit_body, authtoken)

    # Comprueba si el código de estado es 400
    assert kit_response.status_code == 400

# Prueba 1. El número permitido de caracteres (1)
# El parámetro "name" contiene 1 caracter
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert(data.name_one_letter)

# Prueba 2. El número permitido de caracteres (511)
# El parámetro "name" contiene 511 caracteres
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert(data.name_511_letter)

# Prueba 3. El número de caracteres es menor que la cantidad permitida (0)
# El parámetro "name" contiene 0 caracteres
def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert_code_400(data.name_zero_letter)

# Prueba 4. El número de caracteres es mayor que la cantidad permitida (512)
# El parámetro "name" contiene 512 caracteres
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_code_400(data.name_512_letter)

# Prueba 5. Se permiten caracteres especiales
# El parámetro "name" contiene caracteres especiales
def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert(data.name_with_special_symbol)

# Prueba 6. Se permiten espacios
# El parámetro "name" contiene espacios
def test_create_kit_has_space_in_name_get_success_response():
    positive_assert(data.name_with_spaces)

# Prueba 7. Se permiten números
# El parámetro "name" contiene numeros
def test_create_kit_has_number_in_name_get_success_response():
    positive_assert(data.name_with_numbers)

# Prueba 8. El parámetro no se pasa en la solicitud
# La solicitud no contiene el parámetro "name"
def test_create_kit_no_name_get_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "kit_body_copy"
    # De lo contrario, se podrían perder los datos del diccionario de origen
    kit_body_copy = data.kit_body.copy()
    # El parámetro "name" se elimina de la solicitud
    kit_body_copy.pop("name")
    # Se comprueba la respuesta
    negative_assert_no_name_code_400(kit_body_copy)

# Prueba 9. Se ha pasado un tipo de parámetro diferente (número)
# El parámetro "name" es de tipo numerico
def test_create_kit_number_type_name_get_success_response():
    negative_assert_code_400(data.name_of_type_number)