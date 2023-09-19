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
- Is there anything really cool your peer did? _Give them a compliment!_

You'll probably have to tweak your own code based on your peer's feedback as well. Only merge it once the reviewer approves it.

### About the code review

The reviewer will only have access to code that's different from the `main` branch. This means that the reviewer will not be able to see the code from the previous lesson. Because this is the first contact the reviewer will have with your repository, it might be useful for the reviewer so see all your code. You can do this by creating a second pull request to an empty branch. This is how you can do it:

1. Create an empty branch called `empty_branch`:

    ```bash
    git checkout --orphan empty_branch
    git rm -rf .
    git commit --allow-empty -m "root commit"
    git push origin empty_branch

    git checkout refactoring
    git merge empty_branch --allow-unrelated-histories
    git push origin refactoring
    ```

2. Create a pull request from `refactoring` to `empty_branch`.
3. Assign a colleague to review your code.
4. After the review, merge the pull request.
5. Finally a pull request from `refactoring` to `main` or simply merge the `refactoring`.


# Assignment 2: Project Structure

We know that the things presented in the previous modules are orientative guidelines and real-life scenarios will slightly differ based on the project's specific needs. However, it is not uncommon to unnecessarily deviate too much from these.

## 1- Project restructuration

This exercise is very simple, we just want you to fish out some current or older project that you are or were part of and review its organization. What would you change? What would you keep? Why? 


## 2- Structure analysis

<<<<<<< HEAD
In collecting a couple of examples for the project structure module we made a mess and lost track of the structure each of the projects. Give it a go and see if you can figure out which patterns do these projects follow.

[Link to mysterious project 1](https://github.com/qiuyu96/CoDeF/tree/main)

[Link to mysterious project 2](https://github.com/RoberVega/mysterious_project_2)

[Link to mysterious project 3](https://github.com/RoberVega/mysterious_project_3)

[Link to mysterious project 4](https://github.com/cookiecutter/cookiecutter/tree/main)


# Assignment 2: code exploration using a debugger

The last part of this assignment is easy, but very important. One of the most common scenarios is to stumble upon code you have not written yourself. Especially when facing big projects, this might come across as a daunting task. Fortunately, debuggers come to the rescue! One of the possible use cases for debuggers is understanding a new piece of code, especially for studying its intricacies and connections. By introducing strategic breakpoints, one can understand the intended flow of the project and the different parts it is composed of.

That situation takes us to our next exercise: in the next module, we will focus on testing. But first, we would like you to use a debugger to try to understand how the current testing code actually works, what is being called, etc.
=======
Let's practice your ability to navigate projects you have not written yourself. 
- How would you go about understanding the different components of a project for the first time? 
- What if you are looking for a specific feature, class, function, _etc._? How would you proceed then?

Enough chitchat, let us get our hands dirty! Your mission is to understand the structure of two of the most popular python libraries and a bonus repository with a scientific project:
- [requests](https://github.com/psf/requests/tree/main),
- [scikit-learn](https://github.com/scikit-learn/scikit-learn/tree/main),
- [CoDeF](https://github.com/qiuyu96/CoDeF/tree/main). 

By understanding we mean a very simple task: prepare a brief general description of the purpose of the library _just by looking at its folder structure_:

1. Can you identify the main folders? Without looking at the code (you can only look inside other folders) what is their purpose?
2.  Where is the main script of the package located? 
>>>>>>> origin/main
