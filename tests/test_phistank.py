from src.tools.phishtank import check_phishtank

def test_known_phishing_url():
    url = "https://sodlmac.vercel.app/"
    assert check_phishtank(url) is True


def test_unknown_url():
    url = "https://example.com/"
    assert check_phishtank(url) is True
