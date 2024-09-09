from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template with form for temperature conversion
HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Temperature Converter</title>
</head>
<body>
    <h1>Temperature Converter</h1>
    <form method="post">
        <label for="temperature">Temperature:</label>
        <input type="text" id="temperature" name="temperature" required>
        <select name="unit" id="unit">
            <option value="celsius">Celsius to Fahrenheit</option>
            <option value="fahrenheit">Fahrenheit to Celsius</option>
        </select>
        <button type="submit">Convert</button>
    </form>
    {% if result is not none %}
    <h2>Result: {{ result }}</h2>
    {% endif %}
</body>
</html>
'''

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        temperature = float(request.form.get('temperature'))
        unit = request.form.get('unit')
        
        if unit == 'celsius':
            result = f'{temperature} Celsius is {celsius_to_fahrenheit(temperature):.2f} Fahrenheit'
        elif unit == 'fahrenheit':
            result = f'{temperature} Fahrenheit is {fahrenheit_to_celsius(temperature):.2f} Celsius'
    
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(debug=True)
