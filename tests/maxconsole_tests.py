from maxconsole import MaxConsole
from rich.panel import Panel

def test_maxconsole():
    console = MaxConsole()
    assert isinstance(console, MaxConsole), f"Expected MaxConsole, got {type(console)}"
    console.print(
        Panel(
            "Congratulations! You have successfully installed [bold magenta]MaxConsole[/bold magenta]!  "
        )
    )
    
if __name__ == "__main__":
    test_maxconsole()
