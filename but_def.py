from PyQt5.QtWidgets import QMessageBox

def button_click(self):
    print("button clicked")
    QMessageBox.information(MainWindow,'PyQt5 Example', 'Welcome')