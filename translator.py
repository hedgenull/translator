# Imports
import random

import art
from colorama import Fore, init
from deep_translator import GoogleTranslator

# Initialize colorama, print banner
init()
print(Fore.LIGHTBLUE_EX)
art.tprint("TRANSLATOR")
print(f"{Fore.LIGHTYELLOW_EX}----- A New Kind of Obfuscation -----")
print("----- By Hedge Fleming <hedgefleming@gmail.com> -----")
print("----- Copyright (C) 2022. All Rights Reserved. -----")

# Dictionary of language codes and full names
LANGUAGES = {
    abbrev: fullname
    for fullname, abbrev in GoogleTranslator().get_supported_languages(True).items()
}

# Number of languages to select
NUM_LANGS = 10
ENGLISH = "en"

# Pick some random languages
selected_langs = [random.choice(list(LANGUAGES.keys())) for _ in range(NUM_LANGS)]

# Get the user's input
text = input(
    f"{Fore.LIGHTGREEN_EX}[*] Enter your text (multiple lines, press Control+C to finish):{Fore.LIGHTRED_EX}\n"
)

while True:
    try:
        text += input()
    except KeyboardInterrupt:
        break

original_text = text

print(f"{Fore.LIGHTGREEN_EX}\n[*] Ok! Translating...")

translator = GoogleTranslator()

text = translator.translate(text)

last = ENGLISH
for language in selected_langs:
    text = GoogleTranslator(source=last, target=language).translate(text)
    last = language

text = GoogleTranslator(source=last, target=ENGLISH).translate(text)

print("[*] All done!")

print(Fore.LIGHTYELLOW_EX + ("=" * 50))
print(f"Original text:\n{Fore.LIGHTRED_EX}")
print(original_text + Fore.LIGHTYELLOW_EX)
print(f"Translated text:\n{Fore.LIGHTRED_EX}")
print(text + Fore.LIGHTYELLOW_EX)

print(("=" * 50) + "\nLanguages used, in order of translation:" + Fore.LIGHTRED_EX)

print("\n".join([LANGUAGES[abbrev].title() for abbrev in selected_langs]))

print(Fore.LIGHTYELLOW_EX + ("=" * 50))
