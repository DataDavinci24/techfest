from uagents import Agent, Context, Model



import os

class Message(Model):
    message : dict

agent = Agent(name='user', seed='user secret phrase')
recipient_address = 'agent1qtgaehce8tgqafl7h4sxzp2mcdt4zakdjwpmyrx0q3f7a753afhpwm003vj'
def text_to_dict(directory_path):
    result_dict = {}

    # Ensure the directory path is valid
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        raise ValueError("Invalid directory path")

    # Iterate over each file in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Check if the file is a text file
        if os.path.isfile(file_path) and filename.lower().endswith('.txt'):
            # Read the contents of the text file
            with open(file_path, 'r') as file:
                file_contents = file.read()

            # Remove the file extension to use as the dictionary key
            key = os.path.splitext(filename)[0]

            # Add to the dictionary
            result_dict[key] = file_contents

    return result_dict

# Example usage:
res_path = '/Users/nitin/Documents/IBAB/techfest/text_resumes'
res_dict = text_to_dict(res_path)
jd_path = '/Users/nitin/Documents/IBAB/techfest/jd_text'
jd_dict = text_to_dict(jd_path)

@agent.on_event('startup')
async def send_message(ctx: Context):
    await ctx.send(recipient_address, Message(jd_dict))
    await ctx.send(recipient_address, Message(res_dict))

