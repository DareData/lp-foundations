# Clean Code

Let's continue our journey to write better code. In this module we will focus on the how to write comments and name things. Naming things is one of the hardest things in programming, and it's also one of the most important. We will also learn how to add type hints to our code, and how to use a static type checker.

## Uncle Bob - Clean code lesson 2 (1:06)

![Junior dev writing comments](../../images/junior-devs-writing-comments.png)

[Link to video](https://www.youtube.com/watch?v=2a_ytyt9sf8)

In the second part of the "Coding Better World Together", Uncle Bob focuses on the clean code rules for comments and rules to write names.

After this lesson you should:

- Understand what kinds of comments to write,
- Know about _lying comments_ and when _not_ to write comments,
- Be able to reveal your intent while naming things.

## Python Type Checking (Guide) (1:00)

![RealPython cover](../../images/4b3cc00ea7b463fb46c2dfbe07beab3d6e708384e6938b82cc3e4f65767da9e2.png)  

[Link to RealPython guide](https://realpython.com/python-type-checking/)

This is a very complete guide on Python type hints from _RealPython_. It's a comprehensive guide that covers a lot of ground and a good piece to keep for future reference.
Type hints are optional in Python, but using them will allow you to catch bugs before they happen, and allow readers to understand your classes and functions just by looking at their signatures.

After this lesson you should:

- Learn how to add type hints to your code,
- Be able to create type aliases,
- Know how to run a static type checker like `mypy`.

Nowadays, VSCode usually comes with a type checked installed by default. But the button to activate is easy to miss. If you have a type checker installed, you should see a button like this one on the bottom bar of your VSCode window:

![<img src="../../images/activate_type_checking.png" alt="Activate type checking on VSCode" width="300"/>](../../images/activate_type_checking.png)

Now you should see the errors and warnings in your code in the "Problems" tab (it sits next to your integrated terminal window). Personally, I like to use the [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens) add-on to make the errors and warnings more visible:

![Error Lens add-on](../../images/error_lens.png)

## Extra resources

- [Virtual environments](virtual_environments.md) - If you are curious about how virtual environments work, you should definitely see this article from RealPython.
