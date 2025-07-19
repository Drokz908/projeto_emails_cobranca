Sistema de Alerta de Pagamentos Pendentes

📄 Descrição do Projeto

Este é um sistema automatizado desenvolvido em Python para identificar clientes com pagamentos pendentes em um banco de dados MySQL e enviar-lhes avisos de cobrança por e-mail.

O objetivo principal é demonstrar a capacidade de:

Integração entre aplicações Python e bancos de dados relacionais (MySQL).

Automação de processos de comunicação (envio de e-mails via SMTP).

Manuseio seguro de credenciais e variáveis de ambiente.

Modelagem e consulta de dados em SQL.

✨ Funcionalidades
Conexão Segura: Estabelece conexão com o banco de dados MySQL utilizando variáveis de ambiente para proteção de credenciais.

Identificação de Inadimplentes: Consulta a tabela de clientes para identificar registros onde o status de pagamento (pago) indica pendência.

Envio de E-mails Automatizado: Envia e-mails personalizados para cada cliente inadimplente, alertando sobre a situação.

Gestão de Credenciais: Utiliza o arquivo .env para gerenciar informações sensíveis (credenciais de DB e SMTP), garantindo que não sejam expostas no código-fonte nem no controle de versão (Git).

🛠️ Tecnologias Utilizadas
Python 3.x: Linguagem de programação principal.

mysql-connector-python: Driver oficial para conexão com MySQL.

python-dotenv: Para carregar variáveis de ambiente.

smtplib, email.mime.text, email.mime.multipart: Módulos nativos para automação de e-mail.

MySQL: Sistema de gerenciamento de banco de dados relacional.

🚀 Como Executar o Projeto Localmente
Siga estes passos para configurar e rodar o projeto em sua máquina:

Clone o Repositório:

Bash

git clone https://github.com/SeuUsuario/NomeDoSeuRepositorio.git
cd NomeDoSeuRepositorio
(Substitua SeuUsuario/NomeDoSeuRepositorio pelo caminho real do seu repositório no GitHub)

Crie e Ative o Ambiente Virtual:

Bash

python -m venv venv
# No Windows:
.\venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate
Instale as Dependências:

Bash

pip install -r requirements.txt
Dica: Você pode gerar o requirements.txt com pip freeze > requirements.txt antes de commitar seu código.

Configuração do Banco de Dados MySQL:

Certifique-se de ter um servidor MySQL rodando.

Crie um banco de dados chamado cadastro_clientes (ou o nome que você usou no seu código).

Crie a tabela clientes com as colunas nome, email e pago (onde 0 indica não pago).

SQL

-- Exemplo de SQL para criar a tabela e inserir dados de teste
CREATE DATABASE IF NOT EXISTS cadastro_clientes;
USE cadastro_clientes;

CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    pago TINYINT(1) DEFAULT 0 -- 0 para não pago, 1 para pago
);

INSERT INTO clientes (nome, email, pago) VALUES
('Leonan', 'leonan@example.com', 0),
('Thamires', 'thamires@example.com', 0),
('Fernando', 'fernando@example.com', 1);
Crie o Arquivo .env:

Na raiz do projeto (NomeDoSeuRepositorio/), crie um arquivo chamado .env.

Preencha-o com suas credenciais, substituindo os valores de exemplo pelos seus:

Snippet de código

# Configurações do Banco de Dados MySQL
DB_HOST=localhost
DB_DATABASE=cadastro_clientes
DB_USER=root
DB_PASSWORD=SuaSenhaDoMySQL

# Configurações do Servidor SMTP (e-mail)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_LOGIN=seu.email.de.envio@gmail.com
# ATENÇÃO: Para Gmail, use uma Senha de Aplicativo, não sua senha normal!
EMAIL_PASSWORD=SuaSenhaDeAplicativoDoGmail
Execute o Script:

Bash

python main.py
O script se conectará ao seu MySQL, buscará os clientes com pago = 0 e tentará enviar os e-mails. Verifique o console para os logs de execução.

📂 Estrutura do Projeto
projeto_emails/
├── .env                  # Variáveis de ambiente (IGNORADO PELO GIT)
├── main.py               # Script principal do sistema
├── .gitignore            # Arquivos e pastas a serem ignorados pelo Git
├── README.md             # Este arquivo
├── .vscode/              # Configurações do VS Code (inclui launch.json)
│   └── launch.json
└── venv/                 # Ambiente virtual (IGNORADO PELO GIT)
📈 Próximos Passos / Melhorias Potenciais
Log de Erros: Implementar um sistema de log mais robusto para registrar envios falhos e erros de banco de dados.

Flexibilidade na Mensagem: Permitir que o corpo do e-mail seja configurável ou carregado de um template.

Agendamento: Integrar com ferramentas de agendamento (ex: Cron Jobs, APScheduler em Python) para execução automática.

Interface Web: Desenvolver uma interface gráfica simples (com Flask ou Django) para gerenciamento de clientes e visualização do status.

Relatórios: Gerar relatórios de inadimplência após o envio.

📧 Contato
Se tiver alguma dúvida ou sugestão sobre o projeto, sinta-se à vontade para entrar em contato:

Leandro Rodrigues Campos Oliveira
[leandrorodriguescamposti@gmail.com]
[https://www.linkedin.com/in/leandro-oliveira-256916172/]
