# from website.pages.learning import learning

# if __name__ == "__main__":
#     learning()  # Call the function directly

# import os

# file_path = '/Users/shanelim/Desktop/Sem 3.1/BC3409/Project/AISpam/website/__init__.py'
# if os.path.exists(file_path):
#     print("__init__.py exists")
# else:
#     print("__init__.py does not exist")

import sys
import os

# Add the root project directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

# Now import the learning function from website/pages/learning.py
from website.pages.learning import learning

if __name__ == "__main__":
    print("Testing if the learning function is called.")
    learning()  # This will call the learning function directly
