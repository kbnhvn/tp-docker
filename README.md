# Examen du module docker

## Construction des tests

Chaque dossier correspond à un type de test et comporte le dockerfile permettant de lancer le container associé ainsi qu'un fichier python pour le code du test.
Le code de chaque test se présente sous la forme d'une fonction qui prend en paramètre les différents paramètres de la route de l'API à tester : 
- username
- password
- entrypoint
- sentence
- expected

Cela permet de réutiliser cette fonction afin de pouvoir tester d'autres valeurs pour ces paramètres.
