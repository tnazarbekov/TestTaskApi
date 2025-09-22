import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QLineEdit


def xor_encrypt_decrypt(file_path, key, output_suffix):
    with open(file_path, 'rb') as f_in:
        content = f_in.read()

    encrypted_content = bytearray([byte ^ key for byte in content])

    output_file = file_path + output_suffix
    with open(output_file, 'wb') as f_out:
        f_out.write(encrypted_content)

    return output_file


class SimpleCryptoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.key_input = QLineEdit(self)
        self.key_input.setPlaceholderText("Введите ключ")
        self.layout.addWidget(self.key_input)

        self.encrypt_button = QPushButton("Шифровать файл", self)
        self.encrypt_button.clicked.connect(self.encrypt_file)
        self.layout.addWidget(self.encrypt_button)

        self.decrypt_button = QPushButton("Расшифровать файл", self)
        self.decrypt_button.clicked.connect(self.decrypt_file)
        self.layout.addWidget(self.decrypt_button)

        self.result_label = QLabel("")
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def encrypt_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Выбери файл")
        key = int(self.key_input.text())  # Преобразуем ключ в целое число
        output_file = xor_encrypt_decrypt(file_name, key, ".enc")
        self.result_label.setText(f"Файл зашифрован: {output_file}")
    def decrypt_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "файл для расшифровки")

        key = int(self.key_input.text())
        output_file = xor_encrypt_decrypt(file_name, key, ".dec")
        self.result_label.setText(f"расшифрован:{output_file}")



app = QApplication(sys.argv)
window = SimpleCryptoApp()
window.show()
sys.exit(app.exec_())
