from LLM import generate_context
import re


def extract_option_from_text(response, selectedChoice):
    options = re.findall(r'([A-C])\)\s*"(.*?)"', response)
    options_dict = {letter: text for letter, text in options}
    return options_dict.get(selectedChoice.upper(), None)


# Load files
user_prompt2_template = open("prompt/user_prompt2_template.txt").read()
user_prompt1 = open("prompt/user_prompt1_fantasy.txt").read()

# First generation
context = generate_context(user_prompt1)
print(context)

while True:
    userInput = input("Select choice (A/B/C or exit): ").strip().upper()
    if userInput == "EXIT":
        break
    # Get selected choice text
    select_text = extract_option_from_text(context, userInput)

    # Fill prompt with selected choice text
    user_prompt2 = user_prompt2_template.format(choice=userInput, previous_text=context)

    # Generate next part
    prompt2_context = generate_context(user_prompt2)
    print(prompt2_context)
