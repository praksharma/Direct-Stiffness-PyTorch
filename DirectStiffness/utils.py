import torch
from loguru import logger

class Config():
    """
    A configuration class to manage different settings.
    float_type: default data type.
    torch_seed: seed, pretty sure this is redundant
    device: device to run the tensors on
    """
    def __init__(self,
                 torch_type=torch.float32, torch_seed=0, device = "cpu", device_override = False) -> None:
        logger.debug("Config init called")
        self.float_type = torch_type # will implement this is future
        self.torch_seed = torch_seed # not sure if I will need it.
        self.device = self._select_device()
        if device_override:
            torch.set_default_device(torch.device(device))
            logger.debug(f"Manual device override detected. Using {device} as the default device.")
        else:
            torch.set_default_device(self.device)
            logger.debug(f"Using {self.device} as the default device.")
    
    def _torch_seeds(self):
        """Not using it right now."""
        torch.manual_seed(self.torch_seed)

    def _apply_float_type(self):
        """Not using it right now."""
        torch.set_default_dtype(self.float_type)

    def _select_device(self):
        if torch.cuda.is_available(): 
            logger.debug(f"NVIDIA GPU detected : {torch.cuda.get_device_name()}") # single GPU assumption
            return torch.device("cuda")
            
        elif torch.backends.mps.is_available():
            logger.debug(f"Apple Silicon metal framework detected.")
            return torch.device("mps")
        else:
            logger.debug(f"No Device acceleration was found. Falling back to CPU")
            return torch.device("cpu")

    def _default_device(self):
        """
        In case you wanted to force a specific device.
        """
        torch.set_default_device(self.device)

    def _accelerate_computation(self):
        """
        For now stick to default values and find out what they do and if they are even useful.
        """
        torch.backends.cudnn.deterministic = False
        torch.backends.cudnn.benchmark = False