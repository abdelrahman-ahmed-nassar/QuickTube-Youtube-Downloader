#!/bin/bash
# Quick release script for QuickTube
# Usage: ./release.sh 1.0.0

set -e

if [ -z "$1" ]; then
    echo "❌ Error: Version number required"
    echo "Usage: ./release.sh <version>"
    echo "Example: ./release.sh 1.0.0"
    exit 1
fi

VERSION="$1"
TAG="v${VERSION}"

echo "================================================"
echo "🚀 Creating Release: ${TAG}"
echo "================================================"

# Check for uncommitted changes
if ! git diff-index --quiet HEAD --; then
    echo "⚠️  You have uncommitted changes!"
    echo ""
    git status --short
    echo ""
    read -p "Do you want to commit them? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "📝 Enter commit message:"
        read -r COMMIT_MSG
        git add -A
        git commit -m "$COMMIT_MSG"
        git push origin main
    else
        echo "❌ Aborting release. Please commit or stash your changes."
        exit 1
    fi
fi

# Create and push tag
echo "🏷️  Creating tag ${TAG}..."
git tag -a "${TAG}" -m "Release ${VERSION}"

echo "📤 Pushing tag to GitHub..."
git push origin "${TAG}"

echo ""
echo "================================================"
echo "✅ Release ${TAG} triggered!"
echo "================================================"
echo ""
echo "📋 Next steps:"
echo "   1. Go to: https://github.com/abdelrahman-ahmed-nassar/QuickTube-Youtube-Downloader/actions"
echo "   2. Watch the build progress"
echo "   3. Release will be available at:"
echo "      https://github.com/abdelrahman-ahmed-nassar/QuickTube-Youtube-Downloader/releases/tag/${TAG}"
echo ""
echo "⏱️  Builds typically take 5-10 minutes"
echo "================================================"
