import requests

def translate_text():
    # Server URL (make sure your Flask server is running)
    url = "http://localhost:5000/translate"
    
    while True:
        # Get user input
        print("\n=== Translation Service ===")
        text = input("\nEnter text to translate (or 'quit' to exit): ")
        
        # Check if user wants to quit
        if text.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Show available languages
        print("\nAvailable languages:")
        print("es: Spanish")
        print("fr: French")
        print("de: German")
        print("it: Italian")
        print("ja: Japanese")
        print("ko: Korean")
        print("zh-cn: Chinese (Simplified)")
        
        target_lang = input("\nEnter target language code: ")
        
        # Prepare the request data
        data = {
            "text": text,
            "target_lang": target_lang
        }
        
        try:
            # Make the POST request
            response = requests.post(url, json=data)
            
            # Check if request was successful
            if response.status_code == 200:
                result = response.json()
                print("\nOriginal text:", text)
                print("Translated text:", result["translated_text"])
            else:
                print("Error:", response.json().get("error"))
                
        except requests.exceptions.ConnectionError:
            print("Error: Cannot connect to server. Make sure server is running.")

if __name__ == "__main__":
    translate_text()