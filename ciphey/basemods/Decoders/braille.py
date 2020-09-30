from typing import Optional, Dict, List

from ciphey.iface import ParamSpec, Config, T, U, Decoder, registry


@registry.register_multi((str, str), (bytes, bytes))
class Braille(Decoder[T, U]):
    BRAILLE_GLYPH = ['⠀','⠮','⠐','⠼','⠫','⠩','⠯','⠄','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌','⠴','⠂','⠆','⠒','⠲','⠢',
                    '⠖','⠶','⠦','⠔','⠱','⠰','⠣','⠿','⠜','⠹','⠈','⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚','⠅',
                    '⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞','⠥','⠧','⠺','⠭','⠽','⠵','⠪','⠳','⠻','⠘','⠸']
    ASCII_GLYPH = [' ','!','"','#','$','%','&','','(',')','*','+',',','-','.','/',
                    '0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@',
                    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
                    'r','s','t','u','v','w','x','y','z','[','\\',']','^','_']
    BRAILLE_CODE_DICT_INV = dict(zip(BRAILLE_GLYPH, ASCII_GLYPH))    

    def decode(self, text: T) -> Optional[U]:
        result = []
        for char in text:
            result.append(self.BRAILLE_CODE_DICT_INV[char])

        return ''.join(result)

    @staticmethod
    def priority() -> float:
        return 0.05

    def __init__(self, config: Config):
        super().__init__(config)

    @staticmethod
    def getParams() -> Optional[Dict[str, ParamSpec]]:
        """The parameters this returns"""
        pass

    @staticmethod
    def getTarget() -> str:
        return "braille"