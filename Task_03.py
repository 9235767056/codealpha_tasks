#Goal: Build a simple rule-based chatbot.
#Scope:
# Input from user like: "hello", "how are you", "bye". re you", "bye",
# . Predefined replies like: "Hi!", "I'm fine, thanks!", "Goodbye!".
# Key Concepts Used: if-elif, functions, loops, input/output.

import random
import datetime

class SimpleChatbot:
    """
    A more expanded simple rule-based chatbot.
    It recognizes various greetings, farewells, and a few other common phrases.
    It also keeps a basic conversation history.
    """
    def __init__(self):
        self.conversation_history = []
        self.rules = {
            # Greetings
            ("hello", "hi", "hey", "good morning", "good afternoon", "good evening"):
                ["Hi there!", "Hello!", "Hey!", "Greetings!"],
            # How are you?
            ("how are you", "how are you doing", "how's it going", "what's up"):
                ["I'm doing great, thank you for asking!", "I'm fine, thanks!",
                 "All good! How about you?", "Just processing data, as usual."],
            # What's your name?
            ("what's your name", "who are you"):
                ["I am a simple rule-based chatbot.", "You can call me ChatBot.",
                 "I don't have a name, I'm just a program."],
            # Weather (basic, no actual weather data)
            ("weather", "is it raining", "what's the weather like"):
                ["I don't have access to real-time weather data.",
                 "I'm not sure about the weather, I'm just a program!",
                 "You might want to check a weather app for that."],
            # Time (basic, uses system time)
            ("what time is it", "time now"):
                [f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}.",
                 f"It's {datetime.datetime.now().strftime('%I:%M %p')} right now."],
            # Feelings
            ("how do you feel", "are you happy"):
                ["As an AI, I don't have feelings.", "I operate based on logic, not emotions.",
                 "I'm designed to be helpful, so I suppose that makes me 'content'."],
            # Goodbye/Farewells
            ("bye", "goodbye", "see you", "farewell", "exit"):
                ["Goodbye!", "See you later!", "Farewell!", "It was nice chatting!", "Bye for now!"],
            # Thanks
            ("thank you", "thanks", "appreciate it"):
                ["You're welcome!", "No problem!", "Glad to help!"],
            # Default response
            "default":
                ["I'm not sure how to respond to that.", "Could you rephrase that?",
                 "I'm a simple chatbot, so I have limited understanding.",
                 "Please ask me something I understand, like 'hello' or 'how are you'."]
        }

    def get_response(self, user_input):
        """
        Determines the chatbot's response based on the user's input.
        """
        user_input_lower = user_input.lower().strip() # Clean input

        # Add user input to history
        self.conversation_history.append(f"You: {user_input}")

        # Check for matching rules
        for keywords, responses in self.rules.items():
            if isinstance(keywords, tuple): # For multiple keywords
                if any(keyword in user_input_lower for keyword in keywords):
                    response = random.choice(responses)
                    self.conversation_history.append(f"Chatbot: {response}")
                    return response
            elif isinstance(keywords, str) and keywords == user_input_lower: # For exact match
                response = random.choice(responses)
                self.conversation_history.append(f"Chatbot: {response}")
                return response

        # If no specific rule matches, return a default response
        response = random.choice(self.rules["default"])
        self.conversation_history.append(f"Chatbot: {response}")
        return response

    def run(self):
        """
        Starts the chatbot interaction loop.
        """
        print("Chatbot: Hi! I'm an expanded simple rule-based chatbot.")
        print("Chatbot: You can type 'help' for available commands or 'bye' to exit.")

        while True:
            user_input = input("You: ")

            if user_input.lower().strip() == "bye":
                print(f"Chatbot: {random.choice(self.rules[('bye',)])}")
                break
            elif user_input.lower().strip() == "help":
                print("\nChatbot: I understand the following types of phrases:")
                print("         - Greetings (e.g., hello, hi, good morning)")
                print("         - Asking how I am (e.g., how are you, how's it going)")
                print("         - Asking my name (e.g., what's your name)")
                print("         - Asking about time (e.g., what time is it)")
                print("         - Saying thanks (e.g., thank you)")
                print("         - Farewells (e.g., bye, goodbye)")
                print("         - Type 'history' to see our conversation.")
                print("         - Type 'bye' to exit.\n")
            elif user_input.lower().strip() == "history":
                print("\n--- Conversation History ---")
                if not self.conversation_history:
                    print("No conversation yet.")
                else:
                    for item in self.conversation_history:
                        print(item)
                print("--------------------------\n")
            else:
                response = self.get_response(user_input)
                print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.run()
