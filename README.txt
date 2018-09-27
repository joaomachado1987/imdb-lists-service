Para listar as dependencias:
    - pip frezee

Para subir no heroku:
    - criar o requeriments.txt e incluir as dependências a ser instaladas pelo pip install pelo heroku
    - criar o Procfile inforando o módulo e arquivo a ser executado
    - instalar o heroku cli
    - versionar o código:
        $ git init
        $ git add .
        $ git commit -m "criando a aplicação"
    - realizar o login no heroku pelo cmd:
        $ heroku login
    - versionar o projeto no heroku: heroku git:remote -a meu-app-nome
    - criar o projeto no heroku: heroku apps:create meu-app-nome (ou heroku create se o nome da aplicação não for importante, ele cria sozinho)
    - fazendo o deploy: $git push heroku master
    - talvez precise informar a escala: heroku ps:scale web=1

