# Projeto REST-RESTFUL: API RESTful com Python e Flask

## Descrição
Este projeto demonstra a criação de uma API RESTful simples em Python com Flask. A API implementa operações CRUD (Create, Read, Update, Delete) para gerenciamento de tarefas (Todo List) e explora os conceitos fundamentais de REST.

### Link para o repositório
O projeto está disponível em: [REST-RESTFUL](https://github.com/cesarsantana2/REST-RESTFUL).

## Sumário
1. [Introdução](#introdução)
2. [Instalação e Configuração](#instalação-e-configuração)
3. [Estrutura de Diretórios](#estrutura-de-diretórios)
4. [Uso da API](#uso-da-api)
5. [Próximos Passos e Expansões](#próximos-passos-e-expansões)
6. [Referências e Fontes](#referências-e-fontes)

---

## Introdução
A API permite criar, listar, atualizar e deletar tarefas. Cada tarefa é tratada como um recurso independente, e o projeto utiliza um arquivo JSON para persistir os dados, facilitando a configuração inicial sem a necessidade de um banco de dados. Esse projeto serve como um ponto de partida para entender os princípios REST e pode ser expandido para incluir funcionalidades mais avançadas.

## Instalação e Configuração

### Pré-requisitos
- **Python 3.8+**: Certifique-se de ter o Python instalado.
- **Pip**: Gerenciador de pacotes do Python para instalar dependências.

### Setup do Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/cesarsantana2/REST-RESTFUL.git
   cd REST-RESTFUL
   
2. Crie um ambiente virtual e ative-o:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows, use venv\Scripts\activate

3. Instale as dependências:
   ```bash
   ppip install -r requirements.txt

4. Execute o servidor Flask:
   ```bash
   python3 src/app.py
   
5. A API estará disponível em http://127.0.0.1:5000

## Estrutura de Diretórios
```
REST-RESTFUL/
├── src/                    # Código-fonte da API
│   └── app.py              # Arquivo principal da API
├── docs/                   # Documentação adicional e recursos de referência
│   ├── API_Documentation.md # Documentação detalhada da API
│   └── Architecture_Diagram.png # Diagrama de arquitetura da API
├── tests/                  # Testes unitários e de integração
│   └── test_app.py         # Arquivo de testes para os endpoints
├── requirements.txt        # Dependências do projeto
└── .gitignore              # Arquivos e diretórios a serem ignorados pelo Git
```

## Uso da API

Você pode testar a API usando ferramentas como **Postman** ou **cURL**. Aqui estão alguns exemplos de requisições para interagir com a API:

### 1. **GET /todos** - Listar todas as tarefas

   ```bash
   curl -X GET http://127.0.0.1:5000/todos



### 2. **POST /todos** - Criar uma nova tarefa

   ```bash
   curl -X POST http://127.0.0.1:5000/todos -H "Content-Type: application/json" -d '{"task": "New Task", "completed": false}'

