def numbers():
    try:
        with open("./numbers.txt", 'r') as file:
            content = file.read()
        Numbers = content.split(',')
        for Number in Numbers:
            print(Number)
    except Exception as e:
        print(f"an error accurred : {e}")


if __name__ == '__main__':
    numbers()