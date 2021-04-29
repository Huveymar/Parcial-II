from src.configs.db import DB

class Sesiones:
    def guardar(self, datos):
        cursor = DB.cursor()
        cursor.execute("INSERT INTO sesiones(id_materia, fecha, hora_inicio, hora_finalizacion) VALUES(?,?,?,?)", (datos[0],datos[1],datos[2],datos[3],))
        cursor.close()
    
    def editar(self, datos):
        cursor = DB.cursor()
        consulta = f"UPDATE sesiones SET id_materia={datos[1]},fecha='{datos[2]}', hora_inicio='{datos[3]}',hora_finalizacion='{datos[4]}' WHERE id={datos[0]}"
        cursor.execute(consulta)
        cursor.close()

    def eliminar(self, id):
        cursor = DB.cursor()
        cursor.execute("DELETE FROM sesiones WHERE id=?", (id,))
        cursor.close()

    def get_sesiones(self):
        cursor = DB.cursor()
        cursor.execute("SELECT * FROM sesiones")
        sesiones = cursor.fetchall()
        cursor.close()

        return sesiones

    def get_sesion(self, id):
        cursor = DB.cursor()
        cursor.execute("SELECT * FROM sesiones WHERE id=?",(id,))
        sesiones = cursor.fetchone()
        cursor.close()

        return sesiones