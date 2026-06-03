def filter_and_sort_events(numbers):
    even_numbers=[num for num in numbers if num%2==0]
    return sorted(even_numbers)

def count_character_frequency(text):
    text_lower=text.lower()
    frequency_dictionary={}

    for char in text_lower:
        if char.isalpha():
            frequency_dictionary[char]=frequency_dictionary.get(char,0)+1
    return frequency_dictionary
    
if __name__=="__main__":
    print(filter_and_sort_events([3, 1, 4, 7, 1, 5, 9, 2, 6, 8]))
    print(count_character_frequency("This my task for Basic Data Structures & Algorithms"))