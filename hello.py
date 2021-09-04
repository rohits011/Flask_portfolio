from flask import Flask, render_template, url_for,redirect,request
import csv
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/contact.html')
# def contact() :
#     return render_template('contact.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/components.html')
# def component():
#     return render_template('components.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

@app.route('/<string:page_name>')
def page( page_name="/" ):
    try:
        return render_template(page_name)
    except:
        return redirect('/')


@app.route('/submit_form', methods=['GET','POST'])
def submit():
    if request.method=='POST':
        try:
            data=request.form.to_dict()
            write_data_csv(data)
            message='''Thank You, Your form submitted successfully 
             we will get in touch to you shortly!!!'''
            return render_template('thankyou.html',message=message)
        except:
            message='Did not save dat to Database'
            return render_template('thankyou.html',message=message)
    else:
        message='Form not submitted'
        return render_template('thankyou.html',message=message)


def write_data_csv(data):
    email=data['email']
    subject=data['subject']
    message=data['message']
    with open('db.csv','a',newline="") as csvfile:
        db_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        db_writer.writerow([email,subject,message])