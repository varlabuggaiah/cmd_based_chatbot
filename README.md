Python Gemini AI Chatbot 🤖
A simple, terminal-based chatbot powered by Google's Gemini Pro API. This project demonstrates how to build an interactive chat application in Python while securely managing API keys using environment variables and a virtual environment.
![alt text](https://user-images.githubusercontent.com/10121338/200874316-2fd1a216-9c60-4861-a1e6-d7ab09c62cd5.gif)

(Suggestion: You can create a GIF of your chatbot in action using a tool like LICEcap or ScreenToGif and replace the placeholder image link.)
Features
Interactive Chat: Have a continuous, stateful conversation with the Gemini AI directly in your terminal.
Conversation History: The chatbot remembers the context of the current conversation session.
Secure API Key Management: Follows best practices by loading your secret API key from a .env file, which is kept out of version control.
Isolated Environment: Uses a Python virtual environment (venv) to manage dependencies, ensuring the project doesn't interfere with other Python projects on your system.
Easy to Set Up: Get up and running with just a few simple commands.
Prerequisites
Before you begin, ensure you have the following installed and configured:
Python 3.8 or higher
Git
A Google Gemini API Key: You can obtain a free API key from Google AI Studio.
🛠️ Installation & Setup
Follow these steps to get your local environment set up and ready to run.
1. Clone the Repository
First, clone this repository to your local machine using Git:
code
Bash
git clone https://github.com/varlabuggaiah/cmd_based_chatbot.git
cd cmd_based_chatbot
2. Create and Activate a Virtual Environment
It is highly recommended to use a virtual environment to keep project dependencies isolated.
On Windows:
code
Bash
# Create the virtual environment
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\activate
(Your terminal prompt should now be prefixed with (venv))
On macOS/Linux:
code
Bash
# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
(Your terminal prompt should now be prefixed with (venv))
3. Install Dependencies
With your virtual environment active, install the required Python packages from the requirements.txt file.
code
Bash
pip install -r requirements.txt
4. Configure Your API Key
This project uses a .env file to securely store your API key. This file is intentionally not tracked by Git.
i. Create a .env file by making a copy of the example file provided.
On Windows:
code
Bash
copy .env.example .env
On macOS/Linux:
code
Bash
cp .env.example .env
ii. Add your API Key to the .env file:
Open the newly created .env file with a text editor. It will contain the following:
code
Code
# Replace YOUR_API_KEY_GOES_HERE with your actual Google Gemini API Key
GEMINI_API_KEY="YOUR_API_KEY_GOES_HERE"
Replace the placeholder text YOUR_API_KEY_GOES_HERE with your actual Gemini API key. Save and close the file.
🔒 Security Note: The .gitignore file is already configured to ignore the .env file. This is a critical security measure to ensure your secret API key is never uploaded to GitHub.
▶️ How to Run the Chatbot
Once the setup is complete and your virtual environment is active, you can start the chatbot by running the main Python script:
code
Bash
python cmd_based_chatbot.py
You can now start chatting with the AI! To end the session, simply type exit and press Enter.
Example Session
code
Code
Welcome to the AI Chatbot! Type 'exit' to quit.
You: Hello, what are you?
AI: I am a large language model, trained by Google.
You: Can you write a haiku about a cat?
AI: Golden eyes look out,
Silent paws on sunlit floor,
Napping is my job.
You: exit
📁 Project Structure
A brief overview of the key files in this project:
code
Code
.
├── .env              # (Ignored by Git) Holds your secret API key. You create this.
├── .env.example      # An example template for the .env file.
├── .gitignore        # Specifies which files Git should ignore (like venv and .env).
├── cmd_based_chatbot.py # The main Python script containing the chatbot logic.
├── README.md         # This file, providing project documentation.
└── requirements.txt  # A list of Python packages required for this project.
🤝 Contributing
Contributions, issues, and feature requests are welcome! If you have suggestions for improvements, please feel free to fork the repo and create a pull request, or open an issue with the tag "enhancement".
Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request.