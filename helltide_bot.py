import discord

class MyClient(discord.Client):
    # Intents
    def __init__(self):
            super().__init__(intents=intents)

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Menssagem de {0.author}: {0.content}'.format(message))

        # Define o ID do canal em que ele irá responder
        canal = client.get_channel("ID_CANAL")

        # Saudação
        if message.content == "Opa":
            await canal.send(f"{message.author.name}, Opa")

        # Helltide
        if message.content == "helltide":
            from selenium import webdriver

            # Configuração do ChromeDriver
            chrome_driver_path = "./chromedriver.exe"
            options = webdriver.ChromeOptions()

            # Executar em modo headless, sem abrir a janela do navegador
            options.add_argument("--headless")  
            driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

            # Acessa o site
            driver.get("https://helltides.com")

            # Executa o JavaScript para puxar o conteúdo do elemento desejado
            script = "return document.querySelector('.font-mono.mb-2').textContent;"
            informacao = driver.execute_script(script)

            # Fecha o navegador
            driver.quit()

            await canal.send(f"{message.author.name}, segue o horario da próxima Helltide: {informacao}")

intents = discord.Intents.default()  # Cria uma instância dos intents padrão
intents.messages = True  # Habilita o intent para receber eventos de mensagens

client = MyClient()
client.run('BOT_ID')