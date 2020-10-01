from typing import Optional, Dict, List
from loguru import logger
from ciphey.iface import ParamSpec, Config, T, U, Decoder, registry


@registry.register_multi((str, str), (bytes, bytes))
class Braille(Decoder[T, U]):
    UNICODE_STRING = "⠀⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿"
    C_STRING = " A1B'K2L@CIF/MSP\"E3H9O6R^DJG>NTQ,*5<-U8V.%[$+X!&;:4\\0Z7(_?W]#Y)="
    translation = str.maketrans(UNICODE_STRING, C_STRING)

    GRADE_II = {'⠁':'a',
                '⠃':'but',
                '⠉':'can',
                '⠙':'do',
                '⠑':'every',
                '⠋':'from',
                '⠛':'go',
                '⠓':'have',
                '⠚':'just',
                '⠅':'knowledge',
                '⠇':'like',
                '⠍':'more',
                '⠝':'not',
                '⠏':'people', 
                '⠟':'quite', 
                '⠗':'rather', 
                '⠎':'so', 
                '⠞':'that', 
                '⠌':'still',
                '⠥':'us',
                '⠧':'very',
                '⠭':'it',
                '⠽':'you',
                '⠵':'as',
                '⠡':'child',
                '⠩':'shall',
                '⠹':'this',
                '⠱':'which',
                '⠳':'out',
                '⠺':'will',
                '⠆':'be',
                '⠒':'con',
                '⠲':'dis',
                '⠢':'enough',
                '⠖':'to',
                '⠶':'were',
                '⠦':'his',
                '⠔':'in',
                '⠴':'by/was',
                '⠤':'com'
                }



    def decode(self, text: T) -> Optional[U]:
        for c in text:
            if str(c) in self.UNICODE_STRING:
                continue
            logger.trace(f"Non-Braille glyph '{c}' found")
            return None

        return text.translate(self.translation)

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