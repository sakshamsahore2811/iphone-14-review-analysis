import os

def count_words(file_path):
    # read positive and negative word files and store them in a set
    positive_words = set()
    negative_words = set()
    with open(os.path.join(os.path.dirname(__file__), 'E:\Data Science 143\Review Article Analysis --iphone 14\Dictionary\positive-words.txt'), 'r') as f:
        for line in f:
            positive_words.add(line.strip())
    with open(os.path.join(os.path.dirname(__file__), 'E:/Data Science 143/Review Article Analysis --iphone 14/Dictionary/negative-words.txt'), 'r') as f:
        for line in f:
            negative_words.add(line.strip())

    # count positive and negative words in file
    positive_count = 0
    negative_count = 0
    with open(file_path, 'r',encoding='utf-8') as f:
        for line in f:
            for word in line.strip().split():
                if word.lower() in positive_words:
                    positive_count += 1
                elif word.lower() in negative_words:
                    negative_count += 1

    return positive_count, negative_count

# get list of all files in folder
folder_path = 'E:\Data Science 143\Review Article Analysis --iphone 14\Text data'  # replace with the path to your folder
file_names = os.listdir(folder_path)

# loop over files and count words
for file_name in file_names:
    if file_name.endswith('.txt'):
        file_path = os.path.join(folder_path, file_name)
        positive_count, negative_count = count_words(file_path)
        print(f'File: {file_name}')
        print(f'Positive count: {positive_count}')
        print(f'Negative count: {negative_count}')
