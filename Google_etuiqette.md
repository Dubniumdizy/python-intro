# Python Project and GitHub Submission Guidelines

This document provides a general guide on how to structure a Python programming assignment according to industry standard guidelines, document it using Markdown, and publish it publicly on GitHub.

---

## Part 1: Writing Code According to Google's Style Guide

When writing Python code to match industry standards (such as Google's Python Style Guide and PEP 8 - Python Enhancement Proposal 8. It is the official style guide for writing Python code), your focus should be on 
1) clean readability
2) structure consistency
3) clear documentation

* **File Structure**: Always begin your script with a top-level module-level docstring (`"""..."""`) that explicitly describes what the program does.
* **Naming Conventions**: 
  * Use `snake_case` for function names, variable names, and script file names (ex, `calculate_sum.py`, `my_variable`).
  * Use `CAPITAL_SNAKE_CASE` for defining global constants (ex PI = 3.14159).
* **Indentation & Spacing**: Use exactly **4 spaces** per indentation level. Use a single blank line to visually separate functions and distinct logic blocks.
* **Documentation**: Every single function should include a descriptive docstring right below its definition line to explain its purpose, parameters (arguments), and return values.
1) A Single-Line Summary: A concise, imperative sentence stating exactly what the function achieves (e.g., "Calculates the area..." rather than "This function will calculate the area...").
2) Args (Parameters / Arguments): A clear list documenting each input variable name, its expected data type, and a brief description of what it represents.
3) Returns: The expected data type of the output and a description of what value the function sends back to the caller.

Ex:
```python
def calculate_grade_average(grades, round_result=True):
    """Calculates the average score from a list of numerical grades.

    Args:
        grades (list): A list of integers or floats representing student scores.
        round_result (bool): If True, rounds the final average to the nearest
          whole number. Defaults to True.

    Returns:
        float or int: The computed average score, rounded depending on the 
          round_result flag.
    """
    if not grades:
        return 0
        
    total = sum(grades)
    average = total / len(grades)
    
    if round_result:
        return round(average)
    return average
```
---

## Part 2: Documenting via Markdown (`.md`)

A Markdown file (such as a `README.md`) acts as the primary introduction and manual for your project. Good documentation must include the following structural elements:

* **Project Title & Description**: A clear header (`# Title`) followed by a brief overview explaining the repository's contents. (OBS a repository (often shortened to "repo") as a smart, digital project folder hosted on GitHub).
* **Code Blocks**: Use triple backticks (\`\`\`) followed by the language specifier (`python`) to highlight code syntax clearly.
* **Constraints Checklist**: If your project has strict rules (e.g., no forbidden built-in modules, no list comprehensions, no exception handling, or no match-case statements), list them clearly using bullet points to prove compliance.

Ex: 
---
# Hexadecimal Converter Utility

This repository is a smart, digital project folder hosted on GitHub that contains a Python script for converting numbers between decimal and hexadecimal bases. It operates entirely without relying on Python's built-in conversion shortcuts.

---

## Constraints Checklist

To prove compliance with the assignment rules, this project strictly avoids the following features:
* **No Forbidden Modules:** Built-in libraries like `sys` or custom external modules are not imported.
* **No List Comprehensions:** All list operations are built using standard `for` loops.
* **No Exception Handling:** Input validation is handled manually without using `try-except` blocks.

---

## Core Conversion Logic

Below is the foundational function used to map integers to their correct hexadecimal character representations:

```python
def int_to_hexa_char(tal):
    """Converts an integer in the range 0-15 to its hexadecimal character."""
    hexa_chars = "0123456789ABCDEF"
    return hexa_chars[tal]
```
---

## Part 3: Publishing Your Project Publicly on GitHub

To share your local desktop project folder publicly on GitHub, the cleanest and easiest way is to use the official GitHub Desktop application.

### Step 1: Download GitHub Desktop
* Go to [desktop.github.com](https://desktop.github.com) to download and install the official application.
* Launch the app and log directly into your personal GitHub account.

### Step 2: Add your Folder to GitHub Desktop
Turn your local desktop directory into a tracking Git repository:
1. In GitHub Desktop, navigate to the top menu and click **File -> Add local repository...** (or select *New repository* if the folder is completely empty).
2. Click **Choose...** and navigate to your desktop to select your specific assignment folder.
3. Click **Add Repository** to confirm.

### Step 3: Publish the Repository Publicly
Push your local code up to GitHub's cloud servers:
1. Click the **Publish repository** button located at the top right of the application interface.
2. A configuration window will pop up. **CRITICAL STEP:** Ensure that you **uncheck** the box that says *"Keep this code private"* so that your code is publicly visible.
3. Click the final **Publish Repository** button.

### Step 4: View and Share Your Work
1. Once the upload completely finishes, go to the top menu and select **Repository -> View on GitHub**.
2. Your default web browser will open straight to your new public project page.
3. You can now copy that public URL from the address bar to share your submission link with instructors or peers.

---

Type hinting

# Type Hinting in Python

Type hinting is a formal layout standard introduced in PEP 484 that allows developers to explicitly declare the expected data types for variables, function arguments, and return values. While Python remains a dynamically typed language at runtime, incorporating type hints makes code significantly cleaner, easier to debug, and highly readable.

---

## Why Use Type Hinting?

* **Enhanced Readability:** Other developers (and your future self) can instantly see what kind of data a function expects without reading through the entire implementation logic.
* **Better IDE Support:** Code editors can provide highly accurate autocomplete suggestions, parameter descriptions, and inline warnings if you try to pass the wrong data type.
* **Static Analysis:** Tools can scan your code before it runs to catch potential bugs and type mismatches early in development.

---

## Code Example

Below is a Python function demonstrating standard PEP 8 syntax for type hints, showcasing how to declare input parameter types and the final return type.

```python
def calculate_grade_average(grades: list[float], round_result: bool = True) -> float | int:
    """Calculates the average score from a list of numerical grades.

    Args:
        grades (list): A list of floats representing student scores.
        round_result (bool): If True, rounds the final average to the nearest
          whole number. Defaults to True.

    Returns:
        float or int: The computed average score.
    """
    if not grades:
        return 0
        
    total: float = sum(grades)
    average: float = total / len(grades)
    
    if round_result:
        return round(average)
    return average