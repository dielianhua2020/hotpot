from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html',name='francis')

@app.route('/<string:pagename>')
def hello_world3(pagename):
    return render_template(pagename)

def database_csv(data):
    email=data['email']
    subject=data['subject']
    content=data['content']
    with open('./database.csv',mode='a',newline='') as csvfile:
        csvwriter=csv.writer(csvfile,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([email,subject,content])

@app.route('/submit_req',methods=['POST', 'GET'])
def submit_req():
    if request.method=='POST':
      data=request.form.to_dict()

      print(data['email'])
      # return redirect('/thankyou')
      # thankyou_page(data)
      with open('./text.txt','a') as inputFile:
          email=data['email']
          writer=inputFile.write(f'\n{email}')
      database_csv(data)
      return render_template('/thankyou.html',name=data['email'])

    else:
      return 'not updated'


# @app.route('/<string:pagename>')
# def thankyou_page(data):
#     return render_template(pagenam

#     # return 'Hello, World!!!!!'
# @app.route('/works.html')
# def hello_world2():
#     return render_template('works.html')
#
# @app.route('/work.html')    #int has been used as a filter that only integer will be passed in the url otherwise it will give a 404 error
# def find_question():
#     return render_template('work.html')
#
# @app.route('/contact.html')
# def aontact():
#     return render_template('contact.html')
#
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
# @app.route('/components.html')    #int has been used as a filter that only integer will be passed in the url otherwise it will give a 404 error
# def find_question2():
#     return render_template('components.html')
