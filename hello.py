from mod_python import apache
def handler(req):
	req.log_error('handler')
	req.content_type='text/html'
	req.send_http_header()
	return apache.OK

