import sys, csv
import mysql.connector
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem

class alumnos_DB(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi(r"C:\Users\Almazan\OneDrive\Escritorio\4TO SEMESTRE\VISUALIZACION\Evidencia 4\Alumnos_DB.ui", self)
        self.fn_init_UI()

   #Generacion de Funcion Init_UI
    def fn_init_UI(self): 
        #self.fn_connectDB(self)  
        self.btn_Connect_DB.clicked.connect(self.fn_connectDB)   
        self.btn_Registrar.clicked.connect(self.fn_registrar)     
        
        #Conectar funcion consultar al boton consultar
        self.btn_Consultar.clicked.connect(self.fn_consultar)
        #Conectar funcion fn_eliminar al boton Eliminar
        self.btn_Eliminar.clicked.connect(self.fn_eliminar)
        
        #Conectar a Funcion que graba hacia la base de datos
        self.btn_Grabar.clicked.connect(self.fn_grabar_DB)

        #Conectar a funcion Leer CSV
        self.btn_Leer.clicked.connect(self.fn_leer_csv)
        

    def fn_connectDB(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Enemigo_apex_77",
        database="db_alumnos"
        )
        print("Database Connected")

    #Grabar hacia la base de datos
    def fn_registrar(self):
        #self.edt_matricula.setText("Funcion Registras a Base de Datos")
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Enemigo_apex_77",
        database="db_alumnos"
        )
#
        mycursor = mydb.cursor()
 
        sql = "INSERT INTO alumnos (matricula, nombres, a_paterno, a_materno, domicilio, ciudad, estado, carrera, sexo, edad, beca, foraneo, ingles, prog, bd, contab,estadistica,inv_op) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        #val = (self.edt_matricula.text(),self.edt_nombre.text(), self.edt_apppat.text(), self.edt_appmat.text(),self.edt_domicilio.text(),self.cbx_ciudad.currentText(),self.cbx_estado.currentText(),self.cbx_carrera.currentText(), 'M')
        
        mat = self.edt_matricula.text()
        nom = self.edt_nombre.text()
        app = self.edt_apppat.text()
        apm = self.edt_appmat.text()
        dom = self.edt_domicilio.text()
        mun = self.cbx_ciudad.currentText()
        edo = self.cbx_estado.currentText()
        car = self.cbx_carrera.currentText()
        if self.radio_hombre.isChecked():
            sex = 'M'
        if self.radio_mujer.isChecked():
            sex = 'F'
        #edad
        eda = self.spinEdad.text()

        #beca
        if self.radio_cero.isChecked():
            bec = '0'
        elif self.radio_50.isChecked():
            bec = '50'
        elif self.radio_80.isChecked():
            bec = '80'
        elif self.radio_100.isChecked():
            bec = '100'

        #foraneo
        if self.chk_foraneo.isChecked():
            foraneo = 1
        else:
            foraneo = 0
        #ingles
        if self.chk_ingles.isChecked():
            ingles = 1
        else:
            ingles = 0

        #materias
        if self.chk_prog.isChecked():
            pro = 1
        else:
            pro = 0
            
        if self.chk_bd.isChecked():
            bad = 1
        else:
            bad = 0

        if self.chk_contab.isChecked():
            contab = 1
        else:
            contab = 0
            
        if self.chk_estadistica.isChecked():
            esta = 1
        else:
            esta = 0

        if self.chk_inv_op.isChecked():
            inv = 1
        else:
            inv = 0

        val = (mat,nom,app,apm,dom,mun,edo,car,sex,eda,bec,foraneo,ingles,pro,bad,contab,esta,inv)



        print(sql)
        print(val)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

    
        #Generacion de Funcion Consultar
    def fn_consultar(self):
        #self.edt_nombre.setText('Funcion Consultar')    
        varb = self.edt_matricula.text()
        #self.edt_matricula.setText("Funcion Registras a Base de Datos")
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Enemigo_apex_77",
        database="db_alumnos"
        )

        mycursor = mydb.cursor()
        
        sql = "SELECT * FROM alumnos WHERE matricula = "+varb

        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        for x in myresult:
            self.edt_matricula.setText(x[1])
            self.edt_nombre.setText(x[2])
            self.edt_apppat.setText(x[3])
            self.edt_appmat.setText(x[4])
            self.edt_domicilio.setText(x[5])
            self.cbx_ciudad.setCurrentText(x[6])
            #--> Agregar funcionalidad del resto de los datos

            #print(x[3])

    def fn_eliminar(self):
        #self.spinEdad.setValue(21)
              #self.edt_matricula.setText("Funcion Registras a Base de Datos")
        varb = self.edt_matricula.text()
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Enemigo_apex_77",
        database="db_alumnos"
        )

        mycursor = mydb.cursor()
        sql = "DELETE FROM alumnos WHERE matricula = "+varb
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")


    #Generacion de Funcion Grabar CSV
    def fn_grabar_DB(self):

        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Enemigo_apex_77",
        database="db_alumnos"
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO alumnos (matricula, nombres, a_paterno, a_materno, domicilio, ciudad, estado, carrera, sexo) VALUES (%s, %s,  %s, %s, %s, %s, %s, %s, %s)"
        val = ""
        #create datafram object recordset
        for row in range(self.Tabla_Datos.rowCount()):          
            for col in range(self.Tabla_Datos.columnCount()):
                #var1 = self.Tabla_Datos.item(row,col).text()

                if col == 0:
                    mat=self.Tabla_Datos.item(row,col).text()
                elif col == 1:
                    nom = self.Tabla_Datos.item(row,col).text()
                elif col == 2:
                    app = self.Tabla_Datos.item(row,col).text()
                elif col == 3:
                    apm = self.Tabla_Datos.item(row,col).text()
                elif col == 4:
                    dom = self.Tabla_Datos.item(row,col).text()
                elif col == 5:
                    mun = self.Tabla_Datos.item(row,col).text()
                elif col == 6:
                    edo = self.Tabla_Datos.item(row,col).text()
                elif col == 7:
                    car = self.Tabla_Datos.item(row,col).text()
                elif col == 8:
                    sex = self.Tabla_Datos.item(row,col).text()

            val =(mat,nom,app,apm,dom,mun,edo,car,sex)

            #print(val)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
            

    #Generacion de Funcion Leer de CSV
    def fn_leer_csv(self):
        #self.edt_apppat.setText('Funcion Leer desde CSV')
        index=0
        with open(r'C:\Proyectos\Python\UI\alumnos2.csv', newline='') as File:  
            reader = csv.reader(File)
            for row in reader:
                #print(row)
                #print(row[0], row[1])

                if index>0:  
                    rowPosition = self.Tabla_Datos.rowCount()
                    self.Tabla_Datos.insertRow(rowPosition)   
        
                    #Campo Matricula
                    newItem = QTableWidgetItem(row[0])
                    self.Tabla_Datos.setItem(rowPosition, 0, newItem); 

                    #Campo Nombre
                    newItem = QTableWidgetItem(row[1])
                    self.Tabla_Datos.setItem(rowPosition, 1, newItem); 

                    #Campo App Paterno
                    newItem = QTableWidgetItem(row[2])
                    self.Tabla_Datos.setItem(rowPosition, 2, newItem); 

                    #Campo App Materno
                    newItem = QTableWidgetItem(row[3])
                    self.Tabla_Datos.setItem(rowPosition, 3, newItem); 

                    #Campo Domicilio
                    newItem = QTableWidgetItem(row[4])
                    self.Tabla_Datos.setItem(rowPosition, 4, newItem); 

                    #Campo Ciudad, pendiente tomar valor del combobox
                    newItem = QTableWidgetItem(row[5])
                    self.Tabla_Datos.setItem(rowPosition, 5, newItem); 

                    #Campo Estado, pendiente tomar valor del combobox
                    newItem = QTableWidgetItem(row[6])
                    self.Tabla_Datos.setItem(rowPosition, 6, newItem); 

                    #Campo Carrera pendiente tomar valor del combobox
                    newItem = QTableWidgetItem(row[7])
                    self.Tabla_Datos.setItem(rowPosition, 7, newItem); 

                    #Campo Sexo
                    newItem = QTableWidgetItem(row[8])
                    self.Tabla_Datos.setItem(rowPosition, 8, newItem); 

                    #Campo Edad
                    newItem = QTableWidgetItem(row[9])
                    self.Tabla_Datos.setItem(rowPosition, 9, newItem); 

                    #Campo Beca
                    newItem = QTableWidgetItem(row[10])
                    self.Tabla_Datos.setItem(rowPosition, 10, newItem); 

                    #Campo Foraneo
                    newItem = QTableWidgetItem(row[11])
                    self.Tabla_Datos.setItem(rowPosition, 11, newItem); 

                    #Campo Habla Ingles
                    newItem = QTableWidgetItem(row[12])
                    self.Tabla_Datos.setItem(rowPosition, 12, newItem); 

                    #Campo Materia Favorita Programacion
                    newItem = QTableWidgetItem(row[13])
                    self.Tabla_Datos.setItem(rowPosition, 13, newItem); 

                    #Campo Materia Favorita Base de Datos
                    newItem = QTableWidgetItem(row[14])
                    self.Tabla_Datos.setItem(rowPosition, 14, newItem); 

                    #Campo Materia Favorita Contabilidad
                    newItem = QTableWidgetItem(row[15])
                    self.Tabla_Datos.setItem(rowPosition, 15, newItem); 

                    #Campo Materia Favorita Estadística
                    newItem = QTableWidgetItem(row[16])
                    self.Tabla_Datos.setItem(rowPosition, 16, newItem); 

                    #Campo Materia Favorita Investigacion de Operaciones
                    newItem = QTableWidgetItem(row[17])
                    self.Tabla_Datos.setItem(rowPosition, 17, newItem); 
                    
                index+=1

 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = alumnos_DB()
    GUI.show()
    sys.exit(app.exec_())
