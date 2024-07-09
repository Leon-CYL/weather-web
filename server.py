from flask import Flask, request, render_template, flash
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    
    if not bool(city.strip()):
        flash('Please enter a non-empty City! The default weather is returned.', category='error')
        city = 'Castro Valley'
        
    weather_data = get_current_weather(city)
    
    if weather_data['cod'] != 200:
        flash('The City you enter is not Found! The default weather is returned.', category='error')
        weather_data = get_current_weather()
    
    return render_template(
        'weather.html', 
        title=weather_data['name'],
        feels_like=f"{weather_data['main']['feels_like']:.1f}",
        temp=f"{weather_data['main']['temp']:.1f}",
        status=weather_data['weather'][0]['description'].upper()
    )
    


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)