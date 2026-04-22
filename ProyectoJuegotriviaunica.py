# Isabella Cordero - Proyecto Vision JSON PRO - Edition
"""
    Librerias
    - PyQt5: Para la interfaz gráfica de usuario (GUI).
    - json: Para manejar la lectura y escritura de archivos JSON.
    - sys: Para manejar la salida del programa.
    - os: Para manejar rutas de archivos y verificar su existencia.
    - PIL (Pillow): Para la manipulación de imágenes, como abrir, editar y guardar

"""
#Para convertir la imagen de Pillow a un formato compatible con PyQt5 y mostrarla en el QLabel
#Para alinear el texto en el centro del QLabel
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QMessageBox,QLabel, QPushButton, QFileDialog, QGroupBox, QInputDialog, QColorDialog
from PyQt5.QtGui import QImage, QPixmap, QMovie
from PyQt5.QtCore import Qt, QSize
import json
import sys 
import os
from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageColor, ImageFont


class VisionImg(QWidget):
    """
        Clase prinicipal del programa, heredada de la clase  QWidget de PyQt5, que representa la ventana principal de la aplicación.
        Esta clase contiene la lógica para cargar imágenes, mostrar etiquetas, editar imágenes con Pillow y guardar
        los cambios en un archivo JSON. Además, maneja la interfaz gráfica y las interacciones del usuario. 
    """
    def __init__(self):
        """
            Constructor de la clase VisionImg
            - Inicializa la interfaz gráfica, carga los datos del archivo JSON y aplica el estilo a la aplicación.
        """
        super().__init__()
        self.pil_img = None
        self.ruta_actual = ""
        
        self.data_img = []
        self.initUI()
        self.load_data_json()
        self.app_style()
        
        
    
    def initUI(self):
        # Configuración de la ventana principal
        self.setWindowTitle("Vision JSON PRO - Edition")
        self.setGeometry(100,100,1100,800)
        
        #layout principal horizontal
        layout_main = QHBoxLayout()
        layout_central = QVBoxLayout()
        layout_right = QVBoxLayout()
        
        #columna izq: lista
        self.list_names = QListWidget()
        self.list_names.setFixedWidth(250)
        self.list_names.itemClicked.connect(self.show_img)
        print("Conexion establecida")
        
        #columna central: imagen y descripcion
        """
            self.label_img: QLabel que actúa como un canvas para mostrar la imagen seleccionada.
            self.label_descri: QLabel que muestra las etiquetas asociadas a la imagen seleccionada.
        
        """
        self.label_img = QLabel("Seleccione una Imagen")
        self.label_img.setAlignment(Qt.AlignCenter)
        self.label_img.setObjectName("CanvasImagen")
        self.label_img.setStyleSheet("""
            QLabel#CanvasImagen{ background-color: #121212; border: 2px solid #333; border-radius: 10px; }
        """)
        #descripcion y etiquetas
        """
            self.label_descri: QLabel que muestra las etiquetas asociadas a la imagen seleccionada.
            - Se inicializa con el texto "Etiquetas: -" y se configura para permitir el 
            ajuste de texto y un estilo de fuente más grande con padding para mejorar la legibilidad.
        """
        self.label_descri = QLabel("Etiquetas: -")
        self.label_descri.setWordWrap(True)
        self.label_descri.setStyleSheet("font-size: 14px; padding: 10px;")
        
        # Agregar widgets al layout central
        """
            Se agregan el QLabel para la imagen y el QLabel para la descripción al layout central, 
            asignando un stretch de 3 a la imagen para que ocupe más espacio verticalmente, y un 
            stretch de 1 a la descripción para que ocupe menos espacio.
        """
        layout_central.addWidget(self.label_img,stretch=3)
        layout_central.addWidget(self.label_descri, stretch=1)
        
        # Area de Imagen y descripcion (derecha) - Nueva
        #columna derecha: botones y edit
        """
            Se crea un QGroupBox llamado "File" que contiene dos botones: "NEW Open" para seleccionar 
            una nueva imagen y "Save - JSON" para guardar los cambios en el archivo JSON.
            Se conecta cada botón a su respectiva función: select_file para abrir el diálogo de selección
        """         
        team_file = QGroupBox("File")
        layout_file = QVBoxLayout()
        button_select = QPushButton("NEW Open")
        button_select.clicked.connect(self.select_file)
        button_save = QPushButton("Save - JSON")
        button_save.clicked.connect(self.save_file)
        layout_file.addWidget(button_select)
        layout_file.addWidget(button_save)
        team_file.setLayout(layout_file)
        
        #Grupo Edition (Pillow)
        """
            Se crea un QGroupBox llamado "Edition Pro" que contiene botones para editar
            la imagen seleccionada.
            Cada botón está conectado a una función que realiza una operación de 
            edición específica utilizando la biblioteca Pillow:
            - "Girar 90"
            - "Escala Grises"
            - "Blur-Desenfoque"
            - "Draw-Texto"
            - "Change Color"
            - "Change Font"
            - "Save Edit"
            - "Reset Edit" - para cargar la imagen original después de editarla.
        
        """
        team_edit = QGroupBox("Edition Pro")
        layout_edit = QVBoxLayout()
        button_girar = QPushButton("Girar 90")
        button_girar.clicked.connect(self.girar_edit)
        button_grays = QPushButton("Escala Grises")
        button_grays.clicked.connect(self.grays_edit)
        button_blur = QPushButton("Blur-Desenfoque")
        button_blur.clicked.connect(self.blur_edit)
        button_draw = QPushButton("Draw-Texto")
        button_draw.clicked.connect(self.draw_edit)
        button_change_color = QPushButton("Change Color")
        button_change_color.clicked.connect(self.change_color_edit)
        button_save_edit = QPushButton("Save Edit")
        button_save_edit.clicked.connect(self.save_edit)
        button_reset = QPushButton("Reset Edit")
        button_reset.clicked.connect(self.reset_edit)
        layout_edit.addWidget(button_girar)
        layout_edit.addWidget(button_grays)
        layout_edit.addWidget(button_blur)
        layout_edit.addWidget(button_draw)
        layout_edit.addWidget(button_change_color)
        layout_edit.addWidget(button_save_edit)
        layout_edit.addWidget(button_reset)
        team_edit.setLayout(layout_edit)
        
        # Boton de eliminar registro
        """
            Se crea un botón llamado "Delete record" que permite al usuario eliminar 
            un registro de la lista.
            Al hacer clic en el botón, se llama a la función delete_record.
        
        """
        self.button_delete = QPushButton("Delete record")
        self.button_delete.setObjectName("BtnPeligro")
        self.button_delete.clicked.connect(self.delete_record)
        
        # Agregar widgets al layout derecho
        """
            Se agrega cada grupo de widgets al layout derecho.
        """
        layout_right.addWidget(team_file)
        layout_right.addWidget(team_edit)
        layout_right.addStretch()
        layout_right.addWidget(self.button_delete)
        
        # Agregar columnas al layout principal
        """
            Se agregan la lista de nombres al layout principal, luego se agregan el layout central y el layout derecho al layout principal. 
            Finalmente, se establece el layout principal como el layout de la ventana.
        """
        layout_main.addWidget(self.list_names)
        layout_main.addLayout(layout_central)
        layout_main.addLayout(layout_right) 
        
        self.setLayout(layout_main)
    
    # Funciones de edición de imagen con Pillow

        """
            Cada función de edición de imagen realiza una operación específica utilizando 
            la biblioteca Pillow:
        """
    # Funcion para rotar la imagen 90 grados
        """
        - girar_edit: gira la imagen 90 grados en sentido antihorario.
        """
    def girar_edit(self):
        if self.pil_img:
            self.pil_img = self.pil_img.rotate(-90, expand=True)
            self.load_wind()
        else:
            QMessageBox.warning(self, "Aviso", "Primero selecciona una imagen de la lista.")
        
    #Funcion para convertir la imagen a escala de grises
        """
            - grays_edit: convierte la imagen a escala de grises.
        """
    def grays_edit(self):
        if self.pil_img:
            self.pil_img = ImageOps.grayscale(self.pil_img).convert("RGB")
            self.load_wind()
    
    #Funcion para aplicar un filtro de desenfoque a la imagen
        """
            - blur_edit: aplica un filtro de desenfoque a la imagen.
        """
    def blur_edit(self):
        if self.pil_img:
            self.pil_img = self.pil_img.filter(ImageFilter.BLUR)
            self.load_wind()
    
    #Funcion para dibujar texto sobre la imagen
        """
            - draw_edit: permite al usuario dibujar texto sobre la imagen, eligiendo el
            color y la fuente.
        """
    def draw_edit(self):
        if not self.pil_img:
            QMessageBox.warning(self, "Aviso", "Selecciona una imagen primero.")
            return
        text, ok = QInputDialog.getText(self, "Texto", "Escribe el texto a dibujar:")
        if ok and text:
            color = QColorDialog.getColor()
            if color.isValid():
                draw = ImageDraw.Draw(self.pil_img)
                # Convertir QColor a tupla RGB
                rgb = (color.red(), color.green(), color.blue())
                # Intentar usar una fuente más visible (opcional)
                try:
                    # elegimos una fuente común y un tamaño grande para que el texto sea visible
                    # tamaño dinámico basado en el tamaño de la imagen
                    tam, tam_ok = QInputDialog.getInt(self, "Tamaño de Fuente", "Ingrese el tamaño de la fuente:", value=40, min=10, max=10000000)
                    font_size = tam if tam_ok else 40
                    font = ImageFont.truetype("arial.ttf", font_size)
                
                except:
                    font = ImageFont.load_default()
                
                # Dibujar el texto en donde el user quiera
                x, ok_X = QInputDialog.getInt(self, "Posición", "Ingrese la coordenada X:", value=0, min=0, max=self.pil_img.width)
                y, ok_Y = QInputDialog.getInt(self, "Posición", "Ingrese la coordenada Y:", value=0, min=0, max=self.pil_img.height)
                
                pos_x = x if ok_X else 0
                pos_y = y if ok_Y else 0
                
                draw.text((pos_x, pos_y), text, fill=rgb, font=font)
                self.load_wind()
                # Debug
                print(f"Texto dibujado: '{text}' en color {rgb}, dibujado en posición ({pos_x}, {pos_y}) con tamaño de fuente {font_size}")
            else:
                print("Color no válido")
    
    #Funcion para cambiar el color de la imagen
        """ 
        - change_color_edit: permite al usuario cambiar el color de la imagen.
        """
    def change_color_edit(self):
        color = QColorDialog.getColor()
        if color.isValid():
            r, g, b = color.red(), color.green(), color.blue()
            #  mezclar imagen original con el color sólido
            tint = Image.new('RGB', self.pil_img.size, (r, g, b))
            self.pil_img = Image.blend(self.pil_img, tint, 0.5)
            self.load_wind()
    
    #Funcion para guardar la imagen editada en la misma ruta del archivo original
        """
            - save_edit: guarda la imagen editada en la misma ruta del archivo original.
            - Verifica que haya una imagen cargada y una ruta válida, luego guarda la imagen  
        """
    def save_edit(self):
        if self.pil_img and self.ruta_actual:
            try:
                # Guardar la imagen editada en la misma ruta
                directorio_base = os.path.dirname(os.path.abspath(__file__))
                ruta_final = os.path.join(directorio_base, self.ruta_actual)
                self.pil_img.save(ruta_final)
                QMessageBox.information(self, "Save Edit", "Imagen editada guardada correctamente.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo guardar la imagen editada: {e}")
        else:
            QMessageBox.warning(self, "Aviso", "Primero selecciona una imagen de la lista para editar.")  
    
    #Funcion para resetear la imagen original
        """
            - reset_edit: resetea la imagen original.   
            - Verifica que haya una ruta válida, luego vuelve a cargar la imagen original desde el disco,
            reemplazando la imagen editada en memoria y actualizando la visualización.
        """
    def reset_edit(self):
        if self.ruta_actual:
            try:
                directorio_base = os.path.dirname(os.path.abspath(__file__))
                ruta_final = os.path.join(directorio_base, self.ruta_actual)
                self.pil_img = Image.open(ruta_final).convert("RGB")
                self.load_wind()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo cargar la imagen original: {e}")
        else:
            QMessageBox.warning(self, "Aviso", "No hay una imagen seleccionada para resetear.")  
    
    #Funcion para cargar la imagen en el QLabel después de editarla
        """ 
            - load_wind: carga la imagen editada en el QLabel después de editarla.
            - Convierte la imagen de Pillow a un formato compatible con PyQt5 y 
            la muestra en el QLabel.
        """
    def load_wind(self):
        
        try:
            
            img_rgba = self.pil_img.convert("RGBA")
            data = img_rgba.tobytes("raw", "RGBA")
            
            #pix = ImageQt.toqpixmap(self.pil_img)
            
            q_img = QImage(data, img_rgba.width, img_rgba.height, QImage.Format_RGBA8888)
            
            pix = QPixmap.fromImage(q_img)
            
            if pix.isNull():
                print("Error: QPixmap nulo")
            else:
                pix = pix.scaled(600, 400, Qt.KeepAspectRatio,Qt.SmoothTransformation)
                
            self.label_img.setPixmap(pix)
            print("Pixmap asignado correctamente")   # DEBUG
        except Exception as e:
            print(f"Excepción en load_wind: {e}")
        
        
    #Funcion para seleccionar una nueva imagen y agregarla a la lista
        """     
            - select_file: permite al usuario seleccionar una nueva imagen y agregarla a la lista.
            - Abre un diálogo de selección de archivos, valida que el archivo seleccionado sea una imagen válida, 
            guarda la ruta relativa en el diccionario de datos, muestra el nombre del archivo en la lista y 
            selecciona automáticamente la nueva imagen para mostrarla.
        """
    def select_file(self):
        ruta, _ = QFileDialog.getOpenFileName(self, "Picture Select","", "Images (*.png *.jpg *.ppm *.jpeg *.bmp *.gif *.webp *.html *.svg *.ico *.tiff *.tif)")
        if ruta:
            #validemos la ruta
            try:
                Image.open(ruta).verify()
            except Exception:
                QMessageBox.warning(self, "Error", "El archivo no es una imagen valida")
                
                return
            
            #guardar la ruta relativa
            
            directorio_base = os.path.dirname(os.path.abspath(__file__))
            ruta_relativa = os.path.relpath(ruta, directorio_base)
            
            next_img = {"Files": ruta_relativa, "Tags": ["Nuevo"]}
            self.data_img.append(next_img)
            
            #mostrar el nombre del archivo
            self.list_names.addItem(ruta_relativa)
            
            #seleccionar y mostrar automaticamente la nueva img
            self.list_names.setCurrentRow(len(self.data_img) - 1)
            self.show_img(self.list_names.currentItem())
    
    #Funcion para cargar los datos del archivo JSON y mostrar los nombres de las imágenes en la lista
        """
            - load_data_json: carga los datos del archivo JSON y muestra los nombres 
            de las imágenes en la lista.
            - Lee el archivo "trials_1.json", extrae la lista de imágenes y sus etiquetas, 
            y llena la QListWidget con 
            los nombres de los archivos. Si el archivo no existe, inicializa la lista de 
            datos como vacía.
        """        
    def load_data_json(self):
        try:
            with open("trials_1.json","r", encoding="utf-8") as file:
                full_data = json.load(file)
                
                self.data_img = full_data.get("Imagenes", [])
                for item in self.data_img:
                    self.list_names.addItem(item.get("Files", "Sin nombre"))
        except FileNotFoundError:
            self.data_img = []
            
    #Funcion para mostrar la imagen seleccionada en el QLabel y sus etiquetas en la descripción
        """ 
            - show_img: muestra la imagen seleccionada en el QLabel y sus etiquetas en la descripción.
            - Obtiene la ruta del archivo seleccionado, verifica su existencia, abre la imagen con Pillow, 
            la muestra en el QLabel y actualiza las etiquetas en la descripción. Si el archivo no existe, 
            muestra un mensaje de error en el QLabel.
            """        
    def show_img(self, item):
        #Buscar datos en el diccionario
        # 1. Obtenemos el texto del elemento seleccionado
        self.ruta_actual = item.text()
        directorio_base = os.path.dirname(os.path.abspath(__file__))
        ruta_final = os.path.join(directorio_base, self.ruta_actual)
        print(f"Texto del item: {self.ruta_actual}")
        print(f"Ruta final: {ruta_final}")
        print(f"Existe? {os.path.exists(ruta_final)}")
        
        # 3. Verificamos si el archivo realmente existe en el disco
        if os.path.exists(ruta_final):
            try:
                if hasattr(self, "movie") and self.movie:
                    self.movie.stop()
                    
                # Abrimos con Pillow y convertimos a RGB para evitar errores de color
                if ruta_final.lower().endswith('.gif'):
                    # Si es un GIF, mostramos la animación
                    self.movie = QMovie(ruta_final)
                    self.movie.setScaledSize(QSize(600, 400))
                    
                    self.label_img.setMovie(self.movie)
                    self.movie.start()
                    self.pil_img = None
                else:
                    self.label_img.setMovie(None)  # Detener cualquier animación previa
                    self.pil_img = Image.open(ruta_final).convert("RGB")
                    self.load_wind()
                    
                for img in self.data_img:
                    if img["Files"] == self.ruta_actual:
                        tags = ", ".join(img.get("Tags", []))
                        self.label_descri.setText(f"Etiquetas: {tags}")
                        break
            except Exception as e:
                self.label_img.setText(f"Error al cargar la imagen: {e}")
        else:
            self.label_img.clear()
            self.label_img.setText(f"No se encontró la imagen: {self.ruta_actual}")
            self.label_descri.setText("Etiquetas: -")
            
    #Funcion para guardar los cambios en el archivo JSON
        """ 
            - save_file: guarda los cambios en el archivo JSON.
            - Escribe la lista de imágenes y sus etiquetas en el archivo "trials_1.json" con 
            formato JSON. Si ocurre un error durante la escritura, muestra un mensaje de error.
        """
    def save_file(self):
        try:
            with open("trials_1.json", "w", encoding="utf-8") as file:
                json.dump( {"Imagenes": self.data_img}, file, indent=4)
            QMessageBox.information(self, "Save", "Json download")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"no se pudo guardar: {e}")
    
    #Funcion para eliminar un registro de la lista
        """
            - delete_record: elimina un registro de la lista.
            - Elimina la imagen seleccionada de la lista, borra su entrada en el diccionario de datos,
            limpia el canvas y la descripción. Si no hay una imagen seleccionada, muestra un mensaje 
            de advertencia.
        """
    def delete_record(self):
        row = self.list_names.currentRow()
        if row >= 0:
            self.data_img.pop(row)
            self.list_names.takeItem(row)
            self.label_img.clear()
            self.label_img.setText("Delete Picture")
            self.label_descri.setText("Etiquetas: -")
            self.pil_img = None          # ← limpiar imagen en memoria
            self.ruta_actual = ""
    
    #Funcion para aplicar estilo a la aplicación
        """ 
            - app_style: aplica estilo a la aplicación.
            - Define un estilo personalizado para los widgets de la aplicación utilizando CSS. 
            Esto incluye colores de fondo, colores de texto, estilos de borde, fuentes y efectos de hover para los botones.
            El estilo se aplica a toda la aplicación para mejorar la apariencia visual y la experiencia del usuario.
        """
    def app_style(self):
        self.setStyleSheet("""
            QPushButton:Pressed { background-color: #89b4fa; color: #11111b; }
            QWidget { background-color: #1e1e2e; color: #cdd6f4; font-family: 'Segoe UI'; }
            QListWidget { background-color: #181825; border: none; padding: 5px; }
            QListWidget::item { padding: 10px; border-bottom: 1px solid #313244; }
            QListWidget::item:selected { background-color: #89b4fa; color: #1e1e2e; }
            QLabel#CanvasImagen { background-color: #11111b; border: 2px solid #89b4fa; border-radius: 10px; }
            QPushButton { background-color: #313244; border-radius: 5px; padding: 8px; min-height: 20px; }
            QPushButton:hover { background-color: #45475a; }
            QPushButton#BtnPeligro { background-color: #f38ba8; color: #1e1e2e; }
            QGroupBox { font-weight: bold; border: 1px solid #45475a; margin-top: 15px; padding-top: 10px; }
            """)

#Cuerpo principal
        """
            - El bloque principal del programa crea una instancia de QApplication, 
            luego crea una instancia de VisionImg, muestra la ventana y ejecuta el 
            bucle de eventos de la aplicación. Esto permite que la interfaz gráfica 
            se muestre y responda a las interacciones del usuario.
        """

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    visor = VisionImg()
    visor.show()
    sys.exit(app.exec_())