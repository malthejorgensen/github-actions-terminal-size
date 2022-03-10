import fcntl
import os
import shutil
import struct
import termios
from subprocess import check_output

# FROM: https://github.com/pytest-dev/py/blob/master/py/_io/terminalwriter.py#L39-L58
print(f'shutil.get_terminal_size(): {shutil.get_terminal_size()}')

try:
    call = fcntl.ioctl(1, termios.TIOCGWINSZ, b'\000' * 8)
    height, width = struct.unpack("hhhh", call)[:2]
    print(f'termios.TIOCGWINSZ: (height: {height}, width: {width})')
except:
    pass

print(f'COLUMNS environment variable: {os.environ.get("COLUMNS")}')


# FROM: https://github.com/sindresorhus/term-size/blob/62297b0a238ed734459f89d1577a6450cb6f1f38/index.js
try:
    size = check_output('resize -u').decode('ascii').strip()

    print(f'`resize -u`: {size}')
except:
    pass

try:
    columns = check_output(['tput', 'cols']).decode('ascii').strip()
    rows = check_output(['tput', 'lines']).decode('ascii').strip()
    print(f'`tput lines`: {columns}')
    print(f'`tput rows`: {rows}')
except:
    raise

# FROM: https://stackoverflow.com/a/26855761/118608
try:
    size = check_output(['stty', 'size']).decode('ascii').strip()
    print(f'`stty size`: {size}')
except:
    pass
