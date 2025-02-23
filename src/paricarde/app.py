from flask import Flask, render_template

app = Flask(__name__, template_folder="templates", static_folder="static")

riders_list = [
    {"id": 1, "name": "Johan-Baptist Siffer", "team_id": 1, "number": 137, "nationality": "NO"},
    {"id": 2, "name": "Anaïs Caramba", "team_id": 2, "number": 269, "nationality": "ES"},
    {"id": 3, "name": "Pierrot Lasticot", "team_id": 3, "number": 22, "nationality": "CH"},
    {"id": 5, "name": "Alexandro Sambadejaneiro", "team_id": 5, "number": 7, "nationality": "BR"},
    {"id": 7, "name": "Adrien Bisou", "team_id": 7, "number": 4, "nationality": "IT"},
    {"id": 8, "name": "Eve Carpenter", "team_id": 8, "number": 98, "nationality": "IE"},
    {"id": 9, "name": "Martìn Elnormando", "team_id": 9, "number": 29, "nationality": "MX"},
    {"id": 10, "name": "Manuela Tequila", "team_id": 10, "number": 45, "nationality": "CO"},
    {"id": 11, "name": "Michel Michel", "team_id": 11, "number": 3000, "nationality": "BE"},
    {"id": 12, "name": "Mary Robertwood", "team_id": 12, "number": 123, "nationality": "GB"},
]

teams_list = [
    {"id": 1, "name": "Nespresso-Michelin"},
    {"id": 2, "name": "FNAC-FranceBudget"},
    {"id": 3, "name": "Team Darty-SNCF"},
    {"id": 5, "name": "Logitech Cycling Team"},
    {"id": 7, "name": "Logitech Cycling Team"},
    {"id": 8, "name": "Matmut"},
    {"id": 9, "name": "Suntory Racing"},
    {"id": 10, "name": "DonJulio Sporting"},
    {"id": 11, "name": "FT AENF - Decathlon"},
    {"id": 12, "name": "EF Education - Easypost"},
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/participants")
def riders():
    return render_template("riders.html", riders=riders_list, teams=teams_list)

@app.route("/participant/<int:id>")
def rider(id):
    participant = next((p for p in riders_list if p["id"] == id), None)
    if not participant:
        return "Participant non trouvé", 404
    return render_template("rider.html", rider=participant, teams=teams_list)

@app.route("/tracé")
def race():
    return render_template("race.html")

@app.route("/inscription")
def registration():
    return render_template("registration.html")

if __name__ == "__main__":
    app.run(debug=True)