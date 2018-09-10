# Programador Backend (Python)

Instruções do teste
------

Desenvolva uma aplicação em linguagem Python que seja acessível localmente e verifique se um determinado número de CPF está em uma        *Blacklist*.

A aplicação deve:
 
1. Ser acessível como um serviço através de uma URL do tipo `http://IP:PORT/<cpf>`, por exemplo:
`http://127.0.0.1:5000/00000000000`


2. Ser `FREE` se o CPF não estiver na *Blacklist* e `BLOCK` se o CPF estiver na black list.
 
3. Retornar `RUNNING` caso seja acessada sem um CPF.

Para este teste você pode usar qualquer framework de sua escolha.

Os CPFs a serem testados estão no arquivo `blacklist.txt`.


Como entregar este teste
-----

    Esse teste é público. Todos os interessados que fizerem pull request receberão um feedback da equipe
    Otimiza Benefícios
    
    1. Faça um fork deste repositório;
    2. Crie uma branch com o seu nome.
    3. Adicione seu currículo na raiz do repositório.
    4. Envie-nos o PULL-REQUEST para que seja avaliado.
