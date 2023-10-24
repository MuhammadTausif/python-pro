### Day 3: Control Structures: Conditionals & Loops

---

#### **1. Conditional Statements**

   - **Introduction to Conditions**
     - Boolean expressions
     - Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
   
   **Example:**
   ```python
   x = 5
   y = 7
   print(x == y)  # Output: False
   ```

   - **The `if` statement**
     - Basic structure and syntax
   
   **Example:**
   ```python
   age = 18
   if age >= 18:
       print("You are eligible to vote.")
   ```

   - **The `elif` and `else` statements**
     - Building more complex decision trees
   
   **Example:**
   ```python
   score = 85
   if score >= 90:
       print("Grade: A")
   elif score >= 80:
       print("Grade: B")
   else:
       print("Grade: C")
   ```

#### **2. Loops**

   - **Introduction to Loops**
     - Iterative tasks and the significance of loops in programming
   
   - **The `for` loop**
     - Looping through sequences (lists, strings, etc.)
     - The `range()` function
   
   **Examples:**
   ```python
   for i in range(5):
       print(i)  # Output: 0, 1, 2, 3, 4

   fruits = ["apple", "banana", "cherry"]
   for fruit in fruits:
       print(fruit)
   ```

   - **The `while` loop**
     - Setting conditions for iterative tasks
   
   **Example:**
   ```python
   count = 1
   while count <= 5:
       print(count)
       count += 1
   ```

   - **Loop Control: `break`, `continue`, and `pass`**
     - Controlling loop execution
   
   **Examples:**
   ```python
   # Using break
   for i in range(5):
       if i == 3:
           break
       print(i)  # Output: 0, 1, 2

   # Using continue
   for i in range(5):
       if i == 3:
           continue
       print(i)  # Output: 0, 1, 2, 4
   ```

#### **3. Exercises**

   - **Age Classifier:**
     - Take user input for age and classify into "Child" (0-12), "Teen" (13-19), "Adult" (20-64), or "Senior" (65+).
   
   - **Number Guessing Game:**
     - Set a predetermined number. Ask the user to guess. Provide hints like "Too high" or "Too low" based on user input.
   
   - **Printing Patterns:**
     - Use nested loops to print patterns, such as:
     ```
     *
     **
     ***
     ****
     ```

   - **Simple Calculator with Loop:**
     - Build a simple calculator that keeps running and asks the user for two numbers and an operation (+, -, *, /) until the user decides to quit.

---

### Tips for Day 3:

1. **Hands-On Approach:** Continuously practice the examples given. Play around with conditions, maybe even create nested conditions (conditions within conditions) to see how they function.
  
2. **Challenge Yourself:** In the loop section, try to make a loop within a loop and observe the results. For instance, print tables using nested loops.
  
3. **Understand Over Memorize:** Make sure to understand the logic behind conditional statements and loops rather than rote memorization. This foundational understanding is crucial for more advanced programming concepts.

By the end of Day 3, learners should be comfortable with basic decision-making and iterative constructs in Python. These are foundational tools that every programmer should know, as they form the basis for most algorithmic logic.