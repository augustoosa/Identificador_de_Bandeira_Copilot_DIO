# Identificador de Bandeira de Cartão de Crédito

## Descrição

Este projeto tem como objetivo desenvolver uma aplicação simples capaz de identificar a bandeira de um cartão de crédito (como Visa, MasterCard, etc.) com base no número do cartão. Utilizando o GitHub Copilot como assistente de codificação, exploramos como a inteligência artificial pode acelerar o desenvolvimento, sugerir trechos de código e melhorar a produtividade.

O sistema solicita ao usuário que digite o número do cartão de crédito e, a partir dos prefixos (IIN) e do comprimento do número, identifica a bandeira do cartão. As regras de identificação seguem os padrões internacionais, considerando prefixos e tamanhos específicos para cada bandeira, como Visa, MasterCard, American Express, Diners Club, Discover, JCB, Hipercard, entre outros.

## Como funciona

- O usuário executa o script Python.
- O sistema solicita o número do cartão de crédito.
- O número é analisado conforme os prefixos e o comprimento.
- O sistema retorna a bandeira correspondente ou informa se não foi possível identificar.

## Tecnologias utilizadas

- Python 3.x

## Como executar

1. Clone este repositório ou baixe os arquivos.
2. Execute o script `identificador_bandeira.py`:
   ```
   python identificador_bandeira.py
   ```
3. Digite o número do cartão de crédito quando solicitado.

## Exemplo de uso

```
Digite o número do cartão de crédito: 4111111111111111
Bandeira: Visa
```

## Créditos

Desenvolvido com o auxílio do GitHub Copilot, utilizando regras de identificação de bandeiras de cartões de crédito baseadas em prefixos (IIN) e comprimento dos números.

---