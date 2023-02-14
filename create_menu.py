import os
import json
import markdown

menu_items = {
    "Introduction": "introduction.md",
    "Scope": "scope.md",
    "Normative References": "normative-references.md",
    "Terms and Definitions": "terms-and-definitions.md",
    "Requirements for Measurement Management Systems": "requirements-for-measurement-management-systems.md",
    "Management Responsibility": "management-responsibility.md",
    "Measurement System Analysis": "measurement-system-analysis.md",
    "Measurement Equipment Control": "measurement-equipment-control.md",
    "Measurement Process Control": "measurement-process-control.md",
    "Data Analysis": "data-analysis.md",
    "Improvement": "improvement.md"
}

def generate_menu():
    menu = []
    for item, filename in menu_items.items():
        path = os.path.join(os.getcwd(), filename)
        with open(path, 'r') as f:
            content = f.read()
            html = markdown.markdown(content)
            menu.append(f'<li><a href="{filename}">{item}</a></li>\n')
    return ''.join(menu)

  def generate_index():
    menu = generate_menu()
    content = f'# ISO 10012:2003 in Gas Station\n\n<ul>\n{menu}</ul>'
    with open('index.md', 'w') as f:
        f.write(content)

        generate_index()
        
git add .
git commit -m "Initial commit"
git push origin master

