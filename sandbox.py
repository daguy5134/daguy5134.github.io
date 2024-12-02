def four_gram_nested():
    return defaultdict(trigram_nested)
def trigram_nested():
    return defaultdict(final_dict)
def final_dict():
    return defaultdict(Counter)
