import typer
import string

def typerTwo( name: str ):

    naMe = name.capitalize()
    print(f"Welcome Home : {naMe}")


if __name__ == "__main__":
    namae = input("Enter Name : ")
    typerTwo(namae)


#use typer ./typerTwo.py run enos     to test 
