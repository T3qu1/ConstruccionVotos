from backend.models.connection_pool_pg import getcursor
#from connection_pool_pg import getcursor

class AdminModel:
                   
    def create_admin(self, nombre_admin, contra_admin):
        with getcursor() as cur:
            params = {
                'nombre_admin' : nombre_admin,
                'contra_admin' : contra_admin
            }  
            query = """insert into administrador (nombre_admin, contra_admin) 
                values (%(nombre_admin)s, %(contra_admin)s)"""    
            cur.execute(query, params)   

            data = {'nombre_admin': params['nombre_admin'], 'contra_admin': params['contra_admin']}
            return data

    def get_admin(self):  
        with getcursor() as cur:
            cur.execute("SELECT * from administrador")
            result_set = cur.fetchall()

            data = []

            for result in result_set:
                content = {'id': result[0], 'nombre_admin': result[1], 'contra_admin': result[2]}
                data.append(content)

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