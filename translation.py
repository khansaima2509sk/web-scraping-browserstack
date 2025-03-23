from googletrans import Translator

def translate_titles(titles):
    translator = Translator()
    translated_titles = []

    for title in titles:
        translated = translator.translate(title, src='es', dest='en')
        translated_titles.append(translated.text)
    
    return translated_titles
