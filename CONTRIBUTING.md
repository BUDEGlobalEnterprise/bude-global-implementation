# Contributing to Bude Global ERPNext Implementation Docs

First off, thank you for considering contributing to the Bude Global ERPNext Implementation Documentation! It's people like you that make open-source documentation such a valuable resource for the community.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Your First Documentation Contribution](#your-first-documentation-contribution)
  - [Pull Requests](#pull-requests)
- [Style Guides](#style-guides)
  - [Documentation Styleguide](#documentation-styleguide)
  - [Git Commit Messages](#git-commit-messages)
- [Additional Notes](#additional-notes)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [budeglobalerp@gmail.com](mailto:budeglobalerp@gmail.com).

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** to your local machine:
   ```bash
   git clone https://github.com/YOUR_USERNAME/bude-global-implementation.git
   cd bude-global-implementation
   ```
3. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/amazing-docs
   ```

## How Can I Contribute?

### Reporting Bugs

Bugs are tracked as [GitHub issues](https://github.com/BUDEGlobalEnterprise/bude-global-implementation/issues). Create an issue and provide the following information:

- **Clear, descriptive title**
- **Detailed steps to reproduce the issue**
- **Expected behavior vs actual behavior**
- **Screenshots if applicable**
- **Your environment:**
  - Browser and version
  - Operating system

### Suggesting Enhancements

Enhancement suggestions are also tracked as GitHub issues. Please include:

- **Clear, descriptive title**
- **Detailed description of the proposed enhancement**
- **Explanation of why this enhancement would be useful**
- **Any examples of the enhancement if you've seen it elsewhere**

### Your First Documentation Contribution

Unsure where to begin? You can start by looking at issues labeled `good first issue` or `documentation`.

- **Good first issues**: Small documentation fixes or additions
- **Documentation issues**: Areas needing better explanation or new guides

### Pull Requests

Process for submitting a pull request:

1. **Fork** the repository
2. **Create your feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

Please ensure your PR description clearly describes the problem and solution. Include the relevant issue number if applicable.

## Style Guides

### Documentation Styleguide

- Use **Markdown** for all documentation
- Write in clear, concise English
- Use heading levels appropriately (H1, H2, H3, etc.)
- Include code examples where relevant with proper syntax highlighting
- Add screenshots for complex UI explanations
- Keep lines to 80 characters maximum where possible

Example markdown structure:

````markdown
# Main Title

## Section Heading

Content goes here.

### Subsection
````
More detailed content.

````python
# Code examples should use code blocks
def example_function():
    return "Hello World"
````

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or fewer
- Reference issues and pull requests liberally after the first line

## Additional Notes

### Issue and Pull Request Labels

We use the following labeling system:

- `bug` - Something isn't working
- `documentation` - Improvements or additions to documentation
- `duplicate` - This issue or pull request already exists
- `enhancement` - New feature or request
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed

### Recognition

All contributors will be recognized in our [CONTRIBUTORS.md](CONTRIBUTORS.md) file. Significant contributions may also be highlighted in release notes.

Thank you for contributing to making ERPNext documentation better for everyone!
