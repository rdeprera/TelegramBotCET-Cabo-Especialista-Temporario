#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests,telepot,random,time
from bs4 import BeautifulSoup

# Esse Bot foi desenvolvido por mim para acompanhar as atualizacoes do processo seletivo CET 2016 - Cabo Especialista Temporario 2016 do exercito Brasileiro e me notificar pelo telegram.
# Jhonathan Davi A.K.A jh00nbr / Insightl4b lab.insightsecurity.com.br
# jh00nbr: http://jhonathandavi.com.br
# Blog: lab.insightsecurity.com.br
# Github: github.com/jh00nbr
# Twitter @jh00nbr

__author__ = "Jhonathan Davi A.K.A jh00nbr"
__email__ = "jdavi@insightsecurity.com.br"

config = {"bot_key":"5188411229:AAGI6AwmuA6-BWu1FfCovMgoVLyFB-EZxkY","grupo_id":1837262102,"url":"http://www.11rm.eb.mil.br/index.php/ultimas-noticias/207-cet-cabo-especialista-temporario-2019-2020"}
bot = telepot.Bot(config['bot_key'])
group = config['grupo_id']

def carregar_useragents():
    uas = []
    with open("user-agents.txt", 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[0:-1-0])
    random.shuffle(uas)
    return uas

def verificar_novidades():
    ua = random.choice(carregar_useragents())
    req = requests.get(config['url'],headers={'User-Agent': ua})
    soup = BeautifulSoup(req.content,'html.parser')
    #print(vars(soup))

    conteudo_div = soup.find('div',{'class':'item-page'})
    if conteudo_div.findAll('a'):
        atualizacoes = conteudo_div.findAll('a')
        #print(vars(atualizacoes))
    
    qnt_novidades = 10 # Quantidade de noticias em 19/10/2016
    novidades = []

    for novidade in atualizacoes:
        if novidade.string:
            #print(vars(novidade))
            novidades.append(novidade.string)
            qnt_novas_novidades = len(novidades)
            #print(novidade.string)
            novidade = novidade.string 

    if int(qnt_novas_novidades) > qnt_novidades:
        novidade = novidades[1]
        qnt_novidades += 1
        bot.sendMessage(group,novidade)
        print(novidade, " | Novidades: ", qnt_novidades)
    else:
        print("[+] Sem novidades :(")

if __name__ == '__main__':
    while True:
        time.sleep(600) # Verifica de 7 em 7 minutos
        #time.sleep(5) # Verifica de 5 em 5 segundos (debug)
        print('while')
        verificar_novidades()
