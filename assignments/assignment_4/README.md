# Assignment 4: OOP and VSCode Shortcuts

The focus of this assignment is about OOP. In particular, we want to make sure that we only provide valid values for our countries. This is the perfect scenario to make use of the Enum class. Note that this is a special case of classes since they are rarely instantiated. 

But going beyond that, our goal is to create the most annoying assignment ever written. The twist is that there is an easy way out: VSCode shortcuts.

> Don't forget to create a branch for this assignment.

## 1- Enums and Shortcuts

Passing a country as a string is not very safe (imprecise types are a code smell). We can use an enum to make sure that we only pass valid countries.

1. Create an `enum.Enum` called `Country` with possible country values. The idea behind this step is to find the most appropriate VSCode shortcut/s that you learned about in the [text editor](../../07_text_editors/README.md) module. 
2. Modify the necessary functions and tests to accept a `Country` instead of a string. Don't forget the type hints.
3. Finally, add a class method to `Country` that returns a list of all the _actual_ countries (so, it removes values like EU28, EFTA, etc). Add a test for this method. Again, make use of as many shortcuts as possible, it will make your life much easier.