# Ultimate Calculator(know its not ultimate but still) 🧮

This is a command-line calculator we built as a group project while learning
Python. It's not fancy, it's just a program that runs in the terminal and
lets you do math through a menu, instead of typing one line of code every
time you want to calculate something.

We're still learning, so if some of this code looks a bit rough in places,
that's because it is  but it works, and we understood most(if not all) piece of it
before putting it here (mostly by breaking it first, then fixing it 😅).

## What this project actually does

When you run it, you get a menu with three options:

```
===== 📅  Yes,i'm your calculator menu what do you want 🤨 =====
1. Calculator 📠
2. Settings ⚙️
3. Exit 🚫
```

- **Calculator** takes you to a menu of math operations (Add, Sub, Mul, Div,
  and a few others like Log and Exp that we had to look up before we
  understood them).
- **Settings** lets you change how many decimal places show up in your
  results (like `40.00` vs `40.0000`).
- **Exit** closes the program.

At basically any prompt, you can type `quit`, `q`, `exit`, or `e` and it'll
cancel whatever you were doing instead of forcing you to finish it.

## A feature we're kind of proud of: 

If you just calculated something, the next time you go to calculate again,
it'll ask if you want to reuse that previous result instead of typing it all
over again — and it'll even let you choose whether it goes in as the first
number or the second number. This one took us a while to actually get
working properly, so it's the part we understand the best now.

## How to run it

You need Python installed (we used Python 3). Then, from inside the project
folder, run:

```
ultimate_calc.py which serves as the main.py
```

(or `python3 main.py` depending on your computer)

Then just follow the menus — type a number and press Enter.

## How the project is organized

We didn't put everything in one giant file, because you(our instructor)
explained that splitting things up makes it easier to work on as a group
(and honestly, easier to find bugs too). Here's what each file is
responsible for, in plain terms:

| File | What it's for, in simple words |
|---|---|
| `main.py` | The starting point. This is the file you actually run. It just shows the main menu and decides whether to go into the Calculator or Settings. |
| `display.py` | Everything that gets printed to the screen menus, results, and the ℹ️/⚠️/🚫/✅ messages. This file never asks the user anything, it only shows things. |
| `inputs.py` | Everything that asks the user something and checks the answer is valid like making sure a "number" input is actually a number, and catching if someone types `quit`. |
| `arithmetic.py` | The actual math add, subtract, divide, log, etc. These functions just take numbers in and give a number back (or raise an error if something's wrong, like dividing by zero). |
| `state.py` | The "memory" of the app it remembers the last result you calculated, your decimal places setting, and whether you chose to reuse a previous result. Without this file, the calculator would forget everything the moment you moved to a new screen. |
| `routines.py` | The file that actually connects everything above. It's the one that decides "ask for a number, then do the math, then show the result" in the right order. |

## few Things we learned building this

- Splitting code across files only works if everyone agrees on function
  names *before* building, otherwise nothing connects properly.
- A function can only take the exact number of arguments it was written
  for  we broke this rule with our `Exp` function at first (it was written
  for 2 numbers when it should've only needed 1) and had to go back and fix
  both the function itself and the code that calls it.
- Small typos (like a missing underscore in a variable name) cause real
  errors, and Python's error messages actually tell you what it *thinks* you
  meant worth reading them properly instead of panicking.
- Not every red underline in VS Code means the code is broken. Some of them
  are just the editor being extra cautious (we still don't fully understand
  all of that, but the program runs fine, so that's what mattered).

## Known limitations

- If you enter something that isn't a number, it'll ask you again rather
  than crashing but it doesn't remember what you were in the middle of
  doing before that mistake.
- Settings currently only lets you change decimal places, since that's the
  only setting the project asked for.


