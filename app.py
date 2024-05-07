import json

from flask import Flask, render_template

from controller.UserServerController import UserServerController

app = Flask(__name__)

# 处理根路径请求，返回欢迎页面
@app.route('/', methods=['GET'])
def index():

    return render_template('index.html')

@app.route('/phoneus', methods=['GET'])
def phoneus():
    return render_template('phoneus.html')


from flask import request, jsonify

@app.route('/login', methods=['POST'])
def login():
    data = json.loads(request.get_data(as_text=True))  # 更简单的方式来解析 JSON 数据
    print(data)
    con = UserServerController()
    result = con.findloginServerStatus(data)
    if str(data['username']) == '1111' and str(data['password']) == '2222':
        return jsonify({'success': True}), 200  # 返回 JSON 响应，并显示操作成功
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 200  # 返回错误信息和401状态码

@app.route('/register', methods=['POST'])
def register():
    data = json.loads(request.get_data(as_text=True)) # 更简单的方式来解析 JSON 数据
    print(data)
    con = UserServerController()
    result = con.adduserServerStatus(data)
    return jsonify({'success': True}), 200
@app.route('/guangzhou', methods=['GET'])
def goguangzhou():
    return render_template('guangzhou.html')
@app.route('/guangzhou/gz-fengjing', methods=['GET'])
def goguangzhoufengjing():
    return render_template('gz-fengjing.html')
@app.route('/guangzhou/gz-meishi', methods=['GET'])
def goguangzhoumeihshi():
    return render_template('gz-meishi.html')
@app.route('/guangzhou/guangzhou-map', methods=['GET'])
def goguangzhoumap():
    return render_template('guangzhou-map.html')


@app.route('/hongkong/hongkong-food', methods=['GET'])
def goHongKongFood():
    return render_template('hongkong-food.html')

@app.route('/hongkong/hkmap-test', methods=['GET'])
def goHKmap():
    return render_template('hkmap-test.html')


@app.route('/Macau', methods=['GET'])
def gomacau():
    return render_template('Macau.html')


@app.route('/Macau/Mc-fengjing', methods=['GET'])
def gomacaufengjing():
    return render_template('Mc-fengjing.html')


@app.route('/Macau/Mc-meishi', methods=['GET'])
def gomacaumeihshi():
    return render_template('Mc-meishi.html')


@app.route('/Macau/macau-map', methods=['GET'])
def gomacaumap():
    return render_template('macau-map.html')
if __name__ == '__main__':
    app.run(debug=True)
