import glob
import pypandoc


def main():

    path = 'C:\\Users\\Owner\\Google Drive\\Recipes\\'
    md_path = 'C:\\Users\\Owner\\Documents\\GitHub\\capecchifamily.github.io\\_posts\\'
    files = glob.glob(path+'*.*')
    files = [f for f in files if '~' not in f]
    filenames = [f[len(path):] for f in files]
    filenames = [f.split('.')[0] for f in filenames]
    a=1
    for i, f in enumerate(files):
        output = pypandoc.convert_file(f, 'md', outputfile=md_path+filenames[i]+'.md')
        print(md_path+filenames[i]+'.md')



if __name__ == '__main__':
    main()