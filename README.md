# Weather App – Flask + Open-Meteo API

A lightweight web application that displays real-time temperature and wind data for any city.
Built using **Flask**, **Open-Meteo APIs**, and a simple **HTML/CSS/JavaScript** frontend.

The project demonstrates:

- How a frontend sends API requests to a backend
- How Flask handles HTTP routes and returns JSON responses
- How to consume a third-party public API (Open-Meteo)
- Basic chart rendering and UI styling for weather visualization

---

**🚀 Features**

- **Search any city** and get current weather information:
  - **Current temperature**
  - **Wind speed**
  - **Location coordinates**
- Uses **free, keyless** Open-Meteo APIs (rate-friendly)
- Clean, responsive UI (custom CSS)
- JavaScript-based charts for data visualization (e.g., `Chart.js`)
- Backend + frontend served from Flask (no CORS required)

---

**📁 Project Structure**

weather-app/
│
├── `app.py`
├── `requirements.txt`
├── `README.md`
│
└── `templates/`
    └── `index.html`


---

**🖥️ How It Works**

1. User opens the web app
2. The frontend calls the Flask endpoint:

   `/temperature?city=CityName`

3. Flask:
   - Uses Open-Meteo Geocoding API to convert `city` → `latitude, longitude`.
   - Uses Open-Meteo Weather API to fetch current temperature and wind speed for those coordinates.
   - Returns structured JSON back to the frontend.
4. JavaScript updates the UI and renders charts.

---

**📦 Installation & Setup**

Clone the repository:

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask server:

```powershell
python app.py
```

Open in your browser:

```text
http://127.0.0.1:5000
```

**🧪 Example API Usage**

```bash
curl "http://127.0.0.1:5000/temperature?city=Delhi"
```

Example JSON response:

```json
{
  "city": "Delhi",
  "latitude": 28.66,
  "longitude": 77.21,
  "temperature": 23.4,
  "windspeed": 5.0
}
```

---

**📚 Technologies Used**

- Python
- Flask
- Requests
- Open-Meteo API
- HTML5
- CSS3
- JavaScript
- Chart.js (optional)

---

**🙌 Acknowledgements**

Weather data provided by Open-Meteo.

Designed and developed as a practice project for learning APIs, web servers, and full-stack basics.
