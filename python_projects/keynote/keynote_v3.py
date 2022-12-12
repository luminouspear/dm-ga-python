import os
import time
import pptx
from pptx import Presentation

import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s", filename="/Users/quentinmacbook/Library/Mobile Documents/com~apple~CloudDocs/Development/PYTH-15/python_projects/keynote/keynoteapp/logs/debug.log", filemode="a")

logging.info(f"Application started.")

src_file = filepath = sys.argv[1]

logging.debug(f"Input file: {src_file}")
dst_dir = "/Users/quentinmacbook/Library/Mobile Documents/com~apple~Keynote/Documents/_output/UXDI 34"
if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)
    logging.debug(f"Created output directory: {dst_dir}")

today = datetime.date.today().strftime("%Y%m%d")

os.system("osascript -e 'display alert \"Script Starting\"'")
# open the keynote file using keynote-parser
presentation = Presentation(src_file)

# save the file as a keynote
if presentation.save(f"{dst_dir}/{today} {src_file.split('/')[-1]}.key"):
    os.system("osascript -e 'display alert \"Successfully saved input keynote file\"'")
else:
    os.system("osascript -e 'display alert \"Failed to save input keynote file\"'")

# save the file as a powerpoint
presentation.save(f"{dst_dir}/{today} {src_file.split('/')[-1]}.pptx")

# save the file as a pdf
pdf_file = open(f"{dst_dir}/{today} {src_file.split('/')[-1]}.pdf", "w")

for slide in presentation.slides:
    pdf_file.write(slide.image)

pdf_file.close()