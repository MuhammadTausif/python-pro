**Python Course: Day 4 Outline - Control Flow and Loops**

---

**1. Introduction to Control Flow**
- Definition and importance in programming.
- Flowcharts: A visual representation of control flow.

**2. Conditional Statements: `if`**
- Basic `if` statement.
  ```python
  age = 18
  if age >= 18:
      print("You are an adult.")
  ```
- The importance of indentation in Python.

**3. The `else` Clause**
- Using `if-else` together.
  ```python
  age = 16
  if age >= 18:
      print("You are an adult.")
  else:
      print("You are a minor.")
  ```

**4. The `elif` Statement**
- Chain multiple conditions using `elif`.
  ```python
  score = 85
  if score >= 90:
      grade = "A"
  elif score >= 80:
      grade = "B"
  elif score >= 70:
      grade = "C"
  else:
      grade = "D"
  print(f"Your grade is {grade}.")
  ```

**5. Nested Conditionals**
- Understanding and writing nested `if` statements.
  ```python
  age = 20
  if age >= 18:
      if age <= 21:
          print("You are a young adult.")
      else:
          print("You are an adult.")
  else:
      print("You are a minor.")
  ```

**6. Introduction to Loops**
- Importance of loops in automating repetitive tasks.

**7. The `while` Loop**
- Basics of `while` loop.
  ```python
  count = 0
  while count < 5:
      print(count)
      count += 1
  ```
- Infinite loops and how to avoid them.

**8. The `for` Loop**
- Introduction to the `for` loop.
- Iterating over a list.
  ```python
  fruits = ["apple", "banana", "cherry"]
  for fruit in fruits:
      print(fruit)
  ```

**9. The `range()` Function**
- Using `range()` in loops.
  ```python
  for i in range(5):
      print(i)
  ```

**10. `break` and `continue` Statements**
- Using `break` to exit a loop.
- Using `continue` to skip the current iteration.
  ```python
  for i in range(5):
      if i == 3:
          continue
      print(i)
  ```

**11. Nested Loops**
- Writing a loop inside another loop.
  ```python
  for i in range(3):
      for j in range(3):
          print(i, j)
  ```

**12. Practical Exercise: Building a Simple Calculator with Loops**
- Creating a loop-based menu for a calculator.
- Using conditionals to perform different arithmetic operations.

**13. Summary and Q&A**
- Recap of the day's content.
- Addressing questions and providing clarifications.

**14. Homework/Assignments**
- Create a program to check if a number is prime using loops.
- Implement a program that prints patterns (e.g., pyramids) using nested loops.

---

This Day 4 outline aims to get learners comfortable with control flow mechanisms in Python. By the end of the day, they should be capable of making decisions in their code and automating repetitive tasks using loops.