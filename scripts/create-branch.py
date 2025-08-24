#!/usr/bin/env python3
"""
Cross-Platform Git Workflow - Create Branch
Replaces create-branch.sh with Python for Windows/macOS/Linux compatibility
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
    if len(sys.argv) != 3:
        print("❌ Usage: python create-branch.py <branch-name> <commit-message>")
        print("")
        print("Examples:")
        print("  python create-branch.py add-user-auth \"Add user authentication: JWT-based login system\"")
        print("  python create-branch.py fix-api-endpoints \"Fix: API endpoint validation and error handling\"")
        sys.exit(1)
    
    branch_name = sys.argv[1]
    commit_message = sys.argv[2]
    
    print(f"🌿 Creating development branch: {branch_name}")
    print(f"📝 Commit message: {commit_message}")
    print("")
    
    project_root = Path(__file__).parent.parent
    
    # Ensure we're on main and up to date
    print("📥 Pulling latest changes...")
    run_command("git checkout main", cwd=project_root)
    run_command("git pull origin main", cwd=project_root)
    
    # Create and switch to feature branch
    print(f"🆕 Creating feature branch: {branch_name}")
    run_command(f"git checkout -b {branch_name}", cwd=project_root)
    
    # Update roadmap to mark branch as in progress
    update_roadmap_script = project_root / "scripts" / "update-roadmap.py"
    if update_roadmap_script.exists():
        run_command(f"python {update_roadmap_script} \"{branch_name}\" \"{commit_message}\" \"in-progress\"", 
                   cwd=project_root)
    
    print("")
    print("✅ Development branch ready!")
    print("👨‍💻 Make your changes, then when ready, use:")
    print(f"   python scripts/merge-to-main.py \"{commit_message}\"")

if __name__ == "__main__":
    main()
