# 📘 Microsserviço de Atividades
Este repositório contém o microsserviço responsável pela gestão de atividades associadas a professores no contexto de uma aplicação educacional. A API foi construída utilizando Flask e segue os princípios de arquitetura em microsserviços e padrão MVC.

# 🧾 Descrição da API
A API permite o gerenciamento de atividades vinculadas a professores, oferecendo endpoints REST para:

Criar uma atividade

Listar todas as atividades

Listar atividades por professor

Buscar atividade por ID

Deletar atividade

Atualizar atividade

# 🔗 Principais Endpoints
Método	Rota	Descrição
GET	/atividades	Lista todas as atividades
GET	/atividades/professor/<id>	Lista atividades de um professor
GET	/atividades/<id>	Retorna uma atividade por ID
POST	/atividades	Cria uma nova atividade
PUT	/atividades/<id>	Atualiza uma atividade
DELETE	/atividades/<id>	Deleta uma atividade

# 🐳 Instruções de Execução (com Docker)
🔧 Pré-requisitos
Docker instalado na máquina

# ▶️ Executar o microsserviço
bash
Copiar
Editar
# Clonar o repositório
git clone https://github.com/viniciuscassapian/Atividades.git
cd Atividades

# Construir a imagem Docker
docker build -t atividades-service .

# Rodar o contêiner
docker run -d -p 5000:5000 --name atividades_container atividades-service
A API estará disponível em: http://localhost:5002 (necessário adicionar "/atividades" na URL, logo após 5002) 

# 🏛️ Arquitetura Utilizada
O projeto segue o padrão MVC (Model-View-Controller) adaptado para uma API REST:

Model (Modelos): Representação dos dados, manipulados em memória (atividade_model.py)

Controller: Lida com a lógica e rotas da API (atividade_controller.py)

App: Ponto de entrada da aplicação Flask (app.py)

Configuração: Separada em config.py

Cliente HTTP: Comunicação com outros microsserviços (pessoa_service_client.py)

O banco de dados utilizado é o SQLite, simplificando o armazenamento para fins didáticos.

# 🧩 Ecossistema de Microsserviços
Este microsserviço de atividades faz parte de um sistema maior de gerenciamento escolar(Projeto-Flask), composto por múltiplos serviços independentes que se comunicam via HTTP REST.

# 🔄 Integração entre Serviços
Este serviço consome o Microsserviço de Professores para validar e vincular atividades a professores.

A comunicação ocorre através de requisições HTTP realizadas por meio de um cliente interno (pessoa_service_client.py), que consulta dados do serviço de professores.

O ecossistema pode ser orquestrado com Docker Compose ou similar, integrando:

servico-projeto-flask

servico-reservas-de-Salas

servico-atividades (este repositório)

# 👤 Autores
Vinícius Cassapian, Beatriz Alves, Janaina Figueiredo
