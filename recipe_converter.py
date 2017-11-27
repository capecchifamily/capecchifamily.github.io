import glob
import docx


def main():

    path = 'C:\\Users\\Owner\\Google Drive\\Recipes\\'
    md_path = 'C:\\Users\\Owner\\Documents\\GitHub\\capecchifamily.github.io\\source\\_posts\\'
    files = glob.glob(path+'*.*')
    files = [f for f in files if '~' not in f]
    filenames = [f[len(path):] for f in files]
    filenames = [f.split('.')[0] for f in filenames]
    a=1

#author, modified, yyyy-mm-dd

    for i, f in enumerate(files):
        doc = docx.Document(f)
        modified = doc.core_properties.modified
        y = str(modified.year)
        m = str(modified.month)
        d = str(modified.day)
        while len(m) < 2:
            m = '0'+m
        while len(d) < 2:
            d = '0'+d
        tf = open(md_path + y+'-'+m+'-'+d+'-'+'_'.join(filenames[i].split(' ')) + '.md', 'w', encoding='utf-8')
        ingredients = False
        for p in doc.paragraphs:
#            print(p.text)
            if '### Instructions' in p.text:
                ingredients = False
            if ingredients and len(p.text) > 1:
                tf.write('- ')
            if '### Ingredients' in p.text:
                ingredients = True

            if '###' in p.text:
                tf.write('***\n\n')
            tf.write(p.text+"  \n")
        tf.close()
        print(md_path+filenames[i]+'.md')


if __name__ == '__main__':
    main()