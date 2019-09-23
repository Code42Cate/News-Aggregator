from flask import render_template
import connexion
import database


def get_articles():
    articles = database.get_articles_json()[:20]
    for article in articles:
        del article['content']
        del article['_id']
    return articles


# application instance
app = connexion.App(__name__, specification_dir='./')

# swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

# Create a URL route in our application for "/"
@app.route('/')
def home():
    return render_template('newsletter_concept.html')


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
