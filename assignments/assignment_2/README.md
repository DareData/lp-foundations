# Assignment 2: Code Reviews

For this lesson, we will be using the code from the previous lesson. We will be refactoring and reviewing the code of a fellow colleague.

## 1- Refactoring

There was a problem with the previous code. The `clean_data` function was doing too much. It was loading the data, cleaning it, and saving it. This is a violation of the [Single Responsibility Principle](https://en.wikipedia.org/wiki/Single-responsibility_principle). We want to separate the concerns of the code. We want to have a function that loads the data, a function that cleans the data, and a function that saves the data. This way, we can reuse the code in different contexts.

Refactor the code to have 3 functions: `load_data`, `clean_data`, and `save_data`. The `clean_data` function should take the data as an argument and return the cleaned data. The `save_data` function should take the data as an argument and save it to a file. The `load_data` function should return the data.

All three functions should be called from a `main` function. Don't forget to ensure the tests still work with the `main` function.

You can do this in a new branch called `refactoring`. When you are done, create a pull request from `refactoring` to `main`. Don't merge it yet!

## 2- Code Review

Assign a colleague to review your code. You should receive to opportunity to review your colleague's code as well. In your code review, make sure verify the following:

- Is the code legible? Does it follow the [PEP8](https://www.python.org/dev/peps/pep-0008/) style guide?
- Are there comments?
- Are the variable names descriptive?
- Are the functions small and do they have a single responsibility?
- Is the code free of magic numbers?
- Is the code free of duplication?
- Are the functions stored in modules with semantic meaning?

You'll probably have to tweak your own code based on your peer's feedback as well. Only merge it once the reviewer approves it.
