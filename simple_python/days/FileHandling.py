import os

class FileHandling(object):

    def __init__(self, filename):
        self.filename = filename

    def check_file_exists(self):
        file_full_name = "./" + self.filename
        if os.path.exists(file_full_name):
            return True

    def delete_existing_file(self):
        os.remove(self.filename)
        print('File deleted Successfully')

    def create_file(self):
        f = open(self.filename,'w+')
        f.close()

    def append_file(self, texts):
        f = open(self.filename, 'a')
        f.write(texts)
        f.close()

    def append_another_file_before(self,file):
        fh = open(file,'r')
        content = fh.read()
        self.append_file(content)


if __name__ == "__main__":
    fh = FileHandling('hello.txt')
    fh.create_file()
    if fh.check_file_exists():
        fh.append_file('Hello how are you')
        fh.append_file('\n')
        fh.append_file('Second Line')
        fh.append_file('\n')
        fh.append_file('Third Line')
