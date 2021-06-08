# Teste - PokeAPI

## Descrição

Teste realizado na linguagem python, utilizando framework Django, como forma de treinar as habilidades de consumir APIs de terceiros. 

Origem do teste: https://github.com/DanielHe4rt/pokefodase-test

#### O Desafio

- O desafio baseia-se em consumir 2 APIs de diferentes fontes de dados com intuito de agregar as informações e solucionar o problema de acordo com o que foi proposto;

O objetivo é criar uma aplicação web seguindo os seguintes critérios:

- Em uma página HTML deve ser possível informar uma cidade de qualquer lugar do mundo;
- De acordo com as condições climáticas desta cidade deve-se exibir um Pokémon baseado em seu tipo (fogo, água, elétrico, etc) seguindo as seguintes regras:
  - Lugares onde a temperatura for menor **(<) que 5ºC**, deve-se retornar um pokémon de **gelo (ice)**.
  - Lugares onde a temperatura estiver entre **(>=) 5ºC e (<) 10ºC**, deve-se retornar um pokémon do tipo **água (water)**.
  - Lugares onde a temperatura estiver entre **12ºC e 15ºC**, deve-se retornar um pokémon do tipo **grama (grass)**.
  - Lugares onde a temperatura estiver entre **15ºC e 21ºC**, deve-se retornar um pokémon do tipo **terra (ground)**.
  - Lugares onde a temperatura estiver entre **23ºC e 27ºC**, deve-se retornar um pokémon do tipo **inseto (bug)**.
  - Lugares onde a temperatura estiver entre **27ºC e 33ºC inclusive**, deve-se retornar um pokémon do tipo **pedra (rock)**.
  - Lugares onde a temperatura for **maior que 33ºC**, deve-se retornar um pokémon do tipo **fogo (fire)**.
  - **Para qualquer outra temperatura**, deve-se retornar um pokémon do tipo **normal**.
  - E, no caso em que **esteja chovendo na região** um pokémon **elétrico (electric)** deve ser retornado, independente da temperatura.
- Após a consulta deve-se exibir na tela:
  - Temperatural atual da cidade em graus Celcius;
  - Se está chovendo ou não;
  - Nome do Pokémon seguindo as regras acima.

#### Orientações

- Para consultas de condições climáticas utilize a API [OpenWeatherMap](https://openweathermap.org/api);
- Para consultas de Pokémons utilize a API [PokéAPI](https://pokeapi.co/docs/v2.html).

##### Passo 1 - Configurando o OpenweatherMap

- Acesse o link da plataforma em https://openweathermap.org/;
- No topo da página procure e clique no botão de “Sign UP”;
- Entre com as suas credenciais e crie um novo acesso, para que possa gerar um `APPID`, na plataforma;
- Quando estiver logado, procure e clique no botão “API Keys”;
- Ao ser direcionado para a próxima página visualize um pequeno formulário chamado “Create Key”;
- No input “Name”, coloque o nome que achar mais conveniente, por exemplo: “Default”;
- Em seguida clique no botão “Generate”;
- Ao lado do formulário uma “Key” (chave), será gerada com o nome que você informou no passo anterior, essa chave é o que a plataforma chama de `APPID` e será utilizada ao realizarmos as requisições Rest para as API(s) da plataforma.

##### Passo 2 - API do OpenWeatherMap

- Estando logado na plataforma procure pelo botão “API” no menu principal da aplicação, ou simplesmente acesse https://openweathermap.org/api;
- Na página de API procure pelo título **“Current weather data”**, e clique no botão **“API Doc”**, logo abaixo do título;
- Após o redirecionamento, você terá diversas informações sobre o que a API pode fazer, resumidamente iremos utilizá-la para informar o nome da cidade que deseja ver as condições climáticas da região;
- Para isso deve ser utilizada a API chamada **“By city name”**.
  - Ex.: https://api.openweathermap.org/data/2.5/weather?q=NOME_DA_CIDADE&appid=APPID
  - ou https://api.openweathermap.org/data/2.5/weather?q=Campinas&appid=5445a9ae08df1a3117ae57894fa7cdadah
  - Substituindo o conteúdo **NOME_DA_CIDADE** e **APP_ID**, com o nome da cidade que deseja saber o clima e o token gerado no passo 1;
- O resultado dessa requisição será um objeto do tipo JSON, atualmente o mais utilizado para aplicações RESTful;
  - Apenas dois atributos são de importância para o desafio o primeiro é o atributo chamado **“weather”**, que irá dar informação caso esteja chovendo na região, e o atributo **“main”**, que contém a temperatura da cidade em questão.


##### Passo 3 - API do PokeAPI

A plataforma PokéAPI não exige token de autenticação o que torna sua utilização bem mais simples, então acesse o link https://pokeapi.co/

- Logo na página inicial é possível testar a API, basta seguir os exemplos clicando nos links abaixo do input de submit, por exemplo **“/type/3/”**;
- A API que nos interessa nesse caso é exatamente a de tipo, porém ao invés de passar um valor numérico iremos passar o nome do tipo como parâmetro, como pode ser visto na documentação: https://pokeapi.co/docs/v2.html/#types
- Para isso pode-se fazer a seguinte requisição como no exemplo:
  - https://pokeapi.co/api/v2/type/<NOME_DO_TIPO>
  - ou
  - https://pokeapi.co/api/v2/type/electric
  - No qual <NOME_DO_TIPO> deve ser substituído pelo tipo de elemento desejado (ice, water, grass, ground, etc)
  - O retorno dessa requisição também será um objeto do tipo JSON, sendo que um único atributo é de interesse para esse desafio, que se trata do array de elementos chamado “pokemon”;



## Configurações

* Clone ou faça download dos pacotes do repositório.
```
    git clone https://github.com/edson-dias/test-pokeapi.git
```

* Ative ou crie seu ambiente virtual e instale as dependências do programa.
```
    pip install -r requirements.txt
```

* Crie um arquivo 'keys.py' dentro da pasta poke_api. 

* Através do terminal, gere uma nova chave secreta para o django:
```
    python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

* Copie a chave gerada e cole dentro do arquivo 'keys.py' criado anteriormente atribuindo a chave a variável 'DJANGO_KEY':
```
    DJANGO_KEY = 'chave gerada'
```

* Copie a chave secreta gerada na API do OpenWeatherMap e cole dentro do arquivo 'keys.py' atribuindo o valor a variável 'WEATHER_KEY':
```
    WEATHER_KEY = 'chave OpenWeather'
```

* Entre na pasta raiz e rode o servidor do django:
```
    python manage.py runserver
```