# import sys
import os
# from tracker.wsgi import application
# from whitenoise import WhiteNoise


bind = "0.0.0.0:" + os.environ.get("PORT", "8000")
workers = 3
# reload = True


# application = WhiteNoise(application)
# application.add_files('static/', prefix='static/')
# application.add_files('staticfiles/', prefix='staticfiles/')



# class FaviconMiddleware:
#     def __init__(self, app, default_favicon_path='favicon.ico'):
#         self.app = app
#         self.default_favicon_path = default_favicon_path

#     def __call__(self, environ, start_response):
#         if environ['PATH_INFO'] == '/favicon.ico':
#             try:
#                 current_dir = os.path.dirname(__file__)
#                 favicon_path = os.path.join(current_dir, self.default_favicon_path)

#                 print(f"Attempting to read favicon from: {favicon_path}")

#                 with open(favicon_path, 'rb') as f:
#                     favicon_data = f.read()

#                 start_response('200 OK', [('Content-Type', 'image/x-icon')])
#                 return [favicon_data]
#             except FileNotFoundError:
#                 print("Favicon file not found.")
#                 start_response('404 Not Found', [('Content-Type', 'text/plain')])
#                 return [b'Not Found']

#         return self.app(environ, start_response)

# # Wrap the main application with FaviconMiddleware
# application = FaviconMiddleware(application)

