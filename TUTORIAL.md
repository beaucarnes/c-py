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

## 410. Deal and store a card in a variable

### 410.1

Get a single card *not* in a list by adding the following line at the end of your code: `card = deal(1)[0]`.

#### HINTS

- Add the exact line of code given at the end of your code.

## 420. Create a list of dictionaries

### 420.1

Now, update the `ranks` list. Each element in the list should be a dictionary. When lists or list elements are long, it is common to put each element on it's own line. Here is the beginning of the new `ranks` list:
```py
ranks = [
        {"rank": "A", "value": 11},
        {"rank": "2", "value": 2},
        {"rank": "3", "value": 3},
        ...
    ]
```
Update `ranks` in your code using the section above as a starting point. Replace "..." with the other ranks and values. 

#### HINTS

- "J", "K", and "Q" have a value of 10 and the numbers have the value of the number.
- There should be 13 dictionary elements in the list, one for each rank.

## 430. Print a single card

### 430.1

At the end of your code, print `card`. Try running your program to see what prints now that you have updated the `ranks` list.

#### HINTS

- Add `print(card)` as the last line in your code.

## 440. Access a dictionary value inside a list

### 440.1

If you want to get just the rank of `card`, you will first have to access the second element in the list, then you will have to access the `"rank"` item in the dictionary. Because you are accessing something two times, there will be two sets of brackets. Look at this example:
```py
card = ["clubs", {"rank": "J", "value": 10}]
rank = card[1]["rank"]
```
In that code, `rank` now equals "J". Think about the code until you understand why.
Update your code so the `print` statement will print just the "value" in `card`.

#### HINTS

- The example given shows how to access the "rank" in `card`. Use a similar line of code to access the "value" in `card`.

## 450. Create a Deck class

### 450.1

Now you will start defining classes that will be used in order to separate out different aspects of the game. Classes provide a way of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. An object can contain a number of functions (which we call methods) as well as data that is used by those functions (called attributes). You will use classes to model three parts of the game: Card, Deck, and Hand. So far, you've mainly worked on elements of the `Deck` class.

Right after the `import` statement at the top, add this line: `class Deck:`. Then, highlight all the code after that line and hit the "Tab" key on your keyboard. This will indent all the code and make it part of the `Deck` class.

After creating the `Deck` class, remove the unneeded code in the class by removing the last three lines of code (starting with the line `shuffle()`)

#### HINTS

- The `import` statement and `class Deck:` should not be indented. All other lines should be indented four spaces.

## 460. Create an __init__ method

### 460.1

A class is like a template. You can use that class to create an instance of the class, called an object. Then you can use the instance. Each instance keeps it's own state so you can update an instance created from a class and it won't impact other objects created from the same class. Soon, you will see an example of what all this means so it will be easier to understand.

First, let's prepare our class to create an instance from it. When you create an instance of a class, Python automatically calls a function (also called a method) in the class named `__init__`. The contents of this method should be code that is run one time to initialize the instance. Define this function by adding the following line of code directly under `class Deck:`: `def __init__(self):`. Now indent all the code that is not part of the `shuffle` or `deal` functions so the code will be part of this new function.

#### HINTS

- Run your code by typing `python blackjack.py` into the terminal.

## 470. Add self argument to functions in class

### 470.1

Notice the word "self" in the parenthesis of the function you just added. When defining a function, anything inside the parentheses is called an argument. These are variables passed in from the caller to the function. All functions in a class should receive `self` as an argument. `self` represents the instance of the class. By using the `self` keyword, the function can access the attributes and methods of the class. For example, this would allow you to call the `shuffle` function from within the `__init__` function. Add the `self` as the first item inside the parentheses on the definitions of the `shuffle` and `deal` functions. 

#### HINTS

- The `shuffle` function should start like this: `def shuffle(self):`.
- The `deal` function should start like this: `def deal(self, number):`.

## 480. Create instance variables with self

### 480.1

If you look at the variables defined inside the `__init__` function, only `cards` is used in other functions. Inside a class, in order to access a variable in multiple functions (also called methods), the variable has to start with `self.`. Change all instances of `cards` in every function to `self.cards`. 

## 490. Create a Deck instance

### 490.1

You can now create an instance (also called object) of the deck class. At the very end of your code add the line `deck1 = Deck()` (with no indentation).

## 500. Access an attribute of an instance

### 500.1

If you have an instance of a class named `car` with an attribute named `model`, you can access the value of the attribute with `car.model`. In your code, `cards` is an attribute of the `deck1` instance created from the `Deck` class. Print the `cards` attribute. 

## 510. Create a second Deck instance

### 510.1

If you run the code now, you should see the `cards` list from `deck` with the cards in order. You already created an instance of the `Deck` class called `deck1`. Underneath that and before the `print` statement, create another instance of the `Deck` class called `deck2`.

## 520. Call a method of an instance

### 520.1

If you have an instance of a class named `car` with an method named `drive`, you can call the method with `car.drive()`. In your code, `shuffle` is a method of the `deck2` instance created from the `Deck` class. Call that method right before the `print` statement.

#### HINTS

- Call the method with `deck2.shuffle()`.

## 530. Print cards attribute from deck2 

### 530.1

At the end of your code, print the `cards` attribute from the `deck2` instance. If you run the code, you will see that the order of the `cards` list is different each time it is printed. That is because each instance stores the state of it's variables separately. In the `deck2` instance, the cards were shuffled. In the `deck1` instance, the cards were not shuffled.

## 540. Add if statement inside deal function

### 540.1

The `Deck` works. Now let's add safeguards to prevent errors. When the`deal` function is called, a card is removed from the `cards` list. You can only remove a card if there are cards to remove. So before the program tries to `pop()` a card off of `self.cards`, it should check `if` the length of `self.cards` is greater than (`>`) 0.  You can get the number of items in a list with `len()`. Here is an example: `len(self.cards)`. In the `deal` function, put all the code that is in the `for` loop inside the appropriate `if` statement.

#### HINTS

- The following lines in the `for` loop should be inside the `if` statement:  
```  
card = self.cards.pop()  
cards_dealt.append(card)  
```
- The `if` statement should look like this: `if len(self.cards) > 0:`

## 550. Add if statement inside shuffle function

### 550.1

A deck with only one card does not need to be shuffled. Add the appropriate `if` statement to the `shuffle` function.

#### HINTS

- The `if` statement should check if `len(self.cards) > 1`.

## 560. Create a Card class

### 560.1

Since a "Card" is a separate concept than a "Deck", next you'll make a `Card` class. Using the `Deck` class as an example, create a `Card` class above the `Deck` class. Add an `__init__` function and inside that function set `self.suit` to equal "hearts".

#### HINTS

- Check the indentation. The `__init__` function should be indented four spaces and the code inside the function should be indented four more spaces.

## 570. Create the self.rank variable

### 570.1

Also inside `__init__`, create a variable called `self.rank` and set it to "A".

## 580. Initialize an object with parameters

### 580.1

Currently, anytime a `Card` is created, it will be an Ace of Hearts. Refactor the code so the `suit` and `rank` are specified when a `Card` object is constructed. The `__self__` method can take additional parameters (besides `self`) that are passed into it as the object is constructed. Here is an example of a `Person` class where the `name` and `age` are specified when an object is constructed:
```py
class Person:
   def __init__(self, name, age):
     self.name = name
     self.age = age

sally = Person("Sally", 32)
print("Name: " + sally.name + ", Age: " + sally.age)
```
That code prints out "Sally 32".

#### HINTS

- The `__init__` function should start like this: `def __init__(self, suit, rank):`.
- Set `self.suit` and `self.rank` to the parameters `suit` and `rank`.

## 590. Create a __str__ method

### 590.1

When a class has a `__str__` method, it is called when `print()` is invoked on an object from the class. In the `Card` class, add a `__str__` method. Inside the method add `return self.rank['rank'] + " of " + self.suit` to return what should display when a card is printed.

#### HINTS

- The `__str__` method should start like this: `def __str__(self):`.

## 600. Add code to test out the __str__ method

### 600.1

Try out the new `__str__` method. Delete the last five lines in the code (everything after the `Deck` class). Add the following lines:
```py
card1 = Card("diamonds", {"rank": "A", "value": 11})
card2 = Card("spades", {"rank": "5", "value": 5})
print(card1)
print(card2)
```

## 610. Add an f-string

### 610.1

F-strings allow you to include variables inside of strings so you don't have to concatenate the strings. Here is how you would create an f-string with the variables `name` and `age` inside: `f"My name is {name} and I am {age} years old"`. Notice it begins with "f" and the variables are within curly braces. Update the return statement in `__str__` to use an f-string.

#### HINTS

- `__str__` should return `f"{self.rank['rank']} of {self.suit}"`.

## 620. Append an instance of a class to a list

### 620.1

Currently, in the `Deck` class, the last line of the `__init__` method appends a list as an item to the `cards` list. Instead of appending the list (`[suit, rank]`), create and append an instance of the `Card` class (`Card(suit, rank)`). Afterwards, when a `Deck` is created, it is filled with `Card`s.

#### HINTS

- Here is the line that should be modified: `self.cards.append([suit, rank])`
- Replace `[suit, rank]` with `Card(suit, rank)`

## 630. Create a Hand class

### 630.1

The `Deck` and `Card` classes could be used for any card game. Now make a `Hand` class after the `Deck` class. This will represent a hand in the game of blackjack. Add a `__init__` method inside the `Hand` class that initializes a variable called `self.cards` that is set to an empty list. Remove the lines of code at the end that are not in a class.

#### HINTS

- The first three lines of the `Hand` class should look exactly like the `Deck` class, except for the class name.
- Make sure to remove the extra lines of code at the end that are not in a class.

## 640. Create a value variable

### 640.1

Besides keeping track of the `cards`, `Hand` should also keep track of the `value`. Under `self.cards`, create `self.value` and set it to 0.

#### HINTS

- Verify the indentation is correct. The new line should be indented 8 spaces from the beginning of the line so it is in the `__init__` method.

## 650. Add a dealer parameter

### 650.1

In this blackjack game, there will be a human-controlled player and a program-controlled dealer. Add a `dealer` parameter in the `__init__` constructor method of the `Hand` class. When a `Hand` object is created, `dealer` should be set to `True` of `False` to keep track of what type of hand it is.

#### HINTS

- Inside the parentheses of the `__init__` method should be `self, dealer`.

## 660. Assign dealer parameter to a variable

### 660.1

Inside the `__init__` method, create a `self.dealer` variable and set it equal to the `dealer` parameter.

#### HINTS

- Check the indentation.

## 670. Add a default value to a parameter

### 670.1

Function parameters can have default values. Change the parameters `(self, dealer)` to `(self, dealer=False)`. That code sets the default value of `dealer` to `False`. That means a `Hand` object can be constructed with or without passing in the value of `dealer`.

## 680. Create an add_card method

### 680.1

Now a `Hand` can be created. Let's give it some functionality. Add an `add_card` method. The method should take a `card_list` as a parameter. Inside the method, add `self.cards.extend(card_list)`. `extend` will append each item in the `card_list` list onto `cards` (`append` would append the full `card_list` list as a single item onto `cards`).

#### HINTS

- Make sure the first parameter in the `add_card` method is `self`.

## 690. Add code to test out Deck and Hand class

### 690.1

Try out your code so far by adding the following lines of code to the bottom:
```py
deck = Deck()
deck.shuffle()

hand = Hand()
hand.add_card(deck.deal(2))
print(hand.cards)
```

#### HINTS

- Just copy and paste the lines of code into the end of your program

## 700. Create calculate_value method

### 700.1

Now add the ability to calculate the value of a hand. Add a method called `calculate_value` to `Hand`. Inside the method, set `self.value` to 0 since you will add all the values in the hand to this variable.

## 710. Add an f-string

### 710.1

Inside the `calculate_value` method, loop through each card in `self.cards` and get the value of the card. You can do that by adding the following code:
```py
for card in self.cards:
    card_value = card.rank["value"]
```

#### HINTS

- Just copy and paste the code into the end of the `calculate_value` method.

## 720. Convert to an integer with int()

### 720.1

`int()` is used to convert strings to integers. For example: `int("2")` will convert the string `"2"` to the integer `2`. Make sure `card.rank["value"]` is an integer by putting it inside `int()`.

#### HINTS

- Put `card.rank["value"]` inside the parenthesis of `int()`.

## 730. Add a value to a variable with +=

### 730.1

Just getting `card_value` for each card is not enough. Something must be done with that variable. The `+=` operator will add a value to a variable. For example:
```
num = 10
num += 5
```
In the code above, `num` now equals 15. Inside the `for` loop, use the `+=` operator to add `card_value` to `self.value`.

## 740. Assign a boolean to a variable

### 740.1

In blackjack, an Ace can have the value of either 11 or 1, depending on what is better for the player. First check if the hand has an Ace. Below `self.value = 0` create a variable called `has_ace` and set it to `False`. You don't need `self.` before the variable name since we will only use it in this method.

## 745. Check if there is an ace

### 745.1

When looping through `self.cards` to calculate `self.value`, the code should also check if one of the cards is an ace. Inside the `for` loop, add the following code:
```py
if card.rank["rank"] == "A":
    has_ace = True
``` 

#### HINTS

- Copy and paste the code at the same indentation and after the line `self.value += card_value`.

## 750. Subtract a value from a variable with -=

### 750.1

After the last `for` loop you added, check `if has_ace and self.value > 21`. (Note: `if has_ace` means the same thing as `if has_ace == True`.) If the statement evaluates to true, use the `-=` operator to subtract 10 from `self.value`. (This program will not deal with the edge case of multiple Aces having a value of 1.)

#### HINTS

- You should be adding two lines of code: the line with the `if` statement and the contents of the `if` statement.

## 760. Return the hand's value

### 760.1

Add another method to get the value of a hand called `get_value`. The method should return `self.value`.

#### HINTS

- You should be adding two lines of code: the line that defines the method and the line that returns a value from the method.

## 770. Calculate value before returning it

### 770.1

Currently, the value that is returned could be incorrect. In the `get_value` method, before returning `self.value`, calculate the value first by calling `self.calculate_value()`.

## 780. Create is_blackjack method

### 780.1

Create another method called `is_blackjack`. It should return `self.get_value() == 21`. That will be `True` if is a blackjack and `False` otherwise.

## 790. Create display method

### 790.1

Now you will create the final method in the `Hand` class that will display information about the hand. Create a method called `display` that will print "Your hand:".

#### HINTS

- You should be adding two lines of code: the line that defines the method and the line that prints "Your hand:".

## 800. Use triple quotes

### 800.1

You can create a string by either surrounding text with single quotes (`'`) or double quotes 
(`"`). Whichever quote type you use, you can use the other quote type inside the string. If a string contains both single quotes and double quotes inside, you can surround it with `'''`. Change the print line you just added so it will print either "Dealer's hand:" or "Your hand:" by using this line of code: `print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')`.

#### HINTS

- Make sure to copy and paste the code exactly. Also, think about the code until you understand what it is doing.

## 810. Print every card with a for loop

### 810.1

In the `display` method, add a `for` loop that prints out each card in `self.cards`.

#### HINTS

- Look at the `for` loop in the `calculate_value` method for an example.
- Each iteration should `print(card)`.

## 820. Print value in display method

### 820.1

If the player is not the dealer, it should print `"Value:", self.get_value()`. To check if something is not true, just add `not` before the thing you are checking.

#### HINTS

- After the `for` loop and still inside the `display` method add `if not self.dealer:`. Inside, print the appropriate text.

## 830. Print a blank line

### 830.1

Now add an empty `print()` statement so a blank line will be printed.

#### HINTS

- After the `if` statement you just added, add the following line: `print()`.

## 840. Call the display method

### 840.1

Change the last line of the program from `print(hand.cards)` to `print(hands.display())`. Then, run your program.

## 850. Use enumerate() in a for loop

### 850.1

When the dealer's cards are printed during the game, only the second one should display. The first card should display as "hidden". In the `for` loop in the `display` method, you will need to get access to the card index since that will determine which to display. Update the first line of the `for` loop to `for index, card in enumerate(self.cards):` to get access to the card and index on each iteration of the loop.

## 860. Print the first dealer's card as "hidden"

### 860.1

Put the `print(card)` line into an `if` statement. First check `index == 0 and self.dealer`. If that evaluates to true, print "hidden". If that evaluates to false, print the card.

#### HINTS

- The full `for` loop should look like this:  
```py  
for index, card in enumerate(self.cards):  
    if index == 0 and self.dealer:  
        print("hidden")  
    else:  
        print(card)  
```

## 870. Add show_all_dealer_cards parameter

### 870.1

At the end of a game, all the dealers cards should be shown. Add a parameter in the `display` method called `show_all_dealer_cards` and set the default value to `False`.

#### HINTS

- Make sure the first parameter in the `display` method is still `self`.

## 880. Add to an if statement

### 880.1

Now add to the `if` statement so it only prints "hidden" if `show_all_dealer_cards` is not true.

#### HINTS

- The `if` statement should look like: `if index == 0 and self.dealer and not show_all_dealer_cards:`

## 890. Use the result of a method in an if statement

### 890.1

Add one final check to the `if` statement to check if is not a blackjack (`self.is_blackjack()`).

#### HINTS

- Now the `if` statement should look like: `if index == 0 and self.dealer and not show_all_dealer_cards and not self.is_blackjack():`

## 900. Delete code used to test Hand class

### 900.1

You are done creating the `Hand` class so delete all the code under the `Hand` class that was used for testing.

## 910. Create game class

### 910.1

It's time to make the final (and longest) class that runs the game. Create a class called `game`. Inside that class create a method called `play`. Inside that method create a variable called `game_number` and set it to zero.

#### HINTS

- Make sure the `play` method takes a `self` argument.

## 920. Create games_to_play variable

### 920.1

Besides keeping track of the game number we also have to keep track of the number of `games_to_play`. Create that variable and start it at zero.

## 930. Get input from user

### 930.1

A program can request a user's input in the terminal with the `input()` function. For example, the code `name = input("What's your name? ")`, will prompt the user with "What's your name? " and store the inputted text in a variable called `name`. Ask the user for input to the question "How many games do you want to play? " The result should be stored in the `games_to_play` variable. (Note: Keep the `games_to_play = 0` line of code.)

#### HINTS

- Make sure to add a space at the end of the question string.
- `games_to_play` should be set to equal `input("How many games do you want to play? ")`.

## 940. Cast the result of input as an int

### 940.1

Put the `input` function inside an `int` function to make sure the result is an integer.

## 950. Test play method of the game

### 950.1

Add the following lines at the end of your program (not indented):
```py
g = Game()
g.play()
```
Now you can test your program by running `python blackjack.py` in the terminal.

#### HINTS

- Just copy and paste the code.

## 960. Use a "try-except" block

### 960.1

There will be an error if `int()` is called with something that is not a number. In this case, there will be an error that stops the program if a user enters something that is not a number. You can specify how to handle an exception (an error) with a "try-except" block. In this type of block, the program will `try` some code. If there is an error in that code, the program will run the code inside the `except` part of the block instead of stopping the program. Switch the last line in the `play` method with the following "try-except" block:
```py
try:
    games_to_play = int(input("How many games do you want to play?: "))
except:
    print("You must enter a number.")
```

#### HINTS

- Just copy and paste the code.

## 970. Loop until input is correct

### 970.1

Currently, the user gets one chance to input a correct value. Let's make the program keep asking the user for a value until the user enters a number. This can be done with a `while` loop. This type of loop keeps looping "while" something is true. Keep looping until the user enters a number by putting the entire "try-catch" block into a while loop that starts like this: `while games_to_play <= 0:`.

#### HINTS

- Indent the try-except block inside the `while` loop.

## 980. Create main game loop

### 980.1

Now you will create the main game loop. This will loop one time per game played. It should loop `while` `game_number` is less than `games_to_play`. The first line in the loop should increment the `game_number` by one.

#### HINTS

- The main game loop should be after the `while` loop containing the try-except block.
- The loop should start: `while game_number < games_to_play:`
- Inside the loop should be: `game_number += 1`

## 990. Create a deck

### 990.1

Inside that loop create a `Deck` object and assign it to a variable named `deck`. Then shuffle the deck.

#### HINTS

- Create a deck with `Deck()` and assign it to variable `deck`.
- Call the `shuffle()` method of `deck`.


## 1000. Create a hand

### 1000.1

Create a variable called `player_hand` and set it to a `Hand` object.

#### HINTS

- This is vary similar to how you created a deck.

## 1010. Create variable dealer_hand

### 1010.1

Create a variable called `dealer_hand` and set it to a `Hand` object. When creating the object, make sure to specify that `dealer=True`.

#### HINTS

- The variable you create should be equal to `Hand(dealer=True)`.

## 1020. Deal multiple times with a loop

### 1020.1

Create a `for` loop that loops 2 times. Each iteration should add a card to the player's hand that is dealt from the deck and add a card to the dealer's hand that is dealt from the deck.

#### HINTS

- Deal cards to both hands in the loop. Here is how you deal to the first hand: `player_hand.add_card(deck.deal())`.

## 1030. Print an empty line in the game loop

### 1030.1

Information will be printed to the console for each game. Start by printing an empty line.

#### HINTS

- Remember `print()`?
- Do not indent it inside the `for` loop.

## 1040. Use * to repeat a string

### 1040.1

Now print `*` 30 times to make a divider. You can do that with `print("*" * 30)`.

#### HINTS

- Just copy and paste the code.

## 1050. Print current game number

### 1050.1

Print the current game number out of the total number of games. For instance, if the loop is on the 4th game of 10 total games to play, it should print: "Game 4 of 10".


#### HINTS

- Use an f-string to include variables inside a string.

## 1060. Print 30 more *

### 1060.1

Print 30 more `*`.


#### HINTS

- Use the same code from two lines up

## 1070. Display the player's hand

### 1070.1

Display the player's hand.

#### HINTS

- Use the `display()` method.

## 1080. Display the dealer's hand

### 1080.1

Display the dealer's hand.

#### HINTS

- You actually know how to do this and don't need a hint. 😀

## 1090. Create check_winner method

### 1090.1

At this point in the game, someone could have won if they got a blackjack. The code should check if there is a winner. Let's put the code to check if there is a winner in a separate method of the `Game` class. Create a method called `check_winner`. For now the method should just return `False`.

#### HINTS

- The `check_winner` method should be outside of the `play` method.
- The method should look like this:  
```  
def check_winner(self):  
    return False  
```

## 1100. Add arguments to check_winner function

### 1100.1

The `check_winner` should take `player_hand` and `dealer_hand` as arguments.

#### HINTS

- Add the arguments to the function definition, right after `self`.

## 1120. Check if the player busted

### 1120.1

Before `return False`, check if `player_hand.get_value() > 21`. If so, print "You busted. Dealer wins! 😭" and return `True`. Once the program gets to a `return` statement, none of the following statements in the block are run.

#### HINTS

- Inside the `if` statement there should be two lines: one to print and one to return `True`.

## 1130. Check if the dealer busted

### 1130.1

We'll use a few `elif` statements to check for various other conditions. Add an `elif` statement to check if `dealer_hand.get_value() > 21`. If so, print "Dealer busted. You win! 😄" and return `True`.

#### HINTS

- Did you forget a semi-colon after the `elif` statement?

## 1140. Check if both the player and the dealer won

### 1140.1

Add an `elif` statement to check if both players have a blackjack. If so, print "Both players have blackjack! Tie! 🤨" and return `True`.

#### HINTS

- The `elif` statement should start like this: `elif player_hand.is_blackjack() and dealer_hand.is_blackjack():`.

## 1150. Check if the player has a blackjack

### 1150.1

Add an `elif` statement to check if `player_hand` has a blackjack. If so, print "You have blackjack! You win! 😄" and return `True`.

#### HINTS

- Follow the pattern in the code you already have.

## 1160. Check if the dealer has a blackjack

### 1160.1

Add an `elif` statement to check if `dealer_hand` has a blackjack. If so, print "Dealer has blackjack! Dealer wins! 😭" and return `True`.

#### HINTS

- You got this one by yourself.

## 1170. Add a game_over parameter

### 1170.1

The game can also end if both players choose not to get more cards. Add this argument to the `check_winner` method with a default value: `game_over=False`.

#### HINTS

- The `check_winner` method definition should now look like this: `def check_winner(self, player_hand, dearler_hand, game_over=False):`.

## 1180. Check if it is not game over

### 1180.1

Use the new argument. The string of `if` and `elif` statements should only be run `if not game_over`. Make sure the line `return False` is not in the `if` statement.

#### HINTS

- Indent the entire string of `if` and `elif` statements inside the new `if` statement.

## 1190. Check which hand value is greater

### 1190.1

If `game_over` is `True`, check if the player hand's value is more than the dealer hand's value. If so, print "You win! 😄".

#### HINTS

- Add an `else` statement to the `if not game_over` you added in the last lesson.
- In the `else` statement, add this `if` statement: `if player_hand.get_value() > dealer_hand.get_value():`
- Put this inside the `if` statement: `print("You win! 😄")`

## 1200. Check for a tie

### 1200.1

Add an `elif` statement to check if both player's hands equal the same value. If so, print "Tie! 🤨".

#### HINTS

- The next hint will show you what your code should look like. See if you can figure it out yourself first.
- Here is the entire `else` statement:  
```py  
else:  
    if player_hand.get_value() > dealer_hand.get_value():  
        print("You win! 😄")  
    elif player_hand.get_value() == dealer_hand.get_value():  
        print("Tie! 🤨")  
```
## 1210. Else dealer wins

### 1210.1

After the `elif` statement, add an `else` statement that prints "Dealer wins! 😭"

## 1220. return True if game_over equals True

### 1220.1

At the exact same level of indentation as the `else:` line you just added, add the line `return True`. This will make the method return `True` if `game_over` equals `True`.

## 1230. Check for a winner

### 1230.1

Now back to the end of the `play` method inside the `while` loop. Add this code:
```
if self.check_winner(player_hand, dealer_hand):
    continue
```
The `check_winner` method will return `True` if there is a winner. The `continue` line will continue to the next iteration of the `while` loop. Each iteration is a new game.


#### HINTS

- Copy and paste the given code right after the line: `dealer_hand.display()`. Use same level of indentation.

## 1240. Get player input "Hit" or "Stand"

### 1240.1

The player should be able to keep choosing "Hit" or "Stand" until the value of their hand is over 21. Right under the `choice` variable, add a `while` loop that loops while `player_hand`s value is less than 21. Inside the loop add the following line: `choice = input("Please choose 'Hit' or 'Stand': ").lower()`. That line will get a choice as input from the user and convert the input to lowercase letters. 

#### HINTS

- Look at the other `while` loop in your code for an example.

## 1250. Loop should stop if player chooses "Stand"

### 1250.1

The while loop you just added should also stop if the user's choice is "Stand" or "S". Update the line that starts the `while` loop to `while choice not in ["s", "stand"] and player_hand.get_value() < 21:`.

#### HINTS

- Copy and paste the new beginning of the `while` loop.

## 1260. Print empty line after input

### 1260.1

After the input, print an empty line.

#### HINTS

- The `print` statement should be indented the same amount as `choice = input("Please choose 'Hit' or 'Stand': ").lower()`.

## 1270. Keep asking for input until correct input

### 1270.1

The program should keep asking the user for a choice until the user enter's a valid choice. The valid choices are "h", "s", "hit", and "stand". Right after the last `print` statement (same indentation), add a `while` loop that will keep looping until the user enters a valid choice. Use the previous `while` loop as an example. Inside the loop, ask for input again with the line `choice = input("Please enter 'Hit' or 'Stand' (or H/S) ").lower()`.

#### HINTS

- Use this loop: `while choice not in ["h", "s", "hit", "stand"]:`.

## 1280. Print empty line inside loop

### 1280.1

Print an empty line inside the while loop.

#### HINTS

- Check your indentation.

## 1290. Check for hit input

### 1290.1

In the last `while` loop you checked if `choice` was not in a list. Outside of your recently added `while` loop but inside the loop added just before that one, add an `if` statement to check if `choice` is in the list `["hit", "h"]`. If true, add a card to the player's hand that is dealt from the deck.

#### HINTS

- Try again to figure this out. The next hint will show you the exact solution code.
- Here is the solution code in context:
```py  
while choice not in ["s", "stand"] and player_hand.get_value() < 21:  
    choice = input("Please choose 'Hit' or 'Stand': ").lower()  
    print()  
    while choice not in ["h", "s", "hit", "stand"]:  
        choice = input("Please enter 'Hit' or 'Stand' (or H/S) ").lower()  
        print()  
    if choice in ["hit", "h"]:  
        player_hand.add_card(deck.deal())  
```

## 1300. Display player's hand in if statement

### 1300.1

Also inside the `if` statement, display the player's hand.

#### HINTS

- Use the `display()` method.
- Indent the code the same as the line `player_hand.add_card(deck.deal())`.

## 1310. Check for winner after choice

### 1310.1

Outside of all the `while` loops about the player making a choice, check for a winner. Use the same `if` statement and `continue` statement that you used the last time you checked for a winner.

#### HINTS

- Make sure the code is after the `while` loop where the user inputs a choice of hit or stand.

## 1320. Create player_hand_value variable

### 1320.1

Store the value of the player's hand in a variable named `player_hand_value`.

#### HINTS

- This should be indented on the same level as the `if` statement you just added. It should not be in the `if` statement.

## 1330. Create dealer_hand_value variable

### 1330.1

Store the value of the dealer's hand in a variable named `dealer_hand_value`.

## 1340. Make the dealer draw cards

### 1340.1

The dealer should keep drawing cards until `dealer_hand_value` is more than 17. Make this happen with a `while` loop. Inside the loop, make sure the dealer is dealt a card from the deck and `dealer_hand_value` is updated.

#### HINTS

- The first line in the `while` loop should `add_card` to `dealer_hand`. The card should come from `deck.deal()`.
- Set `dealer_hand_value` just like you did a few lines up.

## 1350. Display all the dealer's cards

### 1350.1

Outside of that last `while` loop, display the dealer's hand. When you call the `display` method, make sure to set `show_all_dealer_cards` to `True`.

#### HINTS

- When you call the `dislpay` method, put `show_all_dealer_cards=True` inside the parenthesis. 

## 1360. Check for a winner again

### 1360.1

Check for a winner again, just like before.

## 1370. Print "Final Results"

### 1370.1

Print "Final Results".

## 1380. Print results for player's hand

### 1380.1

Now print "Your hand:" with `player_hand_value` after the string.

## 1390. Print results for dealer's hand

### 1390.1

Print "Dealer's hand:" with the `dealer_hand_value` after the string.

## 1400. Check winner after game is over

### 1400.1

Call `self.check_winner` one final time. This time it should not be in an `if` statement. Pass in the hands like before but this time add a third argument of `True` to indicate that the game is over.

#### HINTS

- The line should look like this: `self.check_winner(player_hand, dealer_hand, True)`.

## 1410. Print "Thanks for playing!"

### 1410.1

At this point in the code, the game is over. Outside of the outer `while` loop in the `play` method, add this final line: `print("\nThanks for playing!")`. Note the `\n` in the string. That will add a new line.

#### HINTS

- Check your indentation.