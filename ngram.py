def make_ngram(txt_list):
    N = 4
    words = txt_list[1]
    result = []
    ngram_list = []

    for it in range(len(words)):
        if it + N > len(words):
            break
        result.append(words[it:it+N])
    ngram_list.append(txt_list[0])
    ngram_list.append(result)
    
    return ngram_list