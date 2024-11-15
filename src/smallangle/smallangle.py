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
)
def sin(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@start_list.command()
@click.option(
    "-n",
    "--number",
    default=10,
)
def tan(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)

if __name__ == "__main__":
    start_list()