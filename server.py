from flask import Flask, render_template, request, redirect, session

app = Flask( __name__ )
app.secret_key = "secret"

@app.route("/", methods = ['GET'])
def userFormData():
    #print( userNameForm )
    return render_template('index.html')

@app.route("/result", methods = ['GET'])
def validateFormInfo():
    userNameForm = request.form['userName']
    locationsForm = request.form['locations']
    languagesForm = request.form['languages']
    commentFormForm = request.form['commentForm']
    return render_template('result.html')




if __name__ == "__main__":
    app.run( debug = True )