from tools.formatter import capitalize_words
from tools.io_helpers import read_input, print_stats
from tools.file_ops import save_text_to_file, read_text_from_file
from tools.utils.reverse import reverse_words

text = read_input()
save_text_to_file(text)
loaded_text = read_text_from_file()

print(capitalize_words(loaded_text))
print_stats(loaded_text)
print(reverse_words(loaded_text))