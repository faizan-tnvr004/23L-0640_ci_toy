def add(a, b):
    return a - b  # bug introduced on purpose to see a red run


def is_ai(p_ai, threshold=0.5):
    return p_ai >= threshold
