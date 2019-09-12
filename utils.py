from jinja2 import Template


def articles_to_csv(articles_tuple):
    with open("dataset.csv", encoding="utf8") as f:
        for url, title in articles_tuple:
            f.write('"{}","{}"'.format(title.replace(
                "\n", "").replace('"', "'"), url))


def articles_to_html(articles_tuple):
    template_string = ""
    with open("newsletter_template.html", "r") as f:
        template_string = f.read()
    articles = []
    for url, title in articles_tuple:
        dict_article = dict(url=url, title=title)
        articles.append(dict_article)
    Template(template_string).stream(articles=articles).dump("newsletter.html")


def get_stopwords():
    with open("stopwords.txt", "r") as stopwords_file:
        return stopwords_file.read().split("\n")


def articles_to_vocabulary(articles_tuple):
    vocabulary = []
    stopwords = get_stopwords()
    with open("vocabulary.txt", "r") as vocabulary_file:
        vocabulary = vocabulary_file.read().split('\n')

    for url, title in articles_tuple:
        words = title.split(" ")
        for word in words:
            word = word.lower()
            if word not in vocabulary and word not in stopwords:
                vocabulary.append(word.replace("\n", ""))
    with open("vocabulary.txt", "w") as vocabulary_file:
        for word in vocabulary:
            vocabulary_file.write("{}\n".format(word))
    print(vocabulary)

# It's in O(n²) and not stable, but hey at least its in-place!
# I am pretty sure that you _could_ do that in something like O(2n) aka O(n)
# But since our n will never be that big (Until now we didnt get over n = 300),
# I think that is good enough and everything else would be over-engineering
def remove_duplicates(articles):
    for url, title in articles:
        articles.remove((url, title)) 
        for url1, title1 in articles:
            if url1 == url:
                articles.remove((url1, title1))
        articles.append((url, title))
    return articles
