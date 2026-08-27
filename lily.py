import sys
import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align

console = Console()

# Frame 1: Kuncup
FRAME_1 = """
       [pink1]  .  [/pink1]
       [pink1] /|\\ [/pink1]
       [magenta] ( ) [/magenta]
       [green]  |  [/green]
       [green]  |  [/green]
"""

# Frame 2: Mulai Terbuka
FRAME_2 = """
       [pink1]  .::.  [/pink1]
     [magenta] .'  |  '. [/magenta]
    [deep_pink1](   [yellow]*[/yellow]   )[/deep_pink1]
     [magenta] '.  |  .' [/magenta]
       [green]  \\|/  [/green]
       [green]   |   [/green]
       [green]  /|   [/green]
"""

# Frame 3: Lily Smooth & Detail (Braille Arts)
FRAME_3 = """
         [light_pink1]⢀⣀[/light_pink1]   [light_pink1]⣀⡀[/light_pink1]
      [pink1]⢀⡴⠋[/pink1]   [bold white]⠘[/bold white]   [pink1]⠉⠳⡀[/pink1]
    [pink1]⢠⠞[/pink1]     [bold white]⡇[/bold white]     [pink1]⠙⣄[/pink1]
   [magenta]⡞[/magenta]   [yellow]⠦⠤[/yellow]  [bold white]⢸[/bold white]  [yellow]⠤⠴[/yellow]   [magenta]⢳[/magenta]
  [deep_pink1]⡇[/deep_pink1]    [yellow]⢀⠔[/yellow]  [bold white]⢸[/bold white]  [yellow]⠢⣀[/yellow]    [deep_pink1]⢸[/deep_pink1]
  [deep_pink1]⠘⣄[/deep_pink1]   [yellow]⠉[/yellow]   [bold white]⢸[/bold white]   [yellow]⠉[/yellow]   [deep_pink1]⣠⠞[/deep_pink1]
    [pink1]⠙⢦⣀[/pink1]   [bold white]⡇[/bold white]   [pink1]⣀⡴⠋[/pink1]
       [green]⠉⠓[bold white]⡇[/bold white]⠚⠉[/green]
         [green]│[/green]
      [dark_green]⣞⠢[/dark_green][green]│[/green]
      [green]│[/green][dark_green]⠔⣳[/dark_green]
         [green]│[/green]
"""

def animate():
    console.clear()
    
    # Animasi 1: Kuncup
    console.print(Align.center(Panel(FRAME_1, border_style="dim magenta", title="[dim]Growing...[/dim]")))
    time.sleep(0.8)
    console.clear()
    
    # Animasi 2: Mekar Separuh
    console.print(Align.center(Panel(FRAME_2, border_style="magenta", title="[dim]Blooming...[/dim]")))
    time.sleep(0.8)
    console.clear()

    # Animasi 3: Lily Sempurna
    title = Text("🌸 Girlfriend Day Special 🌸", style="bold hot_pink")
    panel = Panel(
        Align.center(FRAME_3),
        title=title,
        subtitle="[italic pink1]A blooming lily for you[/italic pink1]",
        border_style="bright_magenta",
        padding=(1, 4)
    )
    console.print(Align.center(panel))

if __name__ == "__main__":
    animate()