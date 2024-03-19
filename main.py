from PySide6.QtWidgets import QApplication, QWidget

# Sys module allows to process command line arguments
import sys

app = QApplication(sys.argv)

window = QWidget()
window.show()

# Start the event loop
app.exec()