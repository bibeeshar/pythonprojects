from mod_python import apache
def index(req):
	req.write("test")
	return "test successful"
