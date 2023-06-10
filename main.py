from flask import *
from potter import *

app = Flask(__name__)


SECRET_KEY = '83asz!lKDKJSkdlk#sjs03lzo%vnl029Dks!j23'


plot_number = 0
plot_list = []
your_name = ''

@app.route('/')
def home():
    disabled = False
    return render_template('index.html', button_disabled=disabled, scroll='scroll_to')

@app.route('/reset', methods=['POST', 'GET'])
def reset():
    global plot_list
    global plot_number
    plot_list = []
    plot_number = 0
    your_name = ''
    return redirect(url_for('home'))

@app.route('/choose_your_character', methods=['POST', 'GET'])
def choose_your_character():
    global your_name
    if request.method == 'POST':
        #print next plot point to screen
        rando = request.form.get('rando')
        yourself = request.form.get('yourself')
        if rando:
            your_name = you + your_rand_name()
            session['random_selected'] = True
            return render_template('index.html', button_disabled=True, rando_selected=True, random_name=your_name)
        elif yourself:
            session['random_selected'] = False
            return redirect(url_for('next_plot'))


@app.route('/next_plot', methods=['POST', 'GET'])
def next_plot(random_selected=None):
    global your_name
    global plot_number
    if len(plot_list) < len(plot_points):
        print("next_plot", len(plot_list), len(plot_points))
        if plot_number == 0:
            new_plot = plot_points[plot_number] + random_student()
        elif plot_number > 0 and plot_number < len(plot_points) - 1:
            new_plot = plot_points[plot_number] + random_char()
        else:
            new_plot = plot_points[plot_number] + random_char() + " & " + random_char()
        plot_list.append(new_plot)
        plot_number += 1
        return render_template('index.html', print_plot=True, new_plot=new_plot, plot_list=plot_list, scroll='scroll_to', button_disabled=True, rando_selected=session['random_selected'], random_name=your_name, restart=False)
    else:
        return render_template('index.html', print_plot=True, plot_list=plot_list, end_of_game=True, ending=random_ending(), scroll='restart', button_disabled=True, rando_selected=session['random_selected'], random_name=your_name, restart=True)





if __name__ == "__main__":
    app.secret_key = SECRET_KEY
    app.config['SESSION_TYPE'] = 'filesystem'


    app.run(debug=True)