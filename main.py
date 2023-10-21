
from string import ascii_uppercase

class Alphabet:
    def __init__(self, lang, letters_str):
        self.lang = lang
        self.letters = list(letters_str)


    def print(self):
        print(self.letters)

    def letters_num(self):
        print(len(self.letters))



class EngAlphabet(Alphabet):

    __letters_num = 26


    def __init__(self):
        super().__init__('En', ascii_uppercase )

    def  is_en_letter(self, letter):
        if letter.upper() in self.letters:
            return True
        return False
    
    def letters_num(self):
        return EngAlphabet.__letters_num
    
    @staticmethod
    def example():
        print('Eng Example: This is example.')


if __name__ == '__main__':
    eng_alphabet = EngAlphabet()
    eng_alphabet.print()
    print(eng_alphabet.letters_num())
    print(eng_alphabet.is_en_letter('F'))
    print(eng_alphabet.is_en_letter('f'))
    print(eng_alphabet.is_en_letter('Щ'))
    print(eng_alphabet.is_en_letter('щ'))
    EngAlphabet.example()