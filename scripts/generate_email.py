from jinja2 import Environment, FileSystemLoader
import os 

def generate_email(template_file, output_file, content):
    # Create a Jinja2 Environment
    env = Environment(loader=FileSystemLoader('./templates'))

    # Load template from above environment
    template = env.get_template(template_file)

    # Render template w/ dynamic content
    dynamic_content = template.render(content)

    # Ensure the 'content' directory exists
    os.makedirs('content', exist_ok=True)

    # Define the output file path within the 'content' directory
    output_path = os.path.join('content', output_file)

    # Write rendered content to the output file
    with open(output_path, 'w') as f:
        f.write(dynamic_content)

# ----- #NOTE: INSERT EMAIL CONTENT HERE -----
content = "hello world this is dynamic content"

if __name__ == "__main__":
    email_data = {
        'title': 'test',
        'content': content,
    }

# Standardise the output file's filename 
output_filename = "email_" + email_data['title'].lower().replace(" ", "_") + ".html"

# Calling the main function with its relevant args
generate_email('email_layout.html', output_filename, email_data)
