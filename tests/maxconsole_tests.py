import maxconsole as mc
from rich.color import ANSI_COLOR_NAMES
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table, Column
from rich import inspect


color_sample = '◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎◼︎'

def test_maxconsole():
    console = mc.MaxConsole()

    theme_color_test = Table(
        title="MaxConsole Theme Test",
        show_header=True,
        show_lines=False,
        show_edge=False,
        width=80,
        padding=(1,1)
    )
    theme_color_test.add_column("Color", justify="left", no_wrap=True, ratio=1)
    theme_color_test.add_column("Color Example", justify="center", no_wrap=True, ratio=3)
    theme_color_test.add_row("magenta", f"[magenta]{color_sample}[/]")
    theme_color_test.add_row("purple", f"[purple]{color_sample}[/]")
    theme_color_test.add_row("blue_violet", f"[blue_violet]{color_sample}[/]")
    theme_color_test.add_row("blue", f"[blue]{color_sample}[/]")
    theme_color_test.add_row("cornflower_blue", f"[cornflower_blue]{color_sample}[/]")
    theme_color_test.add_row("cyan", f"[cyan]{color_sample}[/]")
    theme_color_test.add_row("green", f"[green]{color_sample}[/]")
    theme_color_test.add_row("yellow", f"[yellow]{color_sample}[/]")
    theme_color_test.add_row("orange", f"[orange]{color_sample}[/]")
    theme_color_test.add_row("red", f"[red]{color_sample}[/]")
    theme_color_test.add_row("white", f"[white]{color_sample}[/]")
    theme_color_test.add_row("light_grey", f"[light_grey]{color_sample}[/]")
    theme_color_test.add_row("grey", f"[grey]{color_sample}[/]")
    theme_color_test.add_row("dark_grey", f"[dark_grey]{color_sample}[/DARK_GREY]")
    theme_color_test.add_row("black", f"[black]{color_sample}[/]")
    


    try:
        console.clear()
        console.rule(title="MaxConsole Import Test", style="#00ffff",)
        console.print()
        console.print(
            theme_color_test,
            justify="center",
        )
        console.print()
        console.print()
        colors_correct = Confirm.ask("Are the above colors correct?", console=console, default='y', choices=['y', 'n'])
        if colors_correct:
            console.print(
                Panel(
                    "[bold #00ff00]Congratulations![/] You have successfully installed [italic #ff00ff]MaxConsole[/]!",
                    title="[bold #ffffff]MaxConsole Import Test[/]",
                    style="#00ffff",
                    border_style="#ff00ff"
                    
                ),
                justify="center",
            )
    except Exception as e:
        inspect(e)
    
if __name__ == "__main__":
    test_maxconsole()
