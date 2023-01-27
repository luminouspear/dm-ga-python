import os
import subprocess
from PyQt5 import QtWidgets, QtGui
from datetime import datetime
import shutil

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # set up the main window
        self.setWindowTitle("Keynote Converter")
        self.setAcceptDrops(True)
        self.setStyleSheet("QMainWindow { background-color: #333;  }")

        # create a label to display the dropped file names
        self.label = QtWidgets.QLabel("Drop keynote files here")
        self.label.setWordWrap(True)
        self.label.setStyleSheet("QLabel { background-color: #444; border: 1px solid gray; padding: 10px; color: white; }")

        # create a checkbox to enable automatic confirmation of overwrites.

        self.overwrite_checkbox = QtWidgets.QCheckBox("Automatically confirm overwrites")
        self.overwrite_checkbox.setChecked(True)
        self.overwrite_checkbox.setStyleSheet("QCheckBox { color: white; }")

        # create a layout to hold the label and checkbox
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.overwrite_checkbox)

        #set the layout as the central widget of the main window
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def dragEnterEvent(self, event):
        #accept the drag event if a file is begin dragged.

        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()


    def dropEvent(self, event):

        # get the file paths of the dropped files
        file_paths = [url.toLocalFile() for url in event.mimeData().urls()]

        if not all(path.endswith(".key") for path in file_paths):
            self.label.setText("Error: Not all files are keynote files!")
            return

        date_str = datetime.now().strftime("%Y%m%d")



        # convert the keynote files to PDF and PPT
        converted_files = []
        for file_path in file_paths:
            file_name, _ = os.path.splitext(os.path.basename(file_path))

            dest_dir = os.path.expanduser("~/Downloads")
            output_path_pdf = os.path.join(dest_dir, date_str + " " + file_name + ".pdf")
            output_path_key = os.path.join(dest_dir, date_str + " " + file_name + ".key")
            print('output_path_key: ', output_path_key)
            output_path_ppt = os.path.join(dest_dir, date_str + " " + file_name + ".ppt")
            print(os.path.exists(os.path.dirname(output_path_key)))
            # TODO: Add command line command to perform conversions here.
            command_pdf = ["soffice", "--convert-to", "pdf", file_path, "--outdir", output_path_pdf]
            command_ppt = ["soffice", "--convert-to", "ppt", file_path, "--outdir", output_path_ppt]
            # TODO: Create a copy of the keynote file and save it to the /Downloads folder.
            shutil.copy(file_path, output_path_key)
            subprocess.run(command_pdf)
            subprocess.run(command_ppt)

            converted_files.append((file_path, output_path_key))
            converted_files.append((file_path, output_path_pdf))
            converted_files.append((file_path, output_path_ppt))


        # TODO: Update the label to show the conversion was successful
        self.label.setText("Successfully converted: \n" + "\n".join("{} to {}".format(input_path, output_path) for input_path, output_path in converted_files))

if __name__ == "__main__":
    app  = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
