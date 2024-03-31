from torch.utils.data.dataset import ConcatDataset as _ConcatDataset
from torch.utils.data.dataset import Dataset

from .builder import DATASETS


@DATASETS.register_module()
class ConcatDataset(_ConcatDataset):
    """A wrapper of concatenated dataset.
    Same as :obj:`torch.utils.data.dataset.ConcatDataset`, but
    add `get_cat_ids` function.
    Args:
        datasets (list[:obj:`Dataset`]): A list of datasets.
    """

    def __init__(self, datasets: list):
        super(ConcatDataset, self).__init__(datasets)


@DATASETS.register_module()
class RepeatDataset(object):
    """A wrapper of repeated dataset.
    The length of repeated dataset will be `times` larger than the original
    dataset. This is useful when the data loading time is long but the dataset
    is small. Using RepeatDataset can reduce the data loading time between
    epochs.
    Args:
        dataset (:obj:`Dataset`): The dataset to be repeated.
        times (int): Repeat times.
    """

    def __init__(self, dataset: Dataset, times: int):
        self.dataset = dataset
        self.times = times

        self._ori_len = len(self.dataset)

    def __getitem__(self, idx: int):
        return self.dataset[idx % self._ori_len]

    def __len__(self):
        return self.times * self._ori_len