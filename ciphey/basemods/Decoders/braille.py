from typing import Optional, Dict, List
from loguru import logger
from ciphey.iface import ParamSpec, Config, T, U, Decoder, registry


@registry.register_multi((str, str), (bytes, bytes))
class Braille(Decoder[T, U]):
    UNICODE_STRING = "⠀⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿"
    C_STRING = " a1b'k2l@cif/msp\"e3h9o6r^djg>ntq,*5<-u8v.%[$+x!&;:4\\0z7(_?w]#y)="
    translation = str.maketrans(UNICODE_STRING, C_STRING)

    def decode(self, text: T) -> Optional[U]:
        for c in text:
            if c == ' ' or str(c) in self.UNICODE_STRING:
                continue
            return None

        translated = text.translate(self.translation)[::-1]
        wordArr = []

        for word in translated.split(' '):
            # if two commas are infront of word, capitalize word and remove comma
            if (word.find(',,') != -1):
                wordArr.append(word.replace(',,','').upper())
            else:
                wordArr.append(word)

        string = ' '.join(wordArr)
        skip = False
        result = ""

        for i in range(0, len(string)):
            # check if comma is infront of letter, and if so captialize the letter
            if skip:
                skip = False
                continue
            if i < len(string) - 1 and string[i] == ',' and string[i + 1].isalpha():
                result += string[i + 1].capitalize()
                skip = True
            else:
                result += string[i]
        return result

    @staticmethod
    def priority() -> float:
        return 0.05

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        pass

    @staticmethod
    def getTarget() -> str:
        return "braille"
