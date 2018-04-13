#Carrega libs
import pandas as pd
import glob
import os
import csv
import numpy as np

#Importa zonas
zonasgeral = pd.read_csv('zonas.csv',sep=',')
zonas = zonasgeral.iloc[:,[0,1,2,3,4,5,6]]

#Importa votos
path='votos_tse/'
arquivos=glob.glob(os.path.join(path, "*RJ.txt"))
dados=(pd.read_csv(f,sep=';',encoding ='ISO8859',header=None) for f in arquivos)
votosgeral=pd.concat(dados,ignore_index=True)

# COLUNAS VOTACAO NOMINAL A PARTIR DE 2014
#0 DATA_GERACAO
#1 HORA_GERACAO
#2 ANO_ELEICAO
#3 NUM_TURNO (*)
#4 DESCRICAO_ELEICAO (*)
#5 SIGLA_UF
#6 SIGLA_UE (*)
#7 CODIGO_MUNICIPIO (*)
#8 NOME_MUNICIPIO
#9 NUMERO_ZONA (*)
#10 CODIGO_CARGO (*)
#11 NUMERO_CAND (*)
#12 SQ_CANDIDATO (*)
#13 NOME_CANDIDATO
#14 NOME_URNA_CANDIDATO
#15 DESCRICAO_CARGO
# COD_SIT_CAND_SUPERIOR
# DESC_SIT_CAND_SUPERIOR
# CODIGO_SIT_CANDIDATO
# DESC_SIT_CANDIDATO
#20 CODIGO_SIT_CAND_TOT
#21 DESC_SIT_CAND_TOT
#22 NUMERO_PARTIDO
#23 SIGLA_PARTIDO
#24 NOME_PARTIDO
# SEQUENCIAL_LEGENDA
# NOME_COLIGACAO
# COMPOSICAO_LEGENDA
#28 TOTAL_VOTOS
# TRANSITO


#Seleciona e nomeia colunas que interessam, merge com zonas
votos = votosgeral.iloc[:,[2,3,8,9,12,13,14,15,24,27,28]]
votos.columns = ['Ano','Turno','Cidade','ZE','Seq_Candidato','Nome_Candidato','Nome_Urna','Cargo','Partido','Legenda','Total']
votozona = pd.merge(votos, zonas, on='ZE')


# Estudo pra fazer indice do peso de cada zona
indices = pd.crosstab(votozona.ZE,votozona.Ano,values=votozona.Total,aggfunc=np.sum,normalize='columns')    .round(4)*100
print(indices)


#Estudo para fazer indice de candidato especifico
flavio2016 = votos[(votos.Seq_Candidato == 190000011736)]
flav16 = pd.crosstab(flavio2016.ZE,flavio2016.Ano,values=flavio2016.Total,aggfunc=np.sum,normalize='columns')    .round(4)*100
print(flav16)


#Lista toda familia Bolsonaro
bolsonaro = votos[votos['Nome_Candidato'].str.contains("BOLSONARO")]


#Merge
df = pd.merge(bolsonaro, zonas, on='ZE')
pd.DataFrame(df)


#Exporta
df.to_csv('bolsovoto.csv')

