from wtforms import Form
from wtforms import StringField, TextField
#from wtforms.fields.html5 import EmailField 
from wtforms import validators

class CommentForm(Form):
    #con validaciones
    usuario = StringField('usuario', [
        validators.Required(message='El campo es requerido'),
        validators.length(min=4, max=25, message='Ingrese un campo valido')
        ])
    dni = StringField('dni', [
        validators.Required(message='El campo es requerido'),
        validators.length(min=4, max=25, message='Ingrese un campo valido')
        ])

   
