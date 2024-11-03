import os
import venv
import subprocess
"""
Codo inicial da inicialização do pip

Willian Ohara em 3/11/2024
"""

class CriarAmbienteVirtual:
    def __init__(self, nome_env="venv", requirements_txt="req.txt"):
        """Inicializa a classe com o nome do ambiente virtual e o arquivo de requisitos."""
        self.__nome_env = nome_env
        self.__requirements_txt = requirements_txt

    def cria_virtualenv(self):
        """Cria um ambiente virtual e instala as dependências especificadas."""
        # Verifica se o ambiente virtual já existe
        if os.path.exists(self.__nome_env):
            print(f"O ambiente virtual '{self.__nome_env}' já existe.")
        else:
            # Cria o ambiente virtual
            try:
                venv.create(self.__nome_env, with_pip=True)
                print(f"Ambiente virtual '{self.__nome_env}' criado com sucesso!")

            except Exception as e:
                print(f"Ocorreu um erro ao criar o ambiente virtual: {e}")

        # Instala as dependências do requirements.txt
        self.__instalar_dependencias()
        self.__exibir_instrucoes_venv()
    
    def __exibir_instrucoes_venv(self):
        """Exibe instruções para ativar o ambiente virtual."""
        if os.name == "nt":  # Windows
            comando = f"{os.getcwd()}\\{self.__nome_env}\\Scripts\\activate"
        else:  # macOS/Linux
            comando = f"source {self.__nome_env}/bin/activate"
        
        print(f"Para ativar o ambiente virtual, execute: {comando}")
        print(f"Para acessar o diretório do arquivo: cd {os.getcwd()}")
        print("Para iniciar o shell: python -m idlelib.idle")

    def __instalar_dependencias(self):
        """Instala as dependências especificadas no arquivo requirements.txt."""
        # Verifica se o arquivo requirements.txt existe
        requirements_path = os.path.join(os.getcwd(), self.__requirements_txt)
        if os.path.isfile(requirements_path):
            # Define o caminho para o executável pip dependendo do sistema operacional
            if os.name == "nt":  # Windows
                pip_executable = os.path.join(self.__nome_env, "Scripts", "pip")
            else:  # macOS/Linux
                pip_executable = os.path.join(self.__nome_env, "bin", "pip")

            try: 
                # Comando para instalar dependências
                subprocess.check_call([pip_executable, "install", "-r", requirements_path])
                print("Dependências instaladas com sucesso!")
            except subprocess.CalledProcessError as e:
                print(f"Ocorreu um erro ao instalar as dependências: {e}")
        else:
            print(f"O arquivo {self.__requirements_txt} não foi encontrado.")

    def salvar_requirements_pip(self):
        """Executa o comando pip freeze e salva a saída no arquivo req.txt."""
        with open(self.__requirements_txt, 'w') as f:
            subprocess.run(['pip', 'freeze'], stdout=f)
        print(f"Dependências salvas em {self.__requirements_txt}.")


if __name__ == "__main__":
    env = CriarAmbienteVirtual()
    env.cria_virtualenv()
    env.salvar_requirements_pip()