text = 'hello world'

def main():
    with open('output.txt', 'r') as file:
        content = file.read()

    content += f'\n{text}'
    open(f'output.txt', 'w').write(content)

if __name__ == '__main__':
    main()