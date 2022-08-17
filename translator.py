import random

from colorama import Fore, init
from deep_translator import GoogleTranslator

init()

LANGUAGES = {
    abbrev: fullname
    for fullname, abbrev in GoogleTranslator().get_supported_languages(True).items()
}

# Number of languages to select
NUM_LANGS = 10
ENGLISH = "en"

# Pick some random languages
selected_langs = [random.choice(list(LANGUAGES.keys())) for _ in range(NUM_LANGS)]

text = input(
    f"{Fore.LIGHTGREEN_EX}[*] Enter your phrase (multiple lines, press Control+C to finish):{Fore.LIGHTRED_EX}\n"
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
print(f"Original text:\n{Fore.LIGHTRED_EX}{original_text}{Fore.LIGHTYELLOW_EX}")
print(f"Translated text:\n{Fore.LIGHTRED_EX}{text}{Fore.LIGHTYELLOW_EX}")
print(("=" * 50) + "\nLanguages used, in order of translation:" + Fore.LIGHTRED_EX)

print("\n".join([LANGUAGES[abbrev].title() for abbrev in selected_langs]))

print(Fore.LIGHTYELLOW_EX + ("=" * 50))
