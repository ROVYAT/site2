from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    # Получаем изображение из запроса
    file = request.files['image']
    if file:
      # Сохраняем изображение в папку uploads
      file.save(f'uploads/{file.filename}')

      # Выводим подтверждение успешной загрузки
      return render_template('index.html', message=f"Изображение '{file.filename}' успешно загружено!")
    else:
      return render_template('index.html', message="Ошибка загрузки изображения.")
  else:
    return render_template('index.html')

if __name__ == "__main__":
  app.run(debug=True)
