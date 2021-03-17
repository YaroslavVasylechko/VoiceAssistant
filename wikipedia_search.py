import wikipedia as wiki
import re

wiki.set_lang('en')

def normalize_text_for_wiki(sent):
    return re.sub(r'\(.*?\)', '', sent)

def request_to_wiki(sent):
    try:
        w = sent.split()
        d = []
        for i in w:
            if i not in ['what', 'is', 'who', 'it']:
                d.append(i)
        s2 = ' '.join(d)
        result = normalize_text_for_wiki(wiki.summary(s2, sentences = 2))
        return str(result)
    except wiki.exceptions.PageError:
        return('Sorry, but i don\'t know that')
    except:
        return('Sorry, but wikipedia is not available right now')