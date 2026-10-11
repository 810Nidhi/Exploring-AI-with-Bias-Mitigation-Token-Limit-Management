from groq import generate_response 
#from hf import generate_response
def bias_mitigation_activity():
    print("Bias Mitigation Activity")
    prompt=input("Enter a prompt to explore bias(e.g 'Describe the ideal doctor)").strip()
    if not prompt:
        print("Please enter a prompt")
        return
    initial_response=generate_response(prompt,temperature=0.3,max_tokens=1024)
    print(f"Initial response:\n{initial_response}\n")
    modified_prompt=input("Modify the prompt to make it more neutral(e.g'Describe the qualities of a doctor'): ").strip()
    if modified_prompt:
        modified_response=generate_response(modified_prompt,temperature=0.3,max_tokens=1024)
        print(f"Modified AI response(Neutral): {modified_response}\n")
    else:
        print("No modified prompt provided. Skipping modified response.")
def token_limit_activity():
    print("Token Limit Activity")
    long_prompt=input("Enter a long prompt(more than 300 words,e.g detailed story or description): ").strip()
    if long_prompt:
        long_response=generate_response(long_prompt,temperature=0.3,max_tokens=1024)
        preview=(long_response[:500]+"...")if len(long_response)>500 else long_response
        print(f"Response to long prompt:\n{preview}\n")
    else:
        print("No long prompt provided. Skipping long response.")
    short_prompt=input("Now condense the prompt to be more concise: ").strip()
    if short_prompt:
        short_response=generate_response(short_prompt,temperature=0.3,max_tokens=512)
        print(f"Response to short prompt:\n{short_response}\n")
    else:
        print("No condensed prompt provided. Skipping short response.")
def run_activity():
    print("\nAI Learning Activity ")
    print("Choose an activity:")
    print("1. Bias Mitigation")
    print("2. Token Limits")
    choice=input("Enter your choice (1 or 2): ").strip()
    if choice=="1":
        bias_mitigation_activity()
    elif choice=="2":
        token_limit_activity()
    else:
        print("Invalid choice. Please select 1 or 2.")
if __name__=="__main__":
    run_activity()