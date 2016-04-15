# NLP

Data set : http://times.cs.uiuc.edu/~wang296/Data/
Data set size: 600 tuples
product name : RIO PMP 300 mp3 player
Data set modification:
	sed -i "/\b\(author\|id\|productId\|standardName\|productName\|createDate\|summary\|recommend\|paid\|helpfulNum\|totalNum\|webHome\|webUrl\|htmlPath\|textPath\|commentNum\)\b/d" amazon_mp3
	Set rating above 3 as positive, below 3 as negative

ACCURACY

BIGRAM_RESULTS

77.966
81.67
81.67
80
88.3
88.33
81.67
81.67
86.67
73.33

average = 82.1
UNIGRAM_RESULTS

74.57
80
83.3
78.33
86.67
88.33
88.33
85
86.67
80

average = 83.1
