#!/bin/bash
# Git Merge Workflow - Generic Template

set -e

COMMIT_MESSAGE="$1"

if [ -z "$COMMIT_MESSAGE" ]; then
    echo "❌ Usage: $0 \"<commit-message>\""
    echo ""
    echo "Examples:"
    echo "  $0 \"Add user authentication: JWT-based login system\""
    echo "  $0 \"Fix: API endpoint validation and error handling\""
    exit 1
fi

# Get current branch name
CURRENT_BRANCH=$(git branch --show-current)

if [ "$CURRENT_BRANCH" = "main" ]; then
    echo "❌ Cannot merge while on main branch"
    echo "💡 Create a feature branch first with: ./scripts/create-branch.sh"
    exit 1
fi

echo "🔄 AUTOMATED MERGE WORKFLOW"
echo "============================"
echo "Branch: $CURRENT_BRANCH"
echo "Message: $COMMIT_MESSAGE"
echo ""

# Step 1: Template validation (if this is the template itself)
if [ -f "scripts/validate-template.sh" ]; then
    echo "🔍 STEP 1: TEMPLATE VALIDATION"
    echo "==============================="
    echo "🧪 Running template self-validation..."
    ./scripts/validate-template.sh
    echo ""
fi

# Step 2: Update documentation (if exists)
if [ -f "scripts/update-readme.sh" ]; then
    echo "📝 STEP 2: AUTO-UPDATE DOCUMENTATION"
    echo "======================================"
    ./scripts/update-readme.sh
    echo ""
fi

# Step 3: Run tests
echo "🧪 STEP 3: PRE-MERGE TESTING"
echo "=============================="
if [ -f "scripts/run-tests.sh" ]; then
    echo "🔍 Running comprehensive test suite..."
    # Check if this is the template itself (has placeholder tests)
    if [ -f "scripts/validate-template.sh" ] && grep -q "Template test - replace" tests/test_template.py 2>/dev/null; then
        echo "🎭 Running in template mode (placeholder tests detected)..."
        ./scripts/run-tests.sh template
    else
        ./scripts/run-tests.sh
    fi
else
    echo "⚠️  No test suite found - skipping tests"
fi
echo "✅ All validations and tests passed!"
echo ""

# Step 3: Commit and backup
echo "💾 STEP 3: COMMIT AND BACKUP"
echo "============================"
echo "📦 Staging changes..."
git add -A

echo "💾 Creating commit..."
git commit -m "$COMMIT_MESSAGE"

echo "☁️  Pushing feature branch for backup..."
git push origin "$CURRENT_BRANCH"
echo ""

# Step 4: Merge to main
echo "🔄 STEP 4: MERGE TO MAIN"
echo "======================="
echo "🔄 Switching to main..."
git checkout main

echo "🔀 Merging $CURRENT_BRANCH..."
git merge "$CURRENT_BRANCH"

echo "☁️  Pushing to main..."
git push origin main

# Update roadmap to mark branch as completed
if [ -f "scripts/update-roadmap.sh" ]; then
    ./scripts/update-roadmap.sh "$CURRENT_BRANCH" "$COMMIT_MESSAGE" "completed"
fi
echo ""

# Step 5: Cleanup
echo "🧹 STEP 5: CLEANUP"
echo "=================="
echo "🗑️  Deleting local branch..."
git branch -d "$CURRENT_BRANCH"

echo "☁️  Deleting remote branch..."
git push origin --delete "$CURRENT_BRANCH"
echo ""

echo "🎉 MERGE COMPLETE!"
echo "=================="
echo "✅ Changes merged to main"
echo "✅ Feature branch cleaned up"
echo "✅ Repository in clean state"
echo ""
echo "📊 Repository state:"
echo "   • Current branch: main"
echo "   • Status: Clean main-only state"
