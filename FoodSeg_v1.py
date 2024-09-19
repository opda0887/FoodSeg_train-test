from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset

@DATASETS.register_module()
class FoodDataset(BaseSegDataset):

	METAINFO = dict(
		CLASSES = ('background', 'candy', 'egg tart', 'french fries', 'chocolate', 'biscuit', 'popcorn', 'pudding', 'ice cream', 'cheese butter', 'cake', 'wine', 'milkshake', 'coffee', 'juice', 'milk', 'tea', 'almond', 'red beans', 'cashew', 'dried cranberries', 'soy', 'walnut', 'peanut', 'egg', 'apple', 'date', 'apricot', 'avocado', 'banana', 'strawberry', 'cherry', 'blueberry', 'raspberry', 'mango', 'olives', 'peach', 'lemon', 'pear', 'fig', 'pineapple', 'grape', 'kiwi', 'melon', 'orange', 'watermelon', 'steak', 'pork', 'chicken duck', 'sausage', 'fried meat', 'lamb', 'sauce', 'crab', 'fish', 'shellfish', 'shrimp', 'soup', 'bread', 'corn', 'hamburg', 'pizza', ' hanamaki baozi', 'wonton dumplings', 'pasta', 'noodles', 'rice', 'pie', 'tofu', 'eggplant', 'potato', 'garlic', 'cauliflower', 'tomato', 'kelp', 'seaweed', 'spring onion', 'rape', 'ginger', 'okra', 'lettuce', 'pumpkin', 'cucumber', 'white radish', 'carrot', 'asparagus', 'bamboo shoots', 'broccoli', 'celery stick', 'cilantro mint', 'snow peas', ' cabbage', 'bean sprouts', 'onion', 'pepper', 'green beans', 'French beans', 'king oyster mushroom', 'shiitake', 'enoki mushroom', 'oyster mushroom', 'white button mushroom', 'salad', 'other ingredients'),
		PALETTE = [[82, 94, 117], [255, 105, 180], [240, 150, 80], [255, 211, 77], [210, 105, 30], [222, 184, 135], [255, 239, 160], [244, 242, 177], [255, 182, 193], [255, 223, 87], [250, 112, 190], [128, 0, 0], [255, 240, 245], [111, 78, 55], [255, 165, 0], [250, 250, 250], [205, 133, 63], [255, 235, 205], [165, 42, 42], [255, 222, 173], [220, 20, 60], [255, 248, 220], [160, 82, 45], [245, 222, 179], [255, 255, 224], [255, 8, 0], [153, 76, 0], [251, 206, 177], [86, 130, 3], [255, 225, 53], [252, 90, 141], [222, 49, 99], [79, 134, 247], [227, 11, 93], [255, 179, 71], [128, 128, 0], [255, 229, 180], [255, 247, 0], [209, 226, 49], [143, 96, 78], [86, 60, 13], [111, 45, 168], [142, 229, 63], [247, 183, 163], [255, 127, 0], [252, 108, 133], [101, 67, 33], [255, 192, 203], [255, 218, 185], [205, 92, 92], [153, 101, 21], [116, 84, 81], [139, 69, 19], [255, 140, 0], [70, 130, 180], [255, 153, 85], [255, 107, 107], [255, 228, 196], [188, 133, 67], [255, 254, 173], [101, 82, 22], [255, 160, 122], [255, 250, 205], [255, 239, 213], [255, 181, 108], [255, 228, 181], [255, 255, 240], [181, 101, 29], [245, 245, 245], [147, 112, 219], [226, 188, 144], [255, 20, 147], [250, 250, 210], [255, 99, 71], [85, 107, 47], [46, 139, 87], [127, 255, 0], [255, 255, 102], [218, 165, 32], [143, 188, 143], [124, 252, 0], [227, 100, 20], [152, 251, 152], [230, 230, 230], [250, 128, 114], [60, 179, 113], [240, 230, 140], [34, 139, 34], [173, 255, 47], [0, 128, 0], [85, 139, 47], [85, 255, 85], [245, 245, 220], [234, 190, 143], [255, 69, 0], [50, 205, 50], [0, 255, 0], [210, 180, 140], [112, 66, 20], [255, 248, 240], [238, 232, 170], [250, 240, 230], [144, 238, 144], [211, 211, 211]]
	)

	# img_suffix='.jpg' and seg_map_suffix='.png' are default values
	def __init__(self,
                 seg_map_suffix='.png',
                 reduce_zero_label=False,	# label_id=0 is reserved for background
                 **kwargs) -> None:
		super().__init__(
			seg_map_suffix=seg_map_suffix,
			reduce_zero_label=reduce_zero_label,
			**kwargs
		)