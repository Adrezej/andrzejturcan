from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


class PhoneBot:
    def __init__(self):
        self.phone_list = {
            'Phone1': 50,
            'Phone2': 60,
            'Phone3': 45,
            'Phone4': 70,
            'Phone5': 55
        }

    def check_phone_price(self, user_price, user_phone):
        if user_phone in self.phone_list:
            phone_price = self.phone_list[user_phone]
            if 40 <= user_price <= 70 and user_price >= phone_price:
                return f"Модель {user_phone} стоит {phone_price} евро."
            else:
                return "Извините, указанная цена вне диапазона или недостаточна для выбранного телефона."
        else:
            return "Извините, этого телефона в списке нет."


@app.route('/')
def index():
    return render_template('index.html', phone_list=PhoneBot().phone_list)


@app.route('/send_query', methods=['POST'])
def send_query():
    data = request.json
    user_price = data['user_price']
    user_phone = data['user_phone']

    phone_bot = PhoneBot()
    result = phone_bot.check_phone_price(user_price, user_phone)

    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)
