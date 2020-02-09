# Vlaamse Programmeerwedstrijd

## How Does The Contest Work

There are 4 categories:

* Cat1: high school students
* Cat2: professional bachelor (you)
* Cat3: academic bachelor
* Cat4: everybody else (master, graduated, ...)

The rules are:

* There are five problems (algorithmic in nature) you need to try to solve in 3 hours.
* Teams must count three members.
* Each team can only use one laptop.
* You can use (almost) any programming language (Java, Python, C++, C#, ...)
* You can solve each problem in a different language, or use the same language for all, etc.
* For each problem, there are a number of test cases it will be required to solve, typically around 100. These cases are fed to the solver using STDIN. Solutions for each case will need to be written to STDOUT.
* For each problem, you are given sample input data and expected output data (`voorbeeld.invoer` and `voorbeeld.uitvoer` respectively.)
* When your solver producing the correct output for the sample data, you can upload it to the contest servers. These contain more input/output, which remains hidden to you. Your submission will be queued for evaluation. A minute or so later, you'll get feedback on how your solver performed.
* If your solver can solve `p`% of the cases correctly, you get `p` points. If it solves 100%, you get 150 points.
* The server imposes a time limit on your code. This time limit seems to change from year to year and fluctuates around 30 seconds. Cat-1 and cat-2 problems are generally not difficult to solve within the time limit: the focus lies on the correctness of the results. For cat-3 and cat-4 problems it is often necessary to find an efficient solution. Inputs can become quite large so as to check that your algorithms have have a certain time complexity.

## Repo Usage

Simply clone the repository: `git clone https://github.com/UCLeuvenLimburg/VPW-opgaves`

If you wish to upload your own solutions, you'll need to ask for write access.

## General Advice

* Writing text to a file/console is relatively slow and it is more efficient to output large blocks of text instead of single characters one at a time. For this reason, it often happens that your output gets stored in a temporary buffer (*caching*), which will get "flushed" only when enough data has been accumulated. This can be a problem at the contest: the server imposes a time limit, and after N seconds it kills the process running your code. This means your program does not get the chance to flush its output. If you are in a situation where the server tells you your program timed out and did not output anything, the caching is the most likely culprit. To remedy this, you need to *flush* your output.
* It might be advisable that you use a programming language that all three members know.
* Develop some small libraries, e.g., functions specialized in reading data from STDIN.

## Language Specific Tips

* [Java](docs/java.md)
* [Python](docs/python.md)
