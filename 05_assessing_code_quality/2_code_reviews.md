# How to review changes (0:30)

## The Basics

Michael Fagan is credited with the first published, formalized system of code review while working at IBM in the mid-1970'. Nowadays, code reviews live mostly on DevOps platforms like GitHub, GitLab, and Bitbucket - and they have excellent material on how to do them.

This GitHub tutorial shows on how their pull request reviews work and it contains references to other important documents, like managing a PR and defining code owners.

Don't skip it!

[Link to GitHub tutorial](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews)

After this lesson you should:

- Know how to review a pull request.
- How to re-request a review.

## The Advanced

While DevOps have great material on the basics, many companies have their own internal guidelines on how to do code reviews. Google's is one of the most famous and it's a good reference for how to do code reviews. Here they are

[Google's Standard for code reviews](https://google.github.io/eng-practices/review/reviewer/standard.html)

[How to write good code review comments](https://google.github.io/eng-practices/review/reviewer/comments.html)

## Using labels

Most of code review comments are for requesting changes. But not all of them. Sometimes you want to make a suggestion, ask a question, or just make a nitpick. In those cases, it's good to use labels to make it clear what you're doing.

Here are some useful labels to add to your comments:

- **nitpick** - Trivial things and usually related to personal preferences.
- **suggestion** - These are suggestions to improve the code but shouldn't be blocking its approval.
- **question** - It's useful to be super clear when you are asking question vs politely asking for changes.

> Juniors might think their seniors know it all, and a simple question could be mistaken for a request to change something. So they might end up tweaking the code instead of just answering a friendly question.
