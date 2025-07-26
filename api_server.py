from flask import Flask
import threading
import time
from bme280_read import read_bme280

# Shared HTML string
sensor_data_html = "Loading data..."

# Flask app
app = Flask(__name__)

@app.route("/")
def index():
    return f"""
    <html>
        <head>
            <title>BME280 Sensor</title>
            <meta http-equiv="refresh" content="60">
        </head>
        <body>
            <h1>BME280 Sensor Data</h1>
            <pre>{sensor_data_html}</pre>
        </body>
    </html>
    """

# Background thread to update sensor data every minute
def update_sensor_data():
    global sensor_data_html
    while True:
        temperature, pressure, humidity, dew_point = read_bme280()
        sensor_data_html = (
            f"timestamp={time.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"temp={temperature:.2f}\n"
            f"pressure={pressure:.2f}\n"
            f"humidity={humidity:.2f}\n"
            f"dew_point={dew_point:.2f}\n"
        )
        time.sleep(60)

if __name__ == "__main__":
    threading.Thread(target=update_sensor_data, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)

