import typer
import subprocess

app =typer.Typer()
#k = app.__doc__

@app.command("job")
def jobs(job:str):
    subprocess.run("ps")
    #typer.echo(f"Running task: {task}")
@app.command("qr")
def jobs(qr:str, link:str = typer.Argument):
    qrcommand = ["qrencode",  "-o", "test.png", link ]
    subprocess.run(qrcommand)

@app.command("user")
def users(user:str):
    subprocess.run("whoami")
    #typer.echo(f"output for cmds user and option {user}")
if __name__ == "__main__":
    app()
    #print(k)
    #help(typer.Typer)


