import os 
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import subprocess
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import psutil
import pandas as pd
from selenium.webdriver import Keys
import sys


def validar():
    while True:
        simnao = str(input('[S/N] >>>>> '))
        if simnao in 'SsNn':
            return simnao
        else:
            print('\nValor inválido!\n')


def navegador():
    global driver
    user_data_dir = f'C://Users/{usuarioPc}/Desktop/Script/CRM5'
    remote_debugging_port = 8797
    chrome_executable_path = 'C://Program Files/Google/Chrome/Application/chrome.exe'

    # Verifica se o Chrome já está aberto com as opções especificadas
    chrome_aberto = False
    for proc in psutil.process_iter(['name', 'cmdline']):
        if (proc.info['name'] and 'chrome' in proc.info['name'].lower() and
                proc.info['cmdline'] and
                f'--remote-debugging-port={remote_debugging_port}' in proc.info['cmdline'] and
                f'--user-data-dir={user_data_dir}' in proc.info['cmdline']):
            chrome_aberto = True
            break

    # Abre o Chrome com as opções especificadas se não estiver aberto
    if not chrome_aberto:
        subprocess.Popen([chrome_executable_path, 
                          f'--remote-debugging-port={remote_debugging_port}', 
                          f'--user-data-dir={user_data_dir}'])

    # Configura as opções do Chrome para o WebDriver
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", f"localhost:{remote_debugging_port}")

    print('\nIniciando Whatsapp...')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    print('Iniciado')
    
    return driver


usuarioPc = os.environ.get("USERNAME")
linkWhats = 'https://web.whatsapp.com/send?phone='
diretorioPrincipal = f'C://Users/{usuarioPc}/Desktop/Whatsapp'
mensagem = f'{diretorioPrincipal}/Mensagem.txt'
planilha = f'C://{usuarioPc}/Samuel/Desktop/Whatsapp/Contatos.xlsx'

# confere se o diretorio existe
if os.path.exists(diretorioPrincipal) == False:
    os.mkdir(diretorioPrincipal)

sleep(3)

# confere se o bloco de notas existe 
if os.path.exists(mensagem) == False:
    with open(mensagem, 'w', encoding='utf-8') as notas:
        notas.write(' ')
    notas.close()


colunas = {'CNPJ':[''] , 'LINHAS':[''], 'TELEFONE':[''], 'GESTOR':[''], 'EMPRESA':['']}
dataFrame = pd.DataFrame(columns=colunas)

# confere se a planilha existe 
if os.path.exists(f'{diretorioPrincipal}/Contatos.xlsx') == False:
    dataFrame.to_excel(planilha , index=False)

# inicio
fonte = pd.read_excel(planilha)

# abre o navegador
navegador()
wait = WebDriverWait(driver, 10)

driver.get('https://web.whatsapp.com/')


try:
    wait.until(EC.presence_of_element_located((By.ID, '//*[@id="app"]/div/div[2]/div[3]/div[1]/div/div/div[2]/div/canvas'))).click()
    print('LOGADO?')
    logado = validar()
except:
    print('\nWhatsapp já logado!\n')


# abre o bloco de notas e le a mensagem a ser mandada 
with open(mensagem, 'r', encoding='utf-8') as notas:
    texto = notas.read()
notas.close()


# pede para o usuario escrever uma mensagem no bloco de notas caso nao tenha nada escrito
if texto == ' ' or texto == '':
    print('\nO BLOCO DE NOTAS ESTÁ VAZIO')
    print(' O PROGRAMA SERÁ ENCERRADO!')
    sys.exit()


for n, CNPJ in enumerate (fonte["CNPJ"]):
    TELEFONE = fonte.loc[n, "TELEFONE"]
    
    # gestor
    try:
        GESTOR = fonte.loc[n, "GESTOR"]
    except:
        print('Empresa não encontrada na planilha fonte!')

    # empresa
    try:
        EMPRESA = fonte.loc[n, "EMPRESA"]
    except:
        print('Empresa não encontrada na planilha fonte!')

    # linhas
    try:
        LINHAS = fonte.loc[n, "LINHAS"]
    except:
        print('Linhas não encontrada na planilha fonte!')


    # transforma o delefone em str
    TELEFONE = str(TELEFONE)
    # cria a variavel 
    telefoneCerto = ''

    # tira toda e qualquer formatacao que tiver no numero de telefone
    for numero in TELEFONE:
        if numero in '1234567890':
            telefoneCerto += numero

    # entra no numeto do contato do whats
    driver.get(linkWhats+TELEFONE)


    sleep(35)

    # texto lido do bloco de notas
    texto = eval(f"f'''{texto}'''")
    print(texto)
    

    try:
        chat = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')))
        chat.click()
        chat.send_keys(texto)
        chat.send_keys(Keys.ENTER)
        print('\nMensagem enviada\n')
        
    except:
        print('\nO número de telefone é inválido\n')

    sleep(35)
