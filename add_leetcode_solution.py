# add_leetcode_solution.py

import os
import subprocess

def sanitize_filename(name):
    return name.strip().lower().replace(" ", "_").replace("(", "").replace(")", "")

def main():
    print("=== LeetCode Commit Automation ===")
    topic = input("Enter topic (e.g., arrays, strings, hashing): ").strip().lower()
    problem_name = input("Enter problem name (e.g., Two Sum): ").strip()
    difficulty = input("Enter difficulty (Easy, Medium, Hard): ").capitalize()

    file_name = sanitize_filename(problem_name) + ".py"
    folder_path = os.path.join("LeetCode", topic)
    file_path = os.path.join(folder_path, file_name)

    # Create topic folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    # If file doesn't exist, create it with a boilerplate
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write(f'"""\nLeetCode Problem: {problem_name}\nDifficulty: {difficulty}\nTopic: {topic.capitalize()}\n"""\n\n')
            f.write("# Your solution goes here\n")
        print(f"Created: {file_path}")
    else:
        print(f"File already exists: {file_path}")

    # Git add, commit, push
    subprocess.run(["git", "add", file_path])
    commit_msg = f"Solved LeetCode: {problem_name} [{difficulty}] in {topic.capitalize()}"
    subprocess.run(["git", "commit", "-m", commit_msg])
    subprocess.run(["git", "push"])

if __name__ == "__main__":
    main()

