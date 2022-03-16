import os.path
import pathlib
import sys
import json
from app.pubmed.source_ftp import PubMedFTP
from app.pubmed.data_extractor import parse_pubmed_xml_gzipped, get_object_structure


def print_valid_modes():
    print("Valid Modes:", file=sys.stderr)
    print(" - sync: Synchronise the data files from the PubMed FTP server", file=sys.stderr)
    print(" - test: Run the test Flask webserver", file=sys.stderr)


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print("Expected a run-mode to be supplied.", file=sys.stderr)
        print_valid_modes()
        sys.exit(1)

    mode = args[1]
    if mode == "sync":
        with PubMedFTP() as ftp:
            targets = ftp.sync("./data")

        # Write an example file for us to look at the available data.
        example_target = targets[0]
        example_target_parts = pathlib.Path(example_target).parts
        example_object = parse_pubmed_xml_gzipped(targets[0])
        example_filename = example_target_parts[-2] + example_target_parts[-1]
        example_filename = example_filename[:example_filename.index(".")]
        example_file = "./data/example." + example_filename + ".json"
        with open(example_file, "w") as f:
            f.write(json.dumps(example_object, indent=2, sort_keys=True))

        # Write out a file containing the structure of the example file.
        example_structure_file = "./data/example." + example_filename + ".structure.txt"
        example_structure = get_object_structure(example_object)
        with open(example_structure_file, "w") as f:
            f.write(example_structure)

    elif mode == "test":
        # Run a test server.
        from app import app as application
        application.run(host='0.0.0.0', port=8080, debug=True)
