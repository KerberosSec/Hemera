#!/bin/bash
#coding: utf-8

instalacao() {
chmod +x Hemera.py
setterm -foreground green
printf "["
setterm -foreground white
printf "+"
setterm -foreground green
printf "] "
setterm -foreground cyan
printf "Instalando Recursos e Requisitos...\n"
setterm -foreground white
apt-get update
apt install python
apt install pip
apt install bash
apt install curl
apt install php
apt install jq
git clone https://github.com/PSecurity/ps.ngrok
cd ps.ngrok
mv ngrok ..
cd ..
rm -rf ps.ngrok
chmod +x ngrok
pip install requests
pip install tabulate
verificar
setterm -foreground green
printf "\n[+] Instalação Concluída com Sucesso\n"
}

verificar() {
if [[ -e python ]]; then
echo ""
 else
setterm -foreground red
command -v python > /dev/null 2>&1 || { printf >&2 "Erro ao Instalar Python.Tente novamente."; exit 1; }
fi

if [[ -e curl ]]; then
echo ""
 else
setterm -foreground red
command -v curl > /dev/null 2>&1 || { printf >&2 "Erro ao Instalar o Curl.Tente novamente."; exit 1; }
fi

if [[ -e pip ]]; then
echo ""
 else
setterm -foreground red
command -v pip > /dev/null 2>&1 || { printf >&2 "Erro ao Instalar o Pip.Tente novamente."; exit 1; }
fi

if [[ -e php ]]; then
echo ""
 else
setterm -foreground red
command -v php > /dev/null 2>&1 || { printf >&2 "Erro ao Instalar o Php.Tente novamente."; exit 1; }
fi
}

instalacao
