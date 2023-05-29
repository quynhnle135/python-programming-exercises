from tempertature_conversion import convertToCelcius, convertToFahrenheit


def main():
    print(f"Convert to Celsius {convertToCelcius(0)}")
    print(f"Convert to Celsius {convertToCelcius(180)}")
    print(f"Convert to Fahrenheit {convertToFahrenheit(0)}")
    print(f"Convert to Fahrenheit {convertToFahrenheit(100)}")
    print(f"Convert to Celsius {convertToCelcius(convertToFahrenheit(15))}")


if __name__ == "__main__":
    main()