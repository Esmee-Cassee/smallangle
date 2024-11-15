import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def start_list():
    pass

@start_list.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="The amount of steps in between 0 and 2 pi",
    show_default=True,
)
def sin(number):
    """Takes the sin of {number} numbers between 0 and 2 pi.
    And makes a list, of the float value and the corresponding sin(value).  
    """    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@start_list.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="The amount of steps in between 0 and 2 pi",
    show_default=True,
)
def tan(number):
    """Takes the tan of {number} numbers between 0 and 2 pi.
     And makes a list, of the values (float) and the corresponding tan(value) (float). 
    """    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)

if __name__ == "__main__":
    start_list()