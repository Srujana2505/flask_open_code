from flask import Flask, request, render_template, render_template_string

app = Flask(__name__)
app.secret_key = 'shh! this is a secret'

@app.route('/')
def hello_world():
    return render_template('home.html')
@app.route('/chal_one/')
def hello_name():
    name = request.args.get('name')

    template = '''
        <h1>Hello {}</h1>
    '''.format(name)

    return render_template_string(template)


        
