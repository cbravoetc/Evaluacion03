from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_promedio_aprobacion(notas, asistencia):
    promedio = sum(notas) / len(notas)
    estado = "APROBADO" if promedio >= 40 and asistencia >= 75 else "REPROBADO"
    return round(promedio,1), estado

def obtener_nombre_mas_largo(nombres):
    nombre_mas_largo = max(nombres, key=len)
    return nombre_mas_largo, len(nombre_mas_largo)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        notas = [
            float(request.form['nota1']),
            float(request.form['nota2']),
            float(request.form['nota3'])
        ]
        asistencia = float(request.form['asistencia'])

        promedio, estado = calcular_promedio_aprobacion(notas, asistencia)
        return render_template('ejercicio1.html', promedio=promedio, estado=estado)

    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombres = [
            request.form['nombre1'],
            request.form['nombre2'],
            request.form['nombre3']
        ]

        nombre_mas_largo, longitud = obtener_nombre_mas_largo(nombres)
        return render_template('ejercicio2.html', nombre_mas_largo=nombre_mas_largo, longitud=longitud)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)
