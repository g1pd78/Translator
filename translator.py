import requests
from bs4 import BeautifulSoup
import sys

languages = ['Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese', 'Dutch', 'Polish', 'Portuguese',
             'Romanian', 'Russian', 'Turkish']
args = sys.argv


def translate(language1, language2, word_to_translate):
    if language1 == language2:
        return None
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(f"https://context.reverso.net/translation/"
                            f"{language1.lower()}-{language2.lower()}/{word_to_translate}", headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    words = []
    if response.status_code == 200:
        trans_words = soup.find('div', {'id': "translations-content"}).find_all('a')
        for x in trans_words:
            temp_word = x.text
            temp_word = temp_word.strip()
            words.append(temp_word)
        print(f"\n{language2} Translations:")
        f.write(f"{language2} Translations:\n")
        if len(words) == 0:
            print(f"Sorry, unable to find {word_to_translate}")
            return False
        for temp_word in words[0:1]:
            f.write(temp_word + '\n\n')
            print(temp_word)

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
        print(f"Sorry, unable to find {word_to_translate}")
        return False
        print(response.status_code)
        print('Something wrong with your internet connection')
        return False


def check_is_valid(lang):
    if lang.capitalize() not in languages:
        print(f"Sorry, the program doesn't support {lang}")
        return False
    else:
        return True


if __name__ == '__main__':
    langY = ''
    langX = ''
    word = ''
    checker = True
    if len(args) == 1:
        print("Hello, you're welcome to the translator. Translator supports: ")
        for counter, language in enumerate(languages):
            print(f"{counter + 1}. {language}")
        print("Type the number of your language:")
        langX = int(input())
        print("Type the number of language you want to translate to:")
        langY = int(input())
        if 0 <= langY <= len(languages) and 0 < langX <= len(languages):
            pass
        else:
            checker = False
        print("Type the word you want to translate:")
        word = input()
    else:
        if check_is_valid(args[1]) and (args[2] == 'all' or check_is_valid(args[2])):
            langX = languages.index(args[1].capitalize()) + 1
            if args[2] == 'all':
                langY = 0
            else:
                langY = languages.index(args[2].capitalize()) + 1
            word = args[3]
        else:
            checker = False

    if checker:
        f = open(f"{word}.txt", "w")
        if langY == 0:
            for counter, language in enumerate(languages):
                translate(languages[langX - 1], language, word)

        else:
            translate(languages[langX - 1], languages[langY - 1], word)
        f.close()
