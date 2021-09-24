from flask import Flask, request, render_template, render_template_string
import textwrap

app = Flask(__name__)

# not a SECRET anymore, haha
app.secret_key = 'shh! this is a secret'


def dedent(inner):
    def wrapper():
        return textwrap.dedent(inner()).strip()

    return wrapper


@app.route('/', endpoint='index')
def index():
    return render_template('home.html')


@app.route('/chal_one/', endpoint='hello_name', methods=['GET', 'POST'])
@dedent
def hello_name():
    if request.method == 'POST':
        name = request.form.get('name', None)

        if name:
            template = f'''
                <h1>Hello {name}</h1>
            '''

            return render_template_string(template)

    return '''
        <form action="" method="POST">
            <h3 style="margin: 0px;">Exploit me</h3>
            <input type="text" name="name" value="" placeholder"enter your name"/>
            <input type="submit" name="submit" value="submit"/>
        </form>
    '''


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="1337")
