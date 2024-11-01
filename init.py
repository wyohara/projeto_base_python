import os
import venv
import subprocess
import configparser

def cria_virtualenv(nome_env="venv"):
    # Verifica se o ambiente virtual já existe
    if os.path.exists(nome_env):
        print(f"O ambiente virtual '{nome_env}' já existe.")
    else:
        # Cria o ambiente virtual
        try:
            venv.create(nome_env, with_pip=True)
            print(f"Ambiente virtual '{nome_env}' criado com sucesso!")

        except Exception as e:
            print(f"Ocorreu um erro ao criar o ambiente virtual: {e}")
    # Instala as dependências do requirements.txt
    instalar_dependencias(nome_env)
    instrucoes_venv()
    

def instrucoes_venv(nome_env="venv"):
    if os.name == "nt":  # Windows
        comando = f"{os.getcwd()}\\{nome_env}\\Scripts\\activate"
        print(f"Para ativar o ambiente virtual, execute: {comando}")
        init_venv =f"{os.getcwd()}\\{nome_env}\\Scripts\\activate"
    else:  # macOS/Linux
        comando =f"source {nome_env}/bin/activate"
        print(f"Para ativar o ambiente virtual, execute:{comando}")
    print(f"Para acessar o Diretório do arquivo: cd {os.getcwd()}")
    print("Para iniciar o shell: python -m idlelib.idle")

    
def instalar_dependencias(nome_env="venv"):
    # Verifica se o arquivo requirements.txt existe
    arquivo_requirements="req.txt"
    requirements_path = os.path.join(os.getcwd(), arquivo_requirements)
    if os.path.isfile(requirements_path):
        # Comando para instalar dependências        
        if os.name=="nt": # cria o path dependendo do sistema ser windows ("nt") ou linux
            pip_executable=os.path.join(nome_env, "Scripts", "pip")
        else:
            pip_executable=os.path.join(nome_env, "bin", "pip")
        try: 
            subprocess.check_call([pip_executable, "install", "-r", requirements_path])
            print("Dependências instaladas com sucesso!")
        except subprocess.CalledProcessError as e:
            print(f"Ocorreu um erro ao instalar as dependências: {e}")
    else:
        print(f"O arquivo {arquivo_requirements} não foi encontrado.")

def load_arquivo_ini():
    # Cria um objeto ConfigParser
    config = configparser.ConfigParser()

    # Lê o arquivo de configuração
    config.read('config.ini')

    # convertendo o resultado para um dicionário
    ini_data = {}
    for secao in config.sections(): # recuperando as seções do dicionário
        valores={}
        for chave in config[secao]: # recuperando a chave e valor de cada seção
            valores[chave]= config[secao][chave]
        ini_data[secao] = valores
    return ini_data

        



if __name__ == "__main__":
    cria_virtualenv()
