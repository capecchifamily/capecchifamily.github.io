import glob
import docx
from shutil import copyfile
import os



def main():

    path = 'C:\\Users\\Owner\\Google Drive\\Recipes\\'
    github = 'C:\\Users\\Owner\\Documents\\GitHub\\capecchifamily.github.io\\'
    md_path = github + '_posts\\'

    '''First we delete all present posts in order to update them all again, below'''
    posts = glob.glob(md_path+'*.*')
    for p in posts:
        os.remove(p)

    '''And we restock the Recipes folder with the template from github since we know it hasn't been saved over
    while also deleting anything in there that isn't .docx'''
    googledrive_files = glob.glob(path+'*.*')
    you_shouldnt_be_here = [f for f in googledrive_files if f[-5:] != '.docx']
    for f in you_shouldnt_be_here:
        os.remove(f)
    copyfile(github + '_RECIPE_TEMPLATE_.docx', path + '_RECIPE_TEMPLATE_.docx')

    img_path = 'C:\\Users\\Owner\\Documents\\GitHub\\capecchifamily.github.io\\images\\'
    files = glob.glob(path+'*.*')
    files = [f for f in files if '~' not in f]
    files.remove(path+'_RECIPE_TEMPLATE_.docx')
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
            #print(p.text)
            if '<img>' in p.text:
                img_fn = p.text[5:].strip()
                if os.path.isfile(path+'images\\'+img_fn):
                    if not os.path.isfile(img_path+img_fn):  # if not present, add to github images folder
                        copyfile(path + 'images\\' + img_fn, img_path + img_fn)
                    tf.write('!['+img_fn+'](\\images\\'+img_fn + ' "'+img_fn.split('.')[0]+'")\n')
            else:
                if '### Instructions' in p.text:
                    ingredients = False
                if ingredients and len(p.text) > 1:
                    tf.write('- ')
                if '### Ingredients' in p.text:
                    ingredients = True
                if '###' in p.text:
                    tf.write('***\n\n')
                tf.write(p.text + "  \n")

        tf.close()
        print(md_path+filenames[i]+'.md')


if __name__ == '__main__':
    main()