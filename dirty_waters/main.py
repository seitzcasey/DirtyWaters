import ast

from flask import Flask, request, render_template
from dirty_waters.game.modes.default_game import DefaultGame

app = Flask(__name__)

# Route to display the form
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    grid_html = game.grid_manager.to_html()
    return grid_html

@app.route('/handle_click', methods=['POST'])
def handle_click():
    data = request.json

    fleet_id = int(data.get('fleet_id'))

    # Ensure that the value is converted or cast to a tuple of integers
    coordinate: tuple[int, int] = ast.literal_eval(data.get('coordinate'))
    print(coordinate)

    hit = game.check_hit(1, fleet_id, coordinate)
    return "HIT!" if hit else "MISS!"
    
if __name__ == '__main__':
    game = DefaultGame()

    app.run(debug=True)
