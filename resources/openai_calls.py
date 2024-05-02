# Remember to add libraries to requirements.txt if you add any!
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("API_KEY")

# Function to query OpenAI API
def get_completion(prompt, model="gpt-3.5-turbo"):
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0.7, # this is the degree of randomness of the model's output
        )
        return response.choices[0].message["content"]

# Function to chunk text into smaller segments
def chunk_text(text, chunk_size=20000):
    chunks = []
    words = text.split()
    current_chunk = ''
    for word in words:
        if len(current_chunk) + len(word) < chunk_size:
            current_chunk += word + ' '
        else:
            chunks.append(current_chunk.strip())
            current_chunk = word + ' '
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

def getSummary(articleText):
    """Takes in the text of an individual article and passes it to OpenAI or a similar
    summarizer API. Receives the output and returns it

    Keyword arguments:
    articleText -- The text of an article (getting this text is handled in rss_calls.py)

    Returns:
    summary -- A summary of 100? characters or less of the article text
    """
    text_chunks = chunk_text(articleText)
    summary = ''
    for chunk in text_chunks:
        initial_prompt = f"please summarize the salient points from the following text in 25 words in a properly formatted language: {chunk}"
        summary += get_completion(initial_prompt) + ' '
    return summary

if __name__ == "__main__":
    # print(getSummary("The United States is a country primarily located in North America. It consists of 50 states, a federal district, five major unincorporated territories, 326 Indian reservations, and some minor possessions. At 3.8 million square miles (9.8 million square kilometers), it is the world's third- or fourth-largest country by total area. The United States shares significant land borders with Canada to the north and Mexico to the south as well as limited maritime borders with the Bahamas, Cuba, and Russia. With a population of more than 331 million people, it is the third most populous country in the world. The national capital is Washington, D.C., and the most populous city is New York City."))
    pass
