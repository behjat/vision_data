import glob
import vision_data


class SUN397(vision_data.VisionDataset):
    """
    Uses the provided dataset splits to locate the images.
    """

    def __init__(self):
        super(SUN397, self).__init__(name='sun397',
                                    data_urls={('58b3a6f1b8d6ec003458f940ada226bb',
                                                'SUN397.tar'): ['http://groups.csail.mit.edu/vision/SUN/SUN397.tar'],
                                               ('29a205c0a0129d21f36cbecfefe81881',
                                                'Partitions.zip'): ['http://people.csail.mit.edu/jxiao/SUN/download/Partitions.zip']
                                               },
                                    homepage='http://groups.csail.mit.edu/vision/SUN/',
                                    bibtexs=None,
                 overview=None)

    def scene_rec_parse(self, split='train'):
        """
        Args:
            split: Dataset split, one of 'train', 'test' (default: train)
        
        Returns:
            Dataset as specified by 'split'

            Data is in the form of [image_path] = scene_name
        """
        if split == 'train':
            g = 'Training_*.txt'
        elif split == 'test':
            g = 'Testing_*.txt'
        else:
            raise ValueError('Invalid split vlaue')
        out = {}
        print(self.dataset_path + g)
        for images_fn in glob.glob(self.dataset_path + g):
            print(images_fn)
            with open(images_fn) as fp:
                for image_name in fp:
                    image_name = image_name.strip()
                out['%sSUN397%s' % (self.dataset_path, image_name)] = image_name.split('/')[2]
        return out
