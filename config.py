import os


# Carregar as variáveis de ambiente manualmente
def load_env():
    with open(".env", "r") as en:
        for line in en:
            if "=" in line:
                key, value = line.strip().split("=", 1)
                os.environ[key] = value


load_env()

# Variáveis de configuração
API_TOKEN = os.getenv("API_TOKEN")
