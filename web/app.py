# Karoll Vanessa Pinto Culma T00061162
# Jesus Antonio Martinez Velnadia T00061258


from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from web.module import *

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []

# La función index direcciona la ruta del index


@app.route("/")
def index():
    # Pone la informacion que entra por la web y la almacena
    # en db.json que seria nuestra base de datos
    conversion()
    print("Se encuentra en le index")
    return render_template('index.html')

# La funcion person direcciona a la pagina de donde se puede ver el
# forms para el ingreso de datos


@app.route('/person', methods=['GET'])
def person():
    # Pone la informacion que entra por la web y la almacena
    # en db.json que seria nuestra base de datos
    conversion()
    return render_template('person.html')

# La funcion person_detail hace la asignacion de con model
# la asignacion se hace por las respuestas que dio el forms


@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    # Pone la informacion que entra por la web y la almacena
    # en db.json que seria nuestra base de datos
    model.append(p)
    conversion()
    print("Se ha agregrado la persona ", person.id_person, " con exito")
    return render_template('person_detail.html', value=p)

# La funcion people imprime lo que estaria en la base de datos
# en nuestro caso seria donde se guarda en el json


@app.route('/people')
def people():
    print(" Nuestra base de datos ")
    data = [(i.id_person, i.name, i.last_name) for i in model]
    print(data)
    # Pone la informacion que entra por la web y la almacena
    # en db.json que seria nuestra base de datos
    conversion()
    return render_template('people.html', value=data)


# La funcion update hace el metodo de la modificar la persona esto con un metodo
# post, dando una respuesta ante la peticion del usuario


@app.route('/update', methods=['POST'])
def update():
    for persona in model:
        if persona.id_person == request.form['id_person']:
            model.remove(persona)
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model.append(p)
    # Pone la informacion que entra por la web y la almacena
    # en db.json que seria nuestra base de datos
    conversion()
    print(" Se actualizado la persona "  , person.id_person  , " con exito")
    return render_template('person_detail.html', value=p)

# La funcion de person_update hace una validacion de que la persona que
# se va modificar es el mismo id que entra como parametro


@app.route('/person_update/<string:id>', methods=['GET'])
def person_update(id):
    information = 0
    for persona in model:
        if persona.id_person == id:
            information = persona
    # Pone la informacion que entra por la web y la almacena
    # en db.json que seria nuestra base de datos
    conversion()
    return render_template('person_update.html', data=information)

# la funcion person_detete hace una validacion para eliminar a la persona
# del id que entra por parametro


@app.route('/person_delete/<string:id>')
def person_delete(id):
    for persona in model:
        if persona.id_person == id:
            model.remove(persona)
    # Pone la informacion que entra por la web y la almacena
    # en db.json que seria nuestra base de datos
    conversion()
    print(" Se eliminado la persona ", person.id_person, " con exito")
    return redirect('/people')


def menu():

    # Se crea un mini menu que hace escoger donde quiere hacer el ingreso o modificacion de datos
    # si por el sitio web o consola
    if int(input("\t\t**Choose the type of view**\n\t1. Console\n\t2. Web\n\tOption: ")) == 1:
        main()
    else:
        app.run()


if __name__ == '__main__':
    cargar()
    model = lista
    menu()
