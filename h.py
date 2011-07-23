from mod_python import apache
def handler(req):
	req.content_type='text/html'
	req.send_http_header()
	req.write("hello world")

	return apache.OK


