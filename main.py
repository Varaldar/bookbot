def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read() 
    #print(file_contents)
    words = file_contents.split() # split book into words
    total_words = len(words) # count words in book
    #print(total_words)
    individual_letters = list(file_contents.lower()) # Split book into all lowercase words
    count_dict = {} #creates empty dict for letter counts
    for i in individual_letters: #for each letter in the book
        if i in count_dict: #if that letter is in the dict
            count_dict[i] += 1 #icrement by one
        else: 
            count_dict[i] = 1   #add it to the dict    
    #print(count_dict)

    list_dicts = [] # create empty list
    for i in count_dict: #for every dict entry in dict
        if i.isalpha(): #if the character is a letter
            list_dicts.append({"letter": i, "number": count_dict[i]}) # create a dict per letter and append it to the list
    #print(list_dicts)
    def sort_on(dict): 
        return dict["number"] #tells the sort fucntion with the sort_on key to look at the number half of the dict, not the letter

    list_dicts.sort(reverse=True, key=sort_on) #sorts the list, by the number key in reverse (greatest to smallest) order.
    print(list_dicts)
main()