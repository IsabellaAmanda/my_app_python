import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt

#crear una ventana de interfaz 
class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Ventana de Inicio")
        self.setGeometry(100, 100, 400, 200)
        
        #estilo y colores
        
        TITLE_COLOR = "#2E86C1"
        BACKGROUND_COLOR = "#F2F3F4"
        self.setStyleSheet(f"background-color: {BACKGROUND_COLOR}; color: {TITLE_COLOR};")
        #fondo de pantalla
        self.setStyleSheet("""
            QWidget {
                background-image: url('Fascinating-Examples-Of-Firefly-Photography00002-1-255x385.jpg');
                background-repeat: no-repeat;
                background-position: center;   
                background-size: cover;
            }
        """)
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
        
    def start_app(self):
        print("La APP esta Iniciando...\n")
        self.message.setText("La APP esta Comenzando!")
        self.button.setEnabled(False) #deshabilitar el boton despues de hacer click
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    wind = Windows()
    wind.show()
    sys.exit(app.exec_())