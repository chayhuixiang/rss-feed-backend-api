<h1 align="center">Project Team 3</h1>

**Team Members**: Hui Xiang Chay, Linda Mutesi, Rohit Mittal, Shubham Gupta

### **Goal of the Project:**

To create an application that automatically fetches, summarizes, and stores content from various RSS feeds. Users can subscribe to these feeds, get the latest updates in the form of article summaries, and have the option to bookmark them for later reading.

### **Project Achievements:**

1. `Automatically Fetching Content`: The application fetches articles from RSS feeds using the getArticles function, which retrieves the top 10 articles from a given RSS feed URL.
   The getArticles function in rss_calls.py is responsible for fetching the top articles from an RSS feed.

2. `Summarizing Content`: The application utilizes the OpenAI API to summarize the articles fetched from the RSS feeds. The application processes text in chunks to handle larger articles and provide summaries using the getSummary function.
   The getSummary function in openai_calls.py uses OpenAI's API to create summaries of the articles.

3. `Storing Content`: summaries along with article URLs are stored in a database using the BookmarkModel, to enable the application can keep track of user bookmarks.
   The BookmarkModel class in bookmark.py defines the structure for storing article URLs and summaries in the database, this feature allows users to save or bookmark content.

4. `Option to Bookmark for Later Reading`: API endpoints such as addBookmark and getBookmarks in summary_routes.py, provide functionality for users to bookmark articles they find interesting, to revisit them at a later time.

   API endpoints related to bookmarks, such as addBookmark and getBookmarks in summary_routes (1).py, provide functionality for users to bookmark articles they find interesting, to revisit them at a later time.

### **Mistakes, Challenges and how we overcame them:**

**Technical challenges**:

1. `Unfamiliarity with the RSS feeds ecosystem`: The RSS feeds ecosystem was a novel field for the team, as many members amongst the team had not worked with RSS feeds before. Initially, there was a lack of mutual understanding amongst the team on whether to fetch RSS feeds directly in Python using libraries, or ping a third-party API like <a href="rss.app">rss.app</a>. We overcame this challenge by conducting research on the RSS feeds ecosystem, understanding the pros and cons of each approach, and finally deciding to fetch RSS feeds directly using Python libraries.

2. `Handling large articles for summarization`: The OpenAI API has a token limit for summarization. To handle larger articles, we had to split the text into chunks and summarize each chunk separately. This required careful handling of the text chunks and combining the summaries to provide a coherent summary of the entire article.

**Non-technical challenges**:

1. `Efficient distribution of workload`: Upon deciding on the project idea, it was crucial to distribute the workload effectively among team members. We divided the tasks based on individual strengths and interests, ensuring that each member had a clear understanding of their responsibilities.

2. `Asynchronous collaboration`: Due to various conflicting schedules amongst the team members, it was challenging to find a common time for synchronous meetings. Hence, we had to rely on mostly asynchronous collaboration to settle our individual tasks, setting clear deadlines and expectations for each team member to ensure timely completion of tasks.

**Team member contributions**:

* Hui: `Wrote resources/rss_calls.py`, which takes in an rss feed URL from the query and returns the article URLs and texts from it. Prepared slide.

* Linda: `Wrote the summary API implementation`, which connects together the work we have done to make an API that takes in an RSS feed and returns summaries. Prepared slide.

* Rohit: `Wrote project skeleton`, coordinated work, and wrote bookmarks API/db implementation. Prepared slide and demo.

* Shubham: `Wrote openai_calls.py`, which takes in an article text and returns a summary string it using an external API call. Prepared slide.
