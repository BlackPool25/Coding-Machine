import requests

api_url = 'https://api.api-ninjas.com/v1/randomword'
response = requests.get(api_url, headers={'X-Api-Key': 'gMY+ncDIck3AxtJXl4MIPg==5AGSGXbqdwsqveL2'})
if response.status_code == requests.codes.ok:
    word = response.json()
    word_list = word["word"]
else:
    print("Error:", response.status_code, response.text)
