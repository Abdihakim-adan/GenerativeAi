import requests


class Calculator:
    def __init__(self):
        self.ollama_url = "http://localhost:11434/api/generate"
    
    def ask_ollama(self, question):
        """Send request to Ollama API directly"""
        
        prompt = f"Solve this math problem step by step: {question}. Provide the final answer clearly."
        
        data = {
            "model": "tinyllama",
            "prompt": prompt,
            "stream": False
        }
        
        try:
            response = requests.post(self.ollama_url, json=data)
            if response.status_code == 200:
                result = response.json()
                return result.get("response", "No response received")
            else:
                return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Connection error: {str(e)}"
    
    def start(self):
        print("🧮 Smart Calculator (Ollama Powered)")
        print("Type 'quit' to exit\n")
        
        while True:
            question = input("Enter your math question: ")
            
            if question.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
                
            if question.strip():
                print("Calculating...")
                answer = self.ask_ollama(question)
                print(f"\n📝 Answer: {answer}\n")
            else:
                print("Please enter a valid question.\n")

# Run the calculator
if __name__ == "__main__":
    calc = Calculator()
    calc.start()
