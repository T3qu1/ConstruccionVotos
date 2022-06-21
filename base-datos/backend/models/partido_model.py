from backend.models.connection_pool_pg import getcursor
#from connection_pool_pg import getcursor

class PartidoModel:
                   
    def create_partido(self, nombre_partido, descripcion_partido):
        with getcursor() as cur:
            params = {
                'nombre_partido' : nombre_partido,
                'descripcion_partido' : descripcion_partido
            }  
            query = """insert into partido (nombre_partido, descripcion_partido) 
                values (%(nombre_partido)s, %(descripcion_partido)s, %(tipoCand)s)"""    
            cur.execute(query, params)

            data = {'id': cur.lastrowid, 'nombre_partido': params['nombre_partido'], 'descripcion_partido': params['descripcion_partido']}
            return data

    def get_partido(self):  
        with getcursor() as cur:
            cur.execute("SELECT * from partido")
            result_set = cur.fetchall()

            data = []
            content = {}
            for result in result_set:
                content = {'id': result[0], 'nombre_partido': result[1], 'descripcion_partido': result[2]}
                data.append(content)
                content = {}
            return data

    '''def delete_votante(self, id):
        votante = Votante.query.get(id)
        db.session.delete(votante)
        db.session.commit()
        return votante
    
if __name__ == "__main__":    
    cm = CandidatoModel()     

    #print(tm.get_task(1))
    #print(tm.get_tasks())
    print(cm.get_tasks())
    #print(tm.create_task('prueba 10', 'desde python'))'''