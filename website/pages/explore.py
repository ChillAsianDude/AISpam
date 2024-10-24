from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
import speech_recognition as sr
import textblob
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from website.pages.scam_detection import predict_scam  # Ensure this works correctly

explore_page = Blueprint('explore_page', __name__, template_folder='/templates')

@explore_page.route('/explore', methods=['GET'])
@login_required
def explore():
    # Render the explore page, ensuring templates are in the correct directory
    return render_template("explore.html", user=current_user)

@explore_page.route('/explore/result', methods=['GET', 'POST'])
@login_required
def explore_result():
    data_received = {}  # Dictionary to store the received data
    
    if request.method == 'POST':
        try:
            # Receiving text data, speech data, and audio file
            text_data = request.form.get('text_data')  # Text input
            speech_data = request.form.get('speech_data')  # Speech text input
            audio_data = request.files.get('audio_data')  # Audio file input
            
            if audio_data:
                # Convert audio data to text using speech_recognition
                recognizer = sr.Recognizer()
                audio_file = sr.AudioFile(audio_data)  # Ensure the file is in a readable format
                
                # Read and process the audio file
                with audio_file as source:
                    audio_data = recognizer.record(source)  # Record the audio data
                audio_text = recognizer.recognize_google(audio_data)  # Convert speech to text using Google API
                
                # Add the converted audio text to data_received
                data_received["audio"] = audio_text
            
            # Add the received text and speech data to the data_received dictionary
            if text_data:
                data_received["text"] = text_data
            if speech_data:
                data_received["speech"] = speech_data

        except Exception as e:
            # Handle errors in file processing or speech recognition
            print(f"Error during file processing: {str(e)}")
    
    # Analyze the data (using TextBlob for sentiment analysis)
    analysis_data = {}
    for data_type, content in data_received.items():
        if content and content.strip():  # Ensure content is not empty
            analysis = textblob.TextBlob(content).sentiment
            analysis_data[data_type] = {
                "polarity": analysis.polarity,
                "subjectivity": analysis.subjectivity
            }

    # Spam Detection (using the trained model)
    spam_results = {}
    for data_type, content in data_received.items():
        if content:
            try:
                # Predict whether the content is spam or not
                result = predict_scam(content)
                spam_results[data_type] = result
            except Exception as e:
                # Handle any errors in spam prediction
                spam_results[data_type] = f"Error: {str(e)}"
    
    # Render the results in explore_result.html
    return render_template("explore_result.html", user=current_user,
                           data_received=data_received,
                           analysis_data=analysis_data,
                           spam_results=spam_results)


# from flask import Blueprint, render_template, request
# from flask_login import login_required, current_user
# import speech_recognition as sr
# import textblob
# #from train_model import train_spam_model
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
# from website.pages.scam_detection import predict_scam


# explore_page = Blueprint('explore_page', __name__, template_folder='/templates')

# @explore_page.route('/explore', methods=['GET'])
# @login_required
# def explore():
#     return render_template("explore.html", user=current_user)

# @explore_page.route('/explore/result', methods=['GET', 'POST'])
# @login_required
# def explore_result():
#     data_received = {}
#     if request.method == 'POST':
#         # Receiving text data, speech data, and audio file
#         text_data = request.form.get('text_data')
#         speech_data = request.form.get('speech_data')
#         audio_data = request.files['audio_data']

#         # Convert audio data to text
#         recognizer = sr.Recognizer()
#         audioFile = sr.AudioFile(audio_data)
#         with audioFile as source:
#             data = recognizer.record(source)
#         audio_text = recognizer.recognize_google(data, key=None)

#         # Append data to dictionary
#         data_received["text"] = text_data
#         data_received["speech"] = speech_data
#         data_received["audio"] = audio_text

#     # Analyze the data (using TextBlob for sentiment analysis)
#     analysis_data = {}
#     for data, content in data_received.items():
#         if content and content != "":
#             analysis = textblob.TextBlob(content).sentiment
#             analysis_data[data] = {"polarity": analysis.polarity, "subjectivity": analysis.subjectivity}

#     # Spam Detection (using the trained model)
#     spam_results = {}
#     for data, content in data_received.items():
#         if content:
#             result = predict_scam(content)
#             spam_results[data] = result

#     return render_template("explore_result.html", user=current_user,
#                            data_received=data_received,
#                            analysis_data=analysis_data,
#                            spam_results=spam_results)

