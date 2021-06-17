import pandas as pd
from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/s',methods=['POST'])
def s():
   
    if request.method=='POST':
        global df
        f = request.files['csv']
        df = pd.read_csv(f)
        

        
    else:
        print('unable to get csv')
    return render_template('read.html')

@app.route('/button',methods=["POST"])
def button():
   
    global d
    if request.method=='POST':
        a=request.form['select']
        d=pd.DataFrame(df,columns=[a])
    print(d)    
        
    return str(d)
app.run()