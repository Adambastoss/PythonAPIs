import requests

url = 'https://viacep.com.br/ws/{}/json/'

ceps = [
    '72240413',
    '72127991'
]

registros = []

for cep in ceps:
    resposta = requests.get(url.format(cep))
    if resposta.status_code == 200:
        payload  = resposta.json()
        registros.append(f"{payload['cep']}" \
                         f"{payload['logradouro']}" \
                         f"{payload['complemento']}\n")
        
for registro in registros:
    print(registros)