import argparse
import json
from caseweaver_core.solvers.openfoam.manager import detect_openfoam


def main() -> None:
    parser = argparse.ArgumentParser(prog="caseweaver")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("serve")
    sub.add_parser("generate")
    ing = sub.add_parser("ingest")
    ing.add_argument("path")
    of = sub.add_parser("openfoam")
    of.add_argument("action", choices=["detect", "versions", "validate", "update", "install", "use", "docker-pull"])

    args = parser.parse_args()
    if args.cmd == "openfoam" and args.action == "detect":
        print(json.dumps(detect_openfoam(), indent=2))
    else:
        print(f"Command '{args.cmd}' acknowledged in MVP.")

if __name__ == "__main__":
    main()
