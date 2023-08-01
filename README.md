## Voice Assistant

This is a Python-based Voice Assistant that interacts with the user through voice commands. The assistant can perform various tasks, including playing music from YouTube, providing current time and date, retrieving information from Wikipedia, telling jokes, opening applications, and performing basic arithmetic calculations.


## How to Play
1. Greet the user based on the time of day (Good Morning/Good Afternoon/Good Evening).
2. Play music from YouTube using voice commands.
3. Provide the current time and date when asked.
4. Retrieve information about a topic from Wikipedia.
5. Tell random jokes for entertainment.
6. Open specific applications on the computer based on voice commands.
7. Act as a basic calculator, performing arithmetic calculations.
## Requirements
1. Python 3.x
2. Libraries: pyttsx3, pyjokes, datetime, pywhatkit, wikipedia, speech_recognition
## Setup

1. Install Python 3.x on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory.
4. Install the required Python libraries.
5. Run the Voice Assistant.

## Usage
1. Run the VoiceAssistant.py script to start the Voice Assistant.
2. When prompted with "How may I help you?", speak your desired command.
3. The assistant will recognize your speech, process the command, and respond accordingly.
## Supported Commands
1. "Play [song name]" - Plays the requested song on YouTube.
2. "What time is it?" - Provides the current time.
3. "What is today's date?" - Provides today's date.
4. "Tell me about [topic]" - Retrieves information about the specified topic from Wikipedia.
5. "Tell me a joke" - Tells a random joke.
6. "Open [application name]" - Opens specific applications like Google Chrome or Visual Studio Code.
7. "Calculate [expression]" - Performs basic arithmetic calculations.
## Customization
You can customize the voice used by the assistant by changing the voice property in the "engine.setProperty('voice', voices[1].id)"  
line of the jarvis.py script.  
Experiment with different voice IDs (0 or 1) to find one that suits your preference.
## Contributions
Contributions to this project are welcome! Feel free to open issues or pull requests to suggest improvements, report bugs, or add new features.
## Credits
This Voice Assistant project was created by Harsh.