from flask import Flask, session, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
import pymysql


app = Flask(__name__)
app.secret_key = "cairocoders-ednalan"

mysql = MySQL()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/pag1')
def contacto():
    return render_template("pag1.html")


@app.route('/pag2')
def pagina2():
    return render_template("pag2.html")


@app.route('/pag3')
def pagina3():
    return render_template("pag3.html")


@app.route('/registro')
def registro():
    return render_template("registro.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/inicio_correcto')
def inicio_correcto():
    return render_template("inicio_correcto.html")


@app.route('/inicio_incorrecto')
def inicio_incorrecto():
    return render_template("inicio_incorrecto.html")


@app.route('/usuarios', methods=['POST'])
def usuarios():
    if request.method == 'POST':
        aux_Correo = request.form['correo']
        aux_Contrasena = request.form['contrasena']
        aux_nombre = request.form['nombre']
       
        conn = pymysql.connect(host='localhost', user='root',
                               passwd='', db='agenda', port=3306)
        cursor = conn.cursor()
        cursor.execute('insert into r_empresa (correo,contrasena,nombre) values (%s, %s,%s)',
                       (aux_Correo, aux_Contrasena, aux_nombre))
        conn.commit()
    return redirect(url_for('home'))


@app.route('/iniciar_sesion', methods=['POST'])
def iniciar_sesion():
    if request.method == 'POST':
        aux_Correo = request.form['correo']
        aux_Contrasena = request.form['contrasena']

        conn = pymysql.connect(host='localhost', user='root',
                               passwd='', db='agenda', port=3306)
        cursor = conn.cursor()
        cursor.execute('select * from r_empresa where correo=%s and contrasena=%s',
                       (aux_Correo, aux_Contrasena,))
        dato = cursor.fetchone()
    try:
        if aux_Correo and aux_Contrasena in dato:
            return render_template("inicio_correcto.html")
    except:
        return redirect(url_for('inicio_incorrecto'))


@app.route('/crud')
def crud():
    conn = pymysql.connect(host='localhost', user='root',
                           passwd='', db='agenda', port=3306)
    cursor = conn.cursor()
    cursor.execute('select id, correo, comentarios from comenta order by id')
    datos = cursor.fetchall()
    return render_template("crud.html", comentarios=datos)


@app.route('/editar/<string:id>')
def editar(id):
    conn = pymysql.connect(host='localhost', user='root',
                           passwd='', db='agenda', port=3306)
    cursor = conn.cursor()
    cursor.execute(
        'select id, correo, comentarios from comenta where id = %s', (id))
    dato = cursor.fetchall()
    return render_template("editar.html", comentar=dato[0])


@app.route('/editar_comenta/<string:id>', methods=['POST'])
def editar_comenta(id):
    if request.method == 'POST':
        corr = request.form['correo']
        come = request.form['comentarios']
        conn = pymysql.connect(host='localhost', user='root',
                               passwd='', db='agenda', port=3306)
        cursor = conn.cursor()
        cursor.execute(
            'update comenta set correo=%s, comentarios=%s where id=%s', (corr, come, id))
        conn.commit()
    return redirect(url_for('crud'))


@app.route('/borrar/<string:id>')
def borrar(id):
    conn = pymysql.connect(host='localhost', user='root',
                           passwd='', db='agenda', port=3306)
    cursor = conn.cursor()
    cursor.execute('delete from comenta where id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('crud'))


@app.route('/insertar')
def insertar():
    return render_template("insertar.html")


@app.route('/agrega_comenta', methods=['POST'])
def agrega_comenta():
    if request.method == 'POST':
        aux_Correo = request.form['correo']
        aux_Comentarios = request.form['comentarios']
        conn = pymysql.connect(host='localhost', user='root',
                               passwd='', db='agenda', port=3306)
        cursor = conn.cursor()
        cursor.execute('insert into comenta (correo,comentarios) values (%s, %s)',
                       (aux_Correo, aux_Comentarios))
        conn.commit()
    return redirect(url_for('home'))


# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'agenda'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/add', methods=['POST'])
def add_product_to_cart():
    cursor = None
    try:
        _quantity = int(request.form['quantity'])
        _code = request.form['code']
        # validate the received values
        if _quantity and _code and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT * FROM product WHERE code=%s", _code)
            row = cursor.fetchone()

            itemArray = {
                row['code']: {'name': row['name'], 'code': row['code'], 'quantity': _quantity, 'price': row['price'],
                              'image': row['image'], 'total_price': _quantity * row['price']}}

            all_total_price = 0
            all_total_quantity = 0

            session.modified = True
            if 'cart_item' in session:
                if row['code'] in session['cart_item']:
                    for key, value in session['cart_item'].items():
                        if row['code'] == key:
                            old_quantity = session['cart_item'][key]['quantity']
                            total_quantity = old_quantity + _quantity
                            session['cart_item'][key]['quantity'] = total_quantity
                            session['cart_item'][key]['total_price'] = total_quantity * row['price']
                else:
                    session['cart_item'] = array_merge(
                        session['cart_item'], itemArray)

                for key, value in session['cart_item'].items():
                    individual_quantity = int(
                        session['cart_item'][key]['quantity'])
                    individual_price = float(
                        session['cart_item'][key]['total_price'])
                    all_total_quantity = all_total_quantity + individual_quantity
                    all_total_price = all_total_price + individual_price
            else:
                session['cart_item'] = itemArray
                all_total_quantity = all_total_quantity + _quantity
                all_total_price = all_total_price + _quantity * row['price']

            session['all_total_quantity'] = all_total_quantity
            session['all_total_price'] = all_total_price

            return redirect(url_for('.products'))
        else:
            return 'Error while adding item to cart'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/product')
def products():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM product")
        rows = cursor.fetchall()
        return render_template('product.html', products=rows)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/empty')
def empty_cart():
    try:
        session.clear()
        return redirect(url_for('.products'))
    except Exception as e:
        print(e)


@app.route('/delete/<string:code>')
def delete_product(code):
    try:
        all_total_price = 0
        all_total_quantity = 0
        session.modified = True

        for item in session['cart_item'].items():
            if item[0] == code:
                session['cart_item'].pop(item[0], None)
                if 'cart_item' in session:
                    for key, value in session['cart_item'].items():
                        individual_quantity = int(
                            session['cart_item'][key]['quantity'])
                        individual_price = float(
                            session['cart_item'][key]['total_price'])
                        all_total_quantity = all_total_quantity + individual_quantity
                        all_total_price = all_total_price + individual_price
                break

        if all_total_quantity == 0:
            session.clear()
        else:
            session['all_total_quantity'] = all_total_quantity
            session['all_total_price'] = all_total_price

        return redirect(url_for('.products'))
    except Exception as e:
        print(e)


def array_merge(first_array, second_array):
    if isinstance(first_array, list) and isinstance(second_array, list):
        return first_array + second_array
    elif isinstance(first_array, dict) and isinstance(second_array, dict):
        return dict(list(first_array.items()) + list(second_array.items()))
    elif isinstance(first_array, set) and isinstance(second_array, set):
        return first_array.union(second_array)
    return False

@app.route('/c')
def tenis():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
    cursor = conn.cursor()
    cursor.execute('select idTenis, nombre, apellidos, fechanac, sexo, telefono, correo from tenis order by idTenis')
    datos = cursor.fetchall()
    return render_template("tenis.html", tenis=datos, dat=' ')

@app.route('/tenis_editar/<string:idC>')
def tenis_editar(idC):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('select idTenis, nombre, apellidos, fechanac, sexo, telefono, correo from Tenis where idTenis = %s', (idC))
    dato = cursor.fetchall()
    return render_template("tenis_edi.html", dat=dato[0])

@app.route('/tenis_fedita/<string:idC>',methods=['POST'])
def tenis_fedita(idC):
    if request.method == 'POST':
        nom=request.form['nombre']
        apell=request.form['apellidos']
        fech=request.form['fechanac']
        sexo=request.form['sexo']
        tel=request.form['telefono']
        correo=request.form['correo']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
        cursor = conn.cursor()
        cursor.execute('update Tenis set nombre=%s, apellidos=%s, fechanac=%s, sexo=%s, telefono=%s, correo=%s where idTenis=%s', (nom,apell,fech,sexo,tel,correo,idC))
        conn.commit()
    return redirect(url_for('tenis'))

@app.route('/tenis_borrar/<string:idC>')
def tenis_borrar(idC):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('delete from Tenis where idTenis = {0}'.format(idC))
    conn.commit()
    return redirect(url_for('tenis'))

@app.route('/tenis_agregar')
def tenis_agregar():
    return render_template("tenis_agr.html")
    
@app.route('/tenis_fagrega', methods=['POST'])
def tenis_fagrega():
    if request.method == 'POST':
        nom=request.form['nombre']
        apell=request.form['apellidos']
        fech=request.form['fechanac']
        sexo=request.form['sexo']
        tel=request.form['telefono']
        correo=request.form['correo']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
        cursor = conn.cursor()
        cursor.execute('insert into Tenis (nombre, apellidos, fechanac, sexo, telefono, correo) values (%s,%s,%s,%s,%s,%s)',(nom,apell,fech,sexo,tel,correo))
        conn.commit()
        
    return redirect(url_for('tenis'))



if __name__ == "__main__":
    app.run(debug=True)
