import sys
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

botao = QPushButton('Texto do Botão')
botao.setStyleSheet('font-size: 40px;')
botao.show() # Adiciona o Widget na hierarquia e exibe a janela

# Com 2 botôes dessa forma vão ser abertas 2 janelas
# botao2 = QPushButton('Texto do Botão2')
# botao.show()

app.exec()

####
