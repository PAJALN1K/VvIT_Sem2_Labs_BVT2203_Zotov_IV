import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from functions import is_digit, int_whether_float


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()

        # создаем оси выравнивания
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_output = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_second = QHBoxLayout()
        self.hbox_third = QHBoxLayout()
        self.hbox_fourth = QHBoxLayout()
        self.hbox_result = QHBoxLayout()

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_output)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_third)
        self.vbox.addLayout(self.hbox_fourth)
        self.vbox.addLayout(self.hbox_result)

        # создаем виджеты и добавляем их к соответствующим осям
        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)
        self.output = QLabel(self)
        self.hbox_output.addWidget(self.output)

        self.b_7 = QPushButton("7", self)
        self.hbox_first.addWidget(self.b_7)
        self.b_8 = QPushButton("8", self)
        self.hbox_first.addWidget(self.b_8)
        self.b_9 = QPushButton("9", self)
        self.hbox_first.addWidget(self.b_9)
        self.b_multiply = QPushButton("×", self)
        self.hbox_first.addWidget(self.b_multiply)

        self.b_4 = QPushButton("4", self)
        self.hbox_second.addWidget(self.b_4)
        self.b_5 = QPushButton("5", self)
        self.hbox_second.addWidget(self.b_5)
        self.b_6 = QPushButton("6", self)
        self.hbox_second.addWidget(self.b_6)
        self.b_minus = QPushButton("-", self)
        self.hbox_second.addWidget(self.b_minus)

        self.b_1 = QPushButton("1", self)
        self.hbox_third.addWidget(self.b_1)
        self.b_2 = QPushButton("2", self)
        self.hbox_third.addWidget(self.b_2)
        self.b_3 = QPushButton("3", self)
        self.hbox_third.addWidget(self.b_3)
        self.b_plus = QPushButton("+", self)
        self.hbox_third.addWidget(self.b_plus)

        self.b_0 = QPushButton("0", self)
        self.hbox_fourth.addWidget(self.b_0)
        self.b_float = QPushButton(".", self)
        self.hbox_fourth.addWidget(self.b_float)
        self.b_erase = QPushButton("DEL", self)
        self.hbox_fourth.addWidget(self.b_erase)
        self.b_divide = QPushButton("÷", self)
        self.hbox_fourth.addWidget(self.b_divide)

        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)

        # создаем события, отвечающие за реакции на нажатия по кнопкам
        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_multiply.clicked.connect(lambda: self._operation("×"))
        self.b_divide.clicked.connect(lambda: self._operation("÷"))
        self.b_result.clicked.connect(self._result)

        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_0.clicked.connect(lambda: self._button("0"))

        self.b_float.clicked.connect(lambda: self._button("."))
        self.b_erase.clicked.connect(lambda: self._button("DEL"))

    # Создаем метод класса для обработки кнопок, отвечающих за ввод цифр в линию ввода текста
    def _button(self, param):
        line = self.input.text()
        if param == "DEL":
            self.input.setText(line[:-1])
        else:
            line = self.input.text()
            self.input.setText(line + param)

    # Создаем метод класса для обработки нажатия на кнопку математической операции
    def _operation(self, op):
        line = self.input.text()
        if is_digit(line):
            self.num_1 = int_whether_float(line)
            self.op = op
            self.input.setText("")
        else:
            self.output.setText("Syntax Error")

    def _result(self):
        line = self.input.text()
        if is_digit(line):
            self.num_2 = int_whether_float(line)
            if self.op == "+":
                result = int_whether_float(self.num_1 + self.num_2)
            if self.op == "-":
                result = int_whether_float(self.num_1 - self.num_2)
            if self.op == "×":
                result = int_whether_float(self.num_1 * self.num_2)
            if self.op == "÷":
                if self.num_2 == 0:
                    result = "You can't divide by zero!"
                else:
                    result = int_whether_float(self.num_1 / self.num_2)
            self.output.setText(str(result))
        else:
            self.output.setText("Syntax Error")
        self.input.setText("")


app = QApplication(sys.argv)
win = Calculator()
win.show()
sys.exit(app.exec_())
