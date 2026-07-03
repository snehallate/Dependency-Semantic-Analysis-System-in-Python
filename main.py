import spacy
import tkinter as tk
from tkinter import scrolledtext
# Load spaCy's pre-trained English model
nlp_model = spacy.load("en_core_web_sm")
# --- Helper Function to Get Token Type ---
def get_token_type(token):
    if token.pos_ in ['VERB', 'AUX']:
        return 'Keyword'
    elif token.pos_ in ['NOUN', 'PROPN']:
        return 'Identifier'
    elif token.pos_ == 'PUNCT':
        return 'Punctuator'
    elif token.pos_ == 'SYM':
        return 'Operator'
    elif token.pos_ in ['NUM', 'X']:
        return 'Literal (Numeric)'
    else:
        return 'Other'
# --- GUI Functions ---
def analyze_text():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Please enter a Python code snippet.")
        return
    doc = nlp_model(text)
    # Column headers with proper formatting
    result = "{:<20} {:<20} {:<20} {:<20} {:<20}\n".format("Token", "Head", "Dependency", "POS", "Type")
    result += "-" * 100 + "\n"
    for token in doc:
        token_type = get_token_type(token)
        result += "{:<20} {:<20} {:<20} {:<20} {:<20}\n".format(
            token.text, token.head.text, token.dep_, token.pos_, token_type
        )
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)
def perform_semantic_analysis():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        metrics_output.delete("1.0", tk.END)
        metrics_output.insert(tk.END, "Please enter a Python code snippet.")
        return
    doc = nlp_model(text)  
    result = "🧠 Named Entities:\n"
    result += "-" * 80 + "\n"
    for ent in doc.ents:
        result += f"{ent.text:<25} {ent.label_}\n"
    result += "\n🧩 Noun Chunks:\n"
    result += "-" * 80 + "\n"
    for chunk in doc.noun_chunks:
        result += f"{chunk.text:<25} → Head: {chunk.root.head.text}\n"
    metrics_output.delete("1.0", tk.END)
    metrics_output.insert(tk.END, result)

# --- GUI Setup ---
root = tk.Tk()
root.title("Python Code Dependency & Semantic Analyzer")
root.geometry("900x700")
tk.Label(root, text="Enter Python Code Snippet:", font=("Arial", 12)).pack()
input_text = scrolledtext.ScrolledText(root, height=4, width=100)
input_text.pack(pady=5)
analyze_button = tk.Button(root, text="Analyze Syntax", command=analyze_text, font=("Arial", 12))
analyze_button.pack(pady=5)
tk.Label(root, text="Syntactic Dependencies (Token - Head - Dependency - POS - Type):", font=("Arial", 12)).pack()
output_text = scrolledtext.ScrolledText(root, height=15, width=100)
output_text.pack(pady=5)
semantic_button = tk.Button(root, text="Perform Semantic Analysis", command=perform_semantic_analysis,
                            font=("Arial", 12), bg="lightblue")
semantic_button.pack(pady=5)
tk.Label(root, text="Semantic Analysis Output (Entities & Noun Chunks):", font=("Arial", 12)).pack()
metrics_output = scrolledtext.ScrolledText(root, height=15, width=100)
metrics_output.pack(pady=5)
root.mainloop()
