from flask import Flask, request, jsonify
import psycopg2

conn = psycopg2.connect(host='159.69.151.133', port='5056', dbname='db_19_lag', user='u_19_lag', password='123')
cursor = conn.cursor()


app = Flask(__name__)


@app.route("/")
def test_api():
    return "<p>Welcome to Test API<p>"


@app.route("/zoo_add", methods=['POST'])
def zoo_add_function():
    if request.method == 'POST':
        name = request.form.get('name')
        type_animal = request.form.get('type_animal')
        age = int(request.form.get('age'))
        weight = float(request.form.get('weight'))
    resp = {'name': name,
            'type_animal': type_animal,
            'age': age,
            'weight': weight,
            'food': weight * 0.2
            }
    return jsonify(resp)


@app.route("/zoo_list")
def zoo_list_function():
    zoo_list = {
        'Animals_list': [
            {'name': 'Кэти',
             'type_animal': 'Кошка',
             'age': 2,
             'weight': 4,
             'food': 0.8
             },
            {'name': 'Джордж',
             'type_animal': 'Собака',
             'age': 3,
             'weight': 10,
             'food': 2
             },
            {'name': 'Пэри',
             'type_animal': 'Попугай',
             'age': 10,
             'weight': 1,
             'food': 0.2
             }]}
    return jsonify(zoo_list)

@app.route('/sendparams', methods=['GET'])
def sendparams():

    name = request.args.get('name')
    age = int(request.args.get('age'))

    ageup = age + 10

    resp = [name, ageup]
    return jsonify(resp)

@app.route('/postreq', methods=['POST'])
def postreq():

    name = request.form.get('name')
    age = int(request.form.get('age'))

    ageup = age + 15

    resp = [name, ageup]
    return jsonify(resp)

@approute('/second', methods=['GET'])
def second():

    query = 'SELECT * FROM public.courses;'

    resp = {}
    if conn:
        cursor.execute(query)
        result = cursor.fetcall()

        for i in result:

            name_key - 'name' + str(i[0])

            resp[name_key] = {'name': i[0],
                              'price': i[1]
                              }
            # print('Name = ', i[1])
            # print('Price = ', i[2])

    # print('resp', resp)

        return jsonify(resp)

    else:
        return 'DB connection error'
