from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to this form. Kindly fill all the details'

@app.route('/forms',methods=['GET','POST'])
def forms():
    if request.method=='POST':
        name = request.form['name']
        age = request.form['age']
        school = request.form['school']
        adress=request.form['adress']
        return(f"My name is {name}<br>My age is {age}<br>My school is {school}<br>My adress is {adress}")
        # return(name)
    return render_template('form.html')

if __name__=='__main__':
    app.run(debug=True)