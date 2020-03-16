# Laboratório 1

**Amostragem de quantização em uma imagem monocromática**

O código principal do trabalho está no arquivo *lab1.py*. O arquivo *interactive_lab1.py* oferece uma maneira de executar o lab1 sobre várias imagens de uma vez e testando diversas configurações.

## Instruções de uso - lab1.py

Executar
```
python3 lab1.py <nome_da_imagem> <porcentual_de_amostragem> <tecnica_de_amostragem> <niveis_de_cinza>
```

sendo:

    1. nome_da_imagem: nome do arquivo com extensão
    2. porcentual_de_amostragem: multiplicador que será aplicado ao tamanho da imagem original, entre 0 e 1
    3. tecnica_de_amostragem: 0, 1 ou 2, onde 
        1. 0 é a média dos valores
        2. 1 é a mediana dos valores
        3. 2 é a moda dos valores
    4. niveis_de_cinza: número de níveis de cinza que serão utilizados no arquivo final, entre 2 e 256

Exemplo:
```
python3 lab1.py exemplo.png 0.5 1 16
````

## Instruções de uso - interactive_lab1.py

Executar
```
python3 interactibe_lab1.py
````

e responder as perguntas seguindo o padrão do lab1.py, com um espaço entre as respostas

Exemplo:
```
python3 interactive_lab1.py
File names? exemplo1.png exemplo2.png
Sampling percentages? 0.2 0.5 0.99
Modes? 0 2
Greyscale levels? 2 4 16
````

e o programa gerara um total de 36 imagens diferentes
