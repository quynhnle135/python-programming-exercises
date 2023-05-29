def convertToCelcius(fahrenheit):
    result = (fahrenheit - 32) * (5/ 9)
    return result

def convertToFahrenheit(celsius):
    result = celsius * (9 / 5) + 32
    return result