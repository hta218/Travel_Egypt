import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = "C:\\Users\\Huynh\\AppData\\Local\\Programs\\Python\\Python36\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\Huynh\\AppData\\Local\\Programs\\Python\\Python36\\tcl\\tk8.6"

shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "Travel Egypt",                    # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]Travel Egypt.exe",      # Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     "icon.ico",                     # Icon
     None,                     # IconIndex
     False,                     # ShowCmd
     'TARGETDIR'               # WkDir
     )
    ]

# Now create the table dictionary
msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}

# executables = [cx_Freeze.Executable("main.py")]
executables = [cx_Freeze.Executable("play.py",
                                    targetName="Travel Egypt.exe",
                                    icon="icon.ico"
                                    )
               ]



cx_Freeze.setup(
    name="Travel Egypt",
    options={
        "build_exe": {
            "packages":
                ["pygame"],
            "include_files":
                 ["game.py",
                 "character.py",
                 "configs.py",
                 "Levels.py",
                 "map.py",
                 "Level",
                 "Map",
                 "Sound"
                 ]
            },
        "bdist_msi":
            bdist_msi_options
    },
    executables = executables
    )
