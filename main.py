from app import app
import app.view
from app.app import db
from app.posts.blueprint import posts


app.register_blueprint(posts, url_prefix='/blog')



if __name__ == '__main__':
    app.run()

