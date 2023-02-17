import sys

class ColourPrint:

    _HEADER = '\033[95m'
    _OKBLUE = '\033[94m'
    _OKCYAN = '\033[96m'
    _OKGREEN = '\033[92m'
    _WARNING = '\033[93m'
    _FAIL = '\033[91m'
    _ENDC = '\033[0m'
    _BOLD = '\033[1m'
    _UNDERLINE = '\033[4m'

    def __init__(self, col_ok=_OKGREEN, col_fail=_FAIL, col_warn=_WARNING):
        self._ok = col_ok
        self._fail = col_fail
        self._warning = col_warn

    def ok(self, s, file=sys.stdout, end='\n'):
        print(f'{self._ok}{s}{self._ENDC}', end=end, file=file)

    def warning(self, s, file=sys.stdout, end='\n'):
        print(f'{self._warning}{s}{self._ENDC}', end=end, file=file)
    
    def fail(self, s, file=sys.stdout, end='\n'):
        print(f'{self._fail}{s}{self._ENDC}', end=end, file=file)
    
    def bold(self, s, file=sys.stdout, end='\n'):
        print(f'{self._BOLD}{s}{self._ENDC}', end=end, file=file)

    def underline(self, s, file=sys.stdout, end='\n'):
        print(f'{self._UNDERLINE}{s}{self._ENDC}', end=end, file=file)

    def header(self, s, file=sys.stdout, end='\n'):
        print(f'{self._HEADER}{s}{self._ENDC}', end=end, file=file)
