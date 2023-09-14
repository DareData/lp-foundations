# Assignment 4: Enums and Text Editors

> Don't forget to create a branch for this assignment.

We want to make sure that we only provide valid values for our countries. This is the perfect scenario to make use of the Enum class.

> **Warning**: This assignment will require you to do a lot of repetitive tasks. This can get annoying fast... _UNLESS_ you make use of VSCode's shortcuts. If you do use them, you will be able to complete this assignment in no time!

## 1- Enums and Shortcuts

Passing a country as a string is not very safe (imprecise types are a code smell). We can use an enum to make sure that we only pass valid countries.

1. Create an `enum.Enum` called `Region` with **ALL** possible region values. You will have to extract the values from the `pandas` dataframe and then copy the result to your `Region` class. Use the most appropriate VSCode shortcut/s that you learned about in the [text editor](../../08_text_editors/2_productivity.md) module to make your job easier!
2. Modify the necessary functions and tests to accept a `Region` instead of a string. Don't forget the type hints.
3. Finally, add a class method to `Region` that returns a list of all the _actual_ countries (so, it removes values like EU28, EFTA, etc). Add a test for this method. Again, make use of as many shortcuts as possible, it will make your life much easier.

## 2- Code Review

As with the previous assignment, a peer should review your code and you will be reviewing the code of a fellow colleague.
