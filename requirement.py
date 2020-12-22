import os

libs = {"redis"}


def main():
    try:
        for lib in libs:
            os.system("pip3 install " + lib)
            print(lib, "succeed installation")
        print("\nAll Successful")
    except:
        print("Failed")


if __name__ == '__main__':
    main()
