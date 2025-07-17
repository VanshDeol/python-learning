# push_leetcode_solution.py

import os
import subprocess

def get_untracked_py_files():
    result = subprocess.run(['git', 'ls-files', '--others', '--exclude-standard'], capture_output=True, text=True)
    files = result.stdout.strip().split('\n')
    return [f for f in files if f.startswith('LeetCode/') and f.endswith('.py')]

def main():
    print("=== 🚀 Auto Git Push for LeetCode Solutions ===\n")

    untracked_files = get_untracked_py_files()

    if not untracked_files:
        print("✅ No untracked LeetCode Python files found.")
        return

    print("📄 Untracked LeetCode files:")
    for idx, file in enumerate(untracked_files, 1):
        print(f"{idx}. {file}")

    try:
        choice = int(input("\nSelect the file number to commit: "))
        selected_file = untracked_files[choice - 1]
    except (ValueError, IndexError):
        print("❌ Invalid selection.")
        return

    problem_name = input("Enter problem name (e.g., Two Sum): ").strip()
    difficulty = input("Enter difficulty (Easy, Medium, Hard): ").capitalize()

    topic = selected_file.split("/")[1].capitalize()

    # Stage, Commit, Push
    subprocess.run(["git", "add", selected_file])
    commit_msg = f"Solved LeetCode: {problem_name} [{difficulty}] in {topic}"
    subprocess.run(["git", "commit", "-m", commit_msg])
    subprocess.run(["git", "push"])

    print(f"\n✅ Pushed: {selected_file}")
    print(f"💬 Commit Message: {commit_msg}")

if __name__ == "__main__":
    main()

