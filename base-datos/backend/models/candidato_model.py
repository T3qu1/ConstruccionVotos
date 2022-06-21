from backend.models.connection_pool_pg import getcursor
#from connection_pool_pg import getcursor

class CandidatoModel:
                   
    def create_candidato(self, id_partido, nombre_cand, tipo_cand):
        with getcursor() as cur:
            params = {
                'id_partido' : id_partido,
                'nombre_cand' : nombre_cand,
                'tipo_cand' : tipo_cand
            }  
            query = """insert into candidato (id_partido, nombre_cand, tipo_cand) 
                values (%(id_partido)s, %(nombre_cand)s, %(tipo_cand)s)"""    
            cur.execute(query, params)   

            data = {'id': cur.lastrowid, 'id_partido': params['id_partido'], 'nombre_cand': params['nombre_cand'], 'tipo_cand':params['tipo_cand']}
            return data

    def get_candidato(self):  
        with getcursor() as cur:
            cur.execute("SELECT * from candidato")
            result_set = cur.fetchall()

            data = []
            content = {}
            for result in result_set:
                content = {'id': result[0], 'id_partido': result[1], 'nombre_cand': result[2]}
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