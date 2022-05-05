# possible languages
lang_dict = {1: "Arabic", 2: "German", 3: "English", 4: "Spanish", 5: "French",
             6: "Hebrew", 7: "Japanese", 8: "Dutch", 9: "Polish", 10: "Portuguese",
             11: "Romanian", 12: "Russian", 13: "Turkish"}
lang_list = ["Arabic", "German", "English", "Spanish", "French",
               "Hebrew", "Japanese", "Dutch", "Polish", "Portuguese",
               "Romanian", "Russian", "Turkish", "All"]

# url
link = "https://context.reverso.net/translation"
# headers
headers = {'User-Agent': "Mozilla/5.0"}
# messages
msg_lang_from_index = """Hello, welcome to the translator. Translator supports:
1. Arabic
2. German
3. English
4. Spanish
5. French
6. Hebrew
7. Japanese
8. Dutch
9. Polish
10. Portuguese
11. Romanian
12. Russian
13. Turkish
Type the number of your language:
"""

msg_lang_to_index = "Type the number of a language you want to translate to or '0' to translate to all languages:"
msg_word = 'Type the word you want to translate:'
