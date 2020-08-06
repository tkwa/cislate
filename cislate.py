import googletrans
import secrets
import sys

LANGUAGES = list(googletrans.LANGUAGES.keys())

def cislate_paragraph(text):
    if not text: return ''
    sr = secrets.SystemRandom()
    translator = googletrans.Translator()

    lang = 'en'
    print('en', end='')
    for _ in range(2):
        new_lang = lang
        while new_lang == lang:
            new_lang = sr.choice(LANGUAGES)
        print("->" + new_lang, end='')
        text = translator.translate(text, new_lang, lang).text
        lang = new_lang

    print('->en')
    text = translator.translate(text, 'en', lang).text

    return text

def cislate(text):
    paragraphs = text.split('\n')
    ret = []
    for paragraph in paragraphs:
        ret.append(cislate_paragraph(paragraph))
    text = '\n'.join(ret)
    return text

if __name__ == "__main__":
    if not 2 <= len(sys.argv) <= 3:
        print("usage: python cislate.py infile [outfile]")
        sys.exit(1)

    outfile = sys.argv[2] if len(sys.argv) == 3 else None
    with open(sys.argv[1]) as infile:
        result = cislate(''.join(infile.readlines()))
        if outfile:
            f = open(outfile, 'w')
            f.write(result)
            f.close()
        else:
            print(result)
