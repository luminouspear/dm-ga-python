import os
import time
from keynote_parser import Keynote

src_file = "/path/to/source/file.key"
dst_dir = '/Users/quentinmacbook/Library/Mobile Documents/com~apple~Keynote/Documents/_output/UXDI 34'

# open the keynote file using keynote-parser
presentation = Keynote(src_file)

# save the file as a PDF
presentation.export_pdf(f"{dst_dir}/{date}_{src_file.split('/')[-1]}.pdf")

# save the file as a powerpoint
presentation.export_pptx(f"{dst_dir}/{date}_{src_file.split('/')[-1]}.pptx")

# save the file as a keynote
presentation.export_key(f"{dst_dir}/{date}_{src_file.split('/')[-1]}.key")
