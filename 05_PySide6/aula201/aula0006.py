# Trabalhando com classes e herança no PySide6

import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication, QPushButton, QWidget, QGridLayout, QMainWindow
)


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.central_widget = QWidget()
        
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Minha janela bonita')
        
        # Botão
        self.botao1 = self.make_button('Texto do botão')
        self.botao1.clicked.connect(self.second_marked_action)  # type: ignore

        self.botao2 = self.make_button('Botão 2')

        self.botao3 = self.make_button('Terceiro')

        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)
        
        self.grid_layout.addWidget(self.botao1, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.botao2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.botao3, 3, 1, 1, 2)

        # Status bar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Mensagem Status Bar')

        # Menu Bar
        self.menu = self.menuBar()
        self.first_menu = self.menu.addMenu('Menu')
        self.first_action = self.first_menu.addAction('Action')
        self.first_action.triggered.connect(self.change_statusbar_message)

        self.second_action = self.first_menu.addAction('Sec Action')
        self.second_action.setCheckable(True)
        self.second_action.toggled.connect(self.second_marked_action)
        # self.second_action.hovered.connect(self.second_marked_action)
        
    @Slot()
    def change_statusbar_message(self):
        self.status_bar.showMessage('O meu slot foi executado')

    @Slot()
    def second_marked_action(self):
        print('Está marcado?', self.second_action.isChecked())
        
    def make_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet('font-size: 80px')
        return btn


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show() # Window widget entra na hierarquia e mostra a janela
    app.exec()
