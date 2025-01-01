### **PolarForm Questionnaire Authoring Guide**

PolarForm is a questionnaire generation tool that uses a simple markup syntax to create dynamic HTML surveys. This guide explains the supported syntax and provides examples to help you design your questionnaires.

---

### **1. Structure and Basics**

1. **Headings**  
   - Start each section with `[#]` for a heading.   
     **Example:**
     ```
     [#]Personal Information
     ```

2. **Question Markers**  
   - Use `[*]` for required questions and `[/]` for optional ones.  
   **Example:**
     ```
     [*][~=2,50] Please enter your name
     [/][@] Provide your backup email
     ```

3. **Section Separation**  
   - Use `---` to separate each question or heading.

---

### **2. Question Types**

#### **(1) Single-Choice and Multiple-Choice Questions**
- Marker: `[&=x]`, where `x` specifies the number of choices allowed (1 for single choice, more than 1 for multiple choices).  
- List the options line by line after the question, ending with `---`.  
**Example:**
```
[*][&=1] Select your gender
Male
Female
---
[*][&=2] Choose two favorite fruits
Apple
Banana
Orange
Grape
---
```

#### **(2) Short Answer Questions**
- Marker: `[~=x,y]`, where `x` is the minimum character count, and `y` is the maximum.  
**Example:**
```
[*][~=2,50] Enter your name (2–50 characters)
```

#### **(3) Long Answer Questions**
- Marker: `[_=x,y]`, where `x` is the minimum character count, and `y` is the maximum.  
**Example:**
```
[/][_=0,1000] Provide your feedback (up to 1000 characters)
```

#### **(4) Date Questions**
- Marker: `[%=x]`, where `x` can be:  
  - `md`: Month and day selection.  
  - `y`: Year input.  
**Example:**
```
[*][%=md] Select your birth date (month and day)
[*][%=y] Enter your birth year
```

#### **(5) Email Questions**
- Marker: `[@]` to request an email address, with built-in format validation.  
**Example:**
```
[*][@] Enter your email address
[/][@] Enter a backup email address
```

---

### **3. Formatting Options**

1. **HTML Support**  
   - Basic HTML tags (e.g., `<b>`, `<strong>`) are allowed in descriptions.  
   **Example:**
   ```
   [*][&=2] Choose <strong>two</strong> favorite fruits
   ```

---

### **4. Sample Questionnaire**

```
[#]Multiple-Choice Section
---
[*][&=1] Choose one of the following options
Option 1
Option 2
Option 3
---
[*][&=2] Select two of the following options
Option 1
Option 2
Option 3
Option 4
---

[#] Short Answer Section
---
[*][~=2,50] Please enter your name
[/][_=0,1000] Share your thoughts (up to 1000 characters)
---

[#] Date and Email Section
---
[*][%=md] Select your birth date (month and day)
[*][%=y] Enter your birth year
[*][@] Enter your email address
```

---

### **5. Key Notes**

1. **Question Order**: Write questions sequentially; the tool will auto-number them.  
2. **Option List End Marker**: For multiple-choice and single-choice questions and other questions, always end the option list or question with `---`.  
3. **Character Limit Validation**: Ensure that in `[x,y]`, `x` and `y` are both provided, and `x` is less than `y` to avoid errors.  
4. **Consistent Encoding**: Each marker line must start with `[ ]`, or it will be treated as plain text.

Following these rules, you can efficiently create a variety of questionnaires tailored to your needs!