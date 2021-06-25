def read_file(filename):
    records = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            records.append(line.strip())
    return records

def convert(records):
    new = []
    person = None
    for record in records:
        if record == 'Allen':
            person = record
            continue
        elif record == 'Tom':
            person = record
            continue
        if person:
            new.append(person + ': ' + record)
    return new
    
def write_file(filename, records):
    with open(filename, 'w', encoding='utf-8-sig') as f:
        for record in records:
            f.write(record + '\n')



def main():
    records = read_file('input.txt')
    records = convert(records)
    write_file('output.txt', records)

main()