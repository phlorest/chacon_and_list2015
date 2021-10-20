import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "chacon_and_list2015"

    def cmd_makecldf(self, args):
        self.init(args)
        with self.nexus_summary() as nex:
            self.add_tree_from_newick(args, self.raw_dir / 'phylogeny_tukanoan.tre', nex, 'summary')
