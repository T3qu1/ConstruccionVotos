from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename

from flask_cors import CORS, cross_origin 
# para que no genere errores de CORS al hacer peticiones

#importamos las clases models
from backend.models.admin_model import AdminModel
from backend.models.candidato_model import CandidatoModel
from backend.models.partido_model import PartidoModel
from backend.models.ubicacion_model import UbicacionModel
from backend.models.votante_model import VotanteModel
from backend.models.voto_model import VotoModel

model_adm = AdminModel()
model_cand = CandidatoModel()
model_part = PartidoModel()
model_ubi = UbicacionModel()
model_vota = VotanteModel()
model_voto = VotoModel()


#decorator
task_blueprint = Blueprint('task_blueprint', __name__)


#definimos los views


#------------------------------------------------admin-------------------------------------------nombre_admin, contra_admin
@task_blueprint.route('/admin/create_admin/', methods=['POST'])
@cross_origin()
def create_admin():
    content = model_adm.create_admin(request.json['nombre_admin'], request.json['contra_admin'])
    return jsonify(content)

@task_blueprint.route('/admin/get_admin/', methods=['POST'])
@cross_origin()
def get_admin():
    content = model_adm.get_admin()
    return jsonify(content)
'''
@task_blueprint.route('/votantes/delete_votante/<int:id>', methods=['POST'])
@cross_origin()
def delete_votante(id):
    return jsonify(model_v.delete_votante(id))'''

#------------------------------------------------votante-------------------------------------------
@task_blueprint.route('/votantes/create_votante/', methods=['POST'])
@cross_origin()
def create_votante():
    content = model_vota.create_votante(request.json['nombre_votan'], request.json['dni_votan'],request.json['contra_votan'])
    return jsonify(content)

@task_blueprint.route('/votantes/get_votantes/', methods=['POST'])
@cross_origin()
def get_votantes():
    content = model_vota.get_votantes()    
    return jsonify(content)
'''
@task_blueprint.route('/votantes/delete_votante/<int:id>', methods=['POST'])
@cross_origin()
def delete_votante(id):
    return jsonify(model_v.delete_votante(id))'''


#------------------------------------------Candidato----------------------------------------------
@task_blueprint.route('/candidatos/get_candidatos/', methods=['POST'])
@cross_origin()
def get_candidatos():
    content = model_cand.get_candidato()    
    return jsonify(content)
'''   
@task_blueprint.route('/candidatos/delete_candidato/<int:id>', methods=['POST'])
@cross_origin()
def delete_candidato(id):
    return jsonify(model_v.delete_candidato(id))'''

@task_blueprint.route('/candidatos/create_candidato/', methods=['POST'])
@cross_origin()
def create_candidato():
    content = model_cand.create_candidato(request.json['id_partido'], request.json['nombre_cand'],request.json['tipo_cand'])
    return jsonify(content)

#------------------------------------------Partido----------------------------------------------

@task_blueprint.route('/partido/create_partido/', methods=['POST'])
@cross_origin()
def create_partido():
    content = model_part.create_partido(request.json['nombre_partido'], request.json['descripcion_partido'])
    return jsonify(content)

@task_blueprint.route('/partido/get_partido', methods=['POST'])
@cross_origin()
def get_partidos():
    content = model_part.get_partido()    
    return jsonify(content)

'''
@task_blueprint.route('/partido/delete_partido/<int:id>', methods=['POST'])
@cross_origin()
def delete_partido(id):
    return jsonify(model_v.delete_partido(int(id)))'''



#------------------------------------------Ubicacion----------------------------------------------ciudad, provincia, distrito

@task_blueprint.route('/ubicacion/create_ubicacion/', methods=['POST'])
@cross_origin()
def create_ubicacion():
    content = model_ubi.create_ubicacion(request.json['ciudad'], request.json['provincia'], request.json['distrito'])
    return jsonify(content)

@task_blueprint.route('/ubicacion/get_ubicacion', methods=['POST'])
@cross_origin()
def get_ubicacion():
    content = model_ubi.get_ubicacion()    
    return jsonify(content)

'''
@task_blueprint.route('/partido/delete_partido/<int:id>', methods=['POST'])
@cross_origin()
def delete_partido(id):
    return jsonify(model_v.delete_partido(int(id)))'''

#------------------------------------------Voto----------------------------------------------idCand, idUbicacion, fecha, hora

@task_blueprint.route('/voto/create_voto/', methods=['POST'])
@cross_origin()
def create_voto():
    content = model_voto.create_voto(request.json['id_cand'], request.json['id_ubicacion'], request.json['fecha'],request.json['hora'])
    return jsonify(content)

@task_blueprint.route('/voto/get_voto/', methods=['POST'])
@cross_origin()
def get_voto():
    content = model_voto.get_voto()
    return jsonify(content)

