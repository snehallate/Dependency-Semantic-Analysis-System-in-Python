# Dependency Semantic Analysis System in Python

# Python Code Dependency and Semantic Analysis System

A GUI-based Artificial Intelligence project that performs **syntactic dependency parsing** and **semantic analysis** on Python code snippets using **Natural Language Processing (NLP)** techniques with the help of the spaCy library.

---

## 📌 Project Overview

The **Python Code Dependency and Semantic Analysis System** is designed to analyze Python source code by extracting:

* Syntactic dependencies between tokens
* Token classifications
* Named entities
* Noun chunks
* Structural relationships in code

The system uses **spaCy NLP models** along with a **Tkinter GUI** to provide an interactive environment for Python code analysis.

This project demonstrates how NLP techniques can be adapted for programming language analysis.

---

## 🚀 Features

### ✅ Syntactic Dependency Analysis

* Tokenization of Python code
* Dependency parsing
* Part-of-speech tagging
* Token type classification

### ✅ Semantic Analysis

* Named Entity Recognition (NER)
* Noun Chunk Extraction
* Semantic relationship identification

### ✅ GUI Interface

* User-friendly Tkinter interface
* Input area for Python code
* Separate output sections for:

  * Syntax analysis
  * Semantic analysis

### ✅ Structured Output

Displays:

* Token
* Head Token
* Dependency
* POS Tag
* Token Type

---

## 🧠 Technologies Used

| Technology     | Purpose                                |
| -------------- | -------------------------------------- |
| Python         | Core Programming Language              |
| spaCy          | NLP Processing                         |
| Tkinter        | GUI Development                        |
| NLP Techniques | Dependency Parsing & Semantic Analysis |

---



## ⚙️ Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/your-username/python-code-dependency-analyzer.git
cd python-code-dependency-analyzer
```

---

### Step 2: Install Required Libraries

```bash
pip install -r requirements.txt
```

---

### Step 3: Download spaCy Model

```bash
python -m spacy download en_core_web_sm
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 🖥️ GUI Interface

The application provides:

* Input panel for Python code
* Analyze Syntax button
* Perform Semantic Analysis button
* Output display sections

---

## 📊 Sample Input

```python
def add(a, b):
    result = a + b
    return result

x = add(5, 10)
```

---

## 📈 Sample Syntax Output

| Token  | Head | Dependency | POS  | Type       |
| ------ | ---- | ---------- | ---- | ---------- |
| add    | add  | ROOT       | VERB | Keyword    |
| result | add  | dobj       | NOUN | Identifier |

---

## 📌 Methodology

### 1. Preprocessing

* Input Python code is processed using spaCy NLP pipeline
* Performs:

  * Tokenization
  * POS tagging
  * Dependency parsing
  * Entity recognition

### 2. Token Classification

Each token is categorized as:

* Keyword
* Identifier
* Operator
* Literal
* Punctuator
* Other

### 3. Syntactic Analysis

The system identifies:

* Function calls
* Assignments
* Operators
* Dependencies between tokens

### 4. Semantic Analysis

Extracts:

* Named entities
* Noun chunks
* Semantic relationships

---

## 🧩 Algorithms Used

### 🔹 Dependency Parsing

Used for identifying relationships between tokens.

### 🔹 Named Entity Recognition (NER)

Extracts meaningful entities from code comments and strings.

### 🔹 NLP-based Token Analysis

Uses spaCy linguistic processing pipeline.

---

## 📸 Screenshots

### Main Interface

(Add Screenshot Here)

### Syntax Analysis Output

(Add Screenshot Here)

### Semantic Analysis Output

(Add Screenshot Here)

---

## 🧪 Testing

The project was tested using:

* Simple Python functions
* Conditional statements
* Complex Python structures

### Validation Techniques

* Manual syntax verification
* Structured output inspection
* Dependency relationship validation

---

## 📌 Observations

* Successfully extracts syntactic dependencies
* Provides meaningful semantic insights
* GUI improves usability and interpretation
* Works effectively for educational purposes

---

## ⚠️ Limitations

* spaCy model is not specifically trained for Python code
* Complex Python syntax may not always parse correctly
* Does not perform full static code analysis

---

## 🔮 Future Improvements

* Train custom NLP models for Python
* Add AST visualization
* Add static code analysis
* Improve dependency accuracy
* Integrate with IDEs like VS Code

---

## 🎯 Applications

* Educational tool for learning Python
* Code comprehension
* Syntax visualization
* Dependency analysis
* Research in NLP for programming languages

---

## 👨‍💻 Author

**Snehal Late**
Computer Engineering Student
Vishwakarma University, Pune

---

## 📜 License

This project is developed for academic and educational purposes.

---

## ⭐ Acknowledgements

* spaCy NLP Library
* Python Community
* Vishwakarma University
* Tkinter Documentation
















 





