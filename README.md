# Back-end

🦀 Repositório onde todos os elementos relacionados à aplicação back-end do projeto estão armazenados

## Requisitos

- Python3
- Pip3
- Python Virtualenv

### Como executar

```bash
# Inicie o banco de dados usando Docker
docker-compose up -d

# Execute as migrations. Copie o arquivo src/migrations/* e execute no banco de dados

# Crie um arquivo .env na raiz do repositório e altere as variáveis (se necessário)
cp .env.example .env

# Crie um ambiente virtual com virtualenv
python3 -m venv venv
source venv/bin/activate

# Instale as dependências necessárias
pip3 install -r requirements.txt

# Execute o back-end em ambiente de desenvolvimento
python3 src/main.py

# O back-end estará disponível em http://127.0.0.1:8000/docs
```
