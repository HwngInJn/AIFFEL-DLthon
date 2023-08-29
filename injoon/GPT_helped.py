import pandas as pd

# Load the provided file
data = pd.read_csv('/mnt/data/train.csv')

# Display the first few rows of the dataset
data.head()

# Check for missing values
missing_values = data.isnull().sum()

missing_values

# Check the distribution of classes
class_distribution = data['class'].value_counts()

class_distribution

# Calculate the length of each conversation
data['conversation_length'] = data['conversation'].apply(len)

# Check the distribution of conversation lengths
conversation_length_stats = data['conversation_length'].describe()

conversation_length_stats

import re

def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters and numbers
    text = re.sub(r'[^가-힣a-z\s]', ' ', text)
    
    # Remove extra spaces
    text = ' '.join(text.split())
    
    return text

# Apply the cleaning function to the conversation column
data['cleaned_conversation'] = data['conversation'].apply(clean_text)

# Display the cleaned conversations for the first few rows
data[['conversation', 'cleaned_conversation']].head()


import sentencepiece as spm

# Save cleaned conversations to a text file for training SentencePiece
with open('/mnt/data/cleaned_conversations.txt', 'w', encoding='utf-8') as f:
    for line in data['cleaned_conversation']:
        f.write(line + '\n')

# Train SentencePiece model
spm.SentencePieceTrainer.Train('--input=/mnt/data/cleaned_conversations.txt --model_prefix=sp_model --vocab_size=20000')

# Load trained SentencePiece model
sp = spm.SentencePieceProcessor()
sp.Load("sp_model.model")


# Tokenize sample conversations using the trained SentencePiece model
sample_conversations = data['cleaned_conversation'].head()
tokenized_samples = [sp.EncodeAsPieces(text) for text in sample_conversations]

tokenized_samples


from sklearn.preprocessing import LabelEncoder

# 1. Standardize sentence length to 300 characters
def standardize_length(text, length=300):
    if len(text) > length:
        return text[:length]
    else:
        return text.ljust(length)  # Add padding to the right if text is shorter than desired length

data['standardized_conversation'] = data['cleaned_conversation'].apply(standardize_length)

# 2. Encode class labels
label_encoder = LabelEncoder()
data['encoded_class'] = label_encoder.fit_transform(data['class'])

# Display the standardized and encoded data for the first few rows
data[['cleaned_conversation', 'standardized_conversation', 'class', 'encoded_class']].head()



