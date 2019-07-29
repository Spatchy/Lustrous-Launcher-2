class InvalidThemeException(Exception):
    string = "The loaded theme version is higher than the engine version"
    pass
