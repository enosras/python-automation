#rich is equivalent of eza or glow, makes your output pretty

import subprocess
from rich import print
from rich.progress import track
#for task in track(range(1), description="Processing.."):
for task in track(range(1), description="Processing.."):
    result = subprocess.run(["tree"], capture_output=True, text=True, check=True)
    print("Stdout:", result.stdout)
    print("Stderr:", result.stderr)

    # Execute a command with shell=True (use with caution for security)
    # This allows the shell to interpret the command string
    result_shell = subprocess.run("echo 'Hello from shell!'", shell=True, capture_output=True, text=True)
    print("Shell output:", result_shell.stdout)