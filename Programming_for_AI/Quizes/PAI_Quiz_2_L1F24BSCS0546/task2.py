def build_vocab_index(corpus):

    result = {
        t: {
            "token_id": idx, 
            'char_len' : len(t)
        }

        for c in corpus
        
        for idx, t in enumerate(c.lower().split())

    }


    return result





print(build_vocab_index(["AI is transformative", "data is fuel for AI"]))