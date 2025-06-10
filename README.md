# POS Tagging in NLP
### App Link
- https://nlp-pos-tagging.streamlit.app/
---
### What is POS Tagging?
- POS stands for **Part of Speech**.
- POS Tagging means **labeling each word** in a sentence with its **part of speech** (noun, verb, adjective, etc.)
- It helps machines understand **grammatical structure** and **meaning** in text.
---
### Example Sentence : 
**`"The cat sat on the mat"`**

POS Tags :
- The (Determiner)
- cat (Noun)
- sat (Verb)
- on (Preposition)
- the (Determiner)
- mat (Noun)
---
### Why Use POS Tagging?
- Helps in **text analysis**, **sentiment analysis**, and **information extraction**.
- Important for **parsing**, **question answering**, **chatbots**, etc.
- Assists in **removing unwanted words** (like only keeping nouns/verbs for analysis).
---
### Required Python Packages
- **`nltk`**
- **`streamlit`**
---
### How the App Works -
- **Input :**
```
text = "I love natural language processing"
```
- **Output :**
```
[('I', 'PRP'), ('love', 'VBP'), ('natural', 'JJ'), ('language', 'NN'), ('processing', 'NN')]
```
- Output shows each word tagged with its part of speech :
  - **`PRP` : Personal Pronoun**
  - **`VBP` :** **Verb**, present (non-3rd person)
  - **`JJ` :** **Adjective**
  - **`NN` :** **Noun**, singular
---
### Additional Insights :
- POS tagging helps chatbots understand what action to take.
- Different tag sets like **Penn Treebank** are used.
- Some words can have **multiple POS** based on context.
---
