# Jogo-da-Vida-de-Conway
Jogo da Vida de Conway - resolvendo uma questão da [Olimpíada Brasileira de Informática](https://olimpiada.ic.unicamp.br/static/extras/obi2024/provas/ProvaOBI2024_f1p2.pdf).

O problema do [Jogo da Vida de Conway](https://pt.wikipedia.org/wiki/Jogo_da_vida) consiste na simulação de células vivas e mortas com as seguintes regras:

1) Toda célula morta com exatamente três vizinhos vivos torna-se viva (nascimento).
2) Toda célula viva com menos de dois vizinhos vivos morre por isolamento.
3) Toda célula viva com mais de três vizinhos vivos morre por superpopulação.
4) Toda célula viva com dois ou três vizinhos vivos permanece viva.

O código feit0 neste repositório é construído com funções para poder modularizar e testar mais facilmente. 
