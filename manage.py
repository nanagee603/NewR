from flask import Flask, render_template

app = Flask(__name__)

# Define the home page route
@app.route('/')
def home():
    return render_template('home.html')

# Define the employee registration page route
@app.route('/registration')
def registration():
    return render_template('registration.html')

# Define the employee information page route
@app.route('/information')
def information():
    # Query the database to get all employees
    # You can use any SQLite library for Python, such as sqlite3 or SQLAlchemy
    employees = [(1, 'John', 'Male', '123-456-7890', '1990-01-01'),
                 (2, 'Jane', 'Female', '123-456-7891', '1991-02-02'),
                 (3, 'Bob', 'Male', '123-456-7892', '1992-03-03'),
                 (4, 'Alice', 'Female', '123-456-7893', '1993-04-04'),
                 (5, 'Jack', 'Male', '123-456-7894', '1994-05-05'),
                 (6, 'Jill', 'Female', '123-456-7895', '1995-06-06'),
                 (7, 'David', 'Male', '123-456-7896', '1996-07-07'),
                 (8, 'Emily', 'Female', '123-456-7897', '1997-08-08'),
                 (9, 'Mike', 'Male', '123-456-7898', '1998-09-09')]
    return render_template('information.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)

