from app.assistant import AIAssistant
from app.utils.animation import Animation

def main():
    Animation.welcome("Jarvis")
    assistant = AIAssistant()
    
    while True:
        command = input("\nYou: ")
        if "exit" in command.lower():
            assistant.speak("Goodbye, sir!")
            break
        response = assistant.process_command(command)
        print(f"Jarvis: {response}")

if __name__ == "__main__":
    main()rsonality.json") as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                "responses": {
                    "greeting": ["Hello!", "Hi there!", "Good to see you!"],
                    "farewell": ["Goodbye!", "See you later!", "Bye!"]
                }
            }

    def handle_command(self, command):
        try:
            if "train yourself" in command.lower():
                return self.training_mode()
            return self._process_command(command)
        except Exception as e:
            return f"Error processing command: {str(e)}"

    def training_mode(self):
        print("\n--- Training Mode ---")
        text = input("Enter example phrase: ")
        intent = input("What should this trigger? ")
        self.trainer.add_training_example(text, intent)
        return "Thank you for teaching me!"

    def _process_command(self, command):
        doc = self.nlp(command.lower())
        
        if "exit" in command.lower():
            self.voice.speak("Goodbye!")
            exit()
            
        return "I can help with various tasks! Say 'train yourself' to teach me new things"

if __name__ == "__main__":
    assistant = EnhancedAssistant()
    Animation.welcome("User")
    
    while True:
        command = input("\nYou: ")
        response = assistant.handle_command(command)
        print(f"Assistant: {response}")
        assistant.voice.speak(response)