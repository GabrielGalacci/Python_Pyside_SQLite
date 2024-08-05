import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication, QPushButton, QWidget, QGridLayout, QMainWindow
)


app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha janela bonita')

botao1 = QPushButton('Botão 1')
botao1.setStyleSheet('font-size: 80px;')

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px;')

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px;')

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

@Slot()
def slot_example(status_bar):
    def inner():
        status_bar.showMessage('O meu slot foi executado')
    return inner

@Slot()
def second_slot(checked):
    print('Está marcado?', checked)

@Slot()    
def third_slot(action):
    def inner():
        second_slot(action.isChecked())
    return inner
    
# Status bar
status_bar = window.statusBar()
status_bar.showMessage('Mensagem Status Bar')

# Menu Bar
menu = window.menuBar()
first_menu = menu.addMenu('Menu')
first_action = first_menu.addAction('Action')
first_action.triggered.connect(slot_example(status_bar)
)

second_action = first_menu.addAction('Sec Action')
second_action.setCheckable(True)
second_action.toggled.connect(second_slot)
# second_action.hovered.connect(third_slot(second_action))

botao1.clicked.connect(third_slot(second_action))


window.show() # Window widget entra na hierarquia e mostra a janela
app.exec()
