#! python3
# get_title.py - コピーしたurlとtitelの文字列を返す
# たまに文字化けする。許して。 TODO

import bs4, requests, pyperclip

# urlは後で使うので変数に保存
url = pyperclip.paste()

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")
title = soup.find("title").get_text()

# これでscrapboxへの貼り付けばっちりよ
pyperclip.copy(f"{url} {title}")
