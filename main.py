# Hashzap
# botao de iniciar chat
    # popup para entrar no chat
# quando entrar no chat: (aparece para todo mundo)
    # a mensagem que você entrou no chat
    # o campo e o botão de enviar mensagem
# a cada mensagem que você envia (aparece para todo mundo)
    # Nome: Texto da Mensagem

import flet as ft 

#função pricipal:
def main(pagina):
    #abaixo esta as funcionalidades:

    
    titulo = ft.Text('PyChat')


    titulo_janela= ft.Text('Bem vindo ao PyChat')
    campo_nome_do_usuario = ft.TextField(label= 'Escreva seu nome no chat') #rotulo da caixa de colocar o nome do usuario
    
    chat=ft.Column() #para as mensagem aparecer uma abaixo da outra como se fosse uma coluna
    
    def conexao_tunel(mensagem):
        texto_chat= ft.Text(mensagem) #pego o que foi digitado no campo de mensagem que o usuario enviou
        chat.controls.append(texto_chat) #adiciono o valor do que foi adicionado dentro da coluna chat
        pagina.update()
    pagina.pubsub.subscribe(conexao_tunel) #cria o tunel de comunicacao  publica o site usando o pub
    
    def enviar_mensagem(evento):
       mensagem_enviada = campo_mensagem.value 
       nome_usuario = campo_nome_do_usuario.value
       mensagem = f'{nome_usuario}: {mensagem_enviada}'
       pagina.pubsub.send_all(mensagem) #envio a mensagem para todo mundo usando a funcao do tunel de comunicacao
       
       campo_mensagem.value = '' #para apagar a mensagem anterior do campo de mensagem quando for digitar outra mensagem
       pagina.update()

    campo_mensagem = ft.TextField(label='Digite sua mensagem...' , on_submit=enviar_mensagem) #campo onde o usuario preenche
    botao_enviar_msg = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
    linha_mensagem = ft.Row([campo_mensagem , botao_enviar_msg])

    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_inciar)
        janela.open = False  #fecha janela        
        pagina.add(chat) #abre o chat                                              
        pagina.add(linha_mensagem) #botão para enviar a msg e#add o campo para o usuario digitar a mensagem na mesma linha
        mensagem = f'{campo_nome_do_usuario.value} entrou no chat'
        pagina.pubsub.send_all(mensagem)
        pagina.update()

    botao_entrar_chat = ft.ElevatedButton('Entrar no chat', on_click= entrar_chat)
    janela = ft.AlertDialog(
                            title= titulo_janela ,
                            content=campo_nome_do_usuario,
                            actions= [botao_entrar_chat])
    
    def iniciar_chat(evento):
        pagina.dialog = janela #a janela(dialog é a janela criada)
        janela.open = True #abro a janela pois inicialmente criada ela é fechada
        pagina.update()
        
    botao_inciar = ft.ElevatedButton('Iniciar Chat', on_click= iniciar_chat)
    pagina.add(titulo) #adiciona na pagina principal
    pagina.add(botao_inciar)
    


ft.app(main , view=ft.WEB_BROWSER)
