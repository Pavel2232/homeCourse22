from flask import Blueprint, render_template,request
from app.comment.dao.comment_dao import CommentDAO, COMMENT_PATH
from app.post.dao.post_dao import PostDAO,DATA_PATH


post_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')


@post_blueprint.route("/posts/<postid>")
def post_page(postid):
    posts = PostDAO(DATA_PATH)
    post = posts.get_post_by_pk(postid)
    comment = CommentDAO(COMMENT_PATH)
    result_comment = comment.get_comments_by_post_id(postid)
    return render_template('post.html', result_comment= result_comment, post = post)

@post_blueprint.route("/search")
def post_search():
    s = request.args.get('s')
    posts_data = PostDAO(DATA_PATH)
    posts = posts_data.search_for_posts(s)
    return render_template('search.html', posts = posts)