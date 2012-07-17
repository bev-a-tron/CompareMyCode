from flask import Flask,redirect,url_for,render_template,request,Markup

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('userinfo.html')
    else:
        return redirect(url_for('main'))

@app.route('/main')
def main():
    return redirect(url_for('item'))

@app.route('/item',methods=['GET'])
def item():
    codeinhtml=Markup(\
    '''<pre>
def sum_two(a+b):
    if a==b: return 2*(a+b)
    else return a+b
    </pre>''')
    return render_template('layout.html',num=1,code=codeinhtml)

@app.route('/item',methods=['POST'])
def item2():
    return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(debug=True)
