# KhansoleAcademy

def generate_readme(title, description, instructions):
    readme_content = f"# {title}\n\n{description}\n\n## Instructions\n\n{instructions}"
    return readme_content

def main():
    # Project details
    title = "Arithmetic Learning Software"
    description = "A Python program that helps users practice arithmetic operations."
    
    # Instructions
    instructions = """1. Run the program.
2. The program will generate arithmetic problems randomly.
3. Enter your answer for each problem.
4. The program will provide feedback on whether your answer is correct or incorrect.
5. Keep answering correctly to build a streak of three correct answers in a row.
6. Once you achieve three correct answers in a row, the program will congratulate you for mastering arithmetic.
7. The program will display the total number of problems attempted.

Enjoy learning and improving your arithmetic skills with Khansole Academy!"

if __name__ == '__main__':
    readme = generate_readme(title, description, instructions)
    with open("README.md", "w") as readme_file:
        readme_file.write(readme)
