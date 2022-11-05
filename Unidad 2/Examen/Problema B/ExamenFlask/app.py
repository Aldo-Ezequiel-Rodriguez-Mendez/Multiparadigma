from flask import Flask,render_template,request,jsonify,session,url_for,redirect
from database import db 
from flask_migrate import Migrate
from werkzeug.exceptions import abort
from werkzeug.utils import redirect
from models import Profesor,Empleado,Cliente
from forms import ProfesorForm
from forms import EmpleadoForm 



import logging
app = Flask(__name__)

app.secret_key="llave_secreta"
app.config['SECRET_KEY']="una llave "


#inicio de codigo de proyecto 2 

# Configuracion de la BD
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB =  'localhost' 
NAME_DB = 'Examen'
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
   

@app.route('/Profesores')
def Profesores():
    app.logger.debug(request.headers.get('token'))
    profesores = Profesor.query.all()
    return render_template('indexProfesor.html', profesores=profesores)
 
 
@app.route('/Profesores/<int:id>')
def verProfesor(id):
    app.logger.debug(request.headers.get('token'))
    profesores = Profesor.query.get_or_404(id)
    return render_template('detalleProfesor.html', profesores=profesores)
 
@app.route('/empleados/<int:id>')
def verEmpleado(id):
     app.logger.debug(request.headers.get('token'))
     empleados = Empleado.query.get_or_404(id)
     return render_template('detalleEmpleado.html', empleados=empleados)
 
 
@app.route('/empleados')
def empleados():
    app.logger.debug(request.headers.get('token'))
    empleados = Empleado.query.all()
    return render_template("indexEmpleado.html", empleados=empleados)


 

@app.route('/cliente', methods=["GET", "POST"])
def getClientes():
    app.logger.debug(request.headers.get('token'))
    if request.method == "GET":
        clientes = Cliente.query.all()
        return jsonify(clientes=Cliente.serialize_list(clientes))
    elif request.method == "POST":
        info = request.json
        clientes = Cliente( nombre=info["Nombre"], empresa=info["Empresa"])
        db.session.add(clientes)
        db.session.commit()
        return "cliente agregado"
    
    
@app.route('/cliente', methods=["GET", "POST"])
def getClientes():
    app.logger.debug(request.headers.get('token'))
    if request.method == "GET":
        clientes = Cliente.query.all()
        return jsonify(clientes=Cliente.serialize_list(clientes))
    elif request.method == "POST":
        info = request.json
        clientes = Cliente( nombre=info["Nombre"], empresa=info["Empresa"])
        db.session.add(clientes)
        db.session.commit()
        return "cliente agregado"
    
    
@app.route('/cliente', methods=["GET", "POST"])
def getClientes():
    app.logger.debug(request.headers.get('token'))
    if request.method == "GET":
        clientes = Cliente.query.all()
        return jsonify(clientes=Cliente.serialize_list(clientes))
    elif request.method == "POST":
        info = request.json
        clientes = Cliente( nombre=info["Nombre"], empresa=info["Empresa"])
        db.session.add(clientes)
        db.session.commit()
        return "cliente agregado"        
 
 
 
@app.route('/cliente/<int:id>',methods=["GET","PATCH","DELETE"])
def getCliente(id):
    app.logger.debug(request.headers.get('token'))
    if request.method == "GET":
        cliente = Cliente.query.get_or_404(id)
        return jsonify(Cliente.serialize(cliente))
    elif request.method == "PATCH":
        info = request.json
        cliente = Cliente.query.get_or_404(id)
        cliente.nombre = info["Nombre"]
        cliente.empresa = info["Empresa"]
        db.session.commit()
        return "cliente actualizado"



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username']
        session['username'] = usuario
        return redirect(url_for('inicio'))
    return render_template('login.html')

# agregar alumno 
@app.route('/Profesores/agregar',methods=['GET','POST'])
def agregarProfesor():
    app.logger.debug(request.headers.get('token'))
    profesor = Profesor() 
    profesorForm = ProfesorForm(obj=profesor)
    if request.method == 'POST':
         if profesorForm.validate_on_submit():
              profesorForm.populate_obj(profesor)
              #insert 
              db.session.add(profesor)
              db.session.commit()
              return redirect(url_for('Profesores'))
          
    return render_template('agregarProfesor.html',forma= profesorForm)  


@app.route('/salir')
def salir():
    session.pop('username')
    return abort(404)



# @app.route('/Alumnos/<int:id>')
# def detalleAlumno(id): 
#      alumno = Alumno.query.get_or_404(id)    
#      return render_template('detalleAlumno.html',alumno=alumno)


@app.route('/empleados/agregar',methods=['GET','POST'])
def agregarEmpleado():
    empleado = Empleado() 
    empleadoForm = EmpleadoForm(obj=empleado)
    if request.method == 'POST':
         if empleadoForm.validate_on_submit():
              empleadoForm.populate_obj(empleado)
              #insert 
              db.session.add(empleado)
              db.session.commit()
              return redirect(url_for('empleados'))
          
    return render_template('agregarEmpleado.html',forma= empleadoForm)     





@app.route('/empleados/editar/<int:id>',methods=['GET','POST'])
def editar(id):
    empleado= Empleado.query.get_or_404(id)
    empleadoForm = EmpleadoForm(obj=empleado)
    if request.method == 'POST':
        if empleadoForm.validate_on_submit():
            empleadoForm.populate_obj(empleado)
            db.session.commit()   
            return redirect (url_for('empleados')) 
    return render_template('editarEmpleado.html',forma = empleadoForm)      

#editar alumno
@app.route('/Profesores/editar/<int:id>',methods=['GET','POST'])
def editarProfesor(id):
    profesor= Profesor.query.get_or_404(id)
    profesorForm = ProfesorForm(obj=profesor)
    if request.method == 'POST':
        if profesorForm.validate_on_submit():
            profesorForm.populate_obj(profesor)
            db.session.commit()   
            return redirect (url_for('Profesores')) 
    return render_template('editarProfesor.html',forma = profesorForm)   



@app.route('/empleados/eliminar/<int:id>') 
def eliminar(id):
    empleados = Empleado.query.get_or_404(id)
    db.session.delete(empleados)
    db.session.commit() 
    return redirect (url_for('empleados'))

#eliminar alumno
@app.route('/Profesores/eliminar/<int:id>') 
def eliminarAlumno(id):
    profesores = Profesor.query.get_or_404(id)
    db.session.delete(profesores)
    db.session.commit() 
    return redirect (url_for('Profesores'))


@app.errorhandler(404)
def noEncontrado(error):
    return render_template('404.html', error=error), 404








