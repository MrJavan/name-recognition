f1 = open("data/file1.txt", "r")
f2 = open("data/file2.txt" , "r")
f3 = open("data/file3.txt" , "r")
# f4 = open("file4.txt" , "r")
# f5 = open("file5.txt" , "r")

file1 = f1.read()
file2 = f2.read()
file3 = f3.read()
# file4 = f4.readline()
# file5 = f5.readline()


def search (file1 , file2 ,file3 , text):
    for i in file1, file2, file3 :
        if text in file1:
            print("its Male name")
            return
        elif text in file2:
            print("its Woman name")
            return
        elif text in file3:
            print("its Region name")
            return
        # elif text in file4:
        #     print("found in file4")
        #     return
        # elif text in file5:
        #     print("found in file5")
        #     return
    print("notfound")

text = input('Enter your world:')

search(file1 , file2, file3, text)