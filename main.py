from deep_translator import GoogleTranslator

# Escolha do idioma a ser lido
def para_traduzir(idioma):
    match idioma:
        case "en":
            return "en"
        case "fr":
            return "fr"
        case "pt":
            return "pt"
        case "es":
            return "es"
        case _:
            print("\nIdioma de origem não suportado.\n")
            return None

# Escolha o idioma que vai fazer a tradução
def vai_traduzir(idioma):
    match idioma:
        case "en":
            return "en"
        case "fr":
            return "fr"
        case "pt":
            return "pt"
        case "es":
            return "es"
        case _:
            print("\nIdioma de destino não suportado.\n")
            return None


def start():
    print("--------")
    print("TRADUTOR")
    print("--------")
    print("\nDigite 'f' a qualquer momento para encerrar o programa.")


    # Idiomas suportados
    idiomas = {
        'en': 'Inglês', 
        'fr': 'Francês',
        'pt': 'Portguês',
        'es': 'Espanhol'
    }
    while True:
        print("\n--------")
        print("Idiomas suportados:")
        print("--------")
        for codigo, nome in idiomas.items():
            print(f"{codigo}: {nome}")

        # Entrada do usuário para idioma de origem
        idioma_origem = input("\nEscolha o idioma a ser traduzido: ")
        if idioma_origem.lower() == "f":
            print("\nPrograma encerrado. Até mais!")
            break
        idioma_origem = para_traduzir(idioma_origem)
        if not idioma_origem:
            continue 

        # Entrada do usuário para idioma de destino
        idioma_destino = input("\nEscolha o idioma para traduzir: ")
        if idioma_destino.lower() == "f":
            print("\nPrograma encerrado. Até mais!")
            break
        idioma_destino = vai_traduzir(idioma_destino)
        if not idioma_destino:
            continue 

        # Texto a ser traduzido
        texto = input("\nDigite o texto que deseja traduzir: ").strip()
        if texto.lower() == "f":
            print("\nPrograma encerrado. Até mais!")
            break

        # Realiza a tradução
        try:
            tradutor = GoogleTranslator(source= idioma_origem, target= idioma_destino)
            traducao = tradutor.translate(texto)
            print(f"Tradução: {traducao}")
        except Exception as e:
            print(f"Erro ao traduzir: {e}")        

if __name__ == '__main__':
    start()
