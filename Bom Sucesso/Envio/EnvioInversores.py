#from argparse import _VersionAction
#from dataclasses import dataclass
import aiohttp
import asyncio
#import json


#
# Função para envio dos dados em HTTP (request.post)
#
async def envioPost(dadosMain,url,head):
    async with aiohttp.ClientSession(headers=head) as session:
        print(url)
        for dado in dadosMain:
            async with session.post(url,json=dado) as resp:
                print("Codigo de resposta: <",resp.status,">")
                





def envio_Inversores(vetor):
    #
    # Informações fundamentais para a comunicação com o servidor (token url e cabeçalho)
    #
    myToken = 'NKick68KLONcwzcRMS3KZyI7m4g5xoJwvDcsmS46JDhECTmFaSuhr0ew53yRW5t8f8wIjdpfScR8tRcjEWa8gXiDhVwtAsk9r0Q9oYRjyWoYP9VnMxUvPQnY'
    myUrl = 'https://api-data-receiver.mv-toth.com/inversors'
    head = {'X-API-KEY':myToken}
    print("Preparando envio de inversores")
    a=9
    listaDados = [None] * 22

    #
    # Definir a lista de dados
    #

    for i in range (101,123):
        if(vetor.get(i-100)!=None and len(vetor[i-100])==76):
            if((vetor[i-100][17]/1000)!=0 and (vetor[i-100][31]/1000)!=0):
                eficiencia = (vetor[i-100][31]/1000)/(vetor[i-100][17]/1000)
                eficiencia=eficiencia*100
            else:
                eficiencia =0
            dadosEnviar = {
            "cod":i,
            "e_diaria":float(vetor[i-100][2]/10),
            "e_total": float(vetor[i-100][4]),
            "tempo_total": float(vetor[i-100][6]),  
            "temperatura_inv": float(vetor[i-100][7]/10),
            "potencia_total_dc":float(vetor[i-100][17]/1000),
            "tensao_a": float(vetor[i-100][18]/10),
            "tensao_b": float(vetor[i-100][19]/10),
            "tensao_c": float(vetor[i-100][20]/10),
            "corrente_a": float(vetor[i-100][21]/10),
            "corrente_b": float(vetor[i-100][22]/10),
            "corrente_c": float(vetor[i-100][23]/10),
            "potencia_total_ac": float(vetor[i-100][31]/1000),
            "fp": float(vetor[i-100][34]/1000),
            "frequencia": float(vetor[i-100][35]/10),
            "status": float(vetor[i-100][37]),
            "bus_volt":a,
            "eficiencia": float(eficiencia),
            "pot_ativa": float(vetor[i-100][31]/1000),
            "pot_reativa": float(vetor[i-100][33]/1000),
            "tensao_combiner": 0,
            "temp_combiner": 0,
            "corrente_max": 0,
            "corrente_media": 0,
            "corrente_total": 0,
            "pot_total_dc": 0,
            "e_diaria_combiner": 0,
            "e_total_combiner": 0,
            "alarme": 0,
            "usina_id": 1,
            "modelo": "Modelo XXX",
            "sn": "XXX",
            "pn": "XXX",
            "correntes_string": []
            }
            
        #Estrutura de repetição para armazenar os dados de 14 "correntes_string"
        for y in range(7,20):
            dadosEnviar["correntes_string"].append({"cod": 0,"valor": 0})
             
        # lista com todos os dados para envio    
        listaDados[i-101]=dadosEnviar

    
    #função de envio HTTP
    try:
        asyncio.run(envioPost(listaDados,myUrl,head))
    except:
        print("ERRO no envio: 'Inversores'")
