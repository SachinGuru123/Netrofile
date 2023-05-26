from cx_Freeze import setup, Executable

setup(name="AutoBot",
      version="1.2",
      description="Title Search Automation cook county",
      executables=[Executable("AutoBot.py")])