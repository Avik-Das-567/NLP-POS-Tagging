import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

from nltk import word_tokenize, pos_tag

text = "I love natural language processing"
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

st.write(tagged)