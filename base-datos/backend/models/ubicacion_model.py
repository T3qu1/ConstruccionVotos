from backend.models.connection_pool_pg import getcursor
#from connection_pool_pg import getcursor

class UbicacionModel:
                   
    def create_ubicacion(self, ciudad, provincia, distrito):
        with getcursor() as cur:
            params = {
                'ciudad' : ciudad,
                'provincia' : provincia,
                'distrito' : distrito
            }  
            query = """insert into ubicacion (ciudad, provincia, distrito) 
                values (%(ciudad)s, %(provincia)s, %(distrito)s)"""    
            cur.execute(query, params)   

            data = {'id': cur.lastrowid, 'ciudad': params['ciudad'], 'provincia': params['provincia'], 'distrito': params['distrito']}
            return data

    def get_ubicacion(self):  
        with getcursor() as cur:
            cur.execute("SELECT * from ubicacion")
            result_set = cur.fetchall()

            data = []
            content = {}
            for result in result_set:
                content = {'id': result[0], 'ciudad': result[1], 'provincia': result[2], 'distrito': result[3]}
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