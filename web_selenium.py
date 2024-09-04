from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

tempo_dentro_funcoes = 1.5

def para_mandar_informacoes(lista: list) -> None:
    """
    Preenche e verifica campos

    A função faz login ou insere informações em um formulário web.
    Para cada par de elementos na lista, localiza um campo na página
    usando XPath, limpa o campo, insere o valor correspondente, e verifica 
    se o valor foi corretamente inserido.

    Parâmetros:
    lista (list): Uma lista de pares, onde o primeiro elemento 
    é o XPath do campo e o segundo é o valor a ser inserido.

    """
    x = 0
    while x < len(lista):

        element = WebDriverWait(navegador, 50).until(
            EC.visibility_of_element_located((By.XPATH, lista[x][0]))
        )
        element.clear()
        element.send_keys(lista[x][1])

        # Esperar um pouco para o texto ser atualizado
        time.sleep(tempo_dentro_funcoes)

        # Verificar o valor atual do campo
        texto = element.get_attribute('value')

        # print(f"Texto esperado: '{lista[x][1]}', Texto obtido: '{texto}'")

        if texto == lista[x][1]:
            x += 1
        else:
            time.sleep(2)
            print(f"Erro ao inserir texto no campo {lista[x][0]}. Tentando novamente...")

def para_apertar_botoes(lista: list) -> None:
    """
    Clica em uma série de botões identificados por seus seletores XPath.

    A função percorre uma lista de seletores XPath, espera até que cada botão esteja
    visível na página, e então clica nele. Se um botão não for encontrado ou não estiver 
    visível, a função tenta novamente após uma breve espera.

    Parâmetros:
    lista (list): Uma lista de strings, onde cada string é um seletor XPath 
    que identifica um botão na página.

    Exceções:
    Caso um botão não seja encontrado ou não esteja visível após 50 segundos,
    uma exceção é lançada, e a função tenta clicar novamente após uma pausa.

    """
    i = 0
    j = 0
    while i < len(lista):

        try:
            element = WebDriverWait(navegador, 50).until(
                EC.visibility_of_element_located((By.XPATH, lista[i]))
            ).click()
            i += 1
        
        except Exception as e:
            time.sleep(2)
            j += 1
            print('Botão não encontrado. Tentativa {}'.format(j))

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.maximize_window()
navegador.get('https://analytics.google.com/analytics/web/?authuser=0#/p400308384/reports/intelligenthome')

# Colocando o e-mail da conta:
para_mandar_informacoes([['//*[@id="identifierId"]', 'gabriel.holanda@savvi.com.br']] )
time.sleep(1)
# Apertando para confirmar o login:
para_apertar_botoes(['//*[@id="identifierNext"]/div/button/span'])

# Colocando a senha:
login = [['//*[@id="password"]/div[1]/div/div[1]/input', 'Dgjl1998@#']] 
para_mandar_informacoes(login)

# Apertando para confirmar o login e caminhos dentro do analyticssenha_aqui
caminhos = [
    '//*[@id="passwordNext"]/div/button/span',
    '//*[@id="suite-top-nav"]/gmp-header/gmp-universal-picker/button/span[2]/div[2]/span/span', # Apertando na Sx para mudar
    '//*[@id="cdk-overlay-1"]/div[2]/div[3]/gmp-entity-panel/div/div[1]/gmp-entity-list/cdk-virtual-scroll-viewport/div[1]/ul/li[1]/button/gmp-entity-item/div', # Selecionando Anhaia Mello
    '//*[@id="cdk-overlay-1"]/div[2]/div[3]/gmp-entity-panel/div/div[2]/gmp-entity-list/cdk-virtual-scroll-viewport/div[1]/ul/li/a/gmp-entity-item/div', # Selecionando Anhaia Mello
    '/html/body/ga-hybrid-app-root/ui-view-wrapper/div/app-root/div/div/ui-view-wrapper/div/ga-report-container/div/div/div/report-view/ui-view-wrapper/div/ui-view/ga-explorer-report/div/div',
    '/html/body/ga-hybrid-app-root/ui-view-wrapper/div/app-root/div/xap-deferred-loader-outlet[1]/ga-left-nav2/ga-nav2/ga-primary-nav/mat-nav-list[1]/ga-primary-nav-item[2]/a/mat-icon',
    '/html/body/ga-hybrid-app-root/ui-view-wrapper/div/app-root/div/xap-deferred-loader-outlet[1]/ga-left-nav2/ga-nav2/ga-secondary-nav/mat-tree/mat-tree-node[6]/ga-secondary-nav-item/button',
    '/html/body/ga-hybrid-app-root/ui-view-wrapper/div/app-root/div/xap-deferred-loader-outlet[1]/ga-left-nav2/ga-nav2/ga-secondary-nav/mat-tree/mat-tree-node[8]/ga-secondary-nav-item/button/span[2]/div/span',
    '/html/body/ga-hybrid-app-root/ui-view-wrapper/div/app-root/div/div/ui-view-wrapper/div/ga-report-container/div/div/div/report-view/ui-view-wrapper/div/ui-view/ga-explorer-report/div/ga-report-header-v2/div[1]/div[1]/ga-date-range-selector/ga-date-range-picker-v2/div[2]/button/span[2]/div/div[2]',
    '//*[@id="reach-datepicker-10"]/div[1]/reach-calendar-presets-menu/div/div[1]/div[6]/div',
]
para_apertar_botoes(caminhos)


# Manter a janela aberta depois que a automação acabar
while True:
    print('Página no navegador aberta')
    time.sleep(200)
