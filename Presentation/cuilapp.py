from PyQt6.QtWidgets import QApplication,QDialog;
from FirstDialog import Ui_Dialog
from DniDialog import Ui_Dialog
from Business.calculator import cuilCalculator;

class MyDialog(QDialog,Ui_Dialog):
    def __init__(self,parent=None):
        super(MyDialog, self).__init__(parent);
        self.setupUi(self);
        # self.btn_cancel.clicked.connect(self.ButtonPressed(" "));
        self.lbl_invisible.hide();
        self.btn_cancel.clicked.connect(self.ButtonCancel);
        # self.btn_ok.pressed.connect(self.ButtonPressed);
        self.btn_ok.released.connect(self.ButtonCancel);
        # self.btn_ok.clicked.connect(self.ButtonClick);
        self.btn_ok.clicked.connect(self.cmbSelected);
        self.btn_ok.clicked.connect(self.byeInvisible);
        self.btn_cancel.clicked.connect(self.byeInvisible);
        # self.btn_ok
        
        self.cmb_Genre.addItem("Masculino",'M');
        self.cmb_Genre.addItem("Femenino",'F');
        
        
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
            self.lbl_invisible.setText(f"{e.args[0]}");
        

def run():      
    app=QApplication([]);
    window=MyDialog();
    window.show();
    app.exec();

