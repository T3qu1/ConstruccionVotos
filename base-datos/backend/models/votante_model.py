from backend.models.connection_pool_pg import getcursor
#from connection_pool_pg import getcursor

class VotanteModel:
                   
    def create_votante(self, nombre_votan, dni_votan, contra_votan):
        with getcursor() as cur:
            params = {
                'nombre_votan' : nombre_votan,
                'dni_votan' : dni_votan,
                'contra_votan' : contra_votan
            }  
            query = """insert into votante (nombre_votan, dni_votan, contra_votan) 
                values (%(nombre_votan)s, %(dni_votan)s, %(contra_votan)s)"""    
            cur.execute(query, params)   

            data = {'id': cur.lastrowid, 'nombre_votan': params['nombre_votan'], 'dni_votan': params['dni_votan'], 'contra_votan':params['contra_votan']}
            return data

    def get_votantes(self):  
        with getcursor() as cur:
            cur.execute("SELECT * from votante")
            result_set = cur.fetchall()

            data = []
            content = {}
            for result in result_set:
                content = {'id': result[0], 'nombre_votan': result[1], 'dni_votan': result[2]}
                data.append(content)
                content = {}
            return data

    '''def delete_votante(self, id):
        votante = Votante.query.get(id)
        db.session.delete(votante)
        db.session.commit()
        return votante
    
if __name__ == "__main__":    
    vm = VotanteModel()     

    #print(tm.get_task(1))
    #print(tm.get_tasks())
    print(vm.get_tasks())
    #print(tm.create_task('prueba 10', 'desde python'))'''