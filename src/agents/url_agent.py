from dotenv import load_dotenv
from src.tools.url_analyzer import analyze_url
from src.tools.phishtank import local_phishtank_search
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()

class AIPhishTankResponse(BaseModel):
    verdict: str
    confidence: float
    reasons: list[str]

class URLAgent:
    def __init__(self):
        self.llm = ChatGroq(
            model="qwen/qwen3.8-27b",
            temperature=0.1
        )
        self.structured_llm = self.llm.with_structured_output(AIPhishTankResponse)
        self.prompt_template = ChatPromptTemplate.from_messages([("system", """
        Analyze the following URL for phishing risk.

        - URL:
        {url}

        - URL analysis:
        {url_info}

        - PhishTank result:
        {phishtank_result}
        
        Based only on the provided evidence, determine whether the URL
        appears benign, suspicious, or unknown.

        Explain the main reasons for your verdict.
        """)])

    def run(self, url: str):
        url_info = url_analyzer(url)
        chain = self.prompt_template | self.structured_llm
        return chain.invoke({
            "url": url,
            "url_info": url_info["url_info"],
            "phishtank_result": url_info["phishtank"]
        })

def url_analyzer(url: str):
    url_info = analyze_url(url)
    phishtank_info = local_phishtank_search(url)
    return {
        "url_info": url_info,
        "phishtank": phishtank_info
    }

