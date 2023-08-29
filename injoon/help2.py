# Extract conversations from the Excel file in a concatenated format
concatenated_conversations_list = []

for _, row in general_data_excel.iterrows():
    # Concatenate all the user and system sentences to form the conversation
    conversation = ' '.join([str(row[f'사람문장{i}']) + ' ' + str(row[f'컴퓨터문장{i}']) 
                             for i in range(1, 4) if pd.notnull(row[f'사람문장{i}']) and pd.notnull(row[f'컴퓨터문장{i}'])]).strip()
    if conversation:
        concatenated_conversations_list.append(conversation)

# Create a DataFrame with the concatenated conversations and label them as '일반 대화'
concatenated_conversations_df = pd.DataFrame({
    'class': ['일반 대화'] * len(concatenated_conversations_list),
    'conversation': concatenated_conversations_list
})

# Display the first few concatenated conversations
concatenated_conversations_df.head()



# Display the column names of the Excel file to understand the structure
general_data_excel.columns

# Extract conversations from the Excel file in a concatenated format
concatenated_conversations_list = []

for _, row in general_data_excel.iterrows():
    # Concatenate all the user and system sentences to form the conversation
    conversation = ' '.join([str(row[f'사람문장{i}']) + ' ' + str(row[f'시스템문장{i}']) 
                             for i in range(1, 4) if pd.notnull(row[f'사람문장{i}']) and pd.notnull(row[f'시스템문장{i}'])]).strip()
    if conversation:
        concatenated_conversations_list.append(conversation)

# Create a DataFrame with the concatenated conversations and label them as '일반 대화'
concatenated_conversations_df = pd.DataFrame({
    'class': ['일반 대화'] * len(concatenated_conversations_list),
    'conversation': concatenated_conversations_list
})

# Display the first few concatenated conversations
concatenated_conversations_df.head()




# Display the first concatenated general conversation example from the Excel dataset
concatenated_conversations_df.iloc[0]['conversation']

#'일은 왜 해도 해도 끝이 없을까? 화가 난다. 많이 힘드시겠어요. 주위에 의논할 상대가 있나요? 그냥 내가 해결하는 게 나아. 남들한테 부담 주고 싶지도 않고. 혼자 해결하기로 했군요. 혼자서 해결하기 힘들면 주위에 의논할 사람을 찾아보세요.'
