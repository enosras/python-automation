# rich is equivalent of eza or glow, makes your output pretty

import subprocess

from rich import print
from rich.progress import track


def final_execute(one_var, two_var):
    command = ["hyperfine", one_var, two_var]
    for task in track(range(1), description="Processing.."):
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
        )
        print("Stdout:", result.stdout)
        # print("Stderr:", result.stderr)
        # Execute a command with shell=True (use with caution for security)
        # This allows the shell to interpret the command strin
        # this here is just for simple tests before adding constraints
        # result_shell = subprocess.run(
        #     "echo 'Hello from shell!'", shell=True, capture_output=True, text=True
        # )
        # print("Shell output:", result_shell.stdout)


if __name__ == "__main__":
    print("------- enjoy yourself ------- ")
    print("-------------------------------")
    first_cmd = input("Enter first command : ")
    second_cmd = input("enter second to compare : ")
    final_execute(first_cmd, second_cmd)
