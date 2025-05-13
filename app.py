from flask import Flask, render_template
import os

app = Flask(__name__)
app.config['BASE_IMAGES'] = ['base_images/mars1.jpg', 'base_images/mars2.jpg']  # Обязательные базовые изображения


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/gallery')
def gallery():
    images = []
    for img_path in app.config['BASE_IMAGES']:
        full_path = os.path.join('static', img_path)
        if os.path.exists(full_path):
            images.append(img_path)
        else:
            print(f"Warning: Base image not found - {full_path}")

    return render_template('gallery.html', images=images)


if __name__ == '__main__':
    app.run(debug=True)

