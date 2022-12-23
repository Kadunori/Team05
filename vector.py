def vector(ngram,topl):
    sample = [0] * 10
    for ngrams in ngram:
        if ngrams in topl:
            sample[topl.index(ngrams)] = 1
    return sample

