from flask_blog.models import Post
from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.date_posted.desc()).paginate(per_page=10, page=page)

    return render_template('home.html', posts=posts)  # argument in template


@main.route('/about')
def about():
    return render_template('about.html', title='About')
