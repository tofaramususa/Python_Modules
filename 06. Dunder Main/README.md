__Dunder Main__
Module Execution Context:
	When a Python file is run directly, Python sets the special __name__ variable to "__main__". This indicates that the script is being executed as the main program.
	If the same Python file is imported as a module in another script, the __name__ variable is set to the name of the module instead of "__main__". This allows code to differentiate between being run as a standalone script versus being imported as a module.
Depends if its being running directly or its being  imported as a module.
The main module or its being imported
<!-- if __name__ == '__main__' -->

