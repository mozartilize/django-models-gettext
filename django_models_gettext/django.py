class Translatable:
    pass


class TranslationOptions:
    def __init__(self, fields: tuple[str, ...]) -> None:
        self.fields = fields