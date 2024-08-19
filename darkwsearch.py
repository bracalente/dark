from telethon import TelegramClient, events

# Substitua com seus próprios valores de API
api_id = ''
api_hash = ''
grupo_nome = 'Venari_By_BetterCyber'

# Inicializando o cliente Telegram
client = TelegramClient('session', api_id, api_hash)

async def main():
    # Solicitando a palavra-chave ao usuário
    palavra_chave = input("Digite a palavra-chave para pesquisa: ")
    encontrada = False

    # Acessando o grupo e buscando as mensagens
    async for message in client.iter_messages(grupo_nome):
        if palavra_chave in message.text:
            print(f"{message.date}: {message.sender_id} disse: {message.text}")
            encontrada = True
            break
    
    if not encontrada:
        print("Vendor Safe!! Ufa")

# Executando o cliente e a função main
with client:
    client.loop.run_until_complete(main())