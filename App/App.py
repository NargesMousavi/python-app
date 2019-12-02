from wsgiref.simple_server import make_server
import falcon


class TopicModelingResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('Hello World.')


app = falcon.API()
topicModelings = TopicModelingResource()
app.add_route('/topicmodeling', topicModelings)
# if __name__ == '__main__':
#     with make_server('', 8000, app) as httpd:

#         print('Serving on port 8000...')

#         httpd.serve_forever()