import typer
import subprocess

app =typer.Typer()

@app.command()
def run(task:str):
    typer.echo(f"Running task: {task}")
def run(user:str):
    typer.echo(f"{subprocess("finger")}")
if __name__ == "__main__":
    app()
