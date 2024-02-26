import os
import requests

# définition de l'adresse de l'API
api_address = 'api'
# port de l'API
api_port = 8000

# ----- Fonction de test ----- #

def authorization_test(username, password, entrypoint, expected):
    # requête
    r = requests.get(
        url='http://{address}:{port}{entrypoint}'.format(address=api_address, port=api_port, entrypoint=entrypoint),
        params= {
            'username': '{username}'.format(username=username),
            'password': '{password}'.format(password=password),
            'sentence': 'hello world'
        }
    )


    output = '''
    ============================
        Authorization test
    ============================

    request done at "{entrypoint}"
    | username={username}
    | password={password}
    | sentence=hello world

    expected result = {expected}
    actual restult = {status_code}

    ==>  {test_status}

    '''

    # statut de la requête
    status_code = r.status_code

    # affichage des résultats
    if status_code == expected:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = output.format(status_code=status_code, test_status=test_status, username=username, password=password, entrypoint=entrypoint, expected=expected)
    print(output)

    # impression dans un fichier
    print(os.environ.get('LOG'))
    if os.environ.get('LOG') == '1':
        try:
            with open('/log/api_test.log', 'a') as file:
                file.write(output)
        except Exception as e:
            print(f"Erreur lors de l'écriture dans le fichier : {e}")


# Valeurs à tester
values = [{"username": "alice", "password": "wonderland", "entrypoint": "/v1/sentiment", "expected": 200}, 
          {"username": "alice", "password": "wonderland", "entrypoint": "/v2/sentiment", "expected": 200}, 
          {"username": "bob", "password": "builder", "entrypoint": "/v1/sentiment", "expected": 200}, 
          {"username": "bob", "password": "builder", "entrypoint": "/v2/sentiment", "expected": 403}]

# ----- Test des valeurs ----- #

for v in values:
    authorization_test(v["username"], v["password"], v["entrypoint"], v["expected"])
