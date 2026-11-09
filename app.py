from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/products')
def get_products():
    products_list = []
    try:
       
        response = requests.get('https://fakestoreapi.com/products')
        if response.status_code == 200:
            api_data = response.json()
            for item in api_data:
                cat = item['category']
                if 'clothing' in cat:
                    category_pl = 'Odzież'
                elif 'jewelery' in cat:
                    category_pl = 'Biżuteria'
                elif 'electronics' in cat:
                    category_pl = 'Elektronika'
                else:
                    category_pl = 'Inne'

                products_list.append({
                    "name": item['title'],
                    "price_pln": int(item['price'] * 4.5), # Przeliczenie na PLN
                    "category": category_pl,
                    "image": item['image'], # Bezpośredni link do zdjęcia z API
                    "description": item['description']
                })
    except Exception as e:
        print("Błąd pobierania API:", e)

    return jsonify(products_list)

if __name__ == '__main__':
    app.run(debug=True)
