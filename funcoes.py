import os 
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import subprocess
import psutil


def navegador(porta, caminhoChrome):
    global driver

    usuarioPc = os.environ.get("USERNAME")
    user_data_dir = f'C://Users/{usuarioPc}/Desktop/navegadorChrome/{caminhoChrome}'
    remote_debugging_port = porta
    chrome_executable_path = 'C://Program Files/Google/Chrome/Application/chrome.exe'

    # Verifica se o Chrome já está aberto com as opções especificadas
    chrome_aberto = False
    for proc in psutil.process_iter(['name', 'cmdline']):
        if (proc.info['name'] and 'chrome' in proc.info['name'] and
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

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    print('\nNavegador Iniciado! \n')
    return driver      


def formatarCNPJ(cnpj):

    # tira a formatacao do cnpj
    cnpjFormatado = ''
    cnpj = str(cnpj)
    if '.' in cnpj:
        for numero in cnpj:
            if numero in ('.', '/', '-'):
                continue
            else: 
                cnpjFormatado += numero
    else:
        cnpjFormatado = cnpj
    while len(cnpjFormatado) < 14:
            cnpjFormatado = "0" + cnpjFormatado
    return cnpjFormatado



def formatarCNPJ(cnpj):
    # tira a formatacao do cnpj
    cnpjFormatado = ''
    cnpj = str(cnpj)
    if '.' in cnpj:
        for numero in cnpj:
            if numero in ('.', '/', '-'):
                continue
            else: 
                cnpjFormatado += numero
    else:
        cnpjFormatado = cnpj
    while len(cnpjFormatado) < 14:
            cnpjFormatado = "0" + cnpjFormatado
    return cnpjFormatado


def existePasta(diretorioDestino):
    if os.path.exists(diretorioDestino) == False:
        os.mkdir(diretorioDestino)


def existeNotas(diretorioNotas):
    # LE O BLOCO DE NOTAS PARA PEGAR ULTIMA FONTE USADA SEM SER O CRM5
    if os.path.exists(diretorioNotas) == False:
        with open(diretorioNotas, 'w', encoding='utf-8') as ultima:
            ultima.write('CRIADO - CRIADO\n')
        ultima.close()


def InformacaoNotas(diretorioNotas):
    existeNotas(diretorioNotas)
    with open(diretorioNotas, 'r', encoding='utf-8') as ultima:
        informacao = ultima.readline().strip()
    ultima.close()
    return informacao


def salvarInformacaoNotas(nomeNotas, ultimaFonte):
    existeNotas(nomeNotas)
    with open(nomeNotas, 'w', encoding='utf-8') as ultimaInformacao:
        ultimaInformacao.write(str(ultimaFonte))
    ultimaInformacao.close()


def pularCNPJ(nomeNotas, CNPJS):
    print('\nLendo Bloco de notas\n')
    with open(nomeNotas,'r', encoding='utf-8') as notas:
        for linha in notas:
            linha = str(linha)
            CNPJ = linha[0: 14]
            CNPJS.append(CNPJ)
        notas.close()
    print('\nBloco de notas lido\n')
