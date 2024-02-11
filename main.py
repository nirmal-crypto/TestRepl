from requests_html import HTMLSession, user_agent

s = HTMLSession()

query = 'srilanka'
url = f'https://www.google.com/search?q=weather+sri+lanka+{query}'

r = s.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'})

temp = r.html.find('span#wob_tm', first=True).text