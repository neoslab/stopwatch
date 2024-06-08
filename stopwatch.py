""" coding: utf-8 """

# Import libraries
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QHBoxLayout
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QSizePolicy
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QWidget
import sys


# Class StopWatch
class StopWatch(QWidget):

    # @name: __init__()
    # @description: Class initialization
    # @return: self values
    def __init__(self):
        """ Class initialization """
        super().__init__()
        self.displaylabel = QLabel("00:00:00:00")
        self.displaylabel.setStyleSheet("font-size:30px;font-weight:normal;color:#ffffff;")
        self.btn_start = QPushButton("Start")
        self.btn_start.setFixedSize(100, 35)
        self.btn_start.setStyleSheet("""
            QPushButton {
                font-size:13px;
                color:#ffffff;
                background-color:#23262a;
                border:1px solid #787878;
            }
            QPushButton:hover {
                background-color:#3a3f45;
            }
        """)
        self.btn_stop = QPushButton("Stop")
        self.btn_stop.setFixedSize(100, 35)
        self.btn_stop.setStyleSheet("""
            QPushButton {
                font-size:13px;
                color:#ffffff;
                background-color:#23262a;
                border:1px solid #787878;
            }
            QPushButton:hover {
                background-color:#3a3f45;
            }
        """)
        self.btn_reset = QPushButton("Reset")
        self.btn_reset.setFixedSize(100, 35)
        self.btn_reset.setStyleSheet("""
            QPushButton {
                font-size:13px;
                color:#ffffff;
                background-color:#23262a;
                border:1px solid #787878;
            }
            QPushButton:hover {
                background-color:#3a3f45;
            }
        """)
        self.timer = QTimer()
        self.elapsed_time = 0
        self.running = False
        self.gui()

    # @name: gui()
    # @description: Return the visual interface
    # @return: void
    def gui(self):
        """ Return the visual interface """
        self.setWindowTitle("StopWatch")
        self.setFixedSize(350, 150)
        self.setStyleSheet("background-color:#2a2e32;")

        layout = QVBoxLayout()
        self.displaylabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.displaylabel.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout.addWidget(self.displaylabel)
        handlerlayout = QHBoxLayout()
        self.btn_start.clicked.connect(self.start)
        handlerlayout.addWidget(self.btn_start)
        self.btn_stop.clicked.connect(self.stop)
        handlerlayout.addWidget(self.btn_stop)
        self.btn_reset.clicked.connect(self.reset)
        handlerlayout.addWidget(self.btn_reset)
        layout.addLayout(handlerlayout)
        self.setLayout(layout)
        self.timer.timeout.connect(self.update)

    # @name: start()
    # @description: Start the stopwatch
    # @return: void
    def start(self):
        """ Start the stopwatch """
        if not self.running:
            self.timer.start(1)
            self.running = True

    # @name: stop()
    # @description: Stop the stopwatch
    # @return: void
    def stop(self):
        """ Stop the stopwatch """
        self.timer.stop()
        self.running = False

    # @name: reset()
    # @description: Reset the stopwatch
    # @return: void
    def reset(self):
        """ Reset the stopwatch """
        self.timer.stop()
        self.elapsed_time = 0
        self.running = False
        self.refresh()

    # @name: update()
    # @description: Update the stopwatch
    # @return: void
    def update(self):
        """ Update the stopwatch """
        self.elapsed_time += 1
        self.refresh()

    # @name: refresh()
    # @description: Refresh the visual interface
    # @return: void
    def refresh(self):
        """ Refresh the visual interface """
        milliseconds = self.elapsed_time % 1000
        seconds = (self.elapsed_time // 1000) % 60
        minutes = (self.elapsed_time // 60000) % 60
        hours = self.elapsed_time // 3600000
        self.displaylabel.setText(f"{hours:02d}:{minutes:02d}:{seconds:02d}:{milliseconds//10:02d}")


# Main function
def main():
    app = QApplication(sys.argv)
    window = StopWatch()
    window.show()
    sys.exit(app.exec())


# Callback
if __name__ == '__main__':
    main()
