#!/usr/bin/env python3
"""
AI-Native Project Template Initializer

This script sets up a new project with AI-collaborative development patterns.
It uses smart defaults so you can start building immediately without needing
to know your final architecture upfront.

Philosophy: Start simple, evolve with AI
- Uses sensible defaults for everything
- Only asks for project name and description  
- Let the AI help you evolve the structure as you build
- No need to know ports, modules, or endpoints before you start

The generated files can be customized later as your project grows.
"""

import os
import sys
import re
from pathlib import Path

def get_user_input():
    """Get minimal project configuration with smart defaults"""
    print("🤖 AI-Native Project Template Initializer")
    print("=" * 50)
    print("✨ Using smart defaults - just press Enter to accept")
    print("💡 Want to explore first? Type 'skip' for any question to use all defaults")
    print()
    
    import os
    folder_name = os.path.basename(os.getcwd())
    
    config = {}
    
    # Only ask the essentials
    project_name = input(f"Project name [{folder_name.replace('-', ' ').title()}]: ").strip()
    if project_name.lower() == 'skip':
        print("🚀 Using all defaults - let's get you started!")
        project_name = ""
    config['PROJECT_NAME'] = project_name if project_name else folder_name.replace('-', ' ').title()
    
    if project_name.lower() != 'skip':
        description = input("Brief description [A Python project]: ").strip()
        if description.lower() == 'skip':
            description = ""
        config['PROJECT_DESCRIPTION'] = description if description else "A Python project"
    else:
        config['PROJECT_DESCRIPTION'] = "A Python project"
    
    # Smart defaults for everything else
    config['PROJECT_TYPE'] = "Python application"
    config['MAIN_FILE'] = "main.py"
    config['SERVICE_NAME'] = folder_name.replace('-', '_')
    config['PORT'] = "5000"  # Flask default, commonly free
    config['SERVER_URL'] = "http://localhost:5000"
    config['HEALTH_ENDPOINT'] = "/health"
    config['MODULE_1'] = "core"
    config['MODULE_1_DESC'] = "Core business logic"
    config['MODULE_2'] = "utils"
    config['MODULE_2_DESC'] = "Utility functions"
    config['REPO_URL'] = f"https://github.com/yourusername/{folder_name}"
    config['PYTHON_COMMAND'] = "main.py"
    config['ADDITIONAL_REQUIREMENTS'] = "None"
    config['PROJECT_STATUS'] = "In Development"
    config['PROJECT_VERSION'] = "0.1.0"
    config['LAST_UPDATED'] = "2025-01-01"
    config['PROJECT_PHILOSOPHY'] = "Practical development with AI collaboration"
    
    # Default status fields that make sense for any project
    config['STATUS_FIELD_1'] = "Status"
    config['STATUS_VALUE_1'] = "Starting Development"
    config['STATUS_FIELD_2'] = "Features"
    config['STATUS_VALUE_2'] = "Basic Structure"
    config['STATUS_FIELD_3'] = "Testing"
    config['STATUS_VALUE_3'] = "Template Ready"
    
    print(f"\n✅ Project: {config['PROJECT_NAME']}")
    print(f"✅ Type: {config['PROJECT_TYPE']}")
    print(f"✅ Server: {config['SERVER_URL']}")
    print("✅ Ready to start building!")
    
    return config

def replace_placeholders(file_path, config):
    """Replace template placeholders in a file"""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Replace all placeholders
        for key, value in config.items():
            placeholder = f"{{{{{key}}}}}"
            content = content.replace(placeholder, value)
        
        with open(file_path, 'w') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False

def initialize_project(template_dir, target_dir, config):
    """Initialize a new project from template"""
    print(f"\n🚀 Initializing project in {target_dir}")
    print("=" * 50)
    
    # Create target directory
    os.makedirs(target_dir, exist_ok=True)
    
    # Copy template files
    import shutil
    
    for root, dirs, files in os.walk(template_dir):
        # Skip __pycache__ and .git directories
        dirs[:] = [d for d in dirs if d not in ['__pycache__', '.git', '.pytest_cache']]
        
        for file in files:
            if file.endswith('.pyc'):
                continue
                
            src_path = os.path.join(root, file)
            rel_path = os.path.relpath(src_path, template_dir)
            dst_path = os.path.join(target_dir, rel_path)
            
            # Create directory if needed
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)
            
            # Copy file
            shutil.copy2(src_path, dst_path)
            
            # Replace placeholders
            if file.endswith(('.md', '.py', '.sh', '.txt', '.json', '.yml', '.yaml')):
                replace_placeholders(dst_path, config)
            
            print(f"✅ {rel_path}")
    
    # Make scripts executable
    scripts_dir = os.path.join(target_dir, 'scripts')
    if os.path.exists(scripts_dir):
        for script in os.listdir(scripts_dir):
            if script.endswith('.sh'):
                script_path = os.path.join(scripts_dir, script)
                os.chmod(script_path, 0o755)
    
    # Make manage.sh executable
    manage_script = os.path.join(target_dir, 'manage.sh')
    if os.path.exists(manage_script):
        os.chmod(manage_script, 0o755)
    
    print(f"\n🎉 Project initialized successfully!")
    print(f"📁 Location: {target_dir}")
    print(f"\n🚀 Next steps:")
    print(f"   cd {target_dir}")
    print(f"   ./manage.sh setup")
    print(f"   ./manage.sh start")

def main():
    """Main initializer"""
    if len(sys.argv) < 2:
        print("Usage: python init_project.py <target_directory>")
        sys.exit(1)
    
    template_dir = os.path.dirname(os.path.abspath(__file__))
    target_dir = sys.argv[1]
    
    # Get configuration
    config = get_user_input()
    
    # Initialize project
    initialize_project(template_dir, target_dir, config)

if __name__ == "__main__":
    main()
