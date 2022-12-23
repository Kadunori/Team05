def topl(ngram_lists):
    l = 10
    ngram_dict = {}
    ngram_topl_list = []
    for ngram_list in ngram_lists:
        ngrams = tuple(ngram_list)
        if ngrams not in ngram_dict.keys():
            ngram_dict[ngrams] = 0
        ngram_dict[ngrams] += 1
        dic2 = dict(sorted(ngram_dict.items(), key=lambda x:x[1], reverse=True))
        i = 0
    for ngrams in dic2.keys():
        ngram_topl_list.append(list(ngrams))
        i+=1
        if i == l:
            break      
    return ngram_topl_list

