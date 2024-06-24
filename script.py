import os
from imbox import Imbox

#Dados da conta de email
host ='imap.gmail.com'
email = 'SEU_EMAIL@gmail.com'
password='SENHA_PODE_GERAR_SENHA_APP'

# Especificando o remetente
remetente_especifico = 'remetente@banco.com'

#Pasta para onde meus anexos vão
pasta_anexos = 'faturas'


# Função para gerar um nome de arquivo único
def gerar_nome_arquivo_unico(pasta, nome_arquivo):
    base, ext = os.path.splitext(nome_arquivo)
    contador = 1
    novo_nome_arquivo = nome_arquivo
    while os.path.exists(os.path.join(pasta, novo_nome_arquivo)):
        novo_nome_arquivo = f"{base}_{contador}{ext}"
        contador += 1
    return novo_nome_arquivo

#Lendo e-mails
with Imbox(host, username=email, password=password) as imbox:
    unread_messages = imbox.messages(sent_from=remetente_especifico)
    for uid, message in unread_messages:
        if message.attachments and 'fatura' in message.subject.lower():
            remetente = message.sent_from[0]['email'] if message.sent_from else 'Desconhecido'
            titulo = message.subject
            data = message.date
            print(f"Remetente: {remetente}")
            print(f"Título: {titulo}")
            print(f"Data: {data}")
            print('---')

            # Iterar sobre os anexos e salvar cada um na pasta especificada
            for attachment in message.attachments:
                nome_arquivo = attachment.get('filename')
                conteudo = attachment.get('content')

                # Ler o conteúdo do anexo como bytes
                conteudo_bytes = conteudo.read()

                # Gerar um nome de arquivo único
                nome_arquivo_unico = gerar_nome_arquivo_unico(pasta_anexos, nome_arquivo)

                # Caminho completo do arquivo
                caminho_arquivo = os.path.join(pasta_anexos, nome_arquivo_unico)

                # Salvar o anexo na pasta
                with open(caminho_arquivo, 'wb') as f:
                    f.write(conteudo_bytes)
                print(f"Anexo {nome_arquivo_unico} salvo em {caminho_arquivo}")
        else:
            print('lendo email')
print("Fim dos e-mails")