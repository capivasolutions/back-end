# Back-end

🦀 Repositório onde todos os elementos relacionados à aplicação back-end do projeto estão armazenados

## Requisitos

- Python3
- Pip3
- Python Virtualenv

### Como executar

```bash
# Crie um ambiente virtual com virtualenv
python -m venv venv
source venv/bin/Activate

# Instale as dependências necessárias
pip3 install -r requirements.txt

# Execute o back-end em ambiente de desenvolvimento
uvicorn src.main:app --reload

# O back-end estará disponível em http://127.0.0.1:8000/docs
```
