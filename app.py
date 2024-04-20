from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# 处理根路径请求，返回欢迎页面
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/phoneus', methods=['GET'])
def phoneus():
    return render_template('phoneus.html')

if __name__ == '__main__':
    app.run(debug=True)
