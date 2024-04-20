import json

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# 处理根路径请求，返回欢迎页面
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/phoneus', methods=['GET'])
def phoneus():
    return render_template('phoneus.html')

# @app.route('/login', methods=['POST'])
# def login():
#     data = json.loads(request.get_data(as_text=True))
#     print(data)
#     if data['username'] == '1111' and data['password'] == '2222':
#         return 'success'
#     else:
#         return 'error'  # 字典

from flask import Flask, request, jsonify

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # 更简单的方式来解析 JSON 数据
    print(data)
    if str(data['username']) == '1111' and str(data['password']) == '2222':
        return jsonify({'success': True}), 200  # 返回 JSON 响应，并显示操作成功
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 200  # 返回错误信息和401状态码

@app.route('/register', methods=['POST'])
def register():
    data = json.loads(request.get_data(as_text=True)) # 更简单的方式来解析 JSON 数据
    print(data)
    return jsonify({'success': True}), 200

if __name__ == '__main__':
    app.run(debug=True)
