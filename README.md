# About

ByteX is a simple programming language written in Python. You can use it as you wish - e.g. for education.

# Documentation

See [wiki](https://github.com/Cat0125/ByteX/wiki)

# Examples

More examples in **scripts/examples** folder.

> **Note**: some examples can not work with updates.
You can notify me [here](https://github.com/Cat0125/ByteX/issues) or find **actual** examples in scripts/examples folder.

### Calculator

Simple calculator.

```
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

> **Note**: **Why we're using buffer instead of memory?**<br>
Memory is a bigger storage that _always saves_ to file in script folder.
Buffer is a smaller _temporary_ storage that _never be saved_.
