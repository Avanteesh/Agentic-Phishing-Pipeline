from src.agents.url_agent import url_analyzer, URLAgent

def test_url_agent():
    agent = URLAgent()
    print(agent.run("https://sodlmac.vercep.app/"))

def test_url_analyzer_method():
    url = "https://sodlmac.vercel.app/"
    print(url_analyzer(url))
