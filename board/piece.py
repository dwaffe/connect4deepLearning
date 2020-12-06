class Piece:
    def __init__(self, sign: str, color: str = 'white') -> None:
        self._sign = sign
        self._color = color

    def get_sign(self):
        return self._sign

    def get_color(self) -> str:
        return self._color
    