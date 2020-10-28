#!/bin/bash

instalador() {
chmod +x Hemera.py
setterm -foreground green
printf "["
setterm -foreground white
printf "+"
setterm -foreground green
printf "]"
setterm -foreground cyan
printf " Instalando Recursos...\n\n"
sleep 2
setterm -foreground white
apt-get update
apt install python
apt install python3-pip
apt install curl
apt install php
git clone https://github.com/PSecurity/ps.ngrok
cd ps.ngrok
mv ngrok ..
cd ..
rm -rf ps.ngrok
chmod +x ngrok
pip3 install requests
verificar
setterm -foreground green
printf "["
setterm -foreground white
printf "+"
setterm -foreground green
printf "]"
setterm -foreground cyan
printf " Instalação Concluída com Sucesso.\n"
}

verificar() {
if [[ -e python3 ]]; then
echo ""
 else
command -v python3 > /dev/null 2>&1 || { printf >&2 "Não foi possivel instalar o python."; exit 1; }
fi

if [[ -e pip3 ]]; then
echo ""
 else
command -v pip3 > /dev/null 2>&1 || { printf >&2 "Não foi possivel instalar o Pip."; exit 1; }
fi

if [[ -e curl ]]; then
echo ""
 else
command -v curl > /dev/null 2>&1 || { printf >&2 "Não foi possivel instalar o Curl."; exit 1; }
fi

if [[ -e php ]]; then
echo ""
 else
command -v php > /dev/null 2>&1 || { printf >&2 "Não foi possivel instalar o Php."; exit 1; }
fi
}

instalador
