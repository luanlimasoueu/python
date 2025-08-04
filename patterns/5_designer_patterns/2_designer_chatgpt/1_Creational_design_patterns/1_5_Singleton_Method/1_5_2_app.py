import config

def main():
    print(config.valor)
    config.valor = 99
    print(config.valor)

if __name__ == "__main__":
    main()