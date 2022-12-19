# maxconsole/maxconsole.py
from rich.console import Console
from rich.color import Color
from rich.theme import Theme
from rich.traceback import install as install_traceback
import threading

__version__ = '0.5.0'



# MAX_THEME = Theme(
#     {
#         "magenta": "#ff00ff",  #         #ff00ff
#         "purple": "#af00ff",  # P        #af00ff
#         "blue_violet": "#5f00ff",  #       #5f00ff
#         "blue": "bold #0000FF",  #       #0000ff
#         "cornflower_blue": "#249df1",  #    #249df1
#         "cyan": "#00ffff",  #            #00ffff
#         "green": "#00ff00",  #           #00ff00
#         "yellow": "#ffff00",  #          #ffff00
#         "orange": "#ff8800",  #          #ff8800
#         "red": "#ff0000",  #             #ff0000
#         "white": "#ffffff",  #           #ffffff
#         "light_grey": "#e2e2e2",  #        #e2e2e2
#         "grey": "#808080",  #            #808080
#         "dark_grey": "#2e2e2e",  #         #2e2e2e
#         "black": "#000000",  #           #000000
#         "debug": "bold bright_cyan",  #        #00ffff
#         "info": "bold cornflower_blue",  #      #249df1
#         "success": "bold bright_green",  #     #00ff00
#         "warning": "bold bright_yellow",  #    #ffff00
#         "error": "bold orange1",  #            #ff8800
#         "critical": "bold reverse #aa0000",#     #ff0000
#         "value": "bold bright_white",  #       #ffffff
#         "title": "bold purple",#             #af00ff
#         "key": "italic magenta",#            #ff00ff
#         "lines": "blue_violet",  #             #5f00ff
#     }
# )
class Singleton(type):
    _instance_lock = threading.Lock()
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            with Singleton._instance_lock:
                cls.__instance = super().__call__(*args, **kwargs)
                return cls.__instance
        else:
            return cls.__instance

class MaxConsole(Console, metaclass=Singleton):
    """A custom themed console class that inherits from rich.console.Console"""
    theme: Theme = Theme.read('max_theme.ini')

    def __init__ (self, theme: Theme = Theme.read('max_theme.ini'), *args, **kwargs):
        super().__init__(*args, **kwargs, theme=theme)
        install_traceback(console=self)

    def __call__(self, *args, **kwargs):
        return self


if __name__ == "__main__":
    console = MaxConsole()
    console.print("Hello, world!")
    assert isinstance(console, MaxConsole), f"Expected MaxConsole, got {type(console)}"