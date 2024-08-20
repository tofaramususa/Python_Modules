Writing Better Python
Topics - Python Conventions. Write Docstrings. Logging. Python Debugger

PEPS:
pep 8 and pep 20

Classes are usually Uppercased
Functions use underscore and always lowecase
 
 pep 8 is like norminette. We can install it and run it with 
 Import this

The help library. We have the docstrings. -- enclosed in triple quotes.
So we can use the help() function on module.function and we get something from it. The docstrings.

Part 2:
The logging library. import logging
logging.info| logging.warn
logging.basicConfig(file, loglevels)
Record information passed in by the user and log that information in. To see whats going on.
The python debugger. - pdb
import pdb -- breakproint - set_trace()