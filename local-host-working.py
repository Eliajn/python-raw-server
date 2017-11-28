from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

import check_login
# def redirect(location):
#         self.send_response(302)  # 302 Found is a common way of performing URL redirection
#         self.send_header('Location', url)
#         self.end_headers()


class S(BaseHTTPRequestHandler):

    def write_html(self):
        if(self.path == "/"):
            with open("./home.html", mode="rb") as fd:
                read_file = fd.read()
                return self.wfile.write(read_file)
        else:
            with open("." + self.path + ".html", mode="rb") as fd:
                read_file = fd.read()
                return self.wfile.write(read_file)

    def write_header(self):
        with open("./header.html", mode='rb') as fd:
            read_file = fd.read()
            return self.wfile.write(read_file)

    def write_footer(self):
        with open("./footer.html", mode='rb') as fd:
            read_file = fd.read()
            return self.wfile.write(read_file)

    def _set_text_headers(self):  # 'text/html' or "image/png"
        self.send_response(200)
        # self.send_header('Content-type', 'application/json')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _set_img_headers(self):  # 'text/html' or "image/png"
        self.send_response(200)
        # self.send_header('Content-type', 'application/json')
        self.send_header('Content-type', 'image/png')
        self.end_headers()

    def _set_css_header(self):
        self.send_response(200)
        self.send_header('content-type', 'text/css')
        self.end_headers()

    def redirect_to(self, location):
        print("redirecting to" + location)
        self.send_response(302)  # 302 is a common way of performing redirection
        self.send_header('Location', location)
        self.end_headers()

    def do_GET(self):

        def get_extension(self):
            path = self.path
            ar = path.split(".")
            return ar[len(ar) - 1]

        if(self.path == "/home" or self.path == "/"):
            self._set_text_headers()
            self.write_header()
            self.write_html()
            self.write_footer()
        elif(self.path == "/register"):
            self._set_text_headers()
            self.write_header()
            self.write_html()
            self.write_footer()
        elif(self.path == "/log_in_page"):
            self._set_text_headers()
            self.write_header()
            self.write_html()
            self.write_footer()
        elif(self.path == "/logged_in"):
            self._set_text_headers()
            self.write_header()
            self.write_html()
            self.write_footer()
        elif(self.path == "/about"):
            self._set_text_headers()
            self.write_header()
            self.write_html()
            self.write_footer()
        # serve a static file with the given path
        elif(get_extension(self) == "css"):
            self._set_css_header()
            with open("." + self.path, mode='rb') as fd:
                read_file = fd.read()
                self.wfile.write(read_file)
        elif(get_extension(self) == "jpg"):
            self._set_img_headers()
            with open("." + self.path, mode='rb') as fd:
                read_file = fd.read()
                self.wfile.write(read_file)

    def do_POST(self):
        print("HEADERS: ", self.headers)
        if(self.path == "/action_page.php"):
            length = self.headers['content-length']  # check the length of the content from/action_page.php.
            data = self.rfile.read(int(length))  # will read the length posted.
            datas = data.decode('ascii')  # decode to'ascii' to convert the binary to string.
            dict_string = (parse_qs(datas))
            _username = dict_string['Username'][0]  # after having a string, we then parse the data to a dictionary.
            _password = dict_string['Password'][0]
            # print(_username)
            # print(_password)
            if (check_login.check_username_if_exist(_username) == False and check_login.verify_password(_password) == True and check_login.verify_username(_username) == True):
                hashedpass = check_login.hash_password(_password)
                check_login.storing_in_database(_username, hashedpass)
                self.redirect_to('/logged_in')
            elif (check_login.check_username_if_exist(_username) == True and check_login.check_longin(_username, _password) == True):
                self.redirect_to('/logged_in')
            elif(check_login.verify_username(_username) == False | check_login.verify_password(_password)):
                self.redirect_to('/')

            self.wfile.write(b'<a href =  " / " > Home </a>')

        self.wfile.write(b"<html><body><h1>POST!</h1></body></html>")


def run(server_class=HTTPServer, handler_class=S, port=8001):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)  # configuration
    print('Starting httpd...')
    httpd.serve_forever()


run()


#   if(self.path == "/action_page.php"):
#   length = self.headers['content-length']  # check the length of the content from/action_page.php.
#   data = self.rfile.read(int(length))  # will read the length posted.
#   datas = data.decode('ascii')  # decode to'ascii' to convert the binary to string.
#   dict_string = parse_qs(datas)  # after having a string, we then parse the data to a dictionary.
#   print(dict_string)
#   _username=dict_string['Username']
#   _password=dic_string['Password']
#   if (check_username_if_exist(dict_string['Username'])==None):
#       if(verify_password(_password)==True):
#           storing_in_database(_username,_password)
#   else:
#       return True
