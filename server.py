from crypt import methods
from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'esta es una clave secreta' 

@app.route('/')
def contador():

    if 'contador' in session:
        session['contador'] = session['contador'] + 1
    else:
        session['contador'] = 1

    return render_template("index.html")

@app.route('/add', methods=['POST'])
def addPost():

    sumar = int(request.form['sumar'])
    if 'contador' in session:
        session['contador'] = session['contador'] + sumar - 1
    else:
        session['contador'] = sumar - 1
        
    print(request.form)
    return redirect('/')

@app.route('/add/<int:sumar>')
def sumar(sumar):
    if 'contador' in session:
        # le restamos 1, porque al redireccionar a la raiz se aumenta en 1
        session['contador'] = session['contador'] + sumar - 1
    else:
        # le restamos 1, porque al redireccionar a la raiz se aumenta en 1
        session['contador'] = sumar - 1
        
    return redirect('/')

@app.route('/restart')
def restart():
    session['contador'] = 0
    return redirect('/')

@app.route('/destroy_session')
def destroy_sesion():
    session.clear()		    # borra todas las claves
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)