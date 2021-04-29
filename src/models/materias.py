from src.configs.db import DB

class Materias:
    def guardar(self, datos):
        print(datos)
        cursor = DB.cursor()
        cursor.execute("INSERT INTO materias(nombre, semestre) VALUES(?,?)", (datos[0],datos[1],))
        cursor.close()
    
    def editar(self, datos):
        print(datos)
        cursor = DB.cursor()
        consulta = f"UPDATE materias SET nombre='{datos[1]}',semestre='{datos[2]}' WHERE id={datos[0]}"
        cursor.execute(consulta)
        cursor.close()

    def eliminar(self, id):
        cursor = DB.cursor()
        cursor.execute("DELETE FROM materias WHERE id=?", (id,))
        cursor.close()

    def get_materias(self):
        cursor = DB.cursor()
        cursor.execute("SELECT * FROM materias")
        materias = cursor.fetchall()
        cursor.close()

        return materias

    def get_materia(self, id):
        cursor = DB.cursor()
        cursor.execute("SELECT * FROM materias WHERE id=?",(id,))
        materia = cursor.fetchone()
        cursor.close()

        return materia