import requests
from bs4 import BeautifulSoup

languages = ['Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese', 'Dutch', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Turkish']


def translate(language1, language2, word):
    if language1 == language2:
        return None
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(f"https://context.reverso.net/translation/{language1.lower()}-{language2.lower()}/{word}", headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    words = []
    if response.status_code == 200:
        trans_words = soup.find('div', {'id': "translations-content"}).find_all('a')
        for x in trans_words:
            word = x.text
            word = word.strip()
            words.append(word)
        print(f"\n{language2} Translations:")
        f.write(f"{language2} Translations:\n")
        for word in words[0:1]:
            f.write(word + '\n\n')
            print(word)

        final_sentences = []
        examples = soup.find('section', {'id': "examples-content"}).find_all('span', {'class': 'text'})
        for x in examples:
            sentence = x.text.strip()
            final_sentences.append(sentence)
        print(f"\n{language2} Examples:")
        f.write(f"{language2} Examples:\n")
        for sentence in final_sentences[0:2]:
            f.write(sentence + '\n')
            print(sentence)
        f.write('\n')
    else:
        print('sheesh')


if __name__ == '__main__':
    print("Hello, you're welcome to the translator. Translator supports: ")
    for counter, language in enumerate(languages):
        print(f"{counter + 1}. {language}")
    print("Type the number of your language:")
    langX = int(input())
    print("Type the number of language you want to translate to:")
    langY = int(input())
    print("Type the word you want to translate:")
    word = input()
    f = open(f"{word}.txt", "w")
    if langY == 0:
        for counter, language in enumerate(languages):
            translate(languages[langX - 1], language, word)
    else:
        translate(languages[langX - 1], languages[langY - 1], word)
    f.close()