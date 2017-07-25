#! python3
# news.py

import webbrowser

news_list = [
                # news
                'http://www.itmedia.co.jp/',
                'http://jp.techcrunch.com/',
                'http://itpro.nikkeibp.co.jp/?rt=nocnt/',
                'http://japan.cnet.com/',
                'http://techable.jp/',
                'http://diamond.jp/list/sp-itbiz/',
                'http://weekly.ascii.jp/',
                'http://biz.bcnranking.jp/',
                'http://www.gizmodo.jp/',
                'http://gigazine.net/',
                'http://www.lifehacker.jp/',
                'http://gori.me/',
                'http://blogos.com/genre/web/',
                'http://markezine.jp/',
                'http://www.danshihack.com/',
                'http://bazubu.com/',
                'http://omocoro.jp/',
                'http://rocketnews24.com/',
                'http://www.roomie.jp/',
                'http://japanese.engadget.com/',
                'http://www.watch.impress.co.jp/',
                'http://nlab.itmedia.co.jp/',
                'http://tabi-labo.com/',
                'http://www.hatena.ne.jp/',
                'https://www.rbbtoday.com/category/digital/',
                'https://withnews.jp/',
                'https://japan.zdnet.com/',
                'https://retrip.jp/',
                'https://techable.jp/',
                'http://www.atmarkit.co.jp/',
                'http://postd.cc/',
                'https://codeiq.jp/magazine/',
                'https://codezine.jp/',
                'https://geechs-magazine.com/',
                'https://seleck.cc/',
                'http://uxmilk.jp/',
                'https://thinkit.co.jp/'
            ]

for i in range(len(news_list)):
    webbrowser.open(news_list[i])
