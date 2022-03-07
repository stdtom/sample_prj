"""Console script for sample_prj"""
import argparse
import sys

# import sample_prj
from sample_prj import sample_prj as asa

# from sample_prj.sample_prj import sayHello, sum


def main():
    """Console script for sample_prj."""
    parser = argparse.ArgumentParser()
    parser.add_argument("_", nargs="*")
    args = parser.parse_args()

    print("Arguments: " + str(args._))

    asa.sayHello()
    print("3 + 5 = " + str(asa.sum(3, 5)))

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
