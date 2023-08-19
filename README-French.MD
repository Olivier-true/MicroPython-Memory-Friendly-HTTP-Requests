# Requêtes HTTP économes en mémoire pour MicroPython

Un module client HTTP léger et économe en mémoire pour MicroPython, optimisé pour les cas d'utilisation sur des appareils à ressources limitées tels que l'ESP32.

## Caractéristiques
- Empreinte mémoire minimale : Conçu pour économiser les ressources mémoire, ce qui le rend adapté aux systèmes embarqués et aux appareils IoT.
- Faible utilisation de la mémoire : Fournit une gestion efficace de la mémoire pendant les requêtes HTTP, en minimisant l'allocation et la désallocation de la mémoire.
- Prise en charge des requêtes GET et POST : Effectuez facilement des requêtes HTTP GET et POST avec des en-têtes et des données personnalisables.
- Prise en charge de HTTPS : Communiquez en toute sécurité avec les serveurs à l'aide du protocole SSL.
- Idéal pour MicroPython : Spécialement conçu pour les environnements MicroPython, il permet une intégration transparente.

## Tags
- micropython
- esp32
- requêtes
- efficace en mémoire
- faible mémoire
- client http
- iot
- intégré
- léger
- nanoframework

## Installation
1. Cloner ce dépôt : `git clone https://github.com/Olivier-true/MicroPython-Memory-Friendly-HTTP-Requests.git`
2. Copiez `krequests.py` sur votre périphérique MicroPython.
3. Commencez à utiliser le module dans vos projets MicroPython !

## Utilisation
Importez le module :
```python
import krequests as requests
```

### Requête HTTP GET
```requests.get(url -> str, headers={} -> dict, recvsize=1024 -> int) -> return tuple (headers -> dict, response -> bytes)```
```python
# Effectuer une requête HTTP GET
response_headers, response_data = requests.get("http://httpbin.org/")
print("En-tête du serveur:", response_headers)
print("Données de réponse:", response_data)
```
```python
# Effectuer une requête HTTP GET avec des en-têtes personnalisés
custom_headers = {"headerName": "headerValue"}
response_headers, response_data = requests.get("http://httpbin.org/", headers=custom_headers)
print("En-tête du serveur:", response_headers)
print("Données de réponse:", response_data)
```
```python
# Effectuer une requête HTTP GET et spécifier la taille des données reçues
response_headers, response_data = requests.get("http://httpbin.org/", recvsize=2048)
print("En-tête du serveur:", response_headers)
print("Données de réponse:", response_data)
```
### Requête HTTP POST
`requests.post(url -> str, data={} -> dict, data=b"" -> bytes, headers={} -> dict, recvsize=1024 -> int) -> return tuple (headers -> dict, response -> bytes)`
```python
# Effectuer une requête HTTP POST avec les données du formulaire
form_data = {"key": "value", "int": 7}
response_headers, response_data = requests.post("http://httpbin.org/post", data=form_data)
print("En-tête du serveur:", response_headers)
print("Données de réponse:", response_data)
```
```python
# Effectuer une requête HTTP POST avec des données JSON
json_data = "{'key': 'value'}".encode()
custom_headers = {"Content-Type": "application/json"}
response_headers, response_data = requests.post("http://httpbin.org/post", data=json_data, headers=custom_headers)
print("En-tête du serveur:", response_headers)
print("Données de réponse:", response_data)
```
```python
# Effectuer une requête HTTP POST avec des données binaires et spécifier la taille des données reçues
binary_data = b"some data"
response_headers, response_data = requests.post("http://httpbin.org/", data=binary_data, recvsize=2048)
print("En-tête du serveur:", response_headers)
print("Données de réponse:", response_data)
```
N'hésitez pas à contribuer à ce projet et à le rendre encore meilleur. Si vous rencontrez des problèmes ou si vous avez des suggestions, veuillez soumettre un problème ou une demande d'extension sur GitHub.

Réalisé avec ❤️ par Olivier.
