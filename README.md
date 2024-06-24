# Descrição

Este script Python utiliza as bibliotecas os e Imbox para conectar-se a uma conta de email via protocolo IMAP, ler emails de um remetente específico e salvar anexos desses emails em uma pasta local.

# Funcionalidades principais

- Conexão IMAP: O script estabelece uma conexão segura com um servidor IMAP (por exemplo, Gmail) usando a biblioteca Imbox, permitindo acesso aos emails.

- Filtragem por remetente e título: Ele filtra os emails não lidos baseados em um remetente específico e no título, procurando por emails que contenham a palavra-chave "fatura".

- Salvando anexos: Para cada email que corresponde aos critérios, o script salva todos os anexos na pasta local especificada (pasta_anexos). Caso exista um arquivo com o mesmo nome, adiciona um sufixo numérico para evitar sobrescrita.


# Componentes utilizados

- os: Biblioteca padrão do Python para manipulação de diretórios e arquivos.
- Imbox: Uma biblioteca Python para interagir com servidores IMAP e manipular emails.

# Uso
Antes de executar o script, certifique-se de instalar as bibliotecas necessárias (Imbox e PyMuPDF). O script pode ser configurado com suas credenciais de email, o remetente específico a ser filtrado e as pastas onde os anexos e textos serão salvos.

Este script é útil para automação de tarefas que envolvem o processamento de emails com anexos, como extrair faturas, relatórios ou outros documentos importantes anexados aos emails.
