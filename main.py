import sys, re, math 

input_file = sys.argv[1]
output_file = sys.argv[2]
sec_offset = int(sys.argv[3])

def to_time(num):
    if num < 10:
        return '0'+str(int(num))
    else:
        return str(int(num))

def convert_time(time):
    h, m, s = time
    return to_time(h), to_time(m), to_time(s)

def shift_time(time, sec_offset):
    h, m, s = time
    new_s = s + sec_offset
    new_m = m + math.floor(new_s / 60)
    new_h = h + math.floor(new_m / 60)
    return (new_h, new_m%60, new_s%60)

with open(input_file, 'r') as fp:
    text = fp.read().strip()
lines = re.split('\r?\n\r?\n', text)

new_lines = []
subtitles = []

time_format = '{}:{}:{},{} --> {}:{}:{},{}'
for line in lines:
    r = re.search('([0-9]{2}):([0-9]{2}):([0-9]{2}),([0-9]{3}) --> ([0-9]{2}):([0-9]{2}):([0-9]{2}),([0-9]{3})', line)
    r1 = re.search('\n(.+$)', line)
    subtitles.append(r1.group(1))
    time1 = int(r.group(1)), int(r.group(2)), int(r.group(3))
    time2 = int(r.group(5)), int(r.group(6)), int(r.group(7))
    nt1 = convert_time(shift_time(time1, sec_offset))
    nt2 = convert_time(shift_time(time2, sec_offset))
    new_line = time_format.format(nt1[0], nt1[1], nt1[2], r.group(4), nt2[0], nt2[1], nt2[2], r.group(8))
    new_lines.append(new_line)

with open(output_file, 'w') as fp:
    for i, line in enumerate(new_lines):
        fp.write('{}\n{}\n{}\n\n'.format(i+1, line, subtitles[i]))