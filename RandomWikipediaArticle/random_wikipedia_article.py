import requests
import webbrowser

WikiURL = "https://cs.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json"
ListOfYes = ["Y", "YES", "A", "ANO", ""]

WikiRandomArticlesResp = requests.get(WikiURL)
if WikiRandomArticlesResp.status_code != 200:
    # This means something went wrong.
    raise requests.ConnectionError('GET '+WikiURL+' {}'.format(WikiRandomArticlesResp.status_code))

for Article in WikiRandomArticlesResp.json()["query"]["random"]:
    Response = input('Chcete otevřít článek {} {} [Yes/no]?'.format(Article['id'],
                                                                    Article['title'])) or "Yes"
    if Response.upper() in ListOfYes:
        ArticleURL = "https://cs.wikipedia.org/wiki?curid="+str(Article["id"])
        webbrowser.open(ArticleURL)
