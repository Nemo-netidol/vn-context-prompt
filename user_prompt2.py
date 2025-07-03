from LLM import generate_context

previous_response = open("response/user_prompt1_response.txt").read()

user_prompt2_template = open("prompt/user_prompt2_template.txt").read()
user_prompt2 = user_prompt2_template.format(previous_text = previous_response)


user_prompt2_response = generate_context(user_prompt2)

with open("response/user_prompt2_response.txt", "w") as file:
    file.write(user_prompt2_response)


