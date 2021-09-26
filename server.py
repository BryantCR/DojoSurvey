from flask import Flask, render_template, request, redirect, session

app = Flask( __name__ )

app.secret_key = "secret"

@app.route("/", methods = ['GET'])
def userFormData():
    return render_template('index.html')


@app.route("/process", methods = ['POST'])
def validateFormInfo():
    session['userNameForm'] = request.form['userName']
    session['locationsForm'] = request.form['locations']
    session['languagesForm'] = request.form['languages']
    session['commentFormForm'] = request.form['commentForm']
    return redirect('/result')


@app.route("/result", methods = ['GET'])
def userAnswer():
    return render_template('result.html')
    return redirect('/')


if __name__ == "__main__":
    app.run( debug = True )