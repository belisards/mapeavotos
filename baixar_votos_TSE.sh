#!/bin/sh
mkdir votos_tse 
cd votos_tse 
for ano in 2014 2016; do
prefixo="http://agencia.tse.jus.br/estatistica/sead/odsele/votacao_candidato_munzona/votacao_candidato_munzona_"
url="$prefixo$ano.zip"
wget -O "$ano.zip" -nc "$url"
unzip $ano.zip
done