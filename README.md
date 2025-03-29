# Teste Técnico - IntuitiveCare

Bem-vindo ao repositório do teste técnico para a posição de Estágio em Desenvolvimento de Software na IntuitiveCare. Este documento fornece todas as informações necessárias sobre a solução implementada.

## 🚀 Tecnologias Utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias:

- **Python** (Backend)
- **Vue.js** (Frontend)
- **TypeScript** (Frontend)

## 📦 Bibliotecas e Frameworks Utilizados

- **Pandas** - Manipulação e análise de dados
- **Flask** - Criação de API para comunicação backend
- **BeautifulSoup** - Web scraping para extração de informações

## 🛠️ Como Rodar a parte 1, 2 e 3

### 1️⃣ Clonar o Repositório
```sh
git clone https://github.com/seu-usuario/teste-tecnico.git
cd teste-tecnico
```

### 2️⃣ Rodar o projeto
Para rodar o projeto, basta apenas dar um play no main. Isso serve para a parte 1, 2 e 3.

## 🛠️ Como Rodar a parte 4
Na parte 4, eu dividir os arquivos em dois. Pois foi utilizado Vue.js e Python (Flask). Então, é necessário seguir os passos a seguir:
### 1️⃣ Clonar o Repositório
```sh
git clone https://github.com/seu-usuario/teste-tecnico.git
cd teste-tecnico
```
### 2️⃣ Configurar o Backend
```sh
cd server
```
Após isso, execute o seguinte comando no terminal
```sh
uvicorn main:app --reload
```
A aplicação estará disponível em [http://127.0.0.1:5000](http://127.0.0.1:5000) (ou a porta configurada).

### 3️⃣ Configurar o Frontend
```sh
cd interface_web
npm install
npm run dev
```

A aplicação estará disponível em [http://localhost:5000]((http://localhost:5000)) (ou a porta configurada).

Para acessar a rota que retorna os dados do CSV, basta adicionar **/data**, ou seja, irá ficar assim: **http://localhost:5000/data**


## 🤔 Decisões Técnicas

- Utilização de **Flask** para o backend pela leveza e facilidade de criação de APIs.
- **Pandas** para manipulação de dados devido à sua eficiência em análise de tabelas.
- **Vue.js + TypeScript** no frontend para melhor organização do código e tipagem segura.
- **BeautifulSoup** para extração de dados estruturados de páginas web.
- **PostgreeSQL** para integração e manipulação com o banco de dados.

## 📞 Contato

Caso tenha dúvidas ou feedbacks, entre em contato:

- **GitHub**: [ryannardelli](https://github.com/ryannardelli)
- **LinkedIn**: [Seu Nome](https://www.linkedin.com/in/ryannardelli/)
- **E-mail**: ryannardelli12@gmail.com

🚀 Desenvolvido por **Ryan Nardelli** para o teste da IntuitiveCare.
