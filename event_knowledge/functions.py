import pickle
import math

def CP(w1, w2, event2freq, V, event_pair2freq):
    if w1 not in event2freq or w2 not in event2freq:
        return None

    p_x = float(event2freq[w1])
    p_y = float(event2freq[w2])

    if w1 + " " + w2 not in event_pair2freq:
        p_xy = 0.0
    else:
        p_xy = float(event_pair2freq[w1 + " " + w2])
    if w2 + " " + w1 not in event_pair2freq:
        p_yx = 0.0
    else:
        p_yx = float(event_pair2freq[w2 + " " + w1])

    # add one smoothing
    PMI = math.log10((p_xy + p_yx + 2.0) / (p_x + V) / (p_y + V) * V * V)

    # Causal Potential
    return PMI + math.log10((p_xy + 1.0) / (p_yx + 1.0)) * 2


if __name__ == "__main__":
    # two options are provided here

    """
    # 1. consider event verb + preposition
    event2freq = pickle.load(open("all_phrase2freq.p", "rb"))
    event_pair2freqList = pickle.load(open("all_phrase_pair2freqList.p", "rb"))
    """
    
    # 2. only consider event verb
    event2freq = pickle.load(open("all_trigger2freq.p", "rb"))
    event_pair2freqList = pickle.load(open("all_trigger_pair2freqList.p", "rb"))
    V = float(len(event2freq))

    event1 = "graduate"
    event2 = "work"

    CPC = 0
    for i in range(0, 3):
        CP_result = CP(event1, event2, event2freq, V, event_pair2freqList[i])
        if CP_result != None:
            CPC += CP_result / float(i + 1)

    print event1, event2, CPC