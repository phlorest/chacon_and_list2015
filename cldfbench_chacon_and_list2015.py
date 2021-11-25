import pathlib

import phlorest
from phlorest.nexuslib import newick2nexus


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "chacon_and_list2015"

    def cmd_makecldf(self, args):
        self.init(args)
        args.writer.add_summary(
            newick2nexus(self.raw_dir.read('phylogeny_tukanoan.tre')),
            self.metadata,
            args.log)
