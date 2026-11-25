from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Функция для подключения к БД
def get_db():
    conn = sqlite3.connect('collection.db')
    conn.row_factory = sqlite3.Row  # Чтобы можно было обращаться по именам колонок
    return conn

# === ГЛАВНАЯ СТРАНИЦА ===
@app.route('/')
def index():
     #Задание: Получи все элементы из БД и передай в шаблон
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    return render_template('index.html', items=items)
    
@app.route('/item/<int:item_id>')
def item(item_id):
    #Задание: Получи один элемент по ID из БД
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE id = ?", (item_id,))
    item = cursor.fetchone()
    return render_template('item.html', item=item)
    
   
# === ФОРМА ДОБАВЛЕНИЯ ===
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Задание: Получи данные из формы и сохрани в БД
        # title = request.form['title']
        # year = request.form['year']
        # genre = request.form['genre']
        # image_url = request.form['image_url']
        # description = request.form['description']
        
        # conn = get_db()
        # cursor = conn.cursor()
        # cursor.execute("""
        #     INSERT INTO items (title, year, genre, image_url, description)
        #     VALUES (?, ?, ?, ?, ?)
        # """, (title, year, genre, image_url, description))
        # conn.commit()
        
        return redirect(url_for('index'))
    
    return render_template('add.html')

# === СТРАНИЦА "О ПРОЕКТЕ" ===
@app.route('/about')
def about():
    return render_template('about.html')

# === API (для JS-фильтров) ===
@app.route('/api/items')
def api_items():
    # Задание: Верни все элементы в формате JSON
    # conn = get_db()
    # cursor = conn.cursor()
    # cursor.execute("SELECT * FROM items")
    # items = [dict(row) for row in cursor.fetchall()]
    # return jsonify(items)
    
    return "API (доделай!)"

if __name__ == '__main__':
    app.run(debug=True)