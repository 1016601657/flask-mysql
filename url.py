import urllib
import json

params = urllib.urlencode({'industryID': 11})
result = urllib.urlopen("http://local.zhaosha.com/tmpws/fetchGoods.php?%s" % params)
# print res[0]
hjson = json.loads(result.read())
# print hjson['data'][0]['industry_id']
for x in hjson['data']:
	print x['industry_id']
