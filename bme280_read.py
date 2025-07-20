import smbus2
import bme280

# I2C bus (usually 1 on Raspberry Pi and similar devices)
I2C_BUS = 1
# Default I2C address for BME280
BME280_ADDRESS = 0x76

def read_bme280():
    bus = smbus2.SMBus(I2C_BUS)
    # Load calibration parameters
    calibration_params = bme280.load_calibration_params(bus, BME280_ADDRESS)
    
    # Read sensor data
    data = bme280.sample(bus, BME280_ADDRESS, calibration_params)
    print(f"Temperature: {data.temperature:.2f} °C")
    print(f"Pressure: {data.pressure:.2f} hPa")
    print(f"Humidity: {data.humidity:.2f} %")

if __name__ == "__main__":
    read_bme280()