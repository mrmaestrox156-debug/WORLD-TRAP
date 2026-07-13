# wtrap.py
import sys
import time
import os
import re

# Importação e verificação dos módulos ultra-detalhados
try:
    import engine_br
    import engine_intl
except ImportError as e:
    print(f"\033[1;31m[!] Erro crítico de dependência interna: {e}\033[0m")
    print("\033[1;37mCertifique-se de que 'engine_br.py' e 'engine_intl.py' estão no mesmo diretório.\033[0m")
    sys.exit(1)

C_VERDE = "\033[1;32m"
C_VERMELHO = "\033[1;31m"
C_BRANCO = "\033[1;37m"
C_AZUL = "\033[1;34m"
C_RESET = "\033[0m"

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def barra_carregamento():
    limpar_tela()
    largura = 40
    for i in range(largura + 1):
        porcentagem = int((i / largura) * 100)
        barra = '█' * i + '░' * (largura - i)
        sys.stdout.write(f"\r{C_BRANCO}[{barra}] {porcentagem}%{C_RESET}")
        sys.stdout.flush()
        time.sleep(0.01)
    print("\n")

def exibir_banner_inicial():
    limpar_tela()
    print(f"""{C_BRANCO}====================================================================
 _ _ _ _____ _    ____ ____ _  _ ____   ___ ____ 
 | | | |___  |    |    |  | |\\/| |___    |  |  | 
 |_|_| |____ |___ |___ |__| |  | |___    |  |__| 
                                                 
 _ _ _ ____ ____ _    ___     ___ ____ ____ ___  
 | | | |  | |__/ |    |  \\     |  |__/ |__| |__] 
 |_|_| |__| |  \\ |___ |__/     |  |  \\ |  | |    
                                                 
                 --=== WORLD-TRAP V.2 ===--
                 © Copyright Mrmaster (2026)
===================================================================={C_RESET}""")

def exibir_banner_verde():
    limpar_tela()
    print(f"""{C_VERDE}
 __        _____  ____  _     ____      _____ ____      _    ____  
 \\ \\      / / _ \\|  _ \\| |   |  _ \\    |_   _|  _ \\    / \\  |  _ \\ 
  \\ \\ /\\ / / | | | |_) | |   | | | |_____| | | |_) |  / _ \\ | |_) |
   \\ V  V /| |_| |  _ <| |___| |_| |_____| | |  _ <  / ___ \\|  __/ 
    \\_/\\_/  \\___/|_| \\_\\_____|____/      |_| |_| \\_\\/_/   \\_\\_|

                                              +@@@@@@@@@*+=-=+*@@@@@@@@@+
                                         @@@@+     ...............         @@@@@                                         
                                    @@@# +@@@@@@@@@@@@@@@%@@%@@@@@@@@@@@-#@@@@@@@@@@@                                    
                                @@@        @@@@@@@...@#+@@@@@@+*%. .@@@.@@@@  @@@@@@@@@@@                                
                             @@%            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@@@@@@@@                             
                          @@#                *@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@                          
                       =@@@@@                 @@@@@@@@@@@@@@@@@@@@@@@@@@@     @   @@@@@@@@@@@@@@@=                       
                     @@+.+@@@@                 @@@@@@@@@@@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@@                     
                   @@..@@-.=@@@#              @@@@@@@@@@@@@@@@@@@@@@@@@@:      @@@@@@@@@@@@@@@@@@@@@@@                   
                 *@:.@@..-@%.@@@@-          =@@@ @@@@@@@@@@@@@@@@@@@@  @@@      @@@@@@@@@@@@@@@@@@@@@@@*                 
                @@.@@...@@..   @@@@@     @@@@@  @@@@@@@@@@@@@@@@@@@@@@   -@@=    @@@@@@@@@@@@@@@@@@@@  @@                
              @@ %@.. +@:.      .*@@@@@@@@+    @@@@@@@@@@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@@@%.   @@              
             @@.@%  .@@.       .*@           @@@@@@@@@@@@@@@@@@@@@@@@@@@#           @@@@@@@ @@@@=. .#@..  @@             
            @.%@.. .@%.        -@.         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@           %@@ *@@+ .*@.. .@@.   @            
          #@.@@.  .@-.       . @.       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          @..       ..@.  .@@.   @*          
         #@.@+.@@:@..         @#.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         *@.         .@.@@:+@..  @#         
        #@.@=.  .@@@..      .%@. @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        .@%.     ...@@@.. .-@..  @#        
        @.@+. ..@*..:@@%..  .@.. @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        .@.... %@@.. +@.. .-@..  @        
       @.@#.   @@.    ..+@@%@@..*@@@@@@@@@@@@#   *@@@@@@@@@@@@@@@@@@@@   +@@@@@@@      .@@@@@-..    .@@   .#@.  .@       
      @@@@.   :@          . @@@@%@@@@@@@@@          .@@@@@@@@@@@@@@          @@@@@@@   @#@.         ..@-   .@@.  @@      
      @:@.    @-.         .#@.  @@@@@@@@@             @@@@@@@@@@@             @@@@@@@@@ .@*.          :@.   .@-.  @      
     @%@*   .=@.          .@*.  *@@@@@@@@             @@@@@@@@@@@              @@@@@@@@ .=@          ..@#    =@.  %@     
     @-@.   .@=           .@.    @@@@@@@@             @@@@@@@@@@@              @@@@@@@=  .@.           =@    .@=.  @     
    @@@*.   .@.           -@.    @@@@@@@@.           .@@@@@@@@@@@@            @@@@@@@@@@@@@@@          .@.   .*@.  @@    
    @-@..   #@.          .@@.     @@@@@@@@@         @@@@@@#@@@@@@@@=        @@@@@@@@@@@@@@@@@@@         @%     @.  -@    
    @-@.   .@*           .@@       @@@@@@@@@@@@@@@@@@@@ @@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         %@.    @-   @    
    @%@.    @-           .@=.      :@@@@@@@@@@@@@@@@@@@ @@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          :@    .@@.  @    
    @@%    .@.           .@:.        @@@@@@@@@@@@@@@@   @@@@@@@@  @@@@@@@@@@@@@@@@  @@@@@@@@@@   @:     .@.   .%@.  @    
    @@%@@@@@@@@@@@@*@@@@@@@@@@#@@@@@   @@@@@@@@@@@@@    @@@@@@@@@  @@@@@@@@@@@@@+   @@@@@@@@@@    @@@@@@@@@@@@@@@.  @    
    @@%     @.  @@@@@@@@@@@@@@@@@@-      @@@@@@@@@@@@   @@@@@@@@@ @@@@@@@@@@@@     @@@@@@@@@@      @@@  .@     %@.  @    
    @%@     @@@@@@@@@@@@@@@@@@@@@@@@@@      @@@@@@@@@@@ @@@@@@@@@ @@@@@@@@@%      %@@@@@@@@@@      *@@@@:@.   .@%   @    
    @=@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@      @@@@@@@@@@ @@@@@@@@@:@@@@@@@@        %@@@@@@@@@@      @@@@@@@    .@:  -@    
    @@@.. @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      @@@@@@@@@ @@@@@@%*@@@@@@@          @@@@@@@@@@       @@@@@@@+   .@.  @@    
     @@%.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@             @@      @%                 @@@@@@@@@       @@@@@@@@@@ .@@.  @     
     @%@@@@=          @@@@@@@@@@@@@@@@@@@@             @@@@@@@@@=                 @@@@@@@       @@@@@@@@@@@@@.@:  %@     
      @-                   +@@@@@@@@@@@@@@@            @@@@@@@@@             .   @@@@@@      +@@@@@@@@@@@@@@@@@.  @      
      @@.                      +@@@@@@@@@@@            @@@@@@@@@                @@@@@@@@@@@@@@+@@@@@@@@@@@@@@@@  @@      
       @*@                         @@@@@@@@            @@@@@@@@@                  @@@@@@+        @@@@@@@@@@@@@@@@@       
        @@.         @@@@@@@@@@@@      @@@@@            =@@@@@@@@                   @@@@@@         @@@@@@@@@@@@@ @        
        #@.    @@@@@@@@@@@@@@@@@@@@@@    @             .        @@@@@@@@            #@@@@           @@@@@@@@@@ @#        
         #@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@               @@@@@+   ++@++     @@@@@      *@@@@            @@@@@@@ @#         
          #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@           .  @@@@  @@@@@@@@@@@@@ @@@@@      @@@@              @@@@ @*          
            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          @  @ @@@  @@@@@@@@@@@@ @@@@@       @@@                  @            
             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         @ @@@@@@@ @@@@@@@@@@@@  @@@@@       @@#               @@             
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@        @  @@+    @@@@@@@@@@@@  -@@@@       @@@  .           @@              
                @@@@@@@@@@@@@@@@@@@@@@@@@@@@-      :@          @@@@@@@@@@@@@=@           @@ .@         @@                
                 *@@@@@@@@@@@@@@@@@@@@@@@@@@@      @@     %@@@- @@@@@@@@@@@@@            @@.@%       :@*                 
                   @@@@@@@@@@@@@@@@@@@@@@@@@@=     @@   @@@@@@@ @@@@@@@@@@@@@ @           @%...    .@@                   
                     @@@@@@@@@@@@@@@@@@@@@@@@@     @@@   @#     @@@@@@@@@@@@@  @          @@@@.  +@@                     
                       =@@@@@@@@@@@@@@@@@@@@@@     @@@                      : @@          @@.  @@=                       
                          @@@@@@@@@@@@@@@@@@@@+    @@@           @@@@@@@@@@@@@*           @@#@@                          
                             @@@@@@@@@@@@@@@@@@    @@@@    @@@@@ @@@@@@@@@@@@@           %@@                             
                                @@@@@@@@@@@@@@@    @@@@   @@@@@+ :@@@@@@@@@@@@  @     @@@                                
                                    @@@@@@@@@@@    @@@@@          @@@@@@@@@@@@  @#@@@                                    
                                         @@@@@@    @@@@@@*       @@@@@@@@@@%@@@@                                         
                                               +@@@@@@@@@@@=-=+*@@@@@@@@@+

    {C_RESET}""")
    print(f"{C_VERDE}V.2{C_RESET}\n")

def renderizar_painel_final(res, idioma):
    limpar_tela()
    
    if idioma == "pt":
        headers = [
            "INFORMAÇOES BASICAS E DE REGISTRO", 
            "DADOS DE TELECOMUNICAÇAO", 
            "REPUTAÇAO E ANALISE DE RISCO", 
            "PEGADA DIGITAL (OSINT METADATA)",
            "VETORES DE LOCALIZAÇAO E MAPEAMENTO"
        ]
        campos = [
            "Numero Formatado (E.164)", "Tipo de Linha", "Pais de Origem", "Estado / Cidade Regiao", "Fuso Horario",
            "Operadora Original", "Operadora Atual", "Status da Linha", "Tipo de Roteamento",
            "Score de Fraude (0-100)", "Marcado como Spam",
            "Registro no WhatsApp", "Registro no Telegram", "Pegada Digital Textual",
            "Coordenadas Estimadas", "Altitude do Terreno", "Raio de Precisao", "Mapeamento Satelite"
        ]
        status_linha = "ATIVO / OPERANTE"
        prompt_retorno = "\nPressione Enter para retornar ao menu principal..."
    else:
        headers = [
            "BASIC AND REGISTRATION INFORMATION", 
            "TELECOMMUNICATION DATA", 
            "REPUTATION AND RISK ANALYSIS", 
            "DIGITAL FOOTPRINT (OSINT METADATA)",
            "LOCATION AND MAPPING VECTORS"
        ]
        campos = [
            "Formatted Number (E.164)", "Line Type", "Country of Origin", "State / City Region", "Timezone",
            "Original Carrier", "Current Carrier", "Line Status", "Routing Type",
            "Fraud Score (0-100)", "Marked as Spam",
            "WhatsApp Registry", "Telegram Registry", "Textual Digital Footprint",
            "Estimated Coordinates", "Terrain Altitude", "Accuracy Radius", "Satellite Mapping"
        ]
        status_linha = "ACTIVE / OPERATIONAL"
        prompt_retorno = "\nPress Enter to return to the main menu..."

    # Bloco 1: Registro
    print(f"{C_VERDE}[=] {headers[0]}")
    print(f"--------------------------------------------------{C_RESET}")
    print(f"{campos[0]:<27}: {res['e164']}")
    print(f"{campos[1]:<27}: {res['tipo']}")
    print(f"{campos[2]:<27}: {res['pais']}")
    print(f"{campos[3]:<27}: {res['regiao']}")
    print(f"{campos[4]:<27}: {res['fuso']}")
    
    # Bloco 2: Telecomunicações
    print(f"\n{C_VERDE}[=] {headers[1]}")
    print(f"--------------------------------------------------{C_RESET}")
    print(f"{campos[5]:<27}: {res['operadora_origem']}")
    print(f"{campos[6]:<27}: {res['operadora_atual']}")
    print(f"{campos[7]:<27}: {status_linha}")
    print(f"{campos[8]:<27}: {res['tipo_rede']}")
    
    # Bloco 3: Reputação
    print(f"\n{C_VERDE}[=] {headers[2]}")
    print(f"--------------------------------------------------{C_RESET}")
    print(f"{campos[9]:<27}: {res['score']}")
    print(f"{campos[10]:<27}: {res['spam']}")
    
    # Bloco 4: OSINT
    print(f"\n{C_VERDE}[=] {headers[3]}")
    print(f"--------------------------------------------------{C_RESET}")
    print(f"{campos[11]:<27}: {res['whatsapp']}")
    print(f"{campos[12]:<27}: {res['telegram']}")
    print(f"{campos[13]:<27}: {res['exposicao']}")

    # Bloco 5: Geolocalização e Link do Maps (Extraído dos Módulos)
    print(f"\n{C_VERDE}[=] {headers[4]}")
    print(f"--------------------------------------------------{C_RESET}")
    print(f"{campos[14]:<27}: {res['coordenadas']}")
    print(f"{campos[15]:<27}: {res['altitude']}")
    print(f"{campos[16]:<27}: {res['raio_precisao']}")
    print(f"{campos[17]:<27}: {C_AZUL}{res['link_maps']}{C_RESET}")
    
    print(f"\n{C_BRANCO}=================================================={C_RESET}")
    input(prompt_retorno)

def main():
    barra_carregamento()
    exibir_banner_inicial()
    
    print(" [PT] Português")
    print(" [EN] English")
    print("====================================================================")
    
    idioma = input("Selecione / Select: ").strip().lower()
    while idioma not in ['pt', 'en']:
        idioma = input("Selecione [PT] ou [EN]: ").strip().lower()
        
    barra_carregamento()
    
    while True:
        exibir_banner_verde()
        if idioma == "pt":
            print("[1] CONSULTAR NUMERO")
            print("[2] SAIR")
        else:
            print("[1] CONSULT NUMBER")
            print("[2] EXIT")
        print("====================================================================")
        
        opcao = input("-> ").strip()
        
        if opcao == "1":
            limpar_tela()
            prompt = "Digite o identificador internacional: " if idioma == "pt" else "Enter international identifier: "
            numero_alvo = input(prompt).strip()
            
            if not numero_alvo:
                continue
                
            numero_limpo = re.sub(r'\D', '', numero_alvo)
            if len(numero_limpo) < 8:
                err = "[!] Quantidade de digitos insuficiente." if idioma == "pt" else "[!] Insufficient number of digits."
                print(f"{C_VERMELHO}{err}{C_RESET}")
                time.sleep(2)
                continue
                
            status_msg = "[*] Acessando barramento de infraestrutura..." if idioma == "pt" else "[*] Accessing infrastructure bus..."
            print(f"\n{C_AZUL}{status_msg}{C_RESET}")
            
            # Encaminhamento inteligente baseado no prefixo DDI
            if numero_limpo.startswith("55"):
                dados_finais = engine_br.extrair_dados_br(numero_limpo)
            else:
                dados_finais = engine_intl.extrair_dados_intl(numero_limpo, idioma)
                
            if not dados_finais:
                err = "[!] Falha critica na decodificaçao do registro global." if idioma == "pt" else "[!] Critical failure decoding global registry."
                print(f"{C_VERMELHO}{err}{C_RESET}")
                time.sleep(2)
                continue
                
            renderizar_painel_final(dados_finais, idioma)
            
        elif opcao == "2":
            limpar_tela()
            sys.exit()

if __name__ == "__main__":
    main()
