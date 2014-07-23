'''
FileOpener:
Usage: python o.py
'''
import os, sys, re

path, file = os.path.split(__file__)

config_file = os.path.join(path, 'o.index')
if not os.path.exists(config_file):
    open(config_file, 'w').close()
file_index = open(config_file).readlines()

used_file = os.path.join(path, 'o.shortcuts')
if not os.path.exists(used_file):
    open(used_file, 'w').close()
used_index  = open(used_file).readlines()

roots = (
    ('', 'D:\\2seeVids'),
    ('', 'D:\\Ebooks'),
    ('', 'D:\\EdVideos'),
    ('', 'E:\\ET'),
    ('', 'E:\\TV'),
    ('', 'E:\\Pratap Musik')
)

def create_index():
    print 'Creating Index for'
    for root in roots:
        print root[1]
        for path, subdirs, files in os.walk(root[1]):
            for name in files:
                yield os.path.join(path, name) + '\n'
    print 'Index completed'
    return

def filter_index(words, any=0):
    phrase = ' '.join(words).lower()
    flag_cache = 1
    if any == 1:
        result = [i.split('\t')[2] for i in used_index if (i.split('\t')[0] == str(any) and phrase == i.split('\t')[1])]
        if result == []:
            result = [i for i in file_index if all(x in i.lower() for x in words)]
            flag_cache = 0
    else:
        result = [i.split('\t')[2] for i in used_index if (i.split('\t')[0] == str(any) and phrase in i.lower())]
        if result == []:
            result = [i for i in file_index if phrase in i.lower()]
            flag_cache = 0
    if len(result) == 1:
        print 'Opening %s' % result[0][:-1]
        print 'for: " %s "' % phrase
        if flag_cache == 0:
            open(used_file, 'a').write(str(any)+'\t'+phrase+'\t'+result[0][:-1]+'\n')
        os.startfile(result[0][:-1])
    else:
        for i in result:
            print i[:-1]
        print '%d files exist' % len(result)

if len(sys.argv) > 1 and sys.argv[1] == '-index':
    open(config_file, 'w').writelines(create_index())
    open(used_index, 'w').writelines('')
elif len(sys.argv) > 1 and sys.argv[1] == '.':
    filter_index(sys.argv[2:])
elif len(sys.argv) > 1 and sys.argv[1] == ',':
    filter_index(sys.argv[2:], any=1)
else:
    print 'Using a utility file'
    print 'Usage:'
    print 'To recreate index       :  python o.py -index'
    print 'To open a file          '
    print '             Phrase     :  python o.py . steve jobs'
    print '             Anywhere   :  python o.py , steve jobs books'
