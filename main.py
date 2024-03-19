from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

# Sys module allows to process command line arguments
import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("First MainWindow App!")

label = QLabel()
label.setText("Hello world")

window.setCentralWidget(label)

# Show the window
window.show()

# Start the event loop
app.exec()