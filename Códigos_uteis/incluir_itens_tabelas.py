import json
import pandas as pd
import requests
import time

URL = 'https://app.mercos.com/api/v1/produtos_tabela_preco'

HEADERS = {
    "ApplicationToken": "0e71c38e-b916-11e9-92af-0a876c3c98fe",
    "CompanyToken": "67177316-b718-11ea-a4cf-0242ac12000a"
}

with open('TABELAS_COM_ID.json', 'r') as file:
    tabelas = json.loads(file.read())

with open('ITENS_TABELA_PRECO.json', 'r') as file2:
    itens = json.loads(file2.read())

for item in itens:
    resultList = list(filter(lambda d: d['CODIGO_TABELA'] == item['DA1_CODTAB'], tabelas))
    item['TABELA_IDMercos'] = resultList[0]['IDMercos']

n = 0
while n < len(itens):
    item = itens[n]
    cod = item['B1_XIDMERC']

    url = URL
    r = requests.post(url, data=json.dumps({'tabela_id': item['TABELA_IDMercos'], 'produto_id': item['B1_XIDMERC'], "preco": item['DA1_PRCVEN']}), headers=HEADERS)
    print(f'[{n}/{len(itens)}] id {cod}...')
    print(r.text)
    if r.status_code == 429:
        print(r.status_code)
        d = json.loads(r.text)
        print(d)
        time.sleep(d['tempo_ate_permitir_novamente'])
    elif r.status_code == 200 or r.status_code == 201:
        print('Alterado com sucesso!')

        idMercos = r.headers['MeusPedidosID']
        item['PRODUTO_IDMercos'] = idMercos
        print(item['PRODUTO_IDMercos'])

        n += 1
    elif r.status_code == 400:
        print(r.text)
    elif r.status_code == 412:
        print(r.text)
        print(item)

with open('PRODUTOS_TABELA_COM_ID.json', 'w') as file:
    file.write(json.dumps(itens))

df = pd.DataFrame.from_dict(itens)
print(df)