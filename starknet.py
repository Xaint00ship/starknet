from selenium.webdriver.common.by import By
from time import sleep

from metaMaskAutomation.metaMask import MetaMask # либа функций метамаска
from argentX import ArgentX # либа функций аргент икс
from sessionChromeDriver.session import Session # либа создания/загрузки профиля хрома


URL = "https://goerli.starkgate.starknet.io/"
driver = Session(antik_id).createChromeDriverSession()

def connectMetaMask(): # подключение кошелька метамаск
    driver.get(URL)
    sleep(5)
    driver.find_element(By.CLASS_NAME, "MainMenuButton_mainMenuButton__3WcjN").click()
    sleep(3)
    driver.find_element(By.CLASS_NAME, "MultiChoiceItem_icon__2atrw").click()
    sleep(1)
    MetaMask(phrase, metamask_pass, driver).connectWallet()
    sleep(1)



def importWalletArgentX(): # импорт кошелька аргент икс
    connectMetaMask()
    ArgentX(phrase, metamask_pass, driver).importWallet()
    sleep(10)



def connectWalletArgentX(): # подключение кошелька аргент икс
    connectMetaMask()
    try:
        driver.find_element(By.CLASS_NAME, "s-ripple-container").click()
    except:
        pass
    sleep(3)
    ArgentX(phrase, metamask_pass, driver).connectWallet()
    sleep(10)



def deposit(value):
    connectMetaMask()
    sleep(5)
    driver.find_element(By.CLASS_NAME, "MultiChoiceItem_icon__2atrw").click()
    driver.find_element(By.CLASS_NAME, "TokenInput_tokenInput__2Yqb8").find_element(By.TAG_NAME, "input").send_keys(
        str(value))
    sleep(1)
    driver.find_element(By.CLASS_NAME, "MainMenuButton_mainMenuButton__3WcjN").click()
    sleep(3)
    MetaMask(phrase, metamask_pass, driver).confirmTransaction()
    sleep(100)



def withdraw(value):
    connectMetaMask()
    sleep(3)
    driver.find_element(By.CLASS_NAME, "MultiChoiceItem_icon__2atrw").click()
    driver.find_element(By.CLASS_NAME, "Source_tabsContainer__3ROqA").find_elements(By.TAG_NAME, "div")[1].click()
    sleep(5)
    driver.find_element(By.CLASS_NAME, "TokenInput_tokenInput__2Yqb8").find_element(By.TAG_NAME, "input").send_keys(
        str(value))
    sleep(1)
    driver.find_element(By.CLASS_NAME, "MainMenuButton_mainMenuButton__3WcjN").click()
    sleep(5)
    ArgentX(phrase, metamask_pass, driver).connectConfirmWallet()



