#  TelegramBotCET - Cabo Especialista Temporário do Exército Brasileiro

<img align="left" src="tele_bot_img.png"> Acompanhamento de atualizações do processo seletivo de <abbr title="Cabo Especialista Temporário">CET</abbr> através de Bot no Telegram.
<br clear="left"/>


## Instale as dependencias
```shell
pip3 install -r requeriments.txt
```

## Configurações:

É necessário configurar os campos <kbd><samp>bot_key</samp></kbd> (com a *string* do **token do seu bot no Telegram**) e <kbd><samp>grupo_id</samp></kbd> (com o *inteiro* da **id do grupo no Telegram** onde o bot irá publicar as notícias):
```python
config = {"bot_key":"key_do_seu_bot","grupo_id":id_do_seu_grupo,"url":"http://www.11rm.eb.mil.br/index.php/ultimas-noticias/143-cet-cabo-especialista-temporario-2016"}
```
> O token é informado no momento da criação do Bot através do @BotFather  
  Outra forma de descobrir o token do bot é iniciando uma conversa com o bot @BotFather e usar o comando <code>/token <var>@NomeDoSeuBot</var></code>


