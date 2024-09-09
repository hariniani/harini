from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template with form for CGPA calculation
HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>CGPA Calculator</title>
</head>
<body>
    <h1>CGPA Calculator</h1>
    <form method="post">
        <fieldset>
            <legend>Enter your grades and credits:</legend>
            <div id="subjects">
                <div class="subject">
                    <label for="grade_1">Grade:</label>
                    <input type="text" id="grade_1" name="grades" required>
                    <label for="credits_1">Credits:</label>
                    <input type="number" id="credits_1" name="credits" required>
                </div>
            </div>
            <button type="button" onclick="addSubject()">Add More</button>
            <button type="submit">Calculate CGPA</button>
        </fieldset>
    </form>
    {% if cgpa is not none %}
    <h2>CGPA: {{ cgpa }}</h2>
    {% endif %}
    <script>
        let subjectCount = 1;

        function addSubject() {
            subjectCount++;
            const subjectsDiv = document.getElementById('subjects');
            const newSubjectDiv = document.createElement('div');
            newSubjectDiv.className = 'subject';
            newSubjectDiv.innerHTML = `
                <label for="grade_${subjectCount}">Grade:</label>
                <input type="text" id="grade_${subjectCount}" name="grades" required>
                <label for="credits_${subjectCount}">Credits:</label>
                <input type="number" id="credits_${subjectCount}" name="credits" required>
            `;
            subjectsDiv.appendChild(newSubjectDiv);
        }
    </script>
</body>
</html>
'''

def calculate_cgpa(grades, credits):
    total_grade_points = sum(g * c for g, c in zip(grades, credits))
    total_credits = sum(credits)
    return total_grade_points / total_credits if total_credits > 0 else 0

@app.route('/', methods=['GET', 'POST'])
def index():
    cgpa = None
    if request.method == 'POST':
        grades = request.form.getlist('grades')
        credits = request.form.getlist('credits')

        # Convert inputs to floats
        grades = [float(g) for g in grades]
        credits = [float(c) for c in credits]

        # Calculate CGPA
        cgpa = calculate_cgpa(grades, credits)

    return render_template_string(HTML_TEMPLATE, cgpa=cgpa)

if __name__ == '__main__':
    app.run(debug=True)
