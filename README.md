# NLP

Data set : http://times.cs.uiuc.edu/~wang296/Data/
Data set size: 1000 tuples
product name : RIO PMP 300 mp3 player
Data set modification:
	sed -i "/\b\(author\|id\|productId\|standardName\|productName\|createDate\|summary\|recommend\|paid\|helpfulNum\|totalNum\|webHome\|webUrl\|htmlPath\|textPath\|commentNum\)\b/d" amazon_mp3
	Set rating above 3 as positive, below 3 as negative and 3 as neutral
