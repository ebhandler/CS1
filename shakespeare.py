import csv

def count_words(filename, csv_filename):
    stop_words = ['and','the','an', 'to', 'of', 'i', 'a', 'in', 'is', 'it']
    word_dictionary = {}

    try:
        with open(filename, 'r') as file:
            for line in file:
                row = line.strip().split()

                for word in row:
                    word = word.lower()
                    if word in stop_words:
                        continue          
                    elif word in word_dictionary:
                        word_dictionary[word] += 1 
                    else:
                        word_dictionary[word] = 1  
        low_values = []

        for w,v in word_dictionary.items():
            if v < 5:
                low_values.append(w)

        for w in low_values:
            word_dictionary.pop(w)
        sorted_words = dict(sorted(word_dictionary.items(), key=lambda item: item[1], reverse = True))
        print(sorted_words)

        headers = ['Word', 'Count']

        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)

            for k, v in sorted_words.items():
                writer.writerow([k, v])
    except FileNotFoundError:
        print(f"Error: {filename} file not found.")

if __name__ == "__main__":
    count_words('Macbeth.txt', 'Macbeth.csv')
    count_words('Hamlet.txt', 'Hamlet.csv')







