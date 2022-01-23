## What is this?

This is a project reflecting somecode to manage enrollment that has a partial test set

## What should I do

Add more test cases, to achieve more coverage. YOur grade will be based on how
much coverage you can achieve.

## How to measure coverage

Use conda to install pytest, and then try

```bash
pytest --cov --cov-branch --cov-report term-missing test/
```

## How to increase coverage

Just add more tests! Look at the newCourseTest.py file to see
a sample. Then, read through the source code in the src/ directory,
to get an idea of which parts of the code needs to get tested and add more
tests.

## What if a test fails

Well, that means you're a good tester! Rejoice, and then go on and write
more tests to increase coverage.
done
