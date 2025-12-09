import typer
import subprocess

app =typer.Typer()
#k = app.__doc__

@app.command()
def jobs(task:str):
    typer.echo(f"Running task: {task}")

@app.command()
def users(user:str):
    #output = subprocess("finger")
    typer.echo(f"{user}")

if __name__ == "__main__":
    app()
    #print(k)
    #help(typer.Typer)


