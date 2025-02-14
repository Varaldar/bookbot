def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)
    words = file_contents.split() # Split the file contents into a list of words
    total_words = len(words) # Count the number of words in the list
    #print(total_words)
    individual_letters = list(file_contents.lower()) # Split file contents into lowercase words
    count_dict = {}
    for i in individual_letters:
        if i in count_dict:
            count_dict[i] += 1
        else: 
            count_dict[i] = 1       
    print(count_dict)
    #test
main()