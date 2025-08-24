#!/usr/bin/env python3
"""
Cross-Platform Git Workflow - Merge to Main
Replaces merge-to-main.sh with Python for Windows/macOS/Linux compatibility
"""

import sys
import subprocess
from pathlib import Path

def run_command(command, cwd=None):
    """Run a command and handle errors"""
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, check=True, 
                              capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed: {command}")
        print(f"Error: {e.stderr}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("❌ Usage: python merge-to-main.py <commit-message>")
        print("")
        print("Examples:")
        print("  python merge-to-main.py \"Add user authentication: JWT-based login system\"")
        print("  python merge-to-main.py \"Fix: API endpoint validation and error handling\"")
        sys.exit(1)
    
    commit_message = sys.argv[1]
    project_root = Path(__file__).parent.parent
    
    # Get current branch name
    current_branch = run_command("git branch --show-current", cwd=project_root)
    
    if current_branch == "main":
        print("❌ Already on main branch. Create a feature branch first.")
        sys.exit(1)
    
    print(f"🔄 Merging feature branch '{current_branch}' to main")
    print(f"📝 Final commit message: {commit_message}")
    print("")
    
    # Run tests before merging
    print("🧪 Running tests...")
    test_script = project_root / "scripts" / "run-tests.py"
    if test_script.exists():
        run_command(f"python {test_script}", cwd=project_root)
    else:
        # Fallback to original shell script
        test_script_sh = project_root / "scripts" / "run-tests.sh"
        if test_script_sh.exists():
            run_command(f"bash {test_script_sh}", cwd=project_root)
    
    # Stage all changes
    print("📦 Staging changes...")
    run_command("git add .", cwd=project_root)
    
    # Check if there are changes to commit
    try:
        run_command("git diff --staged --exit-code", cwd=project_root)
        print("ℹ️  No changes to commit")
    except subprocess.CalledProcessError:
        # There are changes to commit
        print("💾 Committing changes...")
        run_command(f"git commit -m \"{commit_message}\"", cwd=project_root)
    
    # Switch to main and merge
    print("🔄 Switching to main branch...")
    run_command("git checkout main", cwd=project_root)
    
    print("📥 Pulling latest changes...")
    run_command("git pull origin main", cwd=project_root)
    
    print(f"🔀 Merging {current_branch}...")
    run_command(f"git merge {current_branch} --no-ff -m \"Merge {current_branch}: {commit_message}\"", 
               cwd=project_root)
    
    print("🚀 Pushing to main...")
    run_command("git push origin main", cwd=project_root)
    
    # Clean up feature branch
    print(f"🧹 Cleaning up feature branch: {current_branch}")
    run_command(f"git branch -d {current_branch}", cwd=project_root)
    
    # Update roadmap
    update_roadmap_script = project_root / "scripts" / "update-roadmap.py"
    if update_roadmap_script.exists():
        run_command(f"python {update_roadmap_script} \"{current_branch}\" \"{commit_message}\" \"completed\"", 
                   cwd=project_root)
    
    print("")
    print("✅ Feature successfully merged to main!")
    print("🎉 Development workflow complete")

if __name__ == "__main__":
    main()
