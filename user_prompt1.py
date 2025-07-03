from LLM import generate_context

user_prompt1 = open("user_prompt1_fantasy").read()

context = generate_context(user_prompt1)

with open("response/user_prompt1_response.txt", "w") as file:
    file.write(context)




