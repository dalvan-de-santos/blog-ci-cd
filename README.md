"# blog-ci-cd" 
Sistema web voltado para a criação de blogs personalizados com suporte a posts e gerenciamento de usuários. O projeto é estruturado com práticas modernas de CI/CD (Integração e Entrega Contínua) para garantir agilidade, confiabilidade e escalabilidade no desenvolvimento e implantação.

Funcionalidades
- Cadastro de usuários com autenticação segura
- Cada usuário possui um blog exclusivo
- Blogs podem conter múltiplos posts com imagens, descrições e temas personalizados
- Interface intuitiva para criação e edição de conteúdo
- Estrutura modular e escalável para expansão futura

Estrutura do Projeto
- Frontend: (templates django)
- Backend: (Django)
- Banco de Dados: (PostgreSQL, sqlite3)
- CI/CD: Pipeline automatizado com integração contínua e deploy via (GitHub Actions, GitLab CI, etc.)

Modelo de Dados (ER)
- User: id_user, username, email, password
- Blog: id_blog, name, description, tags, id_user
- Post: id_post, image, description, themes, id_blog
Relacionamentos:
- Um usuário possui um blog (1:1)
- Um blog possui vários posts (1:N)


Tecnologias Utilizadas
- Docker
- Git & GitHub
- CI/CD com GitHub Actions
- django
