import pyautogui as ptg
import webbrowser
from time import sleep

try:
    # 1 - Abrir o Instagram
    webbrowser.open_new('https://www.instagram.com/')
    sleep(3)
    ptg.locateCenterOnScreen('img/aba_instagram.png')
except ptg.ImageNotFoundException:
    # Se abrir, mas não abrir o navegador
    # No meu caso, abrir o navegador ao lado do Chrome
    botao_windows = ptg.locateCenterOnScreen('img/navegador.png')
    sleep(2)
    # Ir para o ícone do Chrome
    ptg.moveTo(x=botao_windows[0], y=botao_windows[1], duration=2)
    ptg.move(-50, 0, duration=2)
    # Clicar nele
    ptg.click(clicks=2, interval=0.5)
    sleep(2)
    # Clicar no Instagram para abrí-lo
    posicao_aba_instagram = ptg.locateCenterOnScreen('img/aba_instagram.png')
    ptg.moveTo(x=posicao_aba_instagram[0], y=posicao_aba_instagram[1], duration=2)  # noqa: E501;
    ptg.click()
    sleep(2)

try:
    # 2 - Procurar pelo botão de login
    botao_login = ptg.locateCenterOnScreen('img/campo_login.png')
except ptg.ImageNotFoundException:
    # Caso de erro, por estar em outra tela
    # Clicar no botão para ir para outra conta
    botao_trocar_de_conta = ptg.locateCenterOnScreen('img/botao_trocar_de_conta.png')  # noqa: E501;
    ptg.moveTo(x=botao_trocar_de_conta[0], y=botao_trocar_de_conta[1], duration=2)  # noqa: E501;
    sleep(1)
    ptg.click()
    sleep(3)
    # E clicar no campo do login
    botao_login = ptg.locateCenterOnScreen('img/campo_login.png')
    ptg.moveTo(x=botao_login[0], y=botao_login[1], duration=2)
    sleep(1)
    ptg.click()
else:
    # Caso não dê nenhum erro, clicar no campo de login direto
    ptg.moveTo(x=botao_login[0], y=botao_login[1], duration=2)
    sleep(1)
    ptg.click()

login = 'inserir e-mail ou usuário'
senha = 'inserir a senha do Instagram'

# 3 - Inserir as informações e dar enter para prosseguir
ptg.typewrite(login)
ptg.press('tab')
sleep(1)
ptg.typewrite(senha)
ptg.press('tab')
sleep(1)
ptg.press('tab')
sleep(1)
ptg.press('enter')
sleep(4)

try:
    # 4 - Recusar as informações de ínicio do Instagram
    nao_salvar_senha = ptg.locateCenterOnScreen('img/recusar_salvar_senha.png')
    sleep(2)
    ptg.moveTo(x=nao_salvar_senha[0], y=nao_salvar_senha[1], duration=2)
    sleep(1)
    ptg.click()
    sleep(5)
except ptg.ImageNotFoundException:
    pass

try:
    nao_salvar_informacoes = ptg.locateCenterOnScreen('img/nao_salvar_informacoes.png')  # noqa: E501;
    sleep(2)
    ptg.moveTo(x=nao_salvar_informacoes[0], y=nao_salvar_informacoes[1], duration=2)  # noqa: E501;
    sleep(1)
    ptg.click()
    sleep(3)
except ptg.ImageNotFoundException:
    pass

try:
    nao_importar_contatos = ptg.locateCenterOnScreen('img/nao_importar_contatos.png')  # noqa: E501;
    sleep(2)
    ptg.moveTo(x=nao_importar_contatos[0], y=nao_importar_contatos[1], duration=2)  # noqa: E501;
    sleep(1)
    ptg.click()
    sleep(5)
except ptg.ImageNotFoundException:
    pass

# 5 - Clicar no botão de pesquisa
botao_pesquisa = ptg.locateCenterOnScreen('img/lupa_pesquisa.png')
sleep(2)
ptg.moveTo(x=botao_pesquisa[0], y=botao_pesquisa[1], duration=2)
sleep(1)
ptg.click()
sleep(3)

# 6 - Pesquisar pela conta da Nike e acessá-la
ptg.typewrite('nike')
sleep(5)
logo_nike = ptg.locateCenterOnScreen('img/logo_nike.png')
sleep(2)
ptg.moveTo(x=logo_nike[0], y=logo_nike[1], duration=2)
sleep(1)
ptg.click()
sleep(5)

# 7 - Acessar a última publicação da conta
ptg.moveTo(x=468, y=644, duration=2)
sleep(2)
ptg.click()
sleep(3)

# 8 - Curtir a publicação
coracao_curtida = ptg.locateCenterOnScreen('img/botao_curtir.png')
sleep(1)
ptg.moveTo(x=coracao_curtida[0], y=coracao_curtida[1], duration=2)
sleep(1)
ptg.click()
sleep(2)

# 9 - E por fim, comentar a publicação
caixinha_comentarios = ptg.locateCenterOnScreen('img/caixinha_comentarios.png')
sleep(1)
ptg.moveTo(x=caixinha_comentarios[0], y=caixinha_comentarios[1], duration=2)
sleep(1)
ptg.click()
sleep(2)
ptg.typewrite('Gostei')
sleep(3)
ptg.press('enter')
