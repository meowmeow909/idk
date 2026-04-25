from time import time
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit

app = QApplication([])


# window 1

main_win = QWidget()

main_win.setWindowTitle('Здоровье')
main_win.resize(1000, 600)

txt_hello = QLabel('Добро пожаловать в программу по определению состояния здоровья!')
txt_instruction= QLabel('Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.\n'
                    'Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\n'
                    'У испытуемого, находящегося в положении лежа на спине в течение 5 мин, определяют частоту пульса за 15 секунд;\n'
                    'затем в течение 45 секунд испытуемый выполняет 30 приседаний.\n'
                    'После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,\n'
                    'а потом — за последние 15 секунд первой минуты периода восстановления.\n')
button_start = QPushButton('Начать')
main_V_layout_1 = QVBoxLayout()

main_V_layout_1.addWidget(txt_hello)
main_V_layout_1.addWidget(txt_instruction)
main_V_layout_1.addWidget(button_start, alignment = Qt.AlignCenter)
main_win.setLayout(main_V_layout_1)

# window 2

work_win = QWidget()

work_win.setWindowTitle('Здоровье')
work_win.resize(1000, 600)

main_H_layout_2 = QHBoxLayout()
left_v_layout = QVBoxLayout()
right_v_layout = QVBoxLayout()

main_H_layout_2.addLayout(left_v_layout)
main_H_layout_2.addLayout(right_v_layout)
work_win.setLayout(main_H_layout_2)

# window 3

result_win = QWidget()
result_win.setWindowTitle('Результат')
result_win.resize(800, 900)

txt_index = QLabel('Индекс Руфье: ')
txt_res = QLabel('Работоспособность сердца: ')

main_v_layout_3 = QVBoxLayout()
main_v_layout_3.addWidget(txt_index, alignment = Qt.AlignCenter)
main_v_layout_3.addWidget(txt_res, alignment = Qt.AlignCenter)

result_win.setLayout(main_v_layout_3)









main_win.show()
result_win.show()
app.exec()


