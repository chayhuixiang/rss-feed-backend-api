import feedparser
from goose3 import Goose

def getArticles(rssFeed):
    """Takes in an RSS feed URL and queries it for its top 10 articles. 
    Returns the URL
    See https://rss.app/docs/api/feeds/retrieve

    Keyword arguments:
    rssFeed -- A properly formatted API endpoint for an RSS feed ex("https://api.rss.app/v1/feeds/:feed_id")

    Returns:
    articleUrls, articleText -- An array of the article urls and text
    """
    rss_data = feedparser.parse(rssFeed).entries
    g = Goose()

    article_urls = []
    article_texts = []

    # Each feed entry corresponds to an article
    for rss_feed_entry in rss_data:

        # Retrieving the article link
        article_url = rss_feed_entry.link

        # Extracting the article text using goose3 library
        article = g.extract(url=article_url)

        article_urls.append(article_url)
        article_texts.append(article.cleaned_text)

    return article_urls, article_texts
    #ex: ["https://www.bbc.com/future/article/20231012-how-solar-eclipses-have-shaped-history", ...], ["Every so often, an eclipse has changed the course of pivotal events – for better and worse...", ...]


if __name__ == "__main__":
    # Uncomment any of these lines to test out the functionality of `getArticles`

    # print(getArticles("http://rss.cnn.com/rss/money_latest.rss"))
    # print(getArticles("http://rss.cnn.com/rss/money_topstories.rss"))
    pass
