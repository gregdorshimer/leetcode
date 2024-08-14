from collections import deque

def predictPartyVictory(senate):
    """
    :type senate: str
    :rtype: str
    """
    deq = deque(senate)
    while len(deq) > 0:
        if deq[0] == 'R':
            try:
                deq.remove('D')
                deq.rotate(-1)
            except:
                return 'Radiant'
        else:
            try:
                deq.remove('R')
                deq.rotate(-1)
            except:
                return 'Dire'
