
from time import sleep
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from funcoes import navegador, existeNotas, existePasta, InformacaoNotas, salvarInformacaoNotas


def pular(nomeNotas, infos):
    print('\nLendo Bloco de notas\n')
    with open(nomeNotas,'r', encoding='utf-8') as notas:
        for linha in notas:
            linha = str(linha)
            n = linha.find('%')
            info = linha[0:n]
            if info not in infos:
                print(info.strip())
                infos.append(info.strip())
    notas.close()
    print('\nBloco de notas lido\n')


infos = []
user = os.environ.get("USERNAME")

pastaMain = f'c://Users/{user}/Desktop/Maps_CEPS/'
ultimaFonteDiretorio = f'{pastaMain}ultimaFonteDiretorio.txt'
ultimaFonteExcel = f'{pastaMain}ultimaFonteExcel.txt'

existePasta(pastaMain)
existeNotas(ultimaFonteDiretorio)
existeNotas(ultimaFonteExcel)

ultimoDiretorio = InformacaoNotas(ultimaFonteDiretorio)

while True:
    comando = str(input(f'Ultima fonte: {InformacaoNotas(ultimaFonteExcel)}\nUltimo dir: {InformacaoNotas(ultimaFonteDiretorio)}\n>>> ')).lower()

    if comando in ('ok', 'play'):
        print('\n')
        break
    elif comando in ('cd', 'dir', 'diretorio'):
        dir = str(input('Deseja usar qual diretorio?\n>>> '))
        ultimaFonteDiretorio
        salvarInformacaoNotas(ultimaFonteDiretorio, dir)
    elif comando in ('excel', 'planilha', 'fonte'):
        excel = str(input('Deseja usar qual planilha?\n>>> '))
        salvarInformacaoNotas(ultimaFonteExcel, excel)
    elif comando in 'help':
        print('''
Ok/Play = Continuar
CD/DIR/Diretorio = Muda o diretorio fonte
Excel/Planilha/Fonte = Muda a planilha fonte''')

    else:
        print('\nVALOR INVÁLIDO!\nDigite HELP para ajuda')
    print('\n')

notasFonte = pastaMain + InformacaoNotas(ultimaFonteExcel) + '.txt'
print(notasFonte)
existeNotas(notasFonte)

pular(notasFonte, infos)

fonte = InformacaoNotas(ultimaFonteDiretorio) + '\\' + InformacaoNotas(ultimaFonteExcel) + '.xlsx'
print(fonte)
fonte = pd.read_excel(fonte)

driver = navegador(8846, 'simplifiquePropostas')
wait = WebDriverWait(driver, 5)

driver.get('https://www.google.com/maps/')

for n, endereco in enumerate (fonte["endereco"]):
    cidade = fonte.loc[n, "cidade"]

    enderecoTEMP = endereco + ' ' + cidade

    if enderecoTEMP.strip() in infos:
        print('Já na fonte!')
        continue

    try:

        # clica na barra de pesquisa 
        pesquisar = wait.until(EC.element_to_be_clickable((By.ID, 'searchboxinput')))
        pesquisar.clear()
        pesquisar.send_keys(enderecoTEMP, Keys.ENTER)

        sleep(2)

        endereco = driver.find_element(By. XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[10]/div[2]/div[2]/span[2]/span')
        endereco = endereco.text
        print(endereco)

    except:
        print('\nEndereço não encontrado!\n')
        endereco = ''
    
    with open(notasFonte, 'a', encoding='utf-8') as notas:
        notas.write(enderecoTEMP + '%' + str(endereco) + '\n')
    notas.close()


print('FINALIZADO!!')