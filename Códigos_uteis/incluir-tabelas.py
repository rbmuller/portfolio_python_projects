import json
import pandas as pd
import requests
import time

URL = 'abc'

HEADERS = {
    "ApplicationToken": "0e71c38e-b916-11e9-92af-0a876c3c98fe",
    "CompanyToken": "67177316-b718-11ea-a4cf-0242ac12000a"
}

url = URL
r = requests.get(url, headers=HEADERS)
print(r.text)

with open('TABELAS_PRECO.json', 'r') as file2:
    tabelas = json.loads(file2.read()) 

n = 0
while n < len(tabelas):
    tabela = tabelas[n]
    cod = tabela['CODIGO_TABELA']

    url = URL
    r = requests.post(url, data=json.dumps({'nome': tabela['DESC_TABELA'], 'tipo': 'P', "excluido": False, "acrescimo": None, "desconto": None}), headers=HEADERS)
    print(f'[{n}/{len(tabelas)}] id {cod}...')
    print(r.text)
    if r.status_code == 429:
        print(r.status_code)
        d = json.loads(r.text)
        print(d)
        time.sleep(d['tempo_ate_permitir_novamente'])
    elif r.status_code == 200 or r.status_code == 201:
        print('Alterado com sucesso!')

        idMercos = r.headers['MeusPedidosID']
        tabela['IDMercos'] = idMercos
        print(tabela['IDMercos'])

        n += 1
    elif r.status_code == 400:
        print(r.text)
    elif r.status_code == 412:
        print(r.text)
        print(tabela)


with open('TABELAS_COM_ID.json', 'w') as file:
    file.write(json.dumps(tabelas))

df = pd.DataFrame.from_dict(tabelas)
print(df)
