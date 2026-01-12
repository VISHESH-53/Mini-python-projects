from spellchecker import SpellChecker

class SpellCheckApp:
    def __init__(self):
        self.spellchecker = SpellChecker()
        self.spellchecker.word_frequency.add("this")

    def check_spelling(self, text):
        words = text.split()
        corrected_words = []

        for word in words:
            lw = word.lower()

            # Explicit fix for common case
            if lw == "ths":
                correction = "this"
            elif lw not in self.spellchecker:
                correction = self.spellchecker.correction(lw)
            else:
                corrected_words.append(word)
                continue

            # Preserve capitalization
            if word[0].isupper():
                correction = correction.capitalize()

            print(f"Correcting '{word}' to '{correction}'")
            corrected_words.append(correction)

        return ' '.join(corrected_words)



    def run(self):
        print("Welcome to the Spell Check Application!")
        while True:
            user_input = input("Enter text to check (or type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Exiting the application. Goodbye!")
                break
            corrected_text = self.check_spelling(user_input)
            print(f"Corrected Text: {corrected_text}")

if __name__ == "__main__":
    SpellCheckApp().run()
