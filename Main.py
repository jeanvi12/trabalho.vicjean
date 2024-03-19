from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path='C:\\Users\\LabJF\\Downloads\\chromedriver-win32 (2)\\chromedriver-win32\\chromedriver.exe')
options = webdriver.ChromeOptions() 
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://www.netshoes.com.br/auth/login")
 
    def enviarDados(usuario, senha,):
        email_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "user"))
        )
        senha_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        btn_Signin = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div[1]/section[1]/form/div[6]/div/div/button'))
        )
        email_login.clear
        senha_login.clear
        email_login.send_keys(usuario)
        senha_login.send_keys(senha)
        btn_Signin.click()
        driver.implicitly_wait(5)  

        
    

    enviarDados("victoriamariana759@gmail.com","victoriamariana")
   
    alert = driver.find_element(By.XPATH, '/html/body/div[2]/header/div[1]/section[2]/section/form/div/input')
    print("teste falhou")
    alert.send_keys('tenis feminino')



except:
    print("Teste Falhou! Erro na execução")



driver.quit()