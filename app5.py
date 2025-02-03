import sys
import logging
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,
    QComboBox, QTextEdit, QHBoxLayout, QFrame, QTabWidget, QTextBrowser, QGridLayout,
    QMessageBox, QMenuBar, QAction, QStatusBar, QFormLayout, QGroupBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPalette, QIntValidator, QDoubleValidator

# -----------------------------------------------------------------------------
# Logging Configuration
# -----------------------------------------------------------------------------
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -----------------------------------------------------------------------------
# Actuarial Calculation Logic (Model)
# -----------------------------------------------------------------------------
def calculate_premium_logic(age: int, gender: str, coverage: float) -> float:
    """
    Calculate premium using simplified actuarial logic.
    
    Parameters:
        age (int): Age of the applicant.
        gender (str): Gender of the applicant ('male' or 'female').
        coverage (float): Coverage amount.
        
    Returns:
        float: Calculated premium.
    """
    gender = gender.lower()
    if gender == 'male':
        if age < 30:
            rate = 0.02
        elif age < 50:
            rate = 0.03
        else:
            rate = 0.05
    elif gender == 'female':
        if age < 30:
            rate = 0.015
        elif age < 50:
            rate = 0.025
        else:
            rate = 0.04
    else:
        raise ValueError("Invalid gender provided.")
    
    premium = coverage * rate
    logging.debug(f"Computed premium: {premium} (Rate: {rate})")
    return premium

# -----------------------------------------------------------------------------
# Calculator Tab (View)
# -----------------------------------------------------------------------------
class CalculatorTab(QWidget):
    """
    CalculatorTab contains the UI elements for entering data and calculating premiums.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)
        
        # Title label
        title_label = QLabel("Actuarial Premium Calculator")
        title_label.setFont(QFont("Arial", 20, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        # Input Group Box
        input_group = QGroupBox("Input Details")
        input_group.setFont(QFont("Arial", 12))
        input_layout = QFormLayout()
        
        # Age input
        self.age_input = QLineEdit()
        self.age_input.setFont(QFont("Arial", 12))
        self.age_input.setPlaceholderText("Enter age (0-150)")
        self.age_input.setValidator(QIntValidator(0, 150, self))
        input_layout.addRow("Age:", self.age_input)
        
        # Gender selection
        self.gender_combo = QComboBox()
        self.gender_combo.setFont(QFont("Arial", 12))
        self.gender_combo.addItems(["Male", "Female"])
        input_layout.addRow("Gender:", self.gender_combo)
        
        # Coverage input
        self.coverage_input = QLineEdit()
        self.coverage_input.setFont(QFont("Arial", 12))
        self.coverage_input.setPlaceholderText("Enter coverage amount ($)")
        self.coverage_input.setValidator(QDoubleValidator(0.0, 1e9, 2, self))
        input_layout.addRow("Coverage Amount ($):", self.coverage_input)
        
        input_group.setLayout(input_layout)
        layout.addWidget(input_group)
        
        # Buttons Layout
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(20)
        
        self.calc_button = QPushButton("Calculate Premium")
        self.calc_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.calc_button.setStyleSheet(
            "background-color: #4caf50; color: white; padding: 10px; border-radius: 8px;"
        )
        self.calc_button.clicked.connect(self.on_calculate)
        buttons_layout.addWidget(self.calc_button)
        
        self.reset_button = QPushButton("Reset")
        self.reset_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.reset_button.setStyleSheet(
            "background-color: #f44336; color: white; padding: 10px; border-radius: 8px;"
        )
        self.reset_button.clicked.connect(self.on_reset)
        buttons_layout.addWidget(self.reset_button)
        
        layout.addLayout(buttons_layout)
        
        # Result Display
        self.result_display = QTextEdit()
        self.result_display.setFont(QFont("Arial", 16))
        self.result_display.setReadOnly(True)
        self.result_display.setStyleSheet(
            "background-color: #f9f9f9; border: 1px solid #cccccc; border-radius: 8px; padding: 10px;"
        )
        layout.addWidget(self.result_display)
        
        self.setLayout(layout)
    
    def on_calculate(self):
        """
        Validates inputs, calculates the premium, and displays the result.
        """
        try:
            age_text = self.age_input.text().strip()
            coverage_text = self.coverage_input.text().strip()
            
            if not age_text or not coverage_text:
                QMessageBox.warning(self, "Input Error", "Please fill in all input fields.")
                return
            
            age = int(age_text)
            coverage = float(coverage_text)
            gender = self.gender_combo.currentText()
            
            logging.debug(f"Inputs - Age: {age}, Gender: {gender}, Coverage: {coverage}")
            premium = calculate_premium_logic(age, gender, coverage)
            
            self.result_display.setPlainText(f"Annual Premium: ${premium:.2f}")
            logging.info("Premium calculated successfully.")
        except ValueError as e:
            logging.error("Calculation error", exc_info=True)
            QMessageBox.critical(self, "Calculation Error", f"An error occurred: {str(e)}")
    
    def on_reset(self):
        """Clears all input fields and the result display."""
        self.age_input.clear()
        self.coverage_input.clear()
        self.gender_combo.setCurrentIndex(0)
        self.result_display.clear()
        logging.debug("Inputs and results have been reset.")

# -----------------------------------------------------------------------------
# Information Tab (View)
# -----------------------------------------------------------------------------
class InfoTab(QWidget):
    """
    InfoTab displays information about the actuarial logic used.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(10)
        
        title_label = QLabel("Actuarial Information")
        title_label.setFont(QFont("Arial", 20, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        info_browser = QTextBrowser()
        info_browser.setFont(QFont("Arial", 12))
        info_browser.setStyleSheet(
            "background-color: white; border: 1px solid #cccccc; border-radius: 8px; padding: 15px;"
        )
        info_browser.setHtml("""
            <p>This calculator uses simplified actuarial logic to estimate insurance premiums based on age, gender, and coverage amount.</p>
            <h3>Calculation Logic:</h3>
            <ul>
                <li><strong>Male:</strong>
                    <ul>
                        <li>Age &lt; 30: 2% of coverage</li>
                        <li>30 ≤ Age &lt; 50: 3% of coverage</li>
                        <li>Age ≥ 50: 5% of coverage</li>
                    </ul>
                </li>
                <li><strong>Female:</strong>
                    <ul>
                        <li>Age &lt; 30: 1.5% of coverage</li>
                        <li>30 ≤ Age &lt; 50: 2.5% of coverage</li>
                        <li>Age ≥ 50: 4% of coverage</li>
                    </ul>
                </li>
            </ul>
            <p><i>Please note:</i> This model is simplified and should not be used for actual underwriting purposes.</p>
        """)
        layout.addWidget(info_browser)
        self.setLayout(layout)

# -----------------------------------------------------------------------------
# Main Window (Controller & View)
# -----------------------------------------------------------------------------
class ActuarialCalculator(QMainWindow):
    """
    ActuarialCalculator is the main window containing the menu, tabs, and overall layout.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Actuarial Premium Calculator")
        self.setGeometry(100, 100, 800, 600)
        self.dark_mode = False  # Start in light mode
        self.init_ui()
    
    def init_ui(self):
        # Set up central widget and main layout
        central_widget = QWidget()
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        
        # Create Menu Bar
        self.create_menu_bar()
        
        # Tab Widget with Calculator and Info tabs
        self.tabs = QTabWidget()
        self.calculator_tab = CalculatorTab(self)
        self.info_tab = InfoTab(self)
        self.tabs.addTab(self.calculator_tab, "Calculator")
        self.tabs.addTab(self.info_tab, "Info")
        main_layout.addWidget(self.tabs)
        
        # Theme toggle button at the bottom
        self.theme_toggle_button = QPushButton("Toggle Dark Mode")
        self.theme_toggle_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.theme_toggle_button.setStyleSheet(
            "background-color: #2196F3; color: white; padding: 8px; border-radius: 8px;"
        )
        self.theme_toggle_button.clicked.connect(self.toggle_theme)
        main_layout.addWidget(self.theme_toggle_button, alignment=Qt.AlignCenter)
        
        # Status bar for feedback
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready", 5000)
        
        # Apply initial theme
        self.apply_theme()
    
    def create_menu_bar(self):
        """Creates the menu bar with File and Help menus."""
        menu_bar = self.menuBar()
        
        # File Menu
        file_menu = menu_bar.addMenu("File")
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Help Menu
        help_menu = menu_bar.addMenu("Help")
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
    
    def show_about(self):
        """Displays the About dialog."""
        QMessageBox.information(
            self,
            "About Actuarial Premium Calculator",
            "Actuarial Premium Calculator\nVersion 1.0\n\nCreated by Expert Software Engineers."
        )
    
    def toggle_theme(self):
        """Toggles between light and dark themes."""
        self.dark_mode = not self.dark_mode
        self.apply_theme()
        mode = "Dark" if self.dark_mode else "Light"
        self.status_bar.showMessage(f"Switched to {mode} Mode", 3000)
        logging.info(f"Theme toggled to {mode} Mode.")
    
    def apply_theme(self):
        """Applies the current theme (dark or light) to the application."""
        if self.dark_mode:
            # Dark theme palette and styles
            dark_palette = QPalette()
            dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
            dark_palette.setColor(QPalette.WindowText, Qt.white)
            dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
            dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
            dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
            dark_palette.setColor(QPalette.ToolTipText, Qt.white)
            dark_palette.setColor(QPalette.Text, Qt.white)
            dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
            dark_palette.setColor(QPalette.ButtonText, Qt.white)
            dark_palette.setColor(QPalette.BrightText, Qt.red)
            dark_palette.setColor(QPalette.Highlight, QColor(142, 45, 197).lighter())
            dark_palette.setColor(QPalette.HighlightedText, Qt.black)
            self.setPalette(dark_palette)
            self.setStyleSheet("""
                QMainWindow { background-color: #2b2b2b; }
                QPushButton { background-color: #4caf50; color: white; }
                QTabWidget::pane { border: 1px solid #444; }
                QTabBar::tab { background: #3c3c3c; padding: 10px; }
                QTabBar::tab:selected { background: #4caf50; }
            """)
        else:
            # Light theme palette and styles
            light_palette = QPalette()
            light_palette.setColor(QPalette.Window, QColor(240, 240, 240))
            light_palette.setColor(QPalette.WindowText, Qt.black)
            light_palette.setColor(QPalette.Base, Qt.white)
            light_palette.setColor(QPalette.AlternateBase, QColor(240, 240, 240))
            light_palette.setColor(QPalette.ToolTipBase, Qt.black)
            light_palette.setColor(QPalette.ToolTipText, Qt.black)
            light_palette.setColor(QPalette.Text, Qt.black)
            light_palette.setColor(QPalette.Button, QColor(230, 230, 230))
            light_palette.setColor(QPalette.ButtonText, Qt.black)
            light_palette.setColor(QPalette.BrightText, Qt.red)
            light_palette.setColor(QPalette.Highlight, QColor(76, 175, 80))
            light_palette.setColor(QPalette.HighlightedText, Qt.white)
            self.setPalette(light_palette)
            self.setStyleSheet("""
                QMainWindow { background-color: #f0f0f0; }
                QPushButton { background-color: #4caf50; color: white; }
                QTabWidget::pane { border: 1px solid #ccc; }
                QTabBar::tab { background: #e0e0e0; padding: 10px; }
                QTabBar::tab:selected { background: #4caf50; }
            """)

# -----------------------------------------------------------------------------
# Main Execution
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ActuarialCalculator()
    window.show()
    sys.exit(app.exec_())
