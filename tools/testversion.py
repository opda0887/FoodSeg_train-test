import torch, torchvision
import mmcv
from mmcv.ops import get_compiling_cuda_version, get_compiler_version
import mmseg

print('PyTorch Version:', torch.__version__)
print('Cuda avaliable:', torch.cuda.is_available())

print('MMCV version:', mmcv.__version__)
print('CUDA Version:', get_compiling_cuda_version())
print('Compiler Version:', get_compiler_version())

print('MMSEG version:', mmseg.__version__)

torch.cuda.empty_cache()
