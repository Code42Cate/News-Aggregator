from flask import render_template
import connexion
import database


def remove_keyword(id, keyword):
    database.remove_keyword(id, keyword["keyword"])


def get_articles(index):
    articles = database.get_articles_json()
    articles = articles[len(articles) - index:len(articles) - index + 20]

    for article in articles:
        del article["content"]
        article["id"] = str(article["_id"])
        del article["_id"]
        categories = []
        keywords = []
        for keyword in article["keywords"]:
            temp = database.get_categories(keyword)
            if len(temp) is 0:
                keywords.append(keyword)
            else:
                categories.extend(temp)
        article["keywords"] = keywords
        article["categories"] = list(dict.fromkeys(categories))
    return articles


def update_keyword(keyword, category):
    database.update_keyword(keyword, category["category"])


# application instance
app = connexion.App(__name__, specification_dir="./")

# swagger.yml file to configure the endpoints
app.add_api("swagger.yml")

# Create a URL route in our application for "/"
@app.route("/")
def home():
    return render_template("newsletter_concept.html")


# If we're running in stand alone mode, run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
