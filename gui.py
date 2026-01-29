# gui.py
from PyQt6.QtWidgets import (
    QWidget, QPushButton, QLabel, QTextEdit,
    QFileDialog, QVBoxLayout, QLineEdit, QMessageBox
)
from crypto import encrypt_message, decrypt_message
from stego import hide_data, extract_data


class OpenStegoX(QWidget):
    def __init__(self):
        super().__init__()  # ✅ MUST be first

        self.setWindowTitle("OpenStegoX")
        self.setFixedSize(400, 350)

        self.image_path = None

        # UI Elements
        self.label = QLabel("Select an image to begin")
        self.text = QTextEdit()
        self.text.setPlaceholderText("Enter secret message here")

        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setPlaceholderText("Password")

        self.btn_image = QPushButton("Select Image")
        self.btn_hide = QPushButton("Hide Message")
        self.btn_show = QPushButton("Extract Message")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn_image)
        layout.addWidget(self.text)
        layout.addWidget(self.password)
        layout.addWidget(self.btn_hide)
        layout.addWidget(self.btn_show)
        self.setLayout(layout)

        # Disable buttons until image selected (UX fix)
        self.btn_hide.setEnabled(False)
        self.btn_show.setEnabled(False)

        # Signals
        self.btn_image.clicked.connect(self.select_image)
        self.btn_hide.clicked.connect(self.hide_message)
        self.btn_show.clicked.connect(self.show_message)

    def select_image(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "", "Images (*.png *.jpg)"
        )
        if path:
            self.image_path = path
            self.label.setText(f"Selected: {path.split('/')[-1]}")
            self.btn_hide.setEnabled(True)
            self.btn_show.setEnabled(True)

    def hide_message(self):
        if not self.image_path:
            return self.error("Select an image first")

        if not self.password.text():
            return self.error("Password cannot be empty")

        if not self.text.toPlainText():
            return self.error("Message cannot be empty")

        try:
            cipher = encrypt_message(self.text.toPlainText(), self.password.text())
            out, _ = QFileDialog.getSaveFileName(
                self, "Save Image", "", "PNG (*.png)"
            )
            if out:
                hide_data(self.image_path, cipher, out)
                QMessageBox.information(self, "Success", "Message hidden successfully")
        except Exception as e:
            self.error(f"Failed to hide message\n{e}")

    def show_message(self):
        if not self.image_path:
            return self.error("Select encoded image")

        if not self.password.text():
            return self.error("Password required")

        try:
            data = extract_data(self.image_path)
            message = decrypt_message(data, self.password.text())
            self.text.setText(message)
        except Exception:
            self.error("Wrong password or no hidden data found")

    def error(self, msg):
        QMessageBox.critical(self, "Error", msg)
