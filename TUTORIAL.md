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
friends = ['Kris', 'Tom', 'Oliver']
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

- Make sure to surround each item with parenthesis.

## 140. Create an empty list

### 140.1

Before the `suits` list, create a new variable called `cards` and assign an empty list (`[]`) to the variable.

#### HINTS

- Nothing should be inside the brackets.
