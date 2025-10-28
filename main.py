text = 'hello world'

import random
r = random.randint(1, 100)

def main():
    open(f'output{r}.txt', 'w').write(text)

if __name__ == '__main__':
    main()