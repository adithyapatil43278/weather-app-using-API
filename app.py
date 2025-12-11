from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/temperature", methods=["GET"])
def get_temperature():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "Provide ?city=CityName"}), 400

    # Step 1: Convert city → lat/lon
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    geo_res = requests.get(geo_url).json()

    if "results" not in geo_res or len(geo_res["results"]) == 0:
        return jsonify({"error": "City not found"}), 404

    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]

    # Step 2: Fetch weather
    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&current_weather=true"
    )
    weather_res = requests.get(weather_url).json()

    temp = weather_res["current_weather"]["temperature"]
    wind = weather_res["current_weather"]["windspeed"]

    return jsonify({
        "city": city,
        "latitude": lat,
        "longitude": lon,
        "temperature": temp,
        "windspeed": wind
    })


@app.route("/suggest", methods=["GET"])
def suggest_cities():
    q = request.args.get("q")
    if not q:
        return jsonify([])

    try:
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={q}&count=10"
        geo_res = requests.get(geo_url, timeout=5).json()
        results = geo_res.get("results", [])
        # Return a simplified list for the frontend
        suggestions = []
        for r in results:
            name = r.get("name")
            admin = r.get("admin1") or r.get("country")
            latitude = r.get("latitude")
            longitude = r.get("longitude")
            display = name
            if admin:
                display = f"{name}, {admin}"
            suggestions.append({
                "display": display,
                "name": name,
                "latitude": latitude,
                "longitude": longitude
            })

        return jsonify(suggestions)
    except Exception:
        return jsonify([]), 500

if __name__ == "__main__":
    app.run(debug=True)
