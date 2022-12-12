import os
import datetime
from pykeynote import Presentation

# set the destination directory for the converted files

dest_dir = '/Users/quentinmacbook/Library/Mobile Documents/com~apple~Keynote/Documents/_output/UXDI 34'

# get the path to the Keynote file from the command line arguments
filepath = sys.argv[1]

# get the current date and t ime
timestamp = time.strftime('%Y%m%d')

# get the file name without the extension
base_name = os.path.splittext(os.path.basename(file_path))[0]

# set the paths for the converted files

pptx_path = os.path.join(dest_dir, timestamp + ' ' + base_name + '.pptx')
pdf_path = os.path.join(dest_dir, timestamp + ' ' + base_name + '.pdf')


# Convert the keynote file to PPT and PDF using the 'keynote' comand line tool
os.system('keynote -e pptx ' + file_path + ' ' + pptx_path)
os.system('keynote -e pdf ' + file_path + ' ' + pdf_path)

# Finally, copy the original keynote file to the destination directory with the timestamp in the file name

shutil.copy(file_path, os.path.join(dest_dir, timestamp + ' ' + base_name + '.key'))