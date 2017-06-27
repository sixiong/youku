import bottle
from bottle import request,response,get
from youku import Youku

youku = Youku()


@get('/')
def getRealUrl():
	url = dict(request.query).get('addr')
	real_urls = youku.get_video_info(url)
	return real_urls

if __name__ == '__main__':
	bottle.run(host='0.0.0.0',port=8080)