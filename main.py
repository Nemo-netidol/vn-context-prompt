from LLM import generate_context
import re


def extract_option_from_text(response, selectedChoice):
    options = re.findall(r'([A-C])\)\s*"(.*?)"', response)
    options_dict = {letter: text for letter, text in options}
    return options_dict.get(selectedChoice.upper(), None)


# Load files
user_prompt2_template = open("prompt/user_prompt2_template.txt").read()

# Ask user to choose theme of the vn
theme = input("What VN theme do you prefer(fantasy, adventure, science): ")

if (theme != "fantasy") and (theme != "adventure") and (theme != "science"):
    print("There is no such theme for visual novel right now. Choosing fantasy theme....")

user_prompt1 = open(f"prompt/user_prompt1_{theme}.txt").read()

# First generation
print("🌟STORY: \n")
context = generate_context(user_prompt1)
print(context, end="\n")



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
    print("\n")
