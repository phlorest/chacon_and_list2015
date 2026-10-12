import pathlib

import newick
import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "chacon_and_list2015"

    def cmd_makecldf(self, args):
        self.init(args)
        # hand-built consensus tree; its uniform branch lengths are a drawing artefact
        tree = newick.read(self.raw_dir / 'phylogeny_tukanoan.tre')[0]
        tree.remove_lengths()
        args.writer.add_summary(
            tree,
            self.metadata,
            args.log)
