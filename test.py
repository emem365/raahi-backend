import requests

BASE = "https://raahi-version-beta.herokuapp.com/"

response = requests.get(BASE+'helloworld/namsmdaasda')
print(response.json())