from flask import Blueprint, render_template,request
from app.comment.dao.comment_dao import CommentDAO, COMMENT_PATH
from app.post.dao.post_dao import PostDAO,DATA_PATH

def post_page(postid):
    posts = PostDAO(DATA_PATH)
    post = posts.get_post_by_pk(postid)
    comment = CommentDAO(COMMENT_PATH)
    result_comment = comment.get_comments_by_post_id(postid)
    return f"{post},{result_comment}"


print(post_page(1))