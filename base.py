import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel


class ClawfishApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Clawfish 🎙")
        self.setGeometry(300, 200, 600, 400)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Clawfish - Ready")
        layout.addWidget(self.label)

        self.record_btn = QPushButton("Record")
        self.record_btn.clicked.connect(self.on_record)
        layout.addWidget(self.record_btn)

        self.setLayout(layout)

    def on_record(self):
        self.label.setText("Recording...")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ClawfishApp()
    window.show()

    sys.exit(app.exec())