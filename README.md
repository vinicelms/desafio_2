# The Guardian API

Este projeto foi feito sob o visão de aprendizado. Não há fins comerciais em seu uso. Caso deseje, utilize-o e altere da forma que desejar.

## Versão Python
O projeto foi desenvolvido e testado com ```Python 3.5```

## Bibliotecas utilziadas no projeto (fora da Python Standard Library)

A biblioteca pode ser encontrada na **Python Package Index**: https://pypi.python.org/pypi

* Requests 2.9.1

## API The Guardian

A API visa facilitar o acesso a informações publicada pelo jornal The Guardian.

A documentação da API pode ser encontrada em: http://open-platform.theguardian.com/

### Chave de acesso para API

A chave garante acesso a API e tem dois perfis de acesso:
* Developer
* Commercial

O perfil **Developer** tem um quantidade de *hits* na API por segundo e diária, garantindo que não seja utilizada para fins comerciais.

O perfil **Commercial** é voltado para empresas, não havendo limites de *hits* na API.

Se for utilizar o projeto para fins de estudo, registre uma chave do tipo **Developer**, já te garantindo uma quantidade suficiente para avaliar o seu uso.

Registro de chave: http://open-platform.theguardian.com/access/

## Como utilizar

* Faça o clone do repositório em seu ambiente
```
git clone https://github.com/vinicelms/desafio_2
```

* Entre no diretório do projeto
```
cd desafio_2
```

* Instale as bibliotecas necessárias
```
pip install requests
```

* Execute o script **content_exporter.py** com seus parâmetros
```
python content_exporter.py --key [SUA_CHAVE_DA_API] --section education --start 2018-02-24 --end 2018-02-25 --resultados 200
```

## Recursos adicionais de uso do projeto

O projeto tem como base as chamadas do módulo **content_exporter.py**, podendo ser utilizada a chave de ajuda.
```
python content_exporter.py --help
```

* Saída esperada:
```
usage: content_exporter.py [-h] --key KEY --section SECTION [--start START]
                           [--end END] [--resultados RESULTADOS]

optional arguments:
  -h, --help            show this help message and exit
  --key KEY             Chave de acesso da API do The Guardian
  --section SECTION     Informa a seção que será buscada
  --start START         Define a data de início de pesquisa. Formato: YYYY-MM-DD
  --end END             Define a data de término de pesquisa. Formato: YYYY-MM-DD
  --resultados RESULTADOS
                        Define a quantidade de retornos que será solicitado
                        para API. Máximo: 200
```

* Parâmetros obrigatórios:
```
--key - Chave de acesso da API
--section -- Seção que será buscada na API
```