#!/usr/bin/env python3
# coding: utf-8

# Import libraries
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSizePolicy
from PyQt6.QtCore import QTimer, Qt


# Class StopWatch
class StopWatch(QWidget):

    # @name: __init__()
    # @description: Class initialization
    # @return: self values
    def __init__(self):
        """ Class initialization """
        super().__init__()
        self.displaylabel = QLabel("00:00:00.00")
        self.startbutton = QPushButton("Start")
        self.stopbutton = QPushButton("Stop")
        self.resetbutton = QPushButton("Reset")
        self.timer = QTimer()
        self.elapsed_time = 0
        self.gui()

    # @name: gui()
    # @description: Return the visual interface
    # @return: void
    def gui(self):
        """ Return the visual interface """
        self.setWindowTitle("StopWatch")
        self.setGeometry(100, 100, 300, 150)
        layout = QVBoxLayout()
        self.displaylabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.displaylabel.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.displaylabel.setStyleSheet("font-size: 24px")  # Increase font size
        layout.addWidget(self.displaylabel)
        handlerlayout = QHBoxLayout()
        self.startbutton.clicked.connect(self.start)
        handlerlayout.addWidget(self.startbutton)
        self.stopbutton.clicked.connect(self.stop)
        handlerlayout.addWidget(self.stopbutton)
        self.resetbutton.clicked.connect(self.reset)
        handlerlayout.addWidget(self.resetbutton)
        layout.addLayout(handlerlayout)
        self.setLayout(layout)
        self.timer.timeout.connect(self.update)

    # @name: start()
    # @description: Start the stopwatch
    # @return: void
    def start(self):
        """ Start the stopwatch """
        self.timer.start(10)

    # @name: stop()
    # @description: Stop the stopwatch
    # @return: void
    def stop(self):
        """ Stop the stopwatch """
        self.timer.stop()

    # @name: reset()
    # @description: Reset the stopwatch
    # @return: void
    def reset(self):
        """ Reset the stopwatch """
        self.timer.stop()
        self.elapsed_time = 0
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
        self.displaylabel.setText(f"{minutes:02d}:{seconds:02d}:{milliseconds//10:02d}.{milliseconds%100:02d}")


# Main function
def main():
    app = QApplication(sys.argv)
    window = StopWatch()
    window.show()
    sys.exit(app.exec())


# Callback
if __name__ == '__main__':
    main()
