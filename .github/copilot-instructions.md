# Copilot instructions

## Style conventions

These conventions apply to all notebooks, Python modules, and markdown documents in this repository.

### 1. Sentence case for headings and list elements

Use sentence case throughout: capitalize only the first word and proper nouns. Do not use title case.

**Correct:**
```markdown
## Problem 1: The word splitter
### Bug 3: The division disaster
- Research string methods that can break a sentence into parts
```

**Incorrect:**
```markdown
## Problem 1: The Word Splitter
### Bug 3: The Division Disaster
- Research String Methods That Can Break a Sentence Into Parts
```

Proper nouns and acronyms that are always capitalized regardless of position: Python, Linux, JSON, VS Code, Docker, Git, JavaScript, Jupyter.

### 2. No em dashes

Do not use em dashes (—). Replace them with a colon, semicolon, or comma as appropriate to the sentence.

**Correct:**
```
Use string methods like .split(): they break a sentence into parts.
Use string methods like .split(); they break a sentence into parts.
```

**Incorrect:**
```
Use string methods like .split() — they break a sentence into parts.
```

### 3. Single quotes in Python strings and docstrings

Use single quotes for all Python string literals and triple-single-quotes for docstrings. Use double quotes only when the string itself contains a single quote and escaping would reduce readability.

**Correct:**
```python
name = 'Alice'
message = 'Hello, world!'
print(f'Name: {name}')

def greet(name):
    '''Greet a user by name.'''
    return f'Hello, {name}!'
```

**Incorrect:**
```python
name = "Alice"
message = "Hello, world!"
print(f"Name: {name}")

def greet(name):
    """Greet a user by name."""
    return f"Hello, {name}!"
```
