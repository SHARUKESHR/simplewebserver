from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    	<title> Image Map </title>
	<body>
		<table border="1">
	<caption> Top five Revenue Generating Software Companies </caption>
	<tr>
		<th>S.No</th>
		<th>Company</th>
		<th>Revenue</th>
	</tr>
	<tr>
		<th>1</th>
		<td>Microsoft</td>
		<td>65 Billion</td>
	</tr>
	<tr>
		<th>2</th>
		<td>Oracle</td>
		<td>29.6 Billion</td>
	</tr>
	<tr>
		<th>3</th>
		<td>IBM</td>
		<td>29.1 Billion</td>
	</tr>
	<tr>
		<th>4</th>
		<td>SAP</td>
		<td>6.4 Billion</td>
	</tr>
	<tr>
		<th>5</th>
		<td>Symantec</td>
		<td>5.6 Bilion</td>
	</tr>
	</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()