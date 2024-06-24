
#definindo variaveis
#arquivo
import pandas as pd
import cx_Oracle
import xml.etree.ElementTree as et

#lendo xml de configuracao
CaminhoArquivoConfig= '/Users/felipefreiresantos/Documents/Work/Topazio/DataCob/CobrancasJudiciais/config.xml'
tree = et.parse(CaminhoArquivoConfig)
root = tree.getroot()
for elem in root.findall('Parametros'):
        diretorio = elem.find('diretorioarquivo').text
        nome_arquivo = elem.find('nomearquivo').text
        CaminhoArquivoCSV = diretorio + nome_arquivo
        df = pd.read_csv(CaminhoArquivoCSV, sep=',', encoding='utf8')
        print(df)
#importanto arquivo csv
diretorio = '/Users/felipefreiresantos/Documents/Work/Topazio/DataCob/CobrancasJudiciais/'
arquivo = 'ArquivoRemessa.csv'
df2 = pd.read_csv(diretorio + arquivo)
print(df2)
#
#insere dados no banco

#Atribuindo paramentros para conectar no BD
username = 'PSAGILIZEFELIPE'
password ='qazwsx@741852'
database_url = 'jdbc:oracle:thin:@10.100.98.74:1521/hcritico'  
conn = cx_Oracle.connect(username, password, database_url)
cursor = conn.cursor()
tabeladb = ''
colunas = ', '.join(df2.columns)



# Montar o script de inserção
script_insert = f"INSERT INTO {tabeladb} ({colunas}) VALUES "
