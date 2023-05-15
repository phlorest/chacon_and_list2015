import pathlib

import newick
import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "chacon_and_list2015"

    def cmd_makecldf(self, args):
        self.init(args)
        args.writer.add_summary(
            newick.read(self.raw_dir / 'phylogeny_tukanoan.tre')[0],
            self.metadata,
            args.log)
