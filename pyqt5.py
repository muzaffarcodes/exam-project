# 4 - masalaning javobi
# PyQt5
import sys 
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout,QPushButton,QWidget,QApplication,QLabel,QTextEdit,QLineEdit

class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.ui_start()
	def ui_start(self):

		self.clear = QPushButton("Clear")
		self.send = QPushButton("Send")
		self.save = QPushButton("Save File")

		self.textBody =QLineEdit()


		h_box = QHBoxLayout()
		h_box.addWidget(self.textBody)
		h_box.addWidget(self.clear)
		h_box.addWidget(self.send)
		h_box.addWidget(self.save)

		v_box = QVBoxLayout()
		v_box.addLayout(h_box) # Birlashtir

		self.setLayout(v_box)
		self.setFixedSize(600,150)

		self.clear.clicked.connect(self.function)
		self.send.clicked.connect(self.function)
		self.save.clicked.connect(self.filega_saqla)
		
		self.show()

	def filega_saqla(self):
		with open("filega_saqla.txt","a") as file:
			matn = self.textBody.text() 
			file.write(matn)
			file.write("\n")
	def function(self):
		if(self.sender().text() == "Clear"):
			self.textBody.clear()
		elif(self.sender().text() == "Send"):
			print(self.textBody.text())

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
