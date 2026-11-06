from src.tools.phishtank import local_phishtank_search

def test_local_known_phishing_url():
    url = "https://sodlmac.vercel.app/"
    print(local_phishtank_search(url))


def test_local_unknown_url():
    url = "https://example.com/"
    print(local_phishtank_search(url))
