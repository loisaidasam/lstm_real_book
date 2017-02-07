
import sys


def parse_line(line):
    data = {}
    pieces = line.split()
    data['bar'], data['beat'] = map(int, pieces[0].split(':'))
    data['time_start'] = float(pieces[1])
    data['duration_beats'] = int(pieces[2])
    data['time_stop'] = float(pieces[3])
    data['chord'] = pieces[4]
    data['chord_alt'] = pieces[5]
    data['key'] = pieces[6]
    return data


def sentence_builder(filename):
    # print "Building sentence for `%s`" % filename
    sentence = []
    with open(filename, 'r') as fp:
        for line in fp:
            line = line.strip()
            # print "line: `%s`" % line
            if not line:
                # Ignore blank lines
                continue
            data = parse_line(line)
            for i in xrange(data['duration_beats']):
                sentence.append(data['chord'])
    return sentence


def main():
    filename = sys.argv[1]
    sentence = sentence_builder(filename)
    print " ".join(sentence)


if __name__ == '__main__':
    main()
