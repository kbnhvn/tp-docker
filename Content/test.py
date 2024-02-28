import os
import requests

# définition de l'adresse de l'API
api_address = 'api'
# port de l'API
api_port = 8000

# ----- Fonction de test ----- #

def content_test(username, password, entrypoint, sentence,  expected):
    # requête
    r = requests.get(
        url='http://{address}:{port}{entrypoint}'.format(address=api_address, port=api_port, entrypoint=entrypoint),
        params= {
            'username': '{username}'.format(username=username),
            'password': '{password}'.format(password=password),
            'sentence': '{sentence}'.format(sentence=sentence),
        }
    )


    output = '''
    ============================
        Content test
    ============================

    request done at "{entrypoint}"
    | username={username}
    | password={password}
    | sentence={sentence}

    expected result = {expected}
    actual restult = {score}

    ==>  {test_status}

    '''

    # score de la requête
    data=r.json()
    score=data.get('score')

    # affichage des résultats
    if expected == 'positive' and score > 0:
        test_status = 'SUCCESS'
    elif expected == 'negative' and score < 0:
        test_status = 'SUCCESS'
    elif expected == 'neutral' and score == 0:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = output.format(score=score, test_status=test_status, username=username, password=password, entrypoint=entrypoint, expected=expected, sentence=sentence)
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
values = [{"username": "alice", "password": "wonderland", "entrypoint": "/v1/sentiment", "sentence":"life is beautiful", "expected": "positive"}, 
          {"username": "alice", "password": "wonderland", "entrypoint": "/v2/sentiment", "sentence":"life is beautiful", "expected": "positive"}, 
          {"username": "alice", "password": "wonderland", "entrypoint": "/v1/sentiment", "sentence":"that sucks", "expected": "negative"}, 
          {"username": "alice", "password": "wonderland", "entrypoint": "/v2/sentiment", "sentence":"that sucks", "expected": "negative"}]

# ----- Test des valeurs ----- #

for v in values:
    content_test(v["username"], v["password"], v["entrypoint"], v["sentence"], v["expected"])
