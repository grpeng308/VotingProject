import csv

from PyQt6.QtGui import QFont

from VotingProject.gui import *
from PyQt6.QtWidgets import *

CANDIDATE_ONE = "Jane"
CANDIDATE_TWO = "John"


def is_int(string: str) -> bool:
    """
    Method to check if string is an integer
    :param string: String to be checked
    :return: True if integer, False otherwise
    """
    try:
        int(string)
        return True
    except ValueError:
        return False


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        """
        Create candidate variable to keep track of who a user votes for
        Create a list to store votes
        """
        self.__candidate = "None"
        self.__votes = []

        """
        Adjust fonts, colors, geometries of labels and buttons
        """

        self.error.setFont(QFont("Helvetica Neue", 11))
        self.error.setGeometry(20, 220, 161, 71)
        self.error.setStyleSheet("color: red")
        self.error.hide()

        self.candidates.setFont(QFont("Helvetica Neue", 13))
        self.candidates.setGeometry(45, 95, 120, 31)

        self.submit.setGeometry(30, 190, 141, 31)
        self.candidate1.setGeometry(68, 133, 91, 21)
        self.candidate2.setGeometry(68, 158, 91, 21)
        self.input_id.setGeometry(62, 59, 113, 20)
        self.title.setGeometry(55, 15, 91, 31)

        self.title.setStyleSheet("color: blue")

        """
        Connect buttons to methods
        """

        self.submit.clicked.connect(lambda: self.submit_clicked())
        self.candidate1.clicked.connect(lambda: self.candidates_clicked())
        self.candidate2.clicked.connect(lambda: self.candidates_clicked())

    def submit_clicked(self) -> None:
        """
        Method to check ID numbers and perform exception handling
        """
        user_input = self.input_id.text()

        if self.candidate1.isChecked() or self.candidate2.isChecked():
            if is_int(user_input):
                if len(user_input) == 8:
                    if any(user_input in x for x in self.__votes):
                        self.error.setText("Error: ID already voted")
                        self.error.show()
                    else:
                        self.error.setText("Success!")
                        self.error.show()
                        self.__votes.append(f"{user_input},{self.__candidate}")
                        self.input_id.setText("")
                        self.buttonGroup.setExclusive(False)
                        self.candidate1.setAutoExclusive(False)
                        self.candidate1.setChecked(False)
                        self.candidate1.setAutoExclusive(True)
                        self.candidate2.setAutoExclusive(False)
                        self.candidate2.setChecked(False)
                        self.candidate2.setAutoExclusive(True)
                        self.buttonGroup.setExclusive(True)
                else:
                    self.error.setText("Error: ID should be 8 digits")
                    self.error.show()
            else:
                self.error.setText("Error: ID should only contain numbers")
                self.error.show()
        else:
            self.error.setText("Error: Please select a candidate")
            self.error.show()

        with open("voters.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Vote"])
            for vote in self.__votes:
                file.write(f"{vote}\n")

    def candidates_clicked(self) -> None:
        """
        Method to store candidate picked in candidate variable
        """
        if self.candidate1.isChecked():
            self.__candidate = CANDIDATE_ONE
        else:
            self.__candidate = CANDIDATE_TWO
