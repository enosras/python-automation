#!/bin/bash
set -euo pipefail

if [[ -f globs.txt ]]; then
ls *.py >> globs.txt
echo "append success"
else
ls *.py > globs.txt
echo "create success"
fi
