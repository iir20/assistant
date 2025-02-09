import requests
from bs4 import BeautifulSoup

class Internet:
    def learn(self, topic):
        try:
            url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            content = soup.find("div", {"class": "mw-parser-output"}).text[:500] + "..."
            return f"Here's what I learned about {topic}:\n{content}"
        except Exception as e:
            return f"Failed to learn about {topic}: {str(e)}"