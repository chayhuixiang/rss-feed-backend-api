# Team 3
## Members: Hui Xiang Chay, Linda Mutesi, Rohit Mittal, Shubham Gupta
The goal of our project is to create an API that takes RSS feeds and summarizes them before returning them to a user. Users create an account with our API and set preferences for which feeds they want to summarize, as well as bookmark articles for later access. This information is persisted in a database and used to connect to https://rss.app, a RESTful API for RSS feeds. The feed information returned from rss.app is then summarized with OpenAI tools before being returned to the user. Information returned to the user depends on what the creator of the work (article, podcast etc) has allowed the public to access.

APIs that we plan to use: 
RSS Feed API 
OpenAI API
