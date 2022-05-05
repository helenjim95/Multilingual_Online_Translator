import os
import re
import requests
from bs4 import BeautifulSoup
import data
import sys

class Translator:

    def __init__(self, lang_from=None, lang_to=None, word=None):
        self.lang_from = lang_from
        self.lang_to = lang_to
        self.word = word
        self.headers = data.headers
        self.output_string = []
        if not lang_from or not lang_to or not word:
            self.get_input()
        if self.lang_to != "All":
            self.link = f"{data.link}/{self.lang_from.lower()}-{self.lang_to.lower()}/{self.word}"
            self.translations = None
            self.examples = []
            self.get_info()
        elif self.lang_to == "All":
            for i in range(len(data.lang_dict)):
                self.lang_to = data.lang_dict.get(i + 1)
                self.link = f"{data.link}/{self.lang_from.lower()}-{self.lang_to.lower()}/{self.word}"
                self.translations = None
                self.examples = []
                self.get_info()
        self.filename = f"{self.word}.txt"
        self.filepath = f"{os.getcwd()}/{self.filename}"
        self.create_file()
        self.update_file()

    def get_input(self):
        """sets language and word if not specified"""
        while True:
            lang_from = sys.argv[1].capitalize()
            lang_to = sys.argv[2].capitalize()
            try:
                assert lang_from in data.lang_list
                self.lang_from = lang_from
            except AssertionError:
                print(f"Sorry, the program doesn't support {lang_from}")
                exit()
            try:
                assert lang_to in data.lang_list
                self.lang_to = lang_to
                self.word = sys.argv[3]
                if lang_to != "All":
                    print(f'You chose "{self.lang_to}" as the language to translate "{self.word}" to.')
                break
            except AssertionError:
                print(f"Sorry, the program doesn't support {lang_to}")
                exit()


    def get_info(self):
        s = requests.Session()
        response = s.get(self.link, headers=self.headers)
        if response.status_code == 200:
            print(f"{response.status_code} OK\n")
        elif response.status_code == 404:
            print(f"Sorry, unable to find {self.word}")
            exit()
        else:
            print("Something wrong with your internet connection")
            exit()

        soup = BeautifulSoup(response.content, "html.parser")
        if self.lang_to != "Arabic" and self.lang_to != "Hebrew":
            find_translation = soup.find_all('a', class_=re.compile("translation ltr dict"), limit=1)
            find_example_src = [src.text.strip() for src in soup.find_all('div', class_=re.compile("src ltr"), limit=1)]
            find_example_trg = [trg.text.strip() for trg in soup.find_all('div', class_=re.compile("trg ltr"), limit=1)]
        else:
            find_translation = soup.find_all('a', class_=re.compile("translation rtl dict"), limit=1)
            find_example_src = [src.text.strip() for src in soup.find_all('div', class_=re.compile("src ltr"), limit=1)]
            find_example_trg = [trg.text.strip() for trg in soup.find_all('div', class_=re.compile("trg rtl"), limit=1)]
        self.translations = [translation.text.strip() for translation in find_translation]
        for (src, trg) in zip(find_example_src, find_example_trg):
            self.examples.append((src, trg))
        # print info
        self.output_string.append(f"{self.lang_to} Translations:")
        print(f"{self.lang_to} Translations:")
        for trans in self.translations:
            self.output_string.append(trans)
            print(trans)
        print()
        self.output_string.append(f"{self.lang_to} Example:")
        print(f"{self.lang_to} Example:")
        for src, trg in self.examples:
            self.output_string.append(src)
            self.output_string.append(trg)
            print(src)
            print(trg)


    # Save results of the search to a file named word.txt,
    # where word is the word that was being translated.
    def create_file(self):
        with open(self.filepath, 'w', encoding="utf-8") as file:
            file.write("")

    def update_file(self):
        with open(self.filepath, 'a', encoding="utf-8") as file:
            file.seek(0)
            print("\n".join(self.output_string))
            # print string from list
            file.write("\n".join(self.output_string))


if __name__ == "__main__":
    translator = Translator()
