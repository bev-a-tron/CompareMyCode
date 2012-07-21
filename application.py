from flask import Flask,redirect,url_for,render_template,request,Markup


stri=['''
def sum_two(a+b):
    if a==b: return 2*(a+b)
    else return a+b''',
'''
def sleep_in(weekday, vacation):
  if not weekday or vacation: return True
  else: return False''']

#stri=[]
#f = open('data.txt')
#for line in f:

app=Flask(__name__)
app.count=0

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('userinfo.html')
    else:
        return redirect(url_for('main'))

@app.route('/main')
def main():
    if app.count<len(stri):
        return redirect(url_for('item'))
    else:
        return render_template('end.html')

@app.route('/item',methods=['GET'])
def item():
    codeinhtml=Markup('''<pre>
%s
</pre>'''%(stri[app.count]))
    app.count+=1
    return render_template('layout.html',num=app.count,code=codeinhtml)

@app.route('/item',methods=['POST'])
def item2():
    return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(debug=True)
