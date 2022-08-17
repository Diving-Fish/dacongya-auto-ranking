# majsoul-auto-ranking

用 Selenium（已过时）做的一个自动抓雀魂后台分的东西

./cr.sh 是自动重启的脚本，爬虫主程序在 crawler_main.py。因为selenium有内存泄漏问题，还是建议用基于 node 的 puppeteer

因为项目非常小，所以只爬第一页 50 个数据，然后用 txt 存，正常来说存数据库或者redis这种都是可以的。如果比较大的数据量或者首次爬可能需要翻页到上次爬完的地方为止

然后 server.py 读 txt 之后 parse，返回数据
