import os

source_dir = "/Users/quentinmacbook/Downloads"

with os.scandir(source_dir) as entries:
    for entry in entries:
        print(entry.name)
        
