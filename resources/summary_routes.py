from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from models import BookmarkModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
import json
from flask import request, jsonify
from resources import openai_calls
from resources import rss_calls

blp = Blueprint("tasks", __name__, description="Summary APIs")

@blp.post('/summaries')
def summaries():
    data = request.get_json()  # Get JSON data sent with the request
    feed_url = data.get('feed_url')  # Extract the RSS feed URL from the JSON data
    if not feed_url:
        return jsonify({"error": "feed_url is required"}), 400  # Return an error if 'feed_url' is not provided

    try:
        # Retrieve article URLs and texts from the RSS feed
        article_urls, article_texts = rss_calls.getArticles(feed_url)
        summaries = []  # Initialize a list to store summaries
        # Iterate over each URL and corresponding text
        for url, text in zip(article_urls, article_texts):
            summary = openai_calls.getSummary(text)  # Summarize the article text
            summaries.append({"article_url": url, "summary": summary})  # Append the summary to the list

        return jsonify({"summaries": summaries}), 200  # Return the summaries as JSON with a 200 status code
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle any exceptions that occur


@blp.post("/bookmarks")
def addBookmark():
    """
    Summarizes top 10 articles in an rss feed. Utilize the functions in openai_calls.py and rss_calls.py

    Input (json): {article_url: "", summary: ""}
    
    Output: None (200 response)
    """
    input = request.get_json()
    if "article_url" in input and "summary" in input:
        bookmark = BookmarkModel(**input)
        try:
            db.session.add(bookmark)
            db.session.commit()
            return {}
        except SQLAlchemyError:
            abort(500, message="Error occured while inserting item")
    else:
        abort(400, message="Invalid arguments")


@blp.get("/bookmarks")
def getBookmarks():
    """
    Summarizes top 10 articles in an rss feed. Utilize the functions in openai_calls.py and rss_calls.py

    Input: None
    
    Output (json): Summaries for the top 10 (?) articles in the feed {bookmarks: [{article_url: "", summary: ""}, {article_url: "", summary: ""}...]}
    """
    bookmarks = BookmarkModel.query.all()
    result = []
    for bookmark in bookmarks:
        result.append({"article_url": bookmark.article_url, "summary": bookmark.summary})
    return {"bookmarks": result}
