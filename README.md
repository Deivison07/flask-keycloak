# Flask-Keycloak

Este projeto integra Flask com Keycloak para autenticação e autorização.

## Instalação

### Pré-requisitos
- Certifique-se de ter o Docker instalado em seu sistema.

### Passos para Instalar

1. **Clonar o repositório:**
    ```bash
    git clone https://github.com/Deivison07/flask-keycloak.git
    ```
2. **Navegar para o diretório do projeto:**
    ```bash
    cd flask-keycloak
    ```

## Como Executar

1. **Construir e executar a aplicação usando Docker Compose:**
    ```bash
    docker-compose up --build
    ```

## Endpoints

### Obter Token

**[POST]** `http://localhost:8080/realms/dev/protocol/openid-connect/token`

#### Parâmetros:
- `grant_type` = password
- `client_id`
- `client_secret`
- `username`
- `password`

### Dados

- **[GET]** `http://localhost:5000/indices`
- **[GET]** `http://localhost:5000/indices-mun`
- **[GET]** `http://localhost:5000/estagos`
- **[GET]** `http://localhost:5000/regioes`
- **[GET]** `http://localhost:5000/municipios`

## Contribuindo

Se você deseja contribuir com este projeto, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma nova branch (`git checkout -b feature-branch`).
3. Commit suas alterações (`git commit -am 'Adicione uma nova funcionalidade'`).
4. Faça o push para a branch (`git push origin feature-branch`).
5. Crie um novo Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para abrir uma issue ou entrar em contato com o proprietário do repositório.
