from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/hello")
def hello_world():
    client_ip = request.remote_addr
    visitor_name = request.args.get('visitor_name')

    location_city = ip2Location(client_ip)
    temperature = city2temperature(location_city)

    return jsonify({
        "client ip": client_ip,
        "location": location_city,
        "greeting": f"Hello, {visitor_name}!, the temperature is {temperature} in {location_city}"
        }),200

def ip2Location(client_ip):

    pass

def city2temperature(location_city):
    
    pass