from PyQt6.QtWidgets import QApplication,QDialog,QMainWindow,QFileDialog;
# from FirstDialog import Ui_Dialog
# from DniDialog import Ui_Dialog
from MainDniWindow import Ui_MainWindow;
from Business.calculator import cuilCalculator;
from RouteDialog import Ui_Dialog;
# from MainWindowPractice import Ui_MainWindow;

# class MyDialog(QMainWindow,Ui_MainWindow):
class MyDialog(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MyDialog, self).__init__(parent);
        #Parte DNI
        
        self.setupUi(self);
        # self.btn_cancel.clicked.connect(self.ButtonPressed(" "));
        self.lbl_invisible.hide();
        self.btn_cancel_.clicked.connect(self.ButtonCancel);
        # self.btn_ok.pressed.connect(self.ButtonPressed);
        self.btn_ok_.released.connect(self.ButtonCancel);
        # self.btn_ok.clicked.connect(self.ButtonClick);
        self.btn_ok_.clicked.connect(self.cmbSelected);
        self.btn_ok_.clicked.connect(self.byeInvisible);
        self.btn_cancel_.clicked.connect(self.byeInvisible);
        
        #Agregar datos al CMB
        self.cmb_Genre.addItem("Masculino",'M');
        self.cmb_Genre.addItem("Femenino",'F');
        
        
        
        self.actionExportar.triggered.connect(self.GetFiles);
        # self.menuArchivo.aboutToShow.connect(self.checkInvisibleLabel());
        
        
        #Parte Window Practice
        # self.Ui_MainWindow(self);
        # self.btn_dialog.clicked.connect(self.openDialog);
        # self.actionNuevo.triggered.connect(self.openDialog);
        # self.actionAbrir.triggered.connect(self.openAction);
        # self.cuenta = 0;
        # self.btn_ok
        
    def checkInvisibleLabel(self):
        if not self.lbl_invisible.text():
            self.actionExportar.setEnabled(False)
        else:
            self.actionExportar.setEnabled(True)

    # Llama a esta función en el constructor o en el momento apropiado para verificar el estado
    def GetFiles1(self):
        self.dialog = QFileDialog(); #Agregarle el self para que el objeto siga existiendo una vez abierto.
        var = self.dialog.exec();
        print(self.dialog.selectedFiles());
        
    def GetFiles(self):
        if self.lbl_invisible.text() != "" and self.lbl_invisible.text() != "Error! Complete todos los campos.":
            file_path, _ = QFileDialog.getSaveFileName(
                self, "Guardar archivo", "", "Archivos de texto (*.txt);;Todos los archivos (*)"
            )
            if file_path:
                with open(file_path, 'w') as file:
                    file.write(self.lbl_invisible.text());
                self.statusBar().showMessage(f"Archivo guardado en: {file_path}", 3000)
            else:
                self.statusBar().showMessage("Selección de archivo cancelada.", 3000)
        else:
            self.statusBar().showMessage(f"Imposible guardar un archivo vacio, no se puede exportar.", 3000)
            
        
    def getDialog(self):
        conn = MyRouteDialog();
        conn.exec();
        
    def ButtonClick(self):
        self.lbl_invisible.setText("Botón Accionado");
    # def ButtonPressed(self,texto):
    #     self.lbl_invisible.setText(f"{texto}");
    def byeInvisible(self):
        if self.lbl_invisible.text() == "":    
            # if self.lbl_invisible.isVisible():
            self.lbl_invisible.hide();
        else:
            self.lbl_invisible.show();
    def ButtonCancel(self):
        self.lbl_invisible.setText("");
        #self.close(); #Cierra el Dialog
        
    def ButtonPressed(self):
        self.lbl_invisible.setText("Presionado");
    def ButtonHover(self):
        self.lbl_invisible.setText("Hover");  
        
    def cmbSelected(self):
        # isNumber = int(self.line_dni.text()) if self.line_dni.text().isdigit() else False;
        # not isNumber or
        try:
            if self.cmb_Genre.currentData() == None or self.lbl_invisible.text() == "Error! Complete todos los campos.":
                # text = "";
                text = "Error! Complete todos los campos."
            else:
                conn = cuilCalculator(self.line_dni.text(),self.cmb_Genre.currentData());
                conn.validateDNI();
                cuil = conn.calculate();
                
                text = f"Género {self.cmb_Genre.currentText()}, {self.cmb_Genre.currentData()}, su DNI: {self.line_dni.text()} y su CUIL: {cuil}";
                
            self.lbl_invisible.setText(text);
        except Exception as e:
            # self.lbl_invisible.setText(f"{e.args[0]}");
            self.statusBar().showMessage(f"Error: {e.args[0]}", 3000);
        

class MyRouteDialog(QDialog,Ui_Dialog):
    
    def __init__(self,parent=None):
        super(MyRouteDialog, self).__init__(parent);
        #Parte DNI
        
        self.setupUi(self);
        
        self.btn_cancel_route.clicked.connect(lambda: self.close()); 
    def openDialog(self):
        # self.dialog = MyRouteDialog(); #Agregarle el self para que el objeto siga existiendo una vez abierto.
        self.dialog = QFileDialog(); #Agregarle el self para que el objeto siga existiendo una vez abierto.
        var = self.dialog.exec();
        print(self.dialog.selectedFiles());
        # var = self.dialog.exec();
        self.dialog.exec();
        # # print(var);
        # if var == 0:
        #     print("Se cerró el dialogo"); #Te avisa cuando se cierra el dialogo 
        #     # Devolver 0 o Close(), es lo mismo
def run():      
    app=QApplication([]);
    window=MyDialog();
    window.show();
    app.exec();

