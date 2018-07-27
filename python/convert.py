def cyrillic_to_latin(word):
    cyr_alphabet_s = "йцукенгшщзхъфывапролджэячсмитьбю"
    cyr_alphabet_c = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
    lat_alphabet_s = "yüukenqşhzxjfıvaproldcgəçsmitğbö"
    lat_alphabet_c = "YÜUKENQŞHZXJFIVAPROLDCGƏÇSMİTĞBÖ"
    
    cyr = cyr_alphabet_s+cyr_alphabet_c
    lat = lat_alphabet_s+lat_alphabet_c
    conv_dict = dict(zip(cyr, lat))
    
    new_word = ""
    for i in range(0, len(word)):
        c = word[i]
        if c not in conv_dict:
            new_word = new_word + c
        else:
            new_word = new_word + conv_dict[c]
    return new_word