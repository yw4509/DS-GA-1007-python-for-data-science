def load_word_counts(filename):
    """
    Load a list of (word, count, percentage) tuples from a file where each
    line is of the form "word count percentage". Lines starting with # are
    ignored.
    """
    counts = []
    with open(filename, "r") as input_fd:
        for line in input_fd:
            if not line.startswith("#"):
                fields = line.split()
                counts.append((fields[0], int(fields[1]), float(fields[2])))
    return counts

def typeset_labels(labels=None, gap=5):
    """
    Given a list of labels, create a new list of labels such that each label
    is right-padded by spaces so that every label has the same width, then
    is further right padded by ' ' * gap.
    """
    labels = [str(i) for i in labels]
    label_lens = [len(s) for s in labels]
    label_width = max(label_lens)
    output = []
    for label in labels:
        label_string = label + ' ' * (label_width - len(label)) + (' ' * gap)
        output.append(label_string)
    assert len(set(len(s) for s in output)) == 1  # Check all have same length.
    return output


def get_ascii_bars(values, truncate=True, maxlen=10, symbol='#'):
    """
    Given a list of values, create a list of strings of symbols, where each
    strings contains N symbols where N = ()(value / minimum) /
    (maximum - minimum)) * (maxlen / len(symbol)).
    """
    maximum = max(values)
    if truncate:
        minimum = min(values) - 1
    else:
        minimum = 0
    
    # Type conversion to floats is required for compatibility with python 2,
    # because it doesn't do integer division correctly (it does floor divison
    # for integers).
    value_range=float(maximum - minimum)
    prop_values = [(float(value - minimum) / value_range) for value in values]
    
    # Type conversion to int required for compatibility with python 2
    biggest_bar = symbol * int(round(maxlen / len(symbol)))
    bars = [biggest_bar[:int(round(prop * len(biggest_bar)))]
            for prop in prop_values]
    
    return bars


def plot_ascii_bars(values, labels=None, screenwidth=80, gap=2, truncate=True):
    """
    Given a list of values and labels, create right-padded labels for each
    label and strings of symbols representing the associated values.
    """
    if not labels:
        try:
            values, labels = list(zip(*values))
        except TypeError:
            labels = len(values)
    labels = typeset_labels(labels=labels, gap=gap)
    bars = get_ascii_bars(values, maxlen=screenwidth - gap - len(labels[0]),
                          truncate=truncate)
    
    return [s + b for s, b in zip(labels, bars)]

