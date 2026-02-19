# ============================================================
# Escape Sequences Characters
# ============================================================
# \b      => Backspace (removes the previous character)
# \       => Escape New Line (when ending line with \)
# \\      => Escape Back Slash
# \'      => Escape Single Quote
# \"      => Escape Double Quote
# \n      => Line Feed (new line)
# \r      => Carriage Return (return cursor to beginning of line)
# \t      => Horizontal Tab
# \xhh    => Character represented by Hex Value
# ============================================================

# -----------------------------
# Backspace
# -----------------------------
print("Hello\bWorld")  
# Output: "HellWorld" (the 'o' is removed)

# -----------------------------
# Escape New Line + Back Slash
# -----------------------------
print("Hello \
I Love \
Python")
# Output in one line: "Hello I Love Python"

# -----------------------------
# Escape Back Slash
# -----------------------------
print("I Love Back Slash \\")
# Output: I Love Back Slash \

# -----------------------------
# Escape Single Quote
# -----------------------------
print('I Love Single Quote \'Test\' ')
# Output: I Love Single Quote 'Test' 

# -----------------------------
# Escape Double Quotes
# -----------------------------
print("I Love Double Quotes \"Test\" ")
# Output: I Love Double Quotes "Test"

# -----------------------------
# Line Feed (\n)
# -----------------------------
print("Hello World\nSecond Line")
# Output:
# Hello World
# Second Line

# -----------------------------
# Horizontal Tab (\t)
# -----------------------------
print("Hello\tPython")
# Output: Hello    Python  (adds a tab space)

# -----------------------------
