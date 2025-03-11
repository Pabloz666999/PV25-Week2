import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QRadioButton, 
    QComboBox, QVBoxLayout, QHBoxLayout, QGroupBox, QMessageBox
)

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Week 2 : Layout - User Registration Form")
        self.setGeometry(100, 100, 500, 400)

        # Layout Utama
        main_layout = QVBoxLayout()

        # Identitas
        identitas_group = QGroupBox("Identitas (vertical box layout)")
        identitas_layout = QVBoxLayout()
        identitas_layout.addWidget(QLabel("Nama : nama_anda"))
        identitas_layout.addWidget(QLabel("NIM : nim_anda"))
        identitas_layout.addWidget(QLabel("Kelas : kelas_anda"))
        identitas_group.setLayout(identitas_layout)
        main_layout.addWidget(identitas_group)

        # Navigasi
        nav_group = QGroupBox("Navigation (horizontal box layout)")
        nav_layout = QHBoxLayout()
        nav_layout.addWidget(QPushButton("Home"))
        nav_layout.addWidget(QPushButton("About"))
        nav_layout.addWidget(QPushButton("Contact"))
        nav_group.setLayout(nav_layout)
        main_layout.addWidget(nav_group)

        # Form Pendaftaran
        form_group = QGroupBox("User Registration (form layout)")
        form_layout = QVBoxLayout()

        self.entry_nama = QLineEdit()
        self.entry_email = QLineEdit()
        self.entry_phone = QLineEdit()

        form_layout.addWidget(QLabel("Full Name:"))
        form_layout.addWidget(self.entry_nama)

        form_layout.addWidget(QLabel("Email:"))
        form_layout.addWidget(self.entry_email)

        form_layout.addWidget(QLabel("Phone:"))
        form_layout.addWidget(self.entry_phone)

        gender_layout = QHBoxLayout()
        gender_layout.addWidget(QLabel("Gender:"))
        self.radio_male = QRadioButton("Male")
        self.radio_female = QRadioButton("Female")
        gender_layout.addWidget(self.radio_male)
        gender_layout.addWidget(self.radio_female)
        form_layout.addLayout(gender_layout)

        form_layout.addWidget(QLabel("Country:"))
        self.combo_country = QComboBox()
        self.combo_country.addItems(["Select Country", "Indonesia", "Malaysia", "Singapore", "Others"])
        form_layout.addWidget(self.combo_country)

        form_group.setLayout(form_layout)
        main_layout.addWidget(form_group)

        # Tombol Aksi
        action_group = QGroupBox("Actions (horizontal box layout)")
        action_layout = QHBoxLayout()
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submit_form)
        cancel_button = QPushButton("Cancel")
        action_layout.addWidget(submit_button)
        action_layout.addWidget(cancel_button)
        action_group.setLayout(action_layout)
        main_layout.addWidget(action_group)

        self.setLayout(main_layout)

    def submit_form(self):
        nama = self.entry_nama.text()
        email = self.entry_email.text()
        phone = self.entry_phone.text()
        gender = "Male" if self.radio_male.isChecked() else "Female" if self.radio_female.isChecked() else "Not Selected"
        country = self.combo_country.currentText()

        if not nama or not email or not phone or country == "Select Country":
            QMessageBox.warning(self, "Peringatan", "Semua kolom harus diisi!")
            return

        result_message = (
            f"Pendaftaran Berhasil!\n"
            f"Nama: {nama}\n"
            f"Email: {email}\n"
            f"Phone: {phone}\n"
            f"Gender: {gender}\n"
            f"Country: {country}"
        )

        QMessageBox.information(self, "Hasil Pendaftaran", result_message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec_())
