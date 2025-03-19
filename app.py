from flask import Flask,render_template,request,redirect
import mysql.connector

app = Flask(__name__)
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user ="root",
        password="",
        database="inventario"

    )
@app.route('/')
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    producto = cursor.fetchall()
    conn.close()
    return render_template('index.html', actividades=producto)

@app.route('/add', methods=['POST'])
def add():
    #se instancian dos variables para poder mandar dos datos sin probocar un null que cause error en la conexión 
    producto = request.form['producto']  
    cantidad = request.form['cantidad']  
    precio = request.form['precio'] 
    vida = request.form['vida'] 
    conn = get_db_connection()
    cursor = conn.cursor()
    #se insertan los valores 
    cursor.execute("INSERT INTO productos (Producto, Cantidad, Precio,Vida) VALUES (%s, %s, %s,%s )", (producto, cantidad, precio,vida))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE ID = %s", (id,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE productos SET Producto = %s, Cantidad = %s, Precio = %s, Vida = %s WHERE ID = %s",(request.form['producto'], request.form['cantidad'], request.form['precio'],request.form['vida'], id))
    
    conn.commit()
    conn.close()
    return redirect('/')