# Documentação do Projeto

## Visão Geral
Este projeto consiste em uma API desenvolvida para automatizar uma das etapas de recrutamento de profissionais de T.I. A aplicação consulta perfis públicos do GitHub com base em filtros como localização, e armazena as informações relevantes em um banco de dados PostgreSQL. O objetivo é oferecer uma interface para coleta, armazenamento e futura análise de dados de candidatos, com endpoints REST disponíveis para interação com o sistema.

## Configuração e Execução

### Configuração do Ambiente
### 1. **Clone o repositório:**
   ```sh
   git clone https://github.com/Toiste/hr-process-automation.git
   cd hr-process-automation/backend
   ```
### 2. **Crie e ative um ambiente virtual:**
  no Windows:
  ```sh
  python -m venv venv
  venv\Scripts\activate   
  ```
ou
  no Linux/macOS:
  ```sh
  python -m venv venv
  source venv/bin/activate   
  ```
### 2. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```
### 3 **Passo a passo para criar e configurar o Banco de Dados. | Etapa Opcional**
#### 3.1 **Crie uma imagem pro banco de dados com Docker:**
   ```sh
   docker pull postgres:latest
   ```
#### 3.2 **Crie e rode o Container pro banco de dados com Docker:**
   ```sh
   docker run --name meu-postgres -e POSTGRES_USER=meu_usuario -e POSTGRES_PASSWORD=minha_senha -e POSTGRES_DB=meu_banco -p 5432:5432 -d postgres
   ```

### 4 **Configure as variáveis de ambiente:**
   edite o arquivo `.env example` renomeie para `.env` e defina os valores referentes ao seu banco, exemplo:
   ```sh
   DB_USER=postgres
   DB_HOST=localhost
   DB_NAME=postgres
   DB_PASSWORD=senha
   DB_PORT=5432
   ```

### 5 **Execute a API:**
   ```sh
   python manage.py runserver
   ```


