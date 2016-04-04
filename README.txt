# NLP

Data set : http://times.cs.uiuc.edu/~wang296/Data/
Data set size: 600 tuples
product name : RIO PMP 300 mp3 player
Data set modification:
	sed -i "/\b\(author\|id\|productId\|standardName\|productName\|createDate\|summary\|recommend\|paid\|helpfulNum\|totalNum\|webHome\|webUrl\|htmlPath\|textPath\|commentNum\)\b/d" amazon_mp3
	Set rating above 3 as positive, below 3 as negative

ACCURACY

CASE1: 78.33%
CASE2: 75.00%
CASE3: 83.33%
CASE4: 78.33%
CASE5: 90.00%
CASE6: 86.67%
CASE7: 86.67%
CASE8: 81.67%
CASE9: 86.67%
CASE10: 81.67%

AVERAGE ACCYRACY: 82.8%
