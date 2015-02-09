#coding:utf-8
import requests
import json

def SearchStock(stockid):
	if stockid:
		url="http://apistore.baidu.com/microservice/stock?stockid="+stockid
	else:
		url="http://apistore.baidu.com/microservice/stock?stockid="+""
	response=requests.get(url)
	jsontext=response.json()
	return jsontext

def HandleStockJson(jsontext):
	result={}
	infolist=['name','code','date','time','OpenningPrice','closingPrice','currentPrice','hPrice','lPrice']
	result['errNum']=jsontext['errNum']
	result['errMsg']=jsontext['errMsg']
	if result['errMsg']=='success':
		for item in jsontext['retData']['stockinfo']:
			if item in infolist:
				result[item]=jsontext['retData']['stockinfo'][item]
		for item in jsontext['retData']['klinegraph']:
			result[item]=jsontext['retData']['klinegraph'][item]
	return result

if __name__=="__main__":
	a= HandleStockJson(SearchStock('sh600000'))
	b=SearchStock('sh600000')
	print json.dumps(b,indent=4)
	for item in a:
		try:
			print item,a[item].encode('utf-8')
		except:
			print item,str(a[item])