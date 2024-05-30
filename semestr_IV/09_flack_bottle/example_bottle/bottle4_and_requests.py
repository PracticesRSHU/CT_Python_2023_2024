import requests # in venv: pip install requests
resp = requests.get('http://localhost:8080/learn/Python and other tools')
if resp.status_code == 200 and resp.text == "Say, let's learn the programming language: python and other tools!":
    print('It worked! That almost never happens!')
else:
    print('Argh, got this:', resp.text)





