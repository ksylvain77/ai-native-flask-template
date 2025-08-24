#!/bin/bash
# GitHub Repository Creation Script
# Automates creating a GitHub repository and setting up the remote

set -e

PROJECT_NAME="{{PROJECT_NAME}}"
PROJECT_DESCRIPTION="{{PROJECT_DESCRIPTION}}"
REPO_VISIBILITY="{{REPO_VISIBILITY:-public}}"

show_help() {
    echo "🚀 GitHub Repository Creator"
    echo "=============================="
    echo ""
    echo "Usage: ./scripts/create-repo.sh [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --private     Create a private repository (default: public)"
    echo "  --public      Create a public repository"
    echo "  --help        Show this help message"
    echo ""
    echo "Prerequisites:"
    echo "  - GitHub CLI (gh) must be installed and authenticated"
    echo "  - Run 'gh auth login' first if not already authenticated"
    echo ""
    echo "Examples:"
    echo "  ./scripts/create-repo.sh"
    echo "  ./scripts/create-repo.sh --private"
}

check_prerequisites() {
    echo "🔍 Checking prerequisites..."
    
    # Check if gh CLI is installed
    if ! command -v gh &> /dev/null; then
        echo "❌ GitHub CLI (gh) is not installed"
        echo "📋 Install with: brew install gh (macOS) or apt install gh (Ubuntu)"
        echo "🔗 More info: https://cli.github.com/"
        exit 1
    fi
    
    # Check if authenticated
    if ! gh auth status &> /dev/null; then
        echo "❌ GitHub CLI is not authenticated"
        echo "🔑 Run: gh auth login"
        exit 1
    fi
    
    # Check if we're in a git repository
    if ! git rev-parse --git-dir &> /dev/null; then
        echo "❌ Not in a Git repository"
        echo "💡 Initialize with: git init"
        exit 1
    fi
    
    # Check if there are commits
    if ! git rev-parse HEAD &> /dev/null; then
        echo "❌ No commits found"
        echo "💡 Make an initial commit first"
        exit 1
    fi
    
    echo "✅ All prerequisites met"
}

create_repository() {
    local visibility=$1
    
    echo "🚀 Creating GitHub repository..."
    echo "📁 Name: $PROJECT_NAME"
    echo "📝 Description: $PROJECT_DESCRIPTION"
    echo "👁️  Visibility: $visibility"
    echo ""
    
    # Create the repository
    if [ "$visibility" = "private" ]; then
        gh repo create "$PROJECT_NAME" --description "$PROJECT_DESCRIPTION" --private --source=. --remote=origin --push
    else
        gh repo create "$PROJECT_NAME" --description "$PROJECT_DESCRIPTION" --public --source=. --remote=origin --push
    fi
    
    echo ""
    echo "✅ Repository created successfully!"
    
    # Get the repository URL
    REPO_URL=$(gh repo view --json url --jq '.url')
    echo "🔗 Repository URL: $REPO_URL"
    echo "🌐 Clone URL: git@github.com:$(gh api user --jq '.login')/$PROJECT_NAME.git"
    
    # Update project files with the actual repo URL if they contain placeholders
    if grep -q "{{REPO_URL}}" *.md 2>/dev/null; then
        echo "📝 Updating project files with repository URL..."
        sed -i.bak "s|{{REPO_URL}}|$REPO_URL|g" *.md 2>/dev/null || true
        rm -f *.md.bak 2>/dev/null || true
    fi
    
    echo ""
    echo "🎉 Setup complete! Your project is now on GitHub."
    echo "💡 Next steps:"
    echo "   - Visit your repository: $REPO_URL"
    echo "   - Set up branch protection rules if needed"
    echo "   - Add collaborators if this is a team project"
}

# Parse command line arguments
VISIBILITY="public"
while [[ $# -gt 0 ]]; do
    case $1 in
        --private)
            VISIBILITY="private"
            shift
            ;;
        --public)
            VISIBILITY="public"
            shift
            ;;
        --help|-h)
            show_help
            exit 0
            ;;
        *)
            echo "❌ Unknown option: $1"
            echo ""
            show_help
            exit 1
            ;;
    esac
done

# Main execution
echo "🚀 GitHub Repository Creation Script"
echo "====================================="
echo ""

check_prerequisites
create_repository "$VISIBILITY"
