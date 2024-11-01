import os
import requests
from flask import Blueprint, render_template, request, jsonify, url_for
from flask_login import login_required, current_user

profile_page = Blueprint('profile_page', __name__, template_folder='templates')

@profile_page.route('/profile', methods=['GET'])
@login_required
def profile():
    return render_template("profile.html", user=current_user)

@profile_page.route('/save-avatar', methods=['POST'])
@login_required
def save_avatar():
    data = request.get_json()
    avatar_url = data.get('avatarUrl')

    if not avatar_url:
        return jsonify({"success": False, "message": "Avatar URL is missing"}), 400

    # Download the avatar image
    response = requests.get(avatar_url)
    if response.status_code != 200:
        return jsonify({"success": False, "message": "Failed to fetch avatar"}), 500

    # Save the image with a predictable filename
    avatar_folder = 'static/avatars'
    os.makedirs(avatar_folder, exist_ok=True)
    avatar_filename = f"user_{current_user.id}_avatar.svg"  # Filename based on user ID
    avatar_path = os.path.join(avatar_folder, avatar_filename)
    
    with open(avatar_path, "wb") as avatar_file:
        avatar_file.write(response.content)

    return jsonify({"success": True, "message": "Avatar saved successfully!"})



# from flask import Blueprint, render_template
# from flask_login import login_required, current_user

# profile_page = Blueprint ('profile_page', __name__, template_folder='/templates')

# @profile_page.route ('/profile', methods = ['GET'])
# @login_required
# def profile ():
#     return render_template ("profile.html", user=current_user)

# @profile_page.route ('/process', methods = ['POST'])
# @login_required
# def process ():
#     return render_template ("profile.html", user=current_user)


# @profile_page.route('/process', methods=['POST'])
# @login_required
# def process_avatar():  # Renamed to process_avatar to avoid conflict
#     return render_template("profile.html", user=current_user)
