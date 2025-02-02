from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QTextEdit, QHBoxLayout, QFrame, QTabWidget, QTextBrowser
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPalette

# Function to calculate the premium
def calculate_premium():
    try:
        age = int(age_input.text())
        gender = gender_combo.currentText().lower()
        coverage = float(coverage_input.text())

        # Example actuarial logic (simplified)
        if gender == 'male':
            if age < 30:
                premium = coverage * 0.02
            elif 30 <= age < 50:
                premium = coverage * 0.03
            else:
                premium = coverage * 0.05
        elif gender == 'female':
            if age < 30:
                premium = coverage * 0.015
            elif 30 <= age < 50:
                premium = coverage * 0.025
            else:
                premium = coverage * 0.04

        result_text.setPlainText(f"Annual Premium: ${premium:.2f}")
    except ValueError:
        result_text.setPlainText("Invalid input. Please check your entries.")

# Create the main application window
class ActuarialCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Actuarial Calculator")
        self.setGeometry(100, 100, 600, 600)

        # Set a modern theme palette
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(240, 240, 240))  # Light gray background
        palette.setColor(QPalette.WindowText, Qt.black)
        palette.setColor(QPalette.Base, QColor(255, 255, 255))  # White base for text areas
        palette.setColor(QPalette.AlternateBase, QColor(240, 240, 240))
        palette.setColor(QPalette.Text, Qt.black)
        palette.setColor(QPalette.Button, QColor(230, 230, 230))  # Button background
        palette.setColor(QPalette.ButtonText, Qt.black)
        palette.setColor(QPalette.Highlight, QColor(76, 175, 80))  # Green highlight
        palette.setColor(QPalette.HighlightedText, Qt.white)
        self.setPalette(palette)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Tab Widget
        tab_widget = QTabWidget()

        # Tab 1: Calculator
        calculator_tab = QWidget()
        calculator_layout = QVBoxLayout()

        # Title
        title_label = QLabel("Actuarial Premium Calculator")
        title_label.setFont(QFont("Arial", 18, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #333333; margin-bottom: 20px;")
        calculator_layout.addWidget(title_label)

        # Input Fields
        input_frame = QFrame()
        input_frame.setFrameShape(QFrame.StyledPanel)
        input_frame.setFrameShadow(QFrame.Raised)
        input_frame.setStyleSheet("background-color: white; border-radius: 10px; padding: 15px;")
        input_layout = QVBoxLayout()

        # Age Input
        age_layout = QHBoxLayout()
        age_label = QLabel("Age:")
        age_label.setFont(QFont("Arial", 12))
        age_label.setStyleSheet("color: #555555;")
        age_input.setFont(QFont("Arial", 12))
        age_input.setStyleSheet("border: 1px solid #cccccc; border-radius: 5px; padding: 5px;")
        age_layout.addWidget(age_label)
        age_layout.addWidget(age_input)
        input_layout.addLayout(age_layout)

        # Gender Selection
        gender_layout = QHBoxLayout()
        gender_label = QLabel("Gender:")
        gender_label.setFont(QFont("Arial", 12))
        gender_label.setStyleSheet("color: #555555;")
        gender_combo.setFont(QFont("Arial", 12))
        gender_combo.setStyleSheet("border: 1px solid #cccccc; border-radius: 5px; padding: 5px;")
        gender_layout.addWidget(gender_label)
        gender_layout.addWidget(gender_combo)
        input_layout.addLayout(gender_layout)

        # Coverage Input
        coverage_layout = QHBoxLayout()
        coverage_label = QLabel("Coverage Amount ($):")
        coverage_label.setFont(QFont("Arial", 12))
        coverage_label.setStyleSheet("color: #555555;")
        coverage_input.setFont(QFont("Arial", 12))
        coverage_input.setStyleSheet("border: 1px solid #cccccc; border-radius: 5px; padding: 5px;")
        coverage_layout.addWidget(coverage_label)
        coverage_layout.addWidget(coverage_input)
        input_layout.addLayout(coverage_layout)

        input_frame.setLayout(input_layout)
        calculator_layout.addWidget(input_frame)

        # Calculate Button
        calculate_button = QPushButton("Calculate Premium")
        calculate_button.setFont(QFont("Arial", 14, QFont.Bold))
        calculate_button.setStyleSheet("""
            background-color: #4caf50;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 10px;
        """)
        calculate_button.setCursor(Qt.PointingHandCursor)
        calculate_button.clicked.connect(calculate_premium)
        calculator_layout.addWidget(calculate_button, alignment=Qt.AlignCenter)

        # Result Display
        result_text.setFont(QFont("Arial", 16, QFont.Bold))
        result_text.setStyleSheet("""
            background-color: #f9f9f9;
            border: 1px solid #cccccc;
            border-radius: 10px;
            color: #333333;
            padding: 15px;
            margin-top: 20px;
        """)
        result_text.setReadOnly(True)
        calculator_layout.addWidget(result_text)

        calculator_tab.setLayout(calculator_layout)
        tab_widget.addTab(calculator_tab, "Calculator")

        # Tab 2: Info
        info_tab = QWidget()
        info_layout = QVBoxLayout()

        info_title = QLabel("Actuarial Information")
        info_title.setFont(QFont("Arial", 18, QFont.Bold))
        info_title.setAlignment(Qt.AlignCenter)
        info_title.setStyleSheet("color: #333333; margin-bottom: 20px;")
        info_layout.addWidget(info_title)

        info_text = QTextBrowser()
        info_text.setFont(QFont("Arial", 12))
        info_text.setStyleSheet("background-color: white; border: 1px solid #cccccc; border-radius: 10px; padding: 15px;")
        info_text.setHtml("""
            <p>This calculator uses simplified actuarial logic to estimate insurance premiums based on age, gender, and coverage amount.</p>
            <h3>Logic Breakdown:</h3>
            <ul>
                <li><strong>Male:</strong></li>
                <ul>
                    <li>Age < 30: 2% of coverage</li>
                    <li>30 ≤ Age < 50: 3% of coverage</li>
                    <li>Age ≥ 50: 5% of coverage</li>
                </ul>
                <li><strong>Female:</strong></li>
                <ul>
                    <li>Age < 30: 1.5% of coverage</li>
                    <li>30 ≤ Age < 50: 2.5% of coverage</li>
                    <li>Age ≥ 50: 4% of coverage</li>
                </ul>
            </ul>
        """)
        info_layout.addWidget(info_text)

        info_tab.setLayout(info_layout)
        tab_widget.addTab(info_tab, "Info")

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(tab_widget)
        central_widget.setLayout(main_layout)

# Initialize the application
if __name__ == "__main__":
    app = QApplication([])

    # Create input fields and widgets
    age_input = QLineEdit()
    gender_combo = QComboBox()
    gender_combo.addItems(["Male", "Female"])
    coverage_input = QLineEdit()
    result_text = QTextEdit()

    # Create the main window
    window = ActuarialCalculator()
    window.show()

    # Run the application
    app.exec_()