from time import time
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit

app = QApplication([])
win_x, win_y = 200, 100
win_width, win_height = 1000, 600

# window 1

main_win = QWidget()

main_win.setWindowTitle('Здоровье')
main_win.resize(win_width, win_height)
main_win.move(win_x, win_y)

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
work_win.resize(win_width, win_height)
work_win.move(win_x, win_y)

work_win.setWindowTitle('Здоровье')
work_win.resize(1000, 600)

main_H_layout_2 = QHBoxLayout()
left_v_layout = QVBoxLayout()
right_v_layout = QVBoxLayout()

txt_fio = QLabel('Введите Ф.И.О.:')
txt_age = QLabel('Полных лет:')
txt_test_1 = QLabel('Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер.\nРезультат запишите в соответствующее поле.')
txt_test_2 = QLabel('Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания",\nчтобы запустить счетчик приседаний.')
txt_test_3 = QLabel('Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.\nНажмите кнопку "Начать финальный тест", чтобы запустить таймер.\nЗеленым обозначены секунды, в течение которых необходимо\nпроводить измерения, черным - минуты без замера пульсаций. Результаты запишите в соответствующие поля.')

but_start_1 = QPushButton('Начать первыей тест')
but_start_2 = QPushButton('Начать делать приседания')
but_start_3 = QPushButton('нНачать финальный тест')
but_result = QPushButton('Отправить результаты')

line_1_fio = QLineEdit('Ф.И.О.')
line_2_age = QLineEdit('0')
line_3_res = QLineEdit('0')
line_4_res = QLineEdit('0')
line_5_res = QLineEdit('0')

time = QTime(0, 0, 15)
txt_timer = time.toString('hh:mm:ss')
text_timer = QLabel(txt_timer)
text_timer.setFont(QFont('Times', 30, QFont.Bold))

left_v_layout.addWidget(txt_fio)
left_v_layout.addWidget(line_1_fio, alignment = Qt.AlignLeft)
left_v_layout.addWidget(txt_age)
left_v_layout.addWidget(line_2_age, alignment = Qt.AlignLeft)
left_v_layout.addWidget(txt_test_1)
left_v_layout.addWidget(but_start_1, alignment = Qt.AlignLeft)
left_v_layout.addWidget(line_3_res, alignment = Qt.AlignLeft)
left_v_layout.addWidget(txt_test_2)
left_v_layout.addWidget(but_start_2, alignment = Qt.AlignLeft)
left_v_layout.addWidget(txt_test_3)
left_v_layout.addWidget(but_start_3, alignment = Qt.AlignLeft)
left_v_layout.addWidget(line_4_res, alignment = Qt.AlignLeft)
left_v_layout.addWidget(line_5_res, alignment = Qt.AlignLeft)
left_v_layout.addWidget(but_result, alignment = Qt.AlignCenter)
right_v_layout.addWidget(text_timer)

main_H_layout_2.addLayout(left_v_layout)
main_H_layout_2.addLayout(right_v_layout)
work_win.setLayout(main_H_layout_2)

# window 3

result_win = QWidget()
result_win.setWindowTitle('Результат')
result_win.resize(win_width, win_height)
result_win.move(win_x, win_y)

txt_index = QLabel('Индекс Руфье: ')
txt_res = QLabel('Работоспособность сердца: ')

main_v_layout_3 = QVBoxLayout()
main_v_layout_3.addWidget(txt_index, alignment = Qt.AlignCenter)
main_v_layout_3.addWidget(txt_res, alignment = Qt.AlignCenter)

result_win.setLayout(main_v_layout_3)


# button work

def next_win2():
    main_win.hide()
    work_win.show()

def next_win3():
    work_win.hide()
    result_win.show()

def test1():
    pass

def test2():
    pass

def test3():
    pass

button_start.clicked.connect(next_win2)
but_result.clicked.connect(next_win3)
but_start_1.clicked.connect(test1)
but_start_2.clicked.connect(test2)
but_start_3.clicked.connect(test3)



main_win.show()
#work_win.show()
#result_win.show()
app.exec()


