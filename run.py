import cli

def main():
    print("River Top Trumps")
    c = cli.RiverCLI()
    c.cmdloop()

    exit(0)


if __name__ == "__main__":
    main()