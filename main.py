text = 'hello world'

# import random
# r = random.randint(1, 100)

def main():
    with open('output.txt', 'r') as file:
        content = file.read()

    content += f'\n{text}'
    open(f'output.txt', 'w').write(content)

if __name__ == '__main__':
    main()