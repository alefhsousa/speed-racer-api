# Speed Racer Api

![](https://media.giphy.com/media/3xz2BqgtWhZvuwdhUk/giphy.gif)

A ideia do projeto é ler um arquivo de log e fazer algumas manipulações com os dados extraídos, nesse projeto é chamado de `report`.

O projeto foi desenvolvido utilizando os conceitos de [DDD](https://www.amazon.com.br/Domain-driven-Design-Eric-Evans/dp/8576085046), dessa forma:

- application
    - é a camada de aplicação da api ou também pode ser chamada como camada http é onde ficam as rotas, resources e mappers necessários
- domain
    - é o core da aplicação e onde temos todas as classes de domínios para o completo funcionamento da api
- infrastructure
    - são todos os recursos que são cross com a aplicação e que pode ser substituído a qualquer momento

Para os testes, foi seguida a métodologia do [test pyramid](https://martinfowler.com/bliki/TestPyramid.html)

## Makefile

Para facilitar o manuseio da aplicação as rotinas para subir e configurar a app foram encapsulados dentro do `Makefile` como forma de abstrair complexidades.
Dessa forma precisamos conhecer apenas dois comando, sendo eles:

### Tasks

- `make build/local`: Irá fazer todo o processo de instalaçãod e libs de terceiros, verificar integridade, rodar linter, rodar os testes e por último irá rodar a aplicação em standalone
- `make build`: Irá fazer todos os passos citados no `build/local` porém ao invés da aplicação rodar standalone, ela fica isolado em um processo docker.
- `make test/run`: Roda apenas os testes
- `make run`: Sobe aplicação em standalone
- `make docker/build/image`: Criar uma imagem com o estado atual da aplicação
- `make docker/run`: Sobe um container com base na imagem criadas.


### Infranecessária para rodar a app

- Ter o docker ou python instalado na máquina

Rodar o comando no seu terminal: 

``` make build```

### endpoints

O endpoint principal é o `/reports` que apresenta o relatório `default` com a informação dos ganhadores da corrida.

`/reports/best_lap` -> melhor volta da corrida
`/reports/best_lap_pilot` -> melhor volta dos pilotos
`/reports/average_time_report` -> velocidade média dos pilotos
`/reports/time_after_winner` -> tempo de chegada dos pilotos depois do vencedor


### Melhorias futuras

- Inclusão de ci/cd usando travis, circle/ci ou até mesmo o jenkins
- Hospedagem da app no heroku
- Melhoria na camada de http para criar melhores abstrações
- Possibilidade de apresentar mais de um relatório ao mesmo tempo
- Criação de testes e2e
- Aumento de perfomance na leitura do arquivo utilizando `asyncio` ou até mesmo `yieldfrom`
- Criação de testes de perfomance
- Inclusão de uma ferramenta para documentação da `api` dinâmicamente algo como `swagger`, `raml`, `apiguee` etc.
