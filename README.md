## What is this?

This some scruffy sample code. The main purpose here is to learn a) how to use Python type annotations properly,
and b)  understand some of the pylint warnings, and eliminate them. 

Some additional changes to study github actions

## What should I do

Add annotations to the 4 files in src/ to suppress all warnings from mypy and from 
pylin (run as indicated below.

## How to run mypy and pylint

Use conda to install mypy and pylint, and then run

```bash
mypy --strict src/
```

and

```bash
pylint -disable==W,C src/

```
Look at the messages.  There will be quite a few of them. Your task 
is to fix the errors, so that the tools above 
indicate that there are no warnings/errors  left

## Why are we doing this. 

Most projects in the real-world utilize some kind of static analysis. For python projects, 
type checking and linting are very commonly used tools. Each project has it's own way they like
to use these tools. Some projects are very conservative and want no warnings of any sort to appear. 
Some are liberal, and don't care about most warnings. The options given above the ones we're using, it's
a moderate sort of scenario. 

Our desired learning outcome is that doing this project will help you understand about 
how to use typing in python, as well as learn and understand some of the errors produced by linters, 
and how to fix these errors. 


## How do I do this? 

The way real programmers do: google the errors, read the documentation, understand what
the errors mean, and then fix them. You are welcome to work with others, but you MUST submit
your own work. 

Also, we've provided some sample annotations in the DataManager.py file. Use thease as a model. 

## SECRET, REMOVE THIS FROM HOMEWORK TEMPLATE

The main branch contains the homework, the other branch has a solution that doesn't produce
any errors. 
