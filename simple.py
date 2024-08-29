import argparse

def main(num_a, num_b):
    print(f'num_a: {num_a}')
    print(f'num_b: {num_b}')
    print(f'sum: {num_a + num_b}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process two numbers.")
    parser.add_argument("num_a", type=int)
    parser.add_argument("num_b", type=int)
    args = parser.parse_args()

    main(args.num_a, args.num_b) 
