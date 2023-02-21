# Temperature Converter

This is a simple Python program for converting temperatures between Fahrenheit and Celsius. The program defines a function that takes in a temperature value and the temperature scale of that value, and returns the converted temperature value in the specified scale. The conversion formulas are straightforward and are based on the formulas for converting between Fahrenheit and Celsius:

* To convert Fahrenheit to Celsius: `(°F - 32) * 5/9`
* To convert Celsius to Fahrenheit: `°C * 9/5 + 32`

## Usage

To use the `convert_temp()` function, simply call the function and pass in the temperature value and the temperature scales. For example, to convert 98.6 degrees Fahrenheit to Celsius, you can call the function like this:
    
    python 
    
    celsius_temp = convert_temp(98.6) 

By default, the `convert_temp()` function assumes the input temperature value is in Fahrenheit and the output temperature scale is Celsius. If you need to convert a Celsius temperature to Fahrenheit, you can specify the input and output scales explicitly:
    
    python 
    
    fahrenheit_temp = convert_temp(37, from_scale='c', to_scale='f') 

## License

This program is licensed under the [MIT License](https://chat.openai.com/LICENSE). You are free to use, modify, and distribute the code as you see fit. Please see the `LICENSE` file for more information.

I hope you find this program useful! If you have any questions or feedback, feel free to open an issue on this repository.
