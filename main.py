from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# DEFINIMOS LAS RUTAS PARA LOS LINKS DEL NAVBAR
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ecosistemas')
def ecosistemas():
    return render_template('ecosistemas.html')   

@app.route('/fauna')
def fauna():
    return render_template('fauna.html')

@app.route('/flora')
def flora():
    return render_template('flora.html')    

@app.route('/parques')
def parques():
    return render_template('parques.html')

# DEFINIMOS LAS RUTAS PARA LOS LINKS DEL DROPDOWN
@app.route('/pnnChingaza', methods=['GET', 'POST'])
def pnn_chingaza():
    return render_weather_template('pnnChingaza.html')

@app.route('/pnnCocuy', methods=['GET', 'POST'])
def pnn_cocuy():
    return render_weather_template('pnnCocuy.html')

@app.route('/pnnOceta', methods=['GET', 'POST'])
def pnn_oceta():
    return render_weather_template('pnnOceta.html')

@app.route('/pnnPisba', methods=['GET', 'POST'])
def pnn_pisba():
    return render_weather_template('pnnPisba.html')

@app.route('/pnnSumapaz', methods=['GET', 'POST'])
def pnn_sumapaz():
    return render_weather_template('pnnSumapaz.html')

@app.route('/paramoGuargua', methods=['GET', 'POST'])
def paramo_guargua():
    return render_weather_template('paramoGuargua.html')

def render_weather_template(template_name):
    weather_data = None
    error_message = None
    
    if request.method == 'POST':
        city = request.form['search']
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.text
            return render_template(template_name, weather=weather_data)
        else:
            error_message = "No se pudo obtener la información del clima."
            return render_template(template_name, error=error_message)
    return render_template(template_name)

if __name__ == '__main__':
    app.run(port=5000, debug=True)