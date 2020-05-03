"""Console script for ssl_certinfo."""
import argparse
import ipaddress
import sys

from ssl_certinfo import ssl_certinfo, validation


def check_hostname_or_ip_address(value):
    """Validate argparse type hostname/ip address."""
    if (
        not validation.is_valid_hostname(value)
        and not validation.is_valid_ip_address(value)
        and not validation.is_valid_ip_network(value)
    ):
        raise argparse.ArgumentTypeError(
            "%s is not a valid hostname or ip address" % value
        )
    return value


def check_positive(value):
    """Validate argparse type positive integer."""
    try:
        ivalue = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)

    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
    return ivalue


def check_valid_port(value):
    """Validate argparse type TCP port number."""
    try:
        ivalue = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)

    if ivalue <= 0 or ivalue > 65535:
        raise argparse.ArgumentTypeError("%s is an invalid port number" % value)
    return ivalue


def expand_hosts(hostlist):
    result = []

    for elem in hostlist:
        if validation.is_valid_hostname(elem) or validation.is_valid_ip_address(elem):
            result.append(elem)
        else:
            try:
                net = ipaddress.ip_network(elem, False)
            except ValueError:
                pass
            else:
                for ipaddr in net:
                    result.append(str(ipaddr))

    return result


def create_parser():
    """Create ArgParser."""
    parser = argparse.ArgumentParser(
        description="Collect information about SSL certificates from a set of hosts"
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose flag")

    parser.add_argument(
        "host",
        nargs="*",
        type=check_hostname_or_ip_address,
        help="Connect to HOST[:PORT]",
    )

    parser.add_argument(
        "-p",
        "--port",
        default=443,
        type=check_valid_port,
        help="Default TCP port to connnect to [0-65535]",
    )

    parser.add_argument(
        "-t",
        "--timeout",
        default=5,
        type=check_positive,
        help="Maximum time allowed for connection",
    )

    return parser


def main():
    """Console script for ssl_certinfo."""
    args = create_parser().parse_args()

    print("Arguments: " + str(args))

    ssl_certinfo.process_hosts(expand_hosts(args.host), args.port, args.timeout)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
