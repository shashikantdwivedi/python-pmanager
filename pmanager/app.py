from flask import Flask, render_template, request, redirect, url_for, flash, session
import database_functions as db_fun

app = Flask(__name__)
# TODO - Replace SECRET-KEY with your application secret key
app.secret_key = "SECRET-KEY"


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/validate_login', methods=["POST"])
def validate_login():
    username = (request.form['username']).strip()
    password = (request.form['password']).strip()
    result = db_fun.validate_login(username, password)
    session["username"] = username
    if result:
        return redirect(url_for('home'))


@app.route('/home')
@app.route('/home/page/<int:page_no>')
def home(page_no=1):
    if 'username' in session:
        records_info = db_fun.page_records(page_no)
        return render_template('index.html', records_info=records_info)
    else:
        return redirect(url_for('login'))


@app.route('/search')
def search(page_no=1):
    if 'username' in session:
        keywords = (request.args.get('keywords')).strip()
        records_info = db_fun.search(keywords=keywords, page_no=page_no)
        return render_template('search.html', records_info=records_info, keywords=keywords)
    else:
        return redirect(url_for('login'))


@app.route('/search/page/<int:page_no>/<keywords>')
def search_page(page_no=1, keywords=''):
    if 'username' in session:
        records_info = db_fun.search(keywords=keywords, page_no=page_no)
        return render_template('search.html', records_info=records_info, keywords=keywords)
    else:
        return redirect(url_for('login'))


@app.route('/add_record', methods=['POST'])
def add_record():
    if 'username' in session:
        email_username = (request.form['email_username']).strip()
        website = (request.form['website']).strip()
        password = (request.form['password']).strip()
        data = {'email_username': email_username, 'website': website, 'password': password}
        db_fun.add_record(data)
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))


@app.route('/update_record', methods=['POST'])
def update_record():
    if 'username' in session:
        sno = int((request.form['sno']).strip())
        email_username = (request.form['email_username']).strip()
        website = (request.form['website']).strip()
        password = (request.form['password']).strip()
        data = {'email_username': email_username, 'website': website, 'password': password, '_id': sno}
        db_fun.update_record(data)
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))


@app.route('/delete_record', methods=['POST'])
def delete_record():
    if 'username' in session:
        _id = int((request.form['sno']).strip())
        db_fun.delete_record(_id)
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
