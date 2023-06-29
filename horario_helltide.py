from selenium import webdriver

# Configuração do ChromeDriver
# Certifique-se de substituir "caminho_para_seu_chromedriver" pelo caminho correto para o seu ChromeDriver
# Por exemplo, "C:/caminho/para/seu/chromedriver.exe"
chrome_driver_path = "./chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Executar em modo headless, sem abrir a janela do navegador
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

# Acessa o site
driver.get("https://helltides.com")

# Executa o JavaScript para obter o conteúdo do elemento desejado
script = "return document.querySelector('.font-mono.mb-2').textContent;"
informacao = driver.execute_script(script)

# Imprime a informação encontrada
print("Informação encontrada:", informacao)

# Fechar o navegador
driver.quit()
