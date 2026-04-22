import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush

#crear una ventana de interfaz 
class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Ventana de Inicio")
        self.setGeometry(100, 100, 600, 400)
        
        #ruta de acceso a  la imagen de fondo
        self.background_path = os.path.abspath(r"C:/Users/nexxus/Downloads/Fascinating-Examples-Of-Firefly-Photography00002-1-255x385.jpg")
        print("Ruta usada:", self.background_path)
        print("Imagen Cargada?", not QPixmap(self.background_path).isNull())
        
        
        #crear un QLabel para el titulo
        #titulo ventana de inicio
        self.acceptDropsTitle = QLabel("Bienvenido a mi APP", self)
        self.acceptDropsTitle.setAlignment(Qt.AlignCenter)#centrar horizontalmente y verticalmente
        self.acceptDropsTitle.setStyleSheet("font-size : 20px; font-weight: bold;")
        
        #subtitulo de la ventanapP
        self.subtittle = QLabel("Seleccione una opcion > Es hora de comenzar")
        self.subtittle.setAlignment(Qt.AlignCenter)#centrar horizontalmente y verticalmente
        self.subtittle.setStyleSheet("font-size : 14px; color: grey;")
        
        #mensaje 
        self.message = QLabel(" ", self)
        self.message.setAlignment(Qt.AlignCenter)
        self.message.setStyleSheet("font-size : 16px; color: green;")
        #Boton de inicio
        self.button = QPushButton("Started")
        self.button.setStyleSheet("font-size: 16px; padding: 8px;")
        self.button.clicked.connect(self.start_app)
        
        #Layout para centrarlo en la ventana
        layout = QVBoxLayout()
        layout.addWidget(self.acceptDropsTitle)
        layout.addWidget(self.subtittle)
        layout.addSpacing(20)
        layout.addWidget(self.button, alignment=Qt.AlignCenter)
        layout.addWidget(self.message)
        layout.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)
    
        self.update_background()
    
    def resizeEvent(self, event):
        #se ejecuta cada vez que la ventana se cambia de tamanio
        self.update_background()
        super().resizeEvent(event)
        
    def update_background(self):
        #escala la imagen al tamanio actual de la ventana
        pixmap = QPixmap(self.background_path).scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(pixmap))
        self.setPalette(palette)
        self.setAutoFillBackground(True)
        #print(QPixmap(self.background_path).isNull())
        
    def start_app(self):
        print("La APP esta Iniciando...\n")
        self.message.setText("La APP esta Comenzando!")
        self.button.setEnabled(False) #deshabilitar el boton despues de hacer click
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    wind = Windows()
    wind.show()
    sys.exit(app.exec_())
    