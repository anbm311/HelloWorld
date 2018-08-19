def fileopening():
    with open("Demo.txt", "w") as f:
        #filecontent = f.read().split()
        f.write("Take it easy\n")
        f.write("what elase you want")
       # f.writelines("what the hell")

    file = open("Demo.txt")
    print(file.readlines())
    file.close()
    
   # for sentence in filecontent:
    #    print(sentence)


if __name__ == "__main__":
    fileopening()
