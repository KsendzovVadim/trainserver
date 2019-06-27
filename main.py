from app import app
import view
from app import db
from posts.blueprint import posts
from markup.blueprint import hands_markup


app.register_blueprint(posts, url_prefix='/blog')
app.register_blueprint(hands_markup, url_prefix='/hands_markup')



if __name__ == '__main__':
    app.run()

