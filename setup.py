from cx_Freeze import setup, Executable

setup(name="NetroSearch",
      version="1.0",
      description="Title Search Automation",
      executables=[Executable("NetroSearch.py")])