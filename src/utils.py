from pathlib import PosixPath


def build_plots_dir_path(root_dir: PosixPath):
    return root_dir / 'book' / '_static' / 'plots'


def build_cache_dir_path(root_dir: PosixPath):
    return root_dir / 'cache'
