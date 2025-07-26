import smbus2
import bme280
import math as m

# I2C bus (usually 1 on Raspberry Pi and similar devices)
I2C_BUS = 1
# Default I2C address for BME280
BME280_ADDRESS = 0x76

def dew_point(temperature: float, humidity:float) -> float:
    a = 17.625
    b = 243.04

    alpha = (a * temperature) / (b + temperature) + m.log(humidity/100)
    Td = (b * alpha) / (a - alpha)

    return Td

def read_bme280() -> tuple:
    bus = smbus2.SMBus(I2C_BUS)
    # Load calibration parameters
    calibration_params = bme280.load_calibration_params(bus, BME280_ADDRESS)
    
    # Read sensor data
    data = bme280.sample(bus, BME280_ADDRESS, calibration_params)
    dew = dew_point(data.temperature, data.humidity)
    return (data.temperature, data.pressure, data.humidity, dew)

if __name__ == "__main__":
    temperature, pressure, humidity, dew = read_bme280()
    print(f"Temperature: {temperature:.2f} °C")
    print(f"Pressure: {pressure:.2f} hPa")
    print(f"Humidity: {humidity:.2f} %")
    print(f"Dew Point: {dew:.2f} ºC")
