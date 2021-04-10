import os, sys, time
import numpy as np
cwd = os.getcwd()
parent = os.path.join(cwd, os.path.join(os.path.dirname("__file__")))
sys.path.append(os.path.join(parent, 'chofer_torchex'))
sys.path.append(os.path.join(parent, 'tda-toolkit'))

from src.animal.generate_dgm_provider import generate_dgm_provider
from src.animal.experiments import experiment
from src.sharedCode.data_downloader import download_provider, download_raw_data
from src.sharedCode.gui import ask_user_for_provider_or_data_set_download
provider_path = os.path.join(os.path.dirname("__file__"), 'data/dgm_provider/npht_animal_32dirs.h5')
raw_data_path = os.path.join(os.path.dirname("__file__"), 'data/raw_data/animal')

start = time.time()
# download_raw_data("animal")
generate_dgm_provider(raw_data_path, provider_path, 32)
end = time.time()
print(end - start)