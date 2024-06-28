import sys
import os

class Error:
    class BaseError(Exception):
        def __init__(self, msg, exit_code=1):
            super().__init__(msg)
            self.exit_code = exit_code
            self.msg = msg

            self.print_error()

        def print_error(self): print(self.msg)

        def exit_program(self): sys.exit(self.exit_code)

    class FileNotFound(BaseError):
        def __init__(self, path):
            msg = f"File Not found at {path}"
            super().__init__(msg, exit_code=0)
            self.exit_program()
    
    class FileIO(BaseError):
        def __init__(self):
            msg = "Unable to Read File"
            super().__init__(msg, exit_code=0)
            self.exit_program()

    class ImproperUsage(BaseError):
        def __init__(self):
            msg = "USAGE: pyhton cue.py <path_to_cue>"
            super().__init__(msg, exit_code=1)
            self.exit_program()

    class InvalidFileExtension(BaseError):
        def __init__(self, ext):
            msg = f"Invalid Extension, Expected '.cue', got '.{ext}'"
            super().__init__(msg, exit_code=2)


def read_cue(path):
    cue_chk = os.path.splitext(path)[1][1:].lower().strip()
    if cue_chk != 'cue': raise Error.InvalidFileExtension(cue_chk)

    try: 
        with open(path, 'r') as f: return f.read()

    except FileNotFoundError: raise Error.FileNotFound(path)
    except IOError: raise Error.FileIO()
        
if __name__ == "__main__":
    if len(sys.argv) != 2: raise Error.ImproperUsage()

    filepath = sys.argv[1]

    try:
        data = read_cue(filepath)
        print(data)
        # TODO: Read Mix Title, date
        # TODO: Main Loop for tracks

    except Error.BaseError: pass
    