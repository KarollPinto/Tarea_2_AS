import json
from logic.person import Person
lista = []
# La funcion carga hace un llamado a db.json la cual lo lee y hace una validacion
# si existe se agrega a la persona en el caso que no arroja error


def cargar():
    try:
        with open('db.json', 'r') as file:
            diccionario = json.load(file)
            for key, value in diccionario.items():
                persona = Person(key, value['name'], value['last_name'])
                lista.append(persona)
    except json.decoder.JSONDecodeError:
        return

# La funcion main hace un menu para mostrar las diferentes interaciones que se puede hacer en la consola


def main():
    cargar()
    print('**CONSOLE VIEW**')
    while True:
        conversion(lista)
        if len(lista) == 0:
            opcion = int(input("\t\t-MENU-\n\t1. Insert\n\t2. Exit\nOption: "))
            if opcion == 1:
                insertar()
            elif opcion == 2:
                break
            else:
                print("UPS! the entered option is invalid!")
        else:
            print("\t\t-MENU-")
            opcion = int(input("\t1. Insert\n\t2. View\n\t3. Modify\n"
                               "\t4. Delete\n\t5. Exit\n\tOption: "))
            if opcion == 1:
                insertar()
            elif opcion == 2:
                visualizar()
            elif opcion == 3:
                modificar(input("\tUser tell us the id of the person to modify: "))
            elif opcion == 4:
                eliminar(input("\tUser say the id of the person to delete: "))
            elif opcion == 5:
                break
            else:
                print("\tUPS! the entered option is invalid!")

# La funcion visualiar imprime lo que se encuentra en la base de datos


def visualizar():
    for person in lista:
        print(person)

# La funcion insertar agrega una nueva persona con su respectivos datos


def insertar():
    print("\t\t**Menu Insert**")
    id = int(input("\tID: "))
    name = input("\tName: ")
    last_name = input("\tLast name: ")
    p = Person(id_person=id, name=name, last_name=last_name)
    lista.append(p)
    print(f'\twas successfully logged in.{name} was successfully logged in.')

# La funcion modificar hace un cambio de los datos de la persona menos en la id


def modificar(id_modificar):
    for person in lista:
        if person.id_person == id_modificar:
            name = input(f'Current name: {person.name} \n\tNew name: ')
            last_name = input(f'Current last name: {person.last_name} \n\tNew last name: ')
            person.name = name
            person.last_name = last_name
            print(f'\tData successfully updated:\n\tName: {person.name}\n\tLast Name: {person.last_name}')

# La funcion eliminar elimina a la persona con el id solicitado


def eliminar(id_eliminar):
    for persona in lista:
        if persona.id_person == id_eliminar:
            lista.remove(persona)
            print("Person successfully eliminated")

# La funcion conversion inserta los datos de la personas y esta se actualiza en cada
# modificacion en la base de datos la cual se encuentra en forma de diccionario


def conversion(data: list = lista):
    datos = {}
    for item in data:
        datos[item.id_person] = {'name': item.name, 'last_name': item.last_name}

    with open('db.json', 'w') as file:
        json.dump(datos, file)
        file.close()


if __name__ == '__main__':
    main()
