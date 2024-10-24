import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd

# Initialize the vectorizer
vectorizer = CountVectorizer()

# Function to clean the 'LABEL' column
def label_category(value):
    # Convert to lowercase and strip leading/trailing whitespaces
    value = value.strip().lower()

    # Label anything with 'scam' or 'suspicious' as 'scam'
    if 'scam' in value or 'suspicious' in value:
        return 'scam'
    # Label legitimate variations as 'legitimate'
    elif 'legitimate' in value or 'neutral' in value:  # Treat 'neutral' as 'legitimate'
        return 'legitimate'
    # Keep as 'remove' for any cases that should not be included
    else:
        return 'remove'

# Function to train multiple models and select the best
def train_spam_model(df):
    # Clean the 'LABEL' column
    df['cleaned_category'] = df['LABEL'].apply(label_category)

    # Check for any rows that are still 'remove'
    invalid_rows = df[df['cleaned_category'] == 'remove']
    if not invalid_rows.empty:
        print("Invalid rows found that should be removed:")
        print(invalid_rows)

    # Remove rows labeled as 'remove'
    df = df[df['cleaned_category'] != 'remove']

    # Count the number of rows labeled as 'scam' and 'legitimate'
    scam_count = df[df['cleaned_category'] == 'scam'].shape[0]
    legitimate_count = df[df['cleaned_category'] == 'legitimate'].shape[0]

    print(f"Number of rows labeled as 'scam': {scam_count}")
    print(f"Number of rows labeled as 'legitimate': {legitimate_count}")

    # Prepare features (TEXT) and target (cleaned_category)
    X = df["TEXT"]
    y = df["cleaned_category"]

    # Vectorize the 'TEXT' data
    X = vectorizer.fit_transform(X)

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize models
    models = {
        'Logistic Regression': LogisticRegression(),
        'Random Forest': RandomForestClassifier(),
        'SVM': SVC()
    }

    best_model = None
    best_score = 0
    best_model_name = ""
    performance_metrics = {}

    # Train and evaluate models
    for model_name, model in models.items():
        # Train the model
        model.fit(X_train, y_train)

        # Predict on the test set
        y_pred = model.predict(X_test)

        # Calculate performance metrics
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted')
        recall = recall_score(y_test, y_pred, average='weighted')
        f1 = f1_score(y_test, y_pred, average='weighted')

        # Store the metrics
        performance_metrics[model_name] = {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1': f1
        }

        # Check if the model is the best one
        if accuracy > best_score:
            best_score = accuracy
            best_model = model
            best_model_name = model_name  # Store the best model's name

    # Print the best model
    print(f"The best model is: {best_model_name} with accuracy: {best_score}")

    # Save the best model
    with open('/Users/shanelim/Desktop/Sem 3.1/BC3409/Project/AISpam/website/pages/pretrained_model/saved_models/best_scam_detection_model.pkl', 'wb') as file:
        pickle.dump(best_model, file)

    # Save the vectorizer as well to use for predictions
    with open('/Users/shanelim/Desktop/Sem 3.1/BC3409/Project/AISpam/website/pages/pretrained_model/saved_models/best_vectorizer.pkl', 'wb') as file:
        pickle.dump(vectorizer, file)

    return best_model, performance_metrics

# Load your dataset and call the function
if __name__ == "__main__":
    # Load the CSV file
    df = pd.read_csv("/Users/shanelim/Desktop/Sem 3.1/BC3409/Project/AISpam/raw_data_for_training/scam_call_transcript.csv")

    # Call the function with the dataset
    best_model, performance_metrics = train_spam_model(df)

    # Print the performance metrics for each model
    print("Performance Metrics:")
    for model_name, metrics in performance_metrics.items():
        print(f"{model_name}: {metrics}")




# import pickle
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.svm import SVC
# from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
# import pandas as pd

# # Initialize the vectorizer
# vectorizer = CountVectorizer()

# # Function to clean the 'LABEL' column
# def label_category(value):
#     # Convert to lowercase and strip leading/trailing whitespaces
#     value = value.strip().lower()

#     # Label anything with 'scam' or 'suspicious' as 'scam'
#     if 'scam' in value or 'suspicious' in value:
#         return 'scam'
#     # Label legitimate variations as 'legitimate'
#     elif 'legitimate' in value:
#         return 'legitimate'
#     # Otherwise, label as 'neutral'
#     elif 'neutral' in value:
#         return 'neutral'
#     else:
#         return 'neutral'  # Assign to 'neutral' if it doesn't fall into other categories

# # Function to train multiple models and select the best
# def train_spam_model(df):
#     # Clean the 'LABEL' column
#     df['cleaned_category'] = df['LABEL'].apply(label_category)

#     # Prepare features (TEXT) and target (cleaned_category)
#     X = df["TEXT"]
#     y = df["cleaned_category"]

#     # Vectorize the 'TEXT' data
#     X = vectorizer.fit_transform(X)

#     # Split data into training and test sets
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#     # Initialize models
#     models = {
#         'Logistic Regression': LogisticRegression(),
#         'Random Forest': RandomForestClassifier(),
#         'SVM': SVC()
#     }

#     best_model = None
#     best_score = 0
#     best_model_name = ""
#     performance_metrics = {}

#     # Train and evaluate models
#     for model_name, model in models.items():
#         # Train the model
#         model.fit(X_train, y_train)

#         # Predict on the test set
#         y_pred = model.predict(X_test)

#         # Calculate performance metrics
#         accuracy = accuracy_score(y_test, y_pred)
#         precision = precision_score(y_test, y_pred, average='weighted')
#         recall = recall_score(y_test, y_pred, average='weighted')
#         f1 = f1_score(y_test, y_pred, average='weighted')

#         # Store the metrics
#         performance_metrics[model_name] = {
#             'accuracy': accuracy,
#             'precision': precision,
#             'recall': recall,
#             'f1': f1
#         }

#         # Check if the model is the best one
#         if accuracy > best_score:
#             best_score = accuracy
#             best_model = model
#             best_model_name = model_name  # Store the best model's name

#     # Print the best model
#     print(f"The best model is: {best_model_name} with accuracy: {best_score}")

#     # Save the best model
#     with open('/Users/shanelim/Desktop/Sem 3.1/BC3409/Project/AISpam/website/pages/pretrained_model/saved_models/best_scam_detection_model.pkl', 'wb') as file:
#         pickle.dump(best_model, file)

#     # Save the vectorizer as well to use for predictions
#     with open('/Users/shanelim/Desktop/Sem 3.1/BC3409/Project/AISpam/website/pages/pretrained_model/saved_models/best_vectorizer.pkl', 'wb') as file:
#         pickle.dump(vectorizer, file)

#     return best_model, performance_metrics

# # Load your dataset and call the function
# if __name__ == "__main__":
#     # Load the CSV file
#     df = pd.read_csv("/Users/shanelim/Desktop/Sem 3.1/BC3409/Project/AISpam/raw_data_for_training/scam_call_transcript.csv")

#     # Call the function with the dataset
#     best_model, performance_metrics = train_spam_model(df)

#     # Print the performance metrics for each model
#     print("Performance Metrics:")
#     for model_name, metrics in performance_metrics.items():
#         print(f"{model_name}: {metrics}")
