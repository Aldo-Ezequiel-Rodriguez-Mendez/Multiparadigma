from flask import Flask,render_template,request,jsonify,session,url_for,redirect
from database import db 
from flask_migrate import Migrate
from werkzeug.exceptions import abort
from werkzeug.utils import redirect
from models import Persona,Alumno,Michi
from forms import PersonaForm
from forms import AlumnoForm


import logging
app = Flask(__name__)

app.secret_key="llave_secreta"
app.config['SECRET_KEY']="una llave "


#inicio de codigo de proyecto 2 

# Configuracion de la BD
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB =  'localhost' 
NAME_DB = 'flask'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI']= FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db.init_app(app) 

#configurar Migracion 

migrate = Migrate()
migrate.init_app(app,db)

#FORM 
logging.basicConfig(filename="error.log",level=logging.DEBUG)


@app.route('/')
@app.route('/menu')
def inicio(): 
   
    if 'username' in session:
         
         return render_template('menu.html')
    else:
         return redirect(url_for('login'))
   

@app.route('/Alumnos')
def Alumnos():
    app.logger.debug(request.headers.get('token'))
    alumnos = Alumno.query.all()
    return render_template('indexAlumno.html', alumnos=alumnos)
 
 
@app.route('/Alumnos/<int:id>')
def verAlumnos(id):
    app.logger.debug(request.headers.get('token'))
    alumnos = Alumno.query.get_or_404(id)
    return render_template('detalleAlumno.html', alumnos=alumnos)
 

@app.route('/personas')
def personas():
    app.logger.debug(request.headers.get('token'))
    personas = Persona.query.all()
    return render_template("index.html", personas=personas)


@app.route('/personas/<int:id>')
def verPersona(id):
    personas = Persona.query.get_or_404(id)
    return render_template('detalle.html', personas=personas)
 
 
 

@app.route('/michi', methods=["GET", "POST"])
def getMichis():
    app.logger.debug(request.headers.get('token'))
    if request.method == "GET":
        michis = Michi.query.all()
        return jsonify(michis=Michi.serialize_list(michis))
    elif request.method == "POST":
        info = request.json
        michis = Michi( nombre=info["Nombre"], raza=info["Raza"],
                                color=info["color"])
        db.session.add(michis)
        db.session.commit()
        return "gato agregado"
 
 
 
@app.route('/michi/<int:id>',methods=["GET","PATCH","DELETE"])
def getMichi(id):
    app.logger.debug(request.headers.get('token'))
    if request.method == "GET":
        michi = Michi.query.get_or_404(id)
        return jsonify(Michi.serialize(michi))
    elif request.method == "PATCH":
        info = request.json
        michi = Michi.query.get_or_404(id)
        michi.nombre = info["Nombre"]
        michi.raza = info["Raza"]
        michi.color = info["color"]
        db.session.commit()
        return "gato actualizado"
    elif request.method == "DELETE":
        info = request.json
        michi = Michi.query.get_or_404(id)
        db.session.delete(michi)
        db.session.commit()
        return "michi eliminado"












@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username']
        session['username'] = usuario
        return redirect(url_for('inicio'))
    return render_template('login.html')

# agregar alumno 
@app.route('/Alumnos/agregar',methods=['GET','POST'])
def agregarAlumno():
    app.logger.debug(request.headers.get('token'))
    alumno = Alumno() 
    alumnoForm = AlumnoForm(obj=alumno)
    if request.method == 'POST':
         if alumnoForm.validate_on_submit():
              alumnoForm.populate_obj(alumno)
              #insert 
              db.session.add(alumno)
              db.session.commit()
              return redirect(url_for('Alumnos'))
          
    return render_template('agregarAlumno.html',forma= alumnoForm)  


@app.route('/salir')
def salir():
    session.pop('username')
    return abort(404)



# @app.route('/Alumnos/<int:id>')
# def detalleAlumno(id): 
#      alumno = Alumno.query.get_or_404(id)    
#      return render_template('detalleAlumno.html',alumno=alumno)


@app.route('/personas/agregar',methods=['GET','POST'])
def agregar():
    persona = Persona() 
    personaForm = PersonaForm(obj=persona)
    if request.method == 'POST':
         if personaForm.validate_on_submit():
              personaForm.populate_obj(persona)
              #insert 
              db.session.add(persona)
              db.session.commit()
              return redirect(url_for('personas'))
          
    return render_template('agregar.html',forma= personaForm)     





@app.route('/personas/editar/<int:id>',methods=['GET','POST'])
def editar(id):
    persona= Persona.query.get_or_404(id)
    personaForm = PersonaForm(obj=persona)
    if request.method == 'POST':
        if personaForm.validate_on_submit():
            personaForm.populate_obj(persona)
            db.session.commit()   
            return redirect (url_for('personas')) 
    return render_template('editar.html',forma = personaForm)      

#editar alumno
@app.route('/Alumnos/editar/<int:id>',methods=['GET','POST'])
def editarAlumno(id):
    alumno= Alumno.query.get_or_404(id)
    alumnoForm = AlumnoForm(obj=alumno)
    if request.method == 'POST':
        if alumnoForm.validate_on_submit():
            alumnoForm.populate_obj(alumno)
            db.session.commit()   
            return redirect (url_for('Alumnos')) 
    return render_template('editarAlumno.html',forma = alumnoForm)   



@app.route('/personas/eliminar/<int:id>') 
def eliminar(id):
    personas = Persona.query.get_or_404(id)
    db.session.delete(personas)
    db.session.commit() 
    return redirect (url_for('personas'))

#eliminar alumno
@app.route('/Alumnos/eliminar/<int:id>') 
def eliminarAlumno(id):
    alumnos = Alumno.query.get_or_404(id)
    db.session.delete(alumnos)
    db.session.commit() 
    return redirect (url_for('Alumnos'))


@app.errorhandler(404)
def noEncontrado(error):
    return render_template('404.html', error=error), 404








