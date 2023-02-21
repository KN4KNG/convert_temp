def convert_temp(temp, from_scale='f', to_scale='c'):
    """Converts temperature between Fahrenheit and Celsius.
    
    Args:
        temp (float): Temperature value to convert.
        from_scale (str): Temperature scale of input value ('f' for Fahrenheit, 'c' for Celsius). Default is 'f'.
        to_scale (str): Temperature scale to convert to ('f' for Fahrenheit, 'c' for Celsius). Default is 'c'.
        
    Returns:
        float: Converted temperature value.
    """
    if from_scale == 'f' and to_scale == 'c':
        return (temp - 32) * 5/9
    elif from_scale == 'c' and to_scale == 'f':
        return temp * 9/5 + 32
    else:
        return temp

# Example usage:
fahrenheit_temp = 98.6
celsius_temp = convert_temp(fahrenheit_temp)
print(f"{fahrenheit_temp}°F is {celsius_temp}°C")

celsius_temp = 37
fahrenheit_temp = convert_temp(celsius_temp, from_scale='c', to_scale='f')
print(f"{celsius_temp}°C is {fahrenheit_temp}°F")
