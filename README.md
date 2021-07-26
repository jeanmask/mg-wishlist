Wishlist API
============

Dependencias
------------
- python 3.9
- poetry

Instalação
----------
> poetry install

> poetry run ./src/manage.py migrate

Execução
--------
> poetry run ./src/manage.py runserver 127.0.0.1:8000

Testes
------
> make test

Acesso
------
http://127.0.0.1:8000/customers/docs (chave de autenticação: supersecret)

TODO
----
* Transformar chamada da api externa em assincrona
* Criar comando com base no campo `_last_update` do produto para atualizar a base já existente periodicamente
* Criar testes dos endpoints de wishlist
* Mover configurações basicas para variaveis de ambiente
* Criar Dockerfile
* Paginação dos endpoints de listagem
* Desativar django-admin e demais modulos não necessários
