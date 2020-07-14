# Blackjack Game

You are going to build a blackjack card game in Python.

Every card in blackjack has a suit, rank, and value. For example, the king of hearts has a rank of "king", a suit of "hearts", and a value of 10 (In blackjack, face cards are worth 10).

## 10. Create a string variable

### 10.1

Let's represent the king of hearts with Python code. Variables store data. The code already has a variable named `suit` that is set to the value of "hearts". Add a variable named `rank` and set it to the value of "K" (for king).

#### HINTS

- Check your spacing and capitalization.
- Spelling must be exact.

## 20. Create a number variable

### 20.1

When variables are set to equal a string, the string should be surrounded by quotation marks. If a variable equals a number, quotation marks are not used around the number. Add a variable named `value` and set it to 10.

#### HINTS

- Numbers don't need quotation marks around them.
- Check your spacing and capitalization.


## 30. Print to console

### 30.1

The code `print("Hello world")` calls the `print()` function and prints the text "Hello World" to the console. Print the the text "Your card is:" to the console.

#### HINTS

- Make sure you are printing this string exactly: "Your card is:"
- The string must be in quotation marks and inside parenthesis.

## 40. Run the blackjack.py file

### 40.1

Most of the time you will be typing into the `blackjack.py` file window. When you want to run your program you will have to type into the terminal window. To run your code so far, enter `python blackjack.py` into the terminal and press enter.

For terminal tests to work, you will have to run the following line once before any other commands: `source ~/.bashrc`

#### HINTS

- Make sure you're in the `project` folder. 

## 50. Print a variable

### 50.1

Instead of passing in a string to the `print()` function (i.e. "Your card is:"), you can also pass in a variable and the value of the variable will print to the console. On a new line, print the value of the `rank` variable to the console.

#### HINTS

- The code should have two print statements. The first should print "Your card is:" and the second should print the rank variable.
- The variable name should not have parenthesis around it.

## 60. Concatenate strings with +

### 60.1

The `+` operator can concatenate strings and/or variables together. Update your code so that the `print()` function is only called one time. It should print the following text to the console, using a variable for the rank: "Your card is: K"

#### HINTS

- This code will print "Name: Quincy" to the console.  
```  
name = "Quincy"  
print("Name: " + name)  
```  
- Make sure there is a space after the colon inside the string.

## 70. Concatenate multiple strings

### 70.1

You can concatenate as many strings and variables as you want. Update your code so that the `print()` function prints the following text to the console, using variables for the rank and suit: "Your card is: K of hearts".

#### HINTS

- Make sure you include the appropriate spaces in your strings.

## 80. Create a list

### 80.1

You can use a list in Python to store multiple values or items at a time. Here is an example of a list of strings: `place = ["first", "second", "third"]`. Above the `suit` variable, create a `suits` variable and assign it to a list of suits (spades, clubs, hearts, diamonds).

#### HINTS

- There should be quotation marks around each element in the list.
- Make sure to add a closing bracket at the end (`]`).

## 90. Access list items

### 90.1

The bracket operator can be used to access a specific element in a list. The number inside the bracket specifies the index of the list to access (indices start at 0). For example, the following code prints "first" to the console:
```py
place = ["first", "second", "third"]
which = place[0]
print(which)
```
Update the `suit` variable so that the value of "clubs" comes from the `suits` list.

#### HINTS

- The second item in a list is at index 1.

## 100. Create a for loop

### 100.1

You can use a `for` loop go through each item in a list:

```py
friends = ["Kris", "Tom", "Oliver"]
for friend in friends:
    print(friend)
```

The above code goes through each item in the `friends` list, stores the value in the `friend` variable on each iteration, then prints it. Add a `for` loop to the end of your code that prints each suit.

#### HINTS

- Indent the `print` statement in the `for` loop four spaces.
- Make sure there is a colon at the end of the `for` loop.

## 110. Append to a list

### 110.1

Let's add another item to the `suits` list, just to see how it works. You can add a new value at the end of a list with `append`. For instance, here is how to add a new name to the `friends` list: `friends.append("Beau")`. Add the string "snakes" to the end of the `suits` list using `append`. Add the new line of code before the `for` loop so the loop will print the list with the new element.

#### HINTS

- Use `suits.append()` and put the item to append in the parenthesis.
- If your code is not working, try running your code to see what it does.

## 120. Refactor code

### 120.1

Now you will start the process of representing a full deck of cards with Python code. Keep the first line and the last two lines but delete everything else. It won't be needed for the deck. Changing or improving previously written code is called refactoring.

#### HINTS

- Your code should look like this now:  
```py  
suits = ["spades", "clubs", "hearts", "diamonds"]  
for suit in suits:  
    print(suit)  
```

## 130. Create a list of ranks

### 130.1

You have the list of suits. After that line create a list of ranks. (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K)

#### HINTS

- Make sure to surround each item with quotation marks.

## 140. Create an empty list

### 140.1

Before the `suits` list, create a new variable called `cards` and assign an empty list (`[]`) to the variable.

#### HINTS

- Nothing should be inside the brackets.

## 150. Print a list in a loop

### 150.1

In the `cards` list, there should be an item for each card in the deck. Each item in the `suits` list should be combined with each item in the `ranks` list for a total of 52 items (cards). We'll work our way up to that. Update the `print` statement in the `for` loop so that it prints a list with two elements. The first element should be `suit` and the second should be the first element of the `ranks` list. This will print an ace ("A") in every suit.

#### HINTS

- The first element in the `ranks` list is at index 0.
- Do not put quotation marks around any element in the list.

## 160. Create nested for loops

### 160.1

Now, instead of just printing an ace in every suit, let's print every rank in every suit. This can be done easily with a `for` loop nested within another `for` loop. Inside the `for` loop, add another `for` loop that loops through the `ranks`. The `print` command should then be inside the second `for` loop instead of the first `for` loop (the `print` command should be indented 8 spaces from the beginning of the line, instead of 4).

#### HINTS

- Pay special attention to how everything is indented.

## 170. Access items from nested loops

### 170.1

If you run the code by typing `python blackjack.py` in the terminal, you will see that it isn't quite what we want. It doesn't print all the ranks because the print command specifies the exact same rank in every iteration. Change `ranks[0]` to `rank`.

## 180. Append items from nested loops

### 180.1

Great! Now all 52 cards are printed as two-item lists. An element in a list can be another list. Instead of printing 52 two-item lists, `append` those 52 lists to the `cards` list.

#### HINTS

- Just change `print` to `cards.append`.

## 190. Print cards

### 190.1

Check what the `cards` list looks like by printing it out at the end of your code. If you run the code by typing `python blackjack.py` in the terminal, you can see the result. Remember, run the code by typing `python blackjack.py` into the terminal.

#### HINTS

- Add `print(cards)` as the last line.

## 200. Import a module

### 200.1

You may notice that all the cards are in order in the `cards` list. For a game like this, the cards must be shuffled. To help with this, add `import random` as the first line in your code. This imports the `random` module, which contains a variety of things related to random number generation. When you import a Python module, it allows you to use additional commands in your code.

#### HINTS

- Only add the line `import random`. Make sure it is the first line in your program.

## 210. Use the random.shuffle() function

### 210.1

Now you can call the `random.shuffle()` function. Call that function right above the `print` command and put `cards` in between the parenthesis to pass the `cards` list into the function. If you run your code afterwards, you should notice that the cards have been shuffled.

#### HINTS

- When `cards` is passed in to the function, the code will look like this: `random.shuffle(cards)`

## 220. Use pop to remove an item from a list

### 220.1

Let's remove a single element from the `cards` list. This is similar to dealing a card from a deck. This can be done with the `pop` method. Consider this code:
```py
people = ["abbey", "mrugesh", "miya"]
person = people.pop()
```
After running that code, `person` equals "miya" and `people` equals `["abbey", "mrugesh"]`.
After shuffling the cards, remove the last item from the `cards` list and store it in a variable named `card`.

#### HINTS

- Remove the last item in the `cards` list with `cards.pop()`.

## 230. Define a function

### 230.1

When you call the `random.shuffle()` function, the program is running a sequence of statements (i.e. lines of code) to performs a computation. You can't see the sequence of statements but they are there inside the `random` module. You can create your own functions that will run the same sequence of statements every time they are called. Here is an example of how to define a function called `greeting` that prints "Hi" every time it is called (`def` is short for "define").
```py
def greeting():
    print("Hi")
```
Put the line that shuffles the cards into a function called `shuffle`.

#### HINTS

- Lines indented underneath a function definition are inside the function. Make sure the line `random.shuffle(cards)` is indented four spaces underneath the function definition.
- Define the shuffle function like this: `def shuffle():`

## 240. Call a function

### 240.1

Right before the `print` statement, call the `shuffle` function. The code inside a function will not run until it is called. Here is how you would call a function named "greeting": `greeting()`

#### HINTS

- Call the shuffle function with `shuffle()`.
- Make sure to call the function right before the `print` statement.

## 250. Print a list in a loop

### 250.1

Create a function named `deal` and put the line `card = cards.pop()` into the function.

#### HINTS

- Define the `deal` function like this: `def deal():`.
- Make sure to indent the line `card = cards.pop()` right after the function definition to put the line inside the function.

## 260. Return a value from a function

### 260.1

Variables can only be accessed in the context they were created. The `card` variable will not be available outside of the `deal` function. You can get a value out of a function by returning a result using the `return` statement. At the end of the `deal` function add `return card`. Every line in a function must be indented the same number of spaces (in this case, 4 spaces).

#### HINTS

- Make sure `return card` is indented correctly.

## 270. Assign a returned value to a variable

### 270.1

After the `shuffle` function is called, call the `deal` function and assign the returned value to a variable named `card`. Then update the `print` function to print `card` instead of `cards`.

#### HINTS

- You can call the `deal` function and assign it to variable `card` all with one line with `card = deal()`.

## 280. Add an argument to a function

### 280.1

What if you want the `deal` function to deal more than one card? Let's refactor the `deal` function to accept an argument. Any number of arguments can appear inside the parentheses when a function is created, separated by commas. Inside the function, the arguments are assigned to variables called parameters. Here is an example of a function that takes an argument:
```py
def print_twice(bruce):
    print(bruce)
    print(bruce)
```
This function assigns the argument to a parameter named `bruce`. When the function is called, it prints the value of the parameter (whatever it is) twice. Make it so the `deal` function takes an argument named `number`. Then, call the function with the new parameter by updating the last two lines of your code to:
```py
cards_dealt = deal(2)
print(cards_dealt)
```

#### HINTS

- Put the word "number" inside the parenthesis of the `deal` function definition.
- Make sure to replace the last two lines of the program with the given code.

## 290. Return a different value from a function

### 290.1

The `deal` function is now going to return a list of cards instead of a single card. In the first line of the function create an empty list named `cards_dealt`. Then update the last line of the function to `return cards_dealt`.

#### HINTS

- Here is how to create an empty list: `cards_dealt = []`.

## 300. Use the range function in a for loop

### 300.1

The `range` function can be used in a `for` loop to determine the number of loops. The following code will print "Hi" six times:
```py
for x in range(6):
    print("Hi")
```
Put the line `card = cards.pop()` into a for loop that also `append`s the `card` onto the `cards_dealt` list. The loop should run the amount of times equal to the `number` parameter.

#### HINTS

- Make sure every line in the `for` loop is indented four spaces.
- Inside the `for` loop add these lines:  
```py  
card = cards.pop()  
cards_dealt.append(card)  
```

## 310. Store first item from list in a variable

### 310.1

Let's separate out a single card from the two cards dealt. At the end of your code create a variable called `card` and set it equal to the first item in the `cards` list. Then print the card.

#### HINTS

- To access a certain item in a list, use brackets at the end of the list name with the index number inside the brackets.
- The index number for the first item in a list is zero.

## 320. Get the rank from a card

### 320.1

Let's separate out the rank part of the single card. After the line where the variable `card` is created, create a variable named `rank` and assign it the rank from `card`. 

#### HINTS

- The rank is at index 1.

## 330. Create an if statement

### 330.1

Each rank has a different value. The value of "A" is 11 (or sometimes 1, but we'll get to that later). "J", "Q", and "K" have the value of 10. The numbers have the value of the number. You need to check what the rank is and set the value depending on the rank. This is the perfect time for a conditional statement, specifically, an `if` statement. Here is an example:
```py
if x == y:
    print('x and y are equal')
```
That code will only print 'x and y are equal' IF the variables names `x` and `y` are equal to the same value. Take special note of the double equal sign (`==`). This is used to check if two values are equal. Make sure not to confuse it with a single equal sign (`=`), which is used to assign a value to a variable. 

Before the `print` statement, add an `if` statement to check if `rank == "A"`. If so, assign 11 to a variable named `value`.

#### HINTS

- Make sure to indent the line inside the `if` statement four spaces.
- Add a colon at the end of the `if` statement.

## 340. Add an elif statement

### 340.1

If `rank` does not equal "A", you'll want to check if it equals "J", "Q", or "K". That can be done with `elif`, which is an abbreviation of “else if.” For example:
```
if age < 13:
    print("You are a kid")
elif age > 17:
    print("You are an adult")
```
Notice in that example that you can use the greater than (`>`) and less than (`<`) signs in conditional statements. Some other comparison operators include `=!` (not equal to), `<=` (less that or equal to), and `>=` (greater than or equal to).

After the `if` statement, add the line `elif rank == "J":`. Then inside the `elif` statement assign 10 to `value`.

#### HINTS

- `elif` should be indented the same amount as `if`.

## 350. Use logical operators

### 350.1

There are three logical operators: `and`, `or`, and `not`. You can use these operators in conditional statements to check multiple conditions at once. Update `elif rank == "J":` to `elif rank == "J" or rank == "Q" or rank == "K":`.

#### HINTS

- If you want to use `and` or `or`, there should be a full conditional on either side. For example, use `rank == "J" or rank == "Q"` and NOT `rank == "J" or "Q"`.

## 360. Add an else statement

### 360.1

There can be any number of `elif` statements after an `if` statement. At the end, there can be an `else` statement. The block of code in an `else` statement executes if the `if` and all `elif` statements evaluate to `False`. Here is an example:
```
if age < 13:
    print("You are a kid")
elif age > 17:
    print("You are an adult")
else:
    print("You are a teenager")
```
After the `elif` statement, add an `else` statement. Inside, assign `rank` to `value`.

#### HINTS

- An `else` statement should not have a conditional in it.

## 370. Add a print statement and run your code

### 370.1

Update the `print` statement at the end to `print(rank, value)`. Then try running the code a few times. You should see a different result each time. (Note: When multiple values in a print statement are listed with a comma separating them, both values are printed with a space in between.)

#### HINTS

- Run your code by typing `python blackjack.py` into the terminal.

## 380. Create a dictionary

### 380.1

A Python dictionary is like a list, but more general. You can think of a dictionary as a mapping between a set of indices (which are called keys) and a set of values. Each key maps to a value. The association of a key and a value is called a key-value pair or sometimes an item. Here is a dictionary that maps from English to Spanish. They keys are the English words and the values are the Spanish words.
```py
eng2sp = {"one": "uno", "two": "dos", "three": "tres"}
```
Above the `print` statement, create variable called `rank_dict` and assign to it this dictionary: `{"rank": rank, "value": value}`.

## 390. Access an item in a dictionary

### 390.1

```py
eng2sp = {"one": "uno", "two": "dos", "three": "tres"}
print(eng2sp["one"])
```
The code above will print "uno". Just like you access an item in a list by specifying the index inside `[]`,  you can access an item in a dictionary by specifying the key inside `[]`. Update the `print` statement so that you are accessing the rank and value from `rank_dict` instead of directly from the variables.

#### HINTS

- You cannot use an index number to specify an item in a dictionary.
- Make sure to put quotes around the key inside the brackets.
- Here is the line of code to use: `print(rank_dict["rank"], rank_dict["value"])`

## 400. Delete code after shuffle()

### 400.1

When writing a program, there are many ways to do almost everything. Now you will refactor your code to get the value of each rank without using an `if` statement. Instead, you will store both the rank name and value in the `ranks` list using dictionaries. Delete all the lines of code after `shuffle()`.


