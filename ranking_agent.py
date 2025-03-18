import requests
from bs4 import BeautifulSoup

class RankingAgent:
    def process(self, hypothesis, memory):
        query = hypothesis.split()[-1]  # Extract keyword
        web_data = self.get_web_data(query)
        score = (len(web_data) % 10) + 1  # Generate a score
        return f"{hypothesis} (Score: {score}/10, Web: {web_data[:100]})"

    def get_web_data(self, query):
        search_url = f"https://en.wikipedia.org/wiki/{query.replace(' ', '_')}"
        response = requests.get(search_url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            return soup.get_text()[:500]  # Extract first 500 characters
        else:
            return "No data found"
