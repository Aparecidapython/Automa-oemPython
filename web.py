from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


# Configuração do Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(
    service=servico,
    options=options
)

wait = WebDriverWait(navegador, 20)

# Abre o site
navegador.get("https://amil.com.br/beneficiario/#/")

# 1. ACEITAR OS COOKIES
try:
    aceitar_cookies = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[contains(normalize-space(.), 'Aceitar todos')]")
        )
    )

    aceitar_cookies.click()

except TimeoutException:
    print("Aviso de cookies não apareceu.")


# 2. CPF
campo_cpf = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//input[not(@type='hidden')])[1]")
    )
)

campo_cpf.click()
campo_cpf.clear()
campo_cpf.send_keys("10700178686")

# 3. SENHA
campo_senha = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//input[@type='password']")
    )
)

campo_senha.click()
campo_senha.clear()
campo_senha.send_keys("Ap15051994@")

# 4. ENTRAR
botao_entrar = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Entrar']")
    )
)

botao_entrar.click()