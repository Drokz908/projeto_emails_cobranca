import smtplib
import mysql.connector
from mysql.connector import Error 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv 
import os 

# Carregar Variáveis de Ambiente ---
from pathlib import Path
dotenv_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=dotenv_path)

# Arquivo .env com informações ficticias por questões de segurança ---
# Configurações do Banco de Dados MySQL (lidas do .env) ---
db_config = {
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_DATABASE'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

# Configurações do Servidor SMTP (lidas do .env) ---
smtp_server = os.getenv('SMTP_SERVER')
smtp_port = int(os.getenv('SMTP_PORT', 587))
email_login = os.getenv('EMAIL_LOGIN')
email_senha = os.getenv('EMAIL_PASSWORD')

# Obter clientes inadimplentes do banco de dados ---
clientes_inadimplentes = []
conn = None 

try:
    print("Tentando conectar ao banco de dados MySQL...")
    conn = mysql.connector.connect(**db_config)
    if conn.is_connected():
        print("Conexão com MySQL estabelecida com sucesso!")
        cursor = conn.cursor()

        # Consulta SQL para buscar clientes inadimplentes
        cursor.execute("SELECT nome, email FROM clientes WHERE pago = 'não'")

        resultados = cursor.fetchall()

        for row in resultados:
            clientes_inadimplentes.append({'nome': row[0], 'email': row[1]})
        
        print(f"Encontrados {len(clientes_inadimplentes)} clientes inadimplentes no DB.")
    else:
        print("Erro: Não foi possível estabelecer conexão com o banco de dados MySQL.")

except Error as e:
    print(f"Erro no banco de dados: {e}")
    exit("Processo abortado devido a erro no banco de dados.") # Interrompe a execução em caso de erro no DB
finally:
    if conn and conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexão MySQL fechada.")

# Enviar e-mails para os clientes inadimplentes ---
if not clientes_inadimplentes:
    print("Nenhum cliente inadimplente encontrado. Nenhum e-mail de cobrança será enviado.")
else:
    print("\n--- Iniciando envio de e-mails ---")
    smtp_server_connection = None # Inicializa a conexão SMTP como None
    try:
        smtp_server_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_server_connection.starttls() # Inicia a criptografia TLS
        smtp_server_connection.login(email_login, email_senha)
        print("Conexão SMTP estabelecida e login realizado.")

        for cliente in clientes_inadimplentes:
            mensagem = MIMEMultipart()
            mensagem['From'] = email_login
            mensagem['To'] = cliente['email']
            mensagem['Subject'] = 'Aviso de Cobrança - Regularize seu Pagamento'

            corpo = f"""
            Olá, {cliente['nome']}!

            Constatamos a pendência em seu pagamento.

            Por favor, regularize sua situação o quanto antes para evitar o bloqueio do serviço.

            Atenciosamente, 
            Equipe de Atendimento
            """

            mensagem.attach(MIMEText(corpo, 'plain'))

            smtp_server_connection.sendmail(email_login, cliente['email'], mensagem.as_string())
            print(f"✅ Aviso enviado para {cliente['nome']} ({cliente['email']})")

    except smtplib.SMTPAuthenticationError:
        print("❌ ERRO SMTP: Falha na autenticação. Verifique seu EMAIL_LOGIN e EMAIL_PASSWORD no .env.")
        print("Para Gmail, lembre-se de usar uma 'Senha de Aplicativo'.")
    except smtplib.SMTPConnectError:
        print("❌ ERRO SMTP: Não foi possível conectar ao servidor SMTP. Verifique SMTP_SERVER e SMTP_PORT no .env.")
    except Exception as e:
        print(f"❌ ERRO Inesperado ao enviar e-mails: {e}")
    finally:
        if smtp_server_connection:
            smtp_server_connection.quit()
        print("--- Processo de envio de e-mails concluído. ---")