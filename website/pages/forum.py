from flask import Blueprint, render_template
from flask_login import login_required, current_user

forum_page = Blueprint('forum_page', __name__, template_folder='/templates')


@forum_page.route('/forum', methods=['GET'])
@login_required
def forum():
    tiles_data = [
        {"title": "Scam Detectors", "members": "23,600", "image": "/images/forum_1.png", "url": "/forum_scam_detect"},
        {"title": "SpecFM", "members": "7,500", "image": "/images/forum_2.png"},
        {"title": "Zeit", "members": "15,500", "image": "/images/forum_3.png"},
        {"title": "Bank Impersonation", "members": "14,200", "image": "path/to/image4.png"},
        {"title": "Unicorn Scams", "members": "7,300", "image": "path/to/image5.png"},
        {"title": "Zeit", "members": "15,500", "image": "path/to/image3.png"},
        {"title": "Bank Impersonation", "members": "14,200", "image": "path/to/image4.png"},
        {"title": "Unicorn Scams", "members": "7,300", "image": "path/to/image5.png"},
        {"title": "Zeit", "members": "15,500", "image": "path/to/image3.png"},
        {"title": "Bank Impersonation", "members": "14,200", "image": "path/to/image4.png"},
        {"title": "Unicorn Scams", "members": "7,300", "image": "path/to/image5.png"},
        # Add more entries as needed
    ]
    return render_template("forum.html", user=current_user, tiles_data=tiles_data)


@forum_page.route('/forum/forum_topics')
@login_required
def forum_topics():
    tiles_data = [
        {"title": "Scam Detectors", "members": "23,600", "image": "/images/forum_1.png", "url": "/forum_scam_detect"},
        {"title": "SpecFM", "members": "7,500", "image": "/images/forum_2.png"},
        {"title": "Zeit", "members": "15,500", "image": "/images/forum_3.png"},
        {"title": "Bank Impersonation", "members": "14,200", "image": "path/to/image4.png"},
        {"title": "Unicorn Scams", "members": "7,300", "image": "path/to/image5.png"},
        {"title": "Zeit", "members": "15,500", "image": "path/to/image3.png"},
        {"title": "Bank Impersonation", "members": "14,200", "image": "path/to/image4.png"},
        {"title": "Unicorn Scams", "members": "7,300", "image": "path/to/image5.png"},
        {"title": "Zeit", "members": "15,500", "image": "path/to/image3.png"},
        {"title": "Bank Impersonation", "members": "14,200", "image": "path/to/image4.png"},
        {"title": "Unicorn Scams", "members": "7,300", "image": "path/to/image5.png"},
        # Add more entries as needed
    ]
    return render_template('forum_topics.html', user=current_user, tiles_data=tiles_data)


@forum_page.route('/forum/forum_topics/forum_scam_detect')
@login_required
def forum_topics_2():
    tiles_data = [
        {"title": "Scam Detectors", "members": "23,600", "image": "/images/forum_1.png", "url": "/forum_scam_detect"},
        {"title": "SpecFM", "members": "7,500", "image": "/images/forum_2.png"},
        {"title": "Zeit", "members": "15,500", "image": "/images/forum_3.png"},
        {"title": "Bank Impersonation", "members": "14,200", "image": "path/to/image4.png"},
        {"title": "Unicorn Scams", "members": "7,300", "image": "path/to/image5.png"},
        {"title": "Zeit", "members": "15,500", "image": "path/to/image3.png"},
        {"title": "Bank Impersonation", "members": "14,200", "image": "path/to/image4.png"},
        {"title": "Unicorn Scams", "members": "7,300", "image": "path/to/image5.png"},
        {"title": "Zeit", "members": "15,500", "image": "path/to/image3.png"},
        {"title": "Bank Impersonation", "members": "14,200", "image": "path/to/image4.png"},
        {"title": "Unicorn Scams", "members": "7,300", "image": "path/to/image5.png"},
        # Add more entries as needed
    ]
    return render_template('forum_scam_detect.html', user=current_user, tiles_data=tiles_data)


@forum_page.route('/forum/forum_topics/forum_scam_detect/forum_post')
@login_required
def forum_topics_3():
    return render_template('forum_post.html', user=current_user)
