#!/usr/bin/env python
# coding: utf-8

# <!-- LOGOTIPO DO PROJETO -->
# <div style="display: flex; justify-content: center;">
#    <a href="https://github.com/edendenis/readme_set_up_install_use_uninstall_rpa">
#      <img src="figures/gold_edf_technology_logo_transparent_background_and_gold_name.png" alt="Logo" width="160" height="160">
#    </a>
# </div>
# 
# <h3 align="center">Configurar/Instalar/Usar/Desinstalar</h3>
# 
# <!-- <div style="display: flex; justify-content: center;">
#   <a href="https://zenodo.org/doi/10.5281/zenodo.10668919">
#     <img src="https://zenodo.org/badge/758237447.svg" alt="DOI">
#   </a>
# </div> -->
# 
# <p align="center">
#  Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar/desinstalar o `Wall paper` no `Linux Ubuntu`.
#  <br />
#  <a href="https://github.com/edendenis/readme_set_up_install_use_uninstall_rpa"><strong>Explore os documentos »</strong></a>
#  <br />
#  <br />
#  <a href="https://github.com/edendenis/readme_set_up_install_use_uninstall_rpa">Ver demonstração</a>
#  ·
#  <a href="https://github.com/edendenis/readme_set_up_install_use_uninstall_rpa/issues">Relatar bug</a>
#  ·
#  <a href="https://github.com/edendenis/readme_set_up_install_use_uninstall_rpa/issues">Solicitar recurso</a>
# </p>
# 

# ## Descrição [2]
# 
# ### `wallpaper`
# 
# Um `wallpaper`, também conhecido como papel de parede, é uma imagem ou padrão de design usado como plano de fundo em uma interface gráfica de usuário, como em computadores, celulares e tablets. Essa imagem é exibida na área de trabalho ou tela inicial do dispositivo, proporcionando personalização estética e refletindo o gosto pessoal do usuário. Os wallpapers podem variar desde fotografias de paisagens e obras de arte até padrões abstratos e ilustrações digitais, permitindo que os usuários escolham a aparência visual que desejam para seu dispositivo.
# 

# ## 1. Como configurar/instalar/usar o `Wall paper` no `Linux Ubuntu` [1]
# 
# Para instalar o `Wall paper` no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# A pasta `backgrounds` geralmente é encontrada no diretório `/usr/share/backgrounds` no `Ubuntu 22.04 LTS`. Você pode acessá-la utilizando o terminal ou o gerenciador de arquivos.
# 
# 1. **Copie a pasta `backgrounds` para a pasta `usr/share/backgrounds`**: Depois de copiar a pasta `backgrounds` para a pasta `~/Desktop`, execute o comando: `sudo cp -r ~/Desktop/backgrounds/* /usr/share/backgrounds/ 

# ## 2. Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `Wall paper` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     NÂO há.
#     ```
# 

# ## 3. Desinstalar o `Wall paper` no `Linux Ubuntu`
# 
# 1. Para desinstalar o aplicativo, exclua o diretório de instalação do `Wall paper `
# 

# <!-- LICENÇA -->
# ## Licença
# 
# Distribuído sob a licença MIT. Consulte `LICENSE.txt` para obter mais informações.
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

# <!-- ROTEIRO -->
# ## Roteiro
# 
# - [x] Adicionar registro de alterações
# - [x] Adicionar links de volta ao topo
# - [x] Adicionar modelos adicionais com exemplos
# - [x] Suporte multilíngue
#      - [x] Espanhol
#      - [x] Inglês
#      - [x] Português
#      - [x] Português brasileiro 
# 
# Consulte os [problemas abertos](https://github.com/edendenis/k_means_python/issues) para obter uma lista completa dos recursos propostos (e problemas conhecidos).
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
# 

# <!-- CONTRIBUIÇÔES -->
# ## Contribuições
# 
# As contribuições são o que tornam a comunidade de código aberto um lugar incrível para aprender, inspirar e criar. Qualquer contribuição que você fizer será **muito apreciada**.
# 
# Se você tiver uma sugestão que possa melhorar isso, bifurque o repositório e crie uma solicitação `pull`. Você também pode simplesmente abrir um problema com a tag “aprimoramento”.
# Não se esqueça de dar uma estrela ao projeto! Obrigado novamente!
# 
# 1. Bifurque o projeto
# 2. Crie sua ramificação de recursos (`git checkout -b feature/AmazingFeature`)
# 3. Confirme suas alterações (`git commit -m 'Add some AmazingFeature'`)
# 4. Envie para a filial (`git push origin feature/AmazingFeature`)
# 5. Abra uma solicitação pull
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
# 

# <!-- ACKNOWLEDGMENTS -->
# ## Agradecimentos
# 
# * [Best README Template](https://github.com/othneildrew/Best-README-Template?tab=readme-ov-file)
# * [Choose an Open Source License](https://choosealicense.com)
# * [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
# * [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
# * [Malven's Grid Cheatsheet](https://grid.malven.co/)
# * [Img Shields](https://shields.io)
# * [GitHub Pages](https://pages.github.com)
# * [Font Awesome](https://fontawesome.com)
# * [React Icons](https://react-icons.github.io/react-icons/search)
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
# 

# ## Referências
# 
# [1] OPENAI. ***Pasta `backgrounds` em `/usr/share/backgrounds`.*** Disponível em: <https://chatgpt.com/c/87a688cc-baac-41c7-b18b-2cf86264b735> (texto adaptado). Acessado em: 09/05/2024 08:00.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 09/05/2024 08:00.
# 
# [3] USER: OTHENEILDREW. ***Best readme template***. Disponível em: <https://github.com/othneildrew/Best-README-Template>. Acessado em: 09/05/2024 08:00.
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
# 
