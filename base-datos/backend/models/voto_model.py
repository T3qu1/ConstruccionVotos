from backend.models.connection_pool_pg import getcursor
#from connection_pool_pg import getcursor

class VotoModel:
                   
    def create_voto(self, id_cand, id_ubicacion, fecha, hora):
        with getcursor() as cur:
            params = {
                'id_cand' : id_cand,
                'id_ubicacion' : id_ubicacion,
                'fecha' : fecha,
                'hora' : hora,
            }  
            query = """insert into voto (id_cand, id_ubicacion, fecha, hora) 
                values (%(id_cand)s, %(id_ubicacion)s, %(fecha)s, %(hora)s)"""    
            cur.execute(query, params)   

            data = {'id': cur.lastrowid, 'id_cand': params['id_cand'], 'id_ubicacion': params['id_ubicacion'], 'fecha':params['fecha'], 'hora':params['hora']}
            return data

    def get_voto(self):  
        with getcursor() as cur:
            cur.execute("SELECT * from voto")
            result_set = cur.fetchall()

            data = []
            content = {}
            for result in result_set:
                content = {'id': result[0], 'id_cand': result[1], 'id_ubicacion': result[2], 'fecha': result[3], 'hora': result[4]}
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