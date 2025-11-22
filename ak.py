import google.generativeai as genai
genai.configure(api_key="AIzaSyDqvl0A347eCJYQHFpolyNCL1FKUnOlw6U")
model = genai.GenerativeModel("gemini-2.0-flash")
def chat():
    print("chatbot meow will help you!./n ")
    while True:
            user_input = input("chello:")
            if user_input.lower() == "exit":
                print("chatbo:hello😍")
                break
            response = model.generate_content(user_input)
            print("chatbot:",response.text,"\n")
if __name__=="__main__":
    chat()
