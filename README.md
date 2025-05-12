# postmorphoses

---

![License](https://img.shields.io/github/license/andreygetmanov/postmorphoses?style=flat&logo=opensourceinitiative&logoColor=white&color=blue)
[![OSA-improved](https://img.shields.io/badge/improved%20by-OSA-yellow)](https://github.com/aimclub/OSA)

Built with:

![aiohttp](https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style={0}&logo=AIOHTTP&logoColor=white)
![flask](https://img.shields.io/badge/Flask-000000.svg?style={0}&logo=Flask&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458.svg?style={0}&logo=pandas&logoColor=white)
![tensorflow](https://img.shields.io/badge/TensorFlow-FF6F00.svg?style={0}&logo=TensorFlow&logoColor=white)

---

## Overview

postmorphoses is an interactive art project exploring the relationship between nature, language, and artificial intelligence. It generates a continuously evolving 'manifesto' through user contributions and AI-driven text generation, inviting reflection on how we perceive and represent the natural world.

---

## Table of Contents

- [Core features](#core-features)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)
- [Citation](#citation)

---
## Core features

1. **Text Generation with RuGPT-3**: Utilizes the RuGPT-3 model to generate text based on input prompts, creating a continuous and evolving 'manifesto'.
2. **Interactive Input via Web Form**: Provides a web interface (using Flask) where users can submit their own text, influencing the generated output of the model.
3. **Data Source from Russian National Corpus**: Leverages data extracted from the Russian National Corpus to provide initial prompts and context for the text generation process, focusing on the theme of 'nature'.
4. **Persistence of Generated Text**: Stores and reads previously generated text from a file ('data/text_for_gen.txt'), allowing the model to build upon its previous outputs.

---

## Installation

Install postmorphoses using one of the following methods:

**Build from source:**

1. Clone the postmorphoses repository:
```sh
git clone https://github.com/andreygetmanov/postmorphoses
```

2. Navigate to the project directory:
```sh
cd postmorphoses
```

3. Install the project dependencies:

```sh
pip install -r requirements.txt
```

---

## Contributing

- **[Report Issues](https://github.com/andreygetmanov/postmorphoses/issues)**: Submit bugs found or log feature requests for the project.

---

## License

This project is protected under the GNU General Public License v3.0. For more details, refer to the [LICENSE](https://github.com/andreygetmanov/postmorphoses/tree/main/LICENSE) file.

---

## Citation

If you use this software, please cite it as below.

### APA format:

    andreygetmanov (2022). postmorphoses repository [Computer software]. https://github.com/andreygetmanov/postmorphoses

### BibTeX format:

    @misc{postmorphoses,

        author = {andreygetmanov},

        title = {postmorphoses repository},

        year = {2022},

        publisher = {github.com},

        journal = {github.com repository},

        howpublished = {\url{https://github.com/andreygetmanov/postmorphoses.git}},

        url = {https://github.com/andreygetmanov/postmorphoses.git}

    }

---
