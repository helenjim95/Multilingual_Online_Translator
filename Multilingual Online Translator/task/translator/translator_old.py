# import requests as requests
# from bs4 import BeautifulSoup
#
# translation = []
# source_sentence_list = []
# target_sentence_list = []
# from_langauge = ""
# to_langauge = ""
# language_dictionary = [{1, "Arabic"}, {2, "German"}, {3, "English"}, {4, "Spanish"}, {5, "French"},
#                        {6, "Hebrew"}, {7, "Japanese"}, {8, "Dutch"}, {9, "Polish"}, {10, "Portuguese"},
#                        {11, "Romanian"}, {12, "Russian"}, {13, "Turkish"}]
# language_index = 0
# num_language = 0
# word = ""
#
#
#
# def print_result():
#     global from_language
#     global translation
#     global source_sentence_list
#     global target_sentence_list
#     print(f"{from_language.capitalize()} Translations")
#     for i in range(5):
#         print(translation[i])
#     print()
#     print(f"{from_language.capitalize()} Examples")
#     for i in range(5):
#         print(source_sentence_list[i])
#         print(target_sentence_list[i])
#         print()
#
#
# def print_welcome_message():
#     print("""Hello, welcome to the translator. Translator supports:
#     1. Arabic
#     2. German
#     3. English
#     4. Spanish
#     5. French
#     6. Hebrew
#     7. Japanese
#     8. Dutch
#     9. Polish
#     10. Portuguese
#     11. Romanian
#     12. Russian
#     13. Turkish
#     """)
#
#
# def take_input():
#     global language_index
#     global num_language
#     global word
#     print("Type the number of your language:")
#     language_index = int(input())
#     print("Type the number of language you want to translate to: ")
#     num_language = int(input())
#     print('Type the word you want to translate:')
#     word = input()
#
# def map_index_to_language():
#     global language_dictionary
#     global language_index
#     if
#
#
# print_welcome_message()
# take_input()
#
# print(f'You chose "{language}" as a language to translate "{word}".')
#
# if language == "fr":
#     from_language = "english"
#     to_language = "french"
# else:
#     from_language = "french"
#     to_language = "english"
# reverso_url = f"https://context.reverso.net/translation/{from_language}-{to_language}/{word}"
# headers = {'User-Agent': 'Mozilla/5.0'}
# r = requests.get(reverso_url, headers=headers)
# status_code = r.status_code
# if status_code == 200:
#     print(status_code, "OK")
# soup = BeautifulSoup(r.content, 'html.parser')
# trans_tags = soup.find_all('a', {"class": "translation"})
# for tran in trans_tags:
#     trans_word = tran.text.strip()
#     translation.append(trans_word)
# translation.remove("Translation")
#
# source_sentence_tags = soup.find_all(class_="src ltr")
# target_sentence_tags = soup.find_all(class_="trg ltr")
#
# for tags in source_sentence_tags:
#     source_sentence = tags.text.strip()
#     source_sentence_list.append(source_sentence)
#
# for tags in source_sentence_tags:
#     target_sentence = tags.text.strip()
#     target_sentence_list.append(target_sentence)
#
# print_result()
#
