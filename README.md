# ENIGMA-360: A Multi-view Dataset for Human Behavior Understanding in Industrial Scenarios

<!-- start badges -->
[![arXiv-Enigma-51](https://img.shields.io/badge/arXiv-ENIGMA51-red.svg)](https://arxiv.org/abs/2309.14809)
[![arXiv-Enigma-360](https://img.shields.io/badge/arXiv-ENIGMA360-red.svg)](https://arxiv.org/abs/2309.14809)
<!-- end badges -->

## 📌 Project Overview

> [ENIGMA-360](https://iplab.dmi.unict.it/ENIGMA-360/) is a novel multi-view dataset captured in a real industrial laboratory, consisting of 180 egocentric and 180 exocentric videos.


<video src="assets/teaser.mp4" controls>
</video>

## Downloading the Dataset

We provide a Python downloader script to easily fetch the dataset components you need. 

*Note: The script requires the presence of an `annotations/` folder containing the split files (`train.txt`, `val.txt`, `test.txt`) with the video IDs to download.*

### Usage

Run the script specifying the desired mode, splits, and camera views:

```bash
python downloader.py --mode <MODE> [--splits <SPLIT1> <SPLIT2>] [--view <VIEW>]
```

### Arguments

| Argument | Description | Choices | Default |
| --- | --- | --- | --- |
| `--mode` | **(Required)** The type of data to download. | `videos`, `frames`, `masks`, `features`, `hoi` | - |
| `--splits` | The dataset splits to download. | `train`, `val`, `test` | `train` |
| `--view` | The camera perspective. | `ego`, `exo`, `both` | `both` |


### Examples

**1. Download raw videos for both train and validation splits (both views):**

```bash
python downloader.py --mode videos --splits train val --view both
```

**2. Download DINOv2 features for the test split (egocentric view only):**

```bash
python downloader.py --mode features --splits test --view ego
```

**3. Download HOI (Human-Object Interaction) frames:**

```bash
python downloader.py --mode hoi
```

## Tasks

### Egocentric Human-Object Interaction detection

The annotations for this task are located in the `annotations/hoi` directory. The format follows the standard of HOS introduced in the [VISOR-HOS GitHub repository](https://github.com/epic-kitchens/VISOR-HOS?tab=readme-ov-file). Please refer to that link for more information on how the annotations are structured.

> To use these annotations, you must first download the corresponding frames using the downloader script provided below with the `--mode hoi` flag.

## 📝 Citing
If you use our **ENIGMA-360** dataset for your research, please cite our paper:
```
Cooming soon! 
```

Additionally, consider citing the original paper:

```
@inproceedings{ragusa2024enigma,
  title={ENIGMA-51: Towards a Fine-Grained Understanding of Human Behavior in Industrial Scenarios},
  author={Ragusa, Francesco and Leonardi, Rosario and Mazzamuto, Michele and Bonanno, Claudia and Scavo, Rosario and Furnari, Antonino and Farinella, Giovanni Maria},
  booktitle={Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision},
  pages={4549--4559},
  year={2024}
}

```


## 🎓 Acknowledgments

This research is supported by [Next Vision](https://www.nextvisionlab.it/) srl, by MISE - PON I&C 2014-2020 - Progetto ENIGMA  - CUP: B61B19000520008, and by the project FAIR – PNRR MUR Cod. PE0000013 - CUP: E63C22001940006.