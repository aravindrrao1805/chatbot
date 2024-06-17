import dash
import dash_html_components as html

students = [
    {"name": "John", "surname": "Doe", "department": "Computer Science", "age": 21, "grade": 88},
    {"name": "Jane", "surname": "Smith", "department": "Mathematics", "age": 22, "grade": 92},
    {"name": "Emily", "surname": "Johnson", "department": "Physics", "age": 20, "grade": 85},
    {"name": "Michael", "surname": "Williams", "department": "Chemistry", "age": 23, "grade": 79},
    {"name": "Sarah", "surname": "Brown", "department": "Biology", "age": 21, "grade": 91},
    {"name": "David", "surname": "Jones", "department": "Computer Science", "age": 22, "grade": 87},
    {"name": "Laura", "surname": "Garcia", "department": "Mathematics", "age": 20, "grade": 94},
    {"name": "Daniel", "surname": "Martinez", "department": "Physics", "age": 22, "grade": 78},
    {"name": "Sophia", "surname": "Rodriguez", "department": "Chemistry", "age": 21, "grade": 82},
    {"name": "James", "surname": "Davis", "department": "Biology", "age": 23, "grade": 89},
    {"name": "Olivia", "surname": "Lopez", "department": "Computer Science", "age": 20, "grade": 90},
    {"name": "William", "surname": "Gonzalez", "department": "Mathematics", "age": 21, "grade": 85},
    {"name": "Ava", "surname": "Wilson", "department": "Physics", "age": 22, "grade": 88},
    {"name": "Ethan", "surname": "Anderson", "department": "Chemistry", "age": 20, "grade": 80},
    {"name": "Isabella", "surname": "Thomas", "department": "Biology", "age": 21, "grade": 92},
    {"name": "Mason", "surname": "Taylor", "department": "Computer Science", "age": 23, "grade": 84},
    {"name": "Mia", "surname": "Moore", "department": "Mathematics", "age": 22, "grade": 90},
    {"name": "Alexander", "surname": "Jackson", "department": "Physics", "age": 21, "grade": 86},
    {"name": "Charlotte", "surname": "Martin", "department": "Chemistry", "age": 20, "grade": 83},
    {"name": "Lucas", "surname": "Lee", "department": "Biology", "age": 23, "grade": 87}
]


app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Students"),
    dash.dash_table.DataTable(students, page_size = 5)
])

if __name__ == "__main__":
    app.run(debug = True)

