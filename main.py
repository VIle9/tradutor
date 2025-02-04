from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source= 'pt', target= 'en')

texto = input("Texto à traduzir: ")

traducao = tradutor.translate(texto)
print(traducao)