# About

ByteX is a simple programming language written in Python. You can use it as you wish - e.g. for education.

# Installation

## Manual

1. Download and extract archive
2. Open folder with ByteX and run in terminal:
```
python main.py
```
3. **Congratulations!**

## Automatic

_Soon..._

> **Note**: make sure to install Python and add it to PATH

# Documentation

See [wiki](https://github.com/Cat0125/ByteX/wiki)

# Examples

More examples in [scripts/examples](https://github.com/Cat0125/ByteX/tree/main/scripts/examples) folder.

> **Note**: some examples can not work with updates.
You can notify me [here](https://github.com/Cat0125/ByteX/issues)
or find **actual** examples in [scripts/examples](https://github.com/Cat0125/ByteX/tree/main/scripts/examples) folder.

### Calculator

Simple calculator.

```bytex
USE @BUF # Means that we're using buffer instead of memory

PRINT Enter number:
GET @NUM m0 # get number

PRINT Enter another number:
GET @NUM m1 # another number

SET m2 m0 # Create copy of m0 to m2
ADD m2 m1 # Add m1 to m2. (Line 7)
PRINT Result:
PRINT m2 # Print result
```
You can change operation at line 7 or create your own menu where user can select operation!

Supported operations:
+ ➕ `ADD` - addition
+ ➖ `SUB` - subtraction
+ ✖️ `MUP` - multiplication
+ ➗ `DIV` - division

> **Note**: **Why we're using buffer instead of memory?**<br>
Memory is a bigger storage that _always saves_ to file in script folder.
Buffer is a smaller _temporary_ storage that _never be saved_.

### Python

This example can execute source Python code.
The whole difficulty lies in fine-tuning the config.

Script folder must contain these files:
- `launcher.bx`. This file is launches Python code.
- `main.py`. This file is our main code.
- `config.yml`. This is a config file.
- `memory.dat`. This file will be automatically created after first script launch. It contains whole memory. Just ignore it.

config.yml:
```yaml
requirements:
  sizes:
    mem: 0
    buf: 0
    # We're don't need memory and buffer

script:
  entrance: "launcher.bx"
  # Entrance point of our program.
  # You can change it as you like.
  # Default: "main.bx"

permissions:
  - terminal
  # Permission to run terminal commands.
  # We're using it to launch our code.
```

launcher.bx:
```bytex
TERMINAL python scripts/ScriptName/main.py
```

And write your code in `main.py`!
