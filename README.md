## What is this?

This some scruffy sample code. The main purpose here is to learn how to use Python annotations properly,
and also remove any warnings from pylint. 

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
to use these tools. The options given above the ones we're using. 

Doing this project will help you understand about how to use typing in python, as well as learn
and understand some of the errors produced by linters. 

## How do I do this? 

The way real programmers do: google the errors, read the documentation, understand what
the errors mean, and then fix them. You are welcome to work with others, but you MUST submit
your own work. 

Also, we've provided some sample annotations in the DataManager.py file. Use thease as a model. 

