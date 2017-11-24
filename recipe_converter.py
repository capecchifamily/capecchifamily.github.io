import glob
import pypandoc


def main():

    path = 'C:\\Users\\Owner\\Google Drive\\Recipes\\'
    md_path =
    files = glob.glob(path+'*.*')
    filenames = [f[len(path):] for f in files]
    filenames = [f.split('.')[0] for f in filenames]
    a=1
    for i, f in enumerate(files):
        output = pypandoc.convert_file(f, 'md', outputfile=filenames[i]+'.md')


if __name__ == '__main__':
    main()