from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, 
    QPushButton, QComboBox, QTextEdit, QHBoxLayout, QFrame, QTabWidget, 
    QTextBrowser, QGridLayout, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPalette


class ActuarialCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Actuarial Premium Calculator")
        self.setGeometry(100, 100, 650, 550)

        # Theme setup
        self.dark_mode = False
        self.set_light_theme()

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Tab Widget
        self.tab_widget = QTabWidget()

        # Create Tabs
        self.create_calculator_tab()
        self.create_info_tab()

        # Add Tabs to Main Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tab_widget)

        # Theme Toggle Button
        self.theme_button = QPushButton("Toggle Dark Mode")
        self.theme_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.theme_button.setStyleSheet("background-color: #4caf50; color: white; border-radius: 10px; padding: 8px;")
        self.theme_button.clicked.connect(self.toggle_theme)
        main_layout.addWidget(self.theme_button, alignment=Qt.AlignCenter)

        central_widget.setLayout(main_layout)

    def create_calculator_tab(self):
        """Creates the calculator UI."""
        self.calculator_tab = QWidget()
        calculator_layout = QVBoxLayout()

        # Title
        title_label = QLabel("Actuarial Premium Calculator")
        title_label.setFont(QFont("Arial", 18, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #333333; margin-bottom: 15px;")
        calculator_layout.addWidget(title_label)

        # Input Frame
        input_frame = QFrame()
        input_frame.setStyleSheet("background-color: white; border-radius: 10px; padding: 20px;")
        input_layout = QGridLayout()

        # Age Input
        self.age_input = QLineEdit()
        self.setup_input_field(self.age_input)
        input_layout.addWidget(QLabel("Age:"), 0, 0)
        input_layout.addWidget(self.age_input, 0, 1)

        # Gender Selection
        self.gender_combo = QComboBox()
        self.gender_combo.addItems(["Male", "Female"])
        self.setup_combo_box(self.gender_combo)
        input_layout.addWidget(QLabel("Gender:"), 1, 0)
        input_layout.addWidget(self.gender_combo, 1, 1)

        # Coverage Input
        self.coverage_input = QLineEdit()
        self.setup_input_field(self.coverage_input)
        input_layout.addWidget(QLabel("Coverage Amount ($):"), 2, 0)
        input_layout.addWidget(self.coverage_input, 2, 1)

        input_frame.setLayout(input_layout)
        calculator_layout.addWidget(input_frame)

        # Calculate Button
        calculate_button = QPushButton("Calculate Premium")
        calculate_button.setFont(QFont("Arial", 14, QFont.Bold))
        calculate_button.setStyleSheet(
            "background-color: #4caf50; color: white; border-radius: 10px; padding: 10px;"
        )
        calculate_button.clicked.connect(self.calculate_premium)
        calculator_layout.addWidget(calculate_button, alignment=Qt.AlignCenter)

        # Result Display
        self.result_text = QTextEdit()
        self.result_text.setFont(QFont("Arial", 14))
        self.result_text.setReadOnly(True)
        self.result_text.setStyleSheet("background-color: #f9f9f9; border: 1px solid #cccccc; border-radius: 10px; padding: 10px;")
        calculator_layout.addWidget(self.result_text)

        self.calculator_tab.setLayout(calculator_layout)
        self.tab_widget.addTab(self.calculator_tab, "Calculator")

    def create_info_tab(self):
        """Creates the information tab."""
        info_tab = QWidget()
        info_layout = QVBoxLayout()

        info_title = QLabel("Actuarial Information")
        info_title.setFont(QFont("Arial", 18, QFont.Bold))
        info_title.setAlignment(Qt.AlignCenter)
        info_title.setStyleSheet("color: #333333; margin-bottom: 20px;")
        info_layout.addWidget(info_title)

        info_text = QTextBrowser()
        info_text.setFont(QFont("Arial", 12))
        info_text.setStyleSheet("background-color: white; border-radius: 10px; padding: 15px;")
        info_text.setHtml("""
            <p>This calculator estimates insurance premiums using actuarial logic.</p>
            <h3>Premium Calculation:</h3>
            <ul>
                <li><b>Male:</b></li>
                <ul>
                    <li>Age < 30: 2% of coverage</li>
                    <li>30 ≤ Age < 50: 3% of coverage</li>
                    <li>Age ≥ 50: 5% of coverage</li>
                </ul>
                <li><b>Female:</b></li>
                <ul>
                    <li>Age < 30: 1.5% of coverage</li>
                    <li>30 ≤ Age < 50: 2.5% of coverage</li>
                    <li>Age ≥ 50: 4% of coverage</li>
                </ul>
            </ul>
        """)
        info_layout.addWidget(info_text)
        info_tab.setLayout(info_layout)
        self.tab_widget.addTab(info_tab, "Info")

    def calculate_premium(self):
        """Calculates insurance premium based on inputs."""
        try:
            age = int(self.age_input.text())
            gender = self.gender_combo.currentText().lower()
            coverage = float(self.coverage_input.text())

            if gender == 'male':
                premium = coverage * (0.02 if age < 30 else 0.03 if age < 50 else 0.05)
            else:
                premium = coverage * (0.015 if age < 30 else 0.025 if age < 50 else 0.04)

            self.result_text.setPlainText(f"Annual Premium: ${premium:.2f}")
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid numerical values.")

    def toggle_theme(self):
        """Toggles between dark and light mode."""
        self.dark_mode = not self.dark_mode
        if self.dark_mode:
            self.set_dark_theme()
        else:
            self.set_light_theme()

    def set_light_theme(self):
        """Sets the light theme."""
        self.setStyleSheet("background-color: #f0f0f0; color: black;")

    def set_dark_theme(self):
        """Sets the dark theme."""
        self.setStyleSheet("background-color: #2c2c2c; color: white;")

    def setup_input_field(self, field):
        """Sets up styling for input fields."""
        field.setFont(QFont("Arial", 12))
        field.setStyleSheet("border: 1px solid #cccccc; border-radius: 5px; padding: 5px;")

    def setup_combo_box(self, combo_box):
        """Sets up styling for combo boxes."""
        combo_box.setFont(QFont("Arial", 12))
        combo_box.setStyleSheet("border: 1px solid #cccccc; border-radius: 5px; padding: 5px;")


if __name__ == "__main__":
    app = QApplication([])
    window = ActuarialCalculator()
    window.show()
    app.exec_()
