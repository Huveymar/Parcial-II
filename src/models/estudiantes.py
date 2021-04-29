from src.configs.db import DB

class Estudiantes:
    def guardar(self, datos):
        print(datos)
        cursor = DB.cursor()
        cursor.execute("INSERT INTO estudiantes(identificacion, nombres, apellidos, celular, email, semestre) VALUES(?,?,?,?,?,?)", (datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],))
        cursor.close()
    
    def editar(self, datos):
        print(datos)
        cursor = DB.cursor()
        consulta = f"UPDATE estudiantes SET identificacion='{datos[1]}',nombres='{datos[2]}',apellidos='{datos[3]}',celular='{datos[4]}',email='{datos[5]}',semestre='{datos[6]}' WHERE id={datos[0]}"
        cursor.execute(consulta)
        cursor.close()

    def eliminar(self, id):
        cursor = DB.cursor()
        cursor.execute("DELETE FROM estudiantes WHERE id=?", (id,))
        cursor.close()

    def get_estudiantes(self):
        cursor = DB.cursor()
        cursor.execute("SELECT * FROM estudiantes")
        estudiantes = cursor.fetchall()
        cursor.close()

        return estudiantes

    def get_estudiante(self, id):
        cursor = DB.cursor()
        cursor.execute("SELECT * FROM estudiantes WHERE id=?",(id,))
        estudiante = cursor.fetchone()
        cursor.close()

        return estudiante