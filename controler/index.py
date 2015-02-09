from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from models.search import SearchStock,HandleStockJson

def index(request,name):
	info={'username':name,'pagename':'STOCK DATA'}
	c=Context(info)
	t=get_template('index.html')
	html=t.render(c)
	return HttpResponse(html)

def search(request,name):
	query=request.GET.get('search_word','')
	stockinfo=HandleStockJson(SearchStock(query))

	info={'username':name,'pagename':'STOCK DATA','stockinfo':stockinfo,'query':query}
	c=Context(info)
	t=get_template('index.html')
	html=t.render(c)
	return HttpResponse(html)
