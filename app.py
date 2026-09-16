from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Weather API Endpoint
@app.route('/api/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', 'Mumbai')
    
    # OpenWeatherMap API Call
    api_key = "YOUR_API_KEY_HERE"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Auth Endpoint (Guest & Custom)
@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username', 'guest')
    return jsonify({
        "status": "success",
        "message": f"Welcome {username}",
        "token": "jwt-token-sample-123"
    })

if __name__ == '__main__':
    app.run(debug=True)
