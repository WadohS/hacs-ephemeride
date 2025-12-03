# Contribution Guidelines

Contributing to this project should be as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Adding new language support

## Github is Used for Everything

Github is used to host code, to track issues and feature requests, as well as accept pull requests.

Pull requests are the best way to propose changes to the codebase.

1. Fork the repo and create your branch from `master`.
2. If you've changed something, update the documentation.
3. Make sure your code lints (using black and flake8).
4. Test your contribution.
5. Issue that pull request!

## Any Contributions You Make Will Be Under the MIT Software License

In short, when you submit code changes, your submissions are understood to be under the same [MIT License](http://choosealicense.com/licenses/mit/) that covers the project. Feel free to contact the maintainers if that's a concern.

## Report Bugs Using Github's [Issues](https://github.com/WadohS/hacs-ephemeride/issues)

We use GitHub issues to track public bugs. Report a bug by [opening a new issue](https://github.com/WadohS/hacs-ephemeride/issues/new); it's that easy!

## Write Bug Reports with Detail, Background, and Sample Code

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

## Adding New Languages

We welcome translations to new languages! To add a new language:

1. Create a new JSON file in `custom_components/ephemeride/languages/` (e.g., `nl.json` for Dutch)
2. Follow the format of existing files (366 dates with saints and feasts)
3. Add the language code to `SUPPORTED_LANGUAGES` in `const.py`
4. Create a translation file in `custom_components/ephemeride/translations/` for the UI
5. Test thoroughly with your language selected

## Use a Consistent Coding Style

* Use [Black](https://black.readthedocs.io/) for code formatting
* Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
* Use type hints where possible
* Write descriptive commit messages

## License

By contributing, you agree that your contributions will be licensed under its MIT License.

## References

This document was adapted from the open-source contribution guidelines for [Facebook's Draft](https://github.com/facebook/draft-js/blob/a9316a723f9e918afde44dea68b5f9f39b7d9b00/CONTRIBUTING.md).
