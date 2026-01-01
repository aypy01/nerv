# NERV - Neural Experiments & Real-world Validation

![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?logo=tensorflow&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)

### WEBSITE:

[![NERV Website](https://img.shields.io/badge/NERV_WEBSITE-CLICK_HERE-FF8C00?style=flat-square&logo=tensorflow&logoColor=FFFFFF&labelColor=000000)](https://web-production-6533e.up.railway.app/nerv/)
 <br>
### DOCUMENTATION:

[![Documentation](https://img.shields.io/badge/DOCUMENTATION-CLICK_HERE-FF8C00?style=flat-square&logo=readthedocs&logoColor=FFFFFF&labelColor=000000)](https://aypy01.github.io/docs/nerv/nerv.html)
 
---
<br>

![NERV Banner](NERV.png)

---
 <br>


NERV is an **educational, applied machine learning project** that demonstrates how trained ML models move from experimentation into **structured, real-world applications**.

It focuses on the *often-skipped middle layer* of ML learning:
> bridging model training → validation → deployment → inference.

This repository is not about chasing accuracy benchmarks.  
It is about **using trained intelligence correctly**.

---

## What NERV Is (and Is Not)

**NERV is:**
- A learning-oriented ML system
- A reference for applying trained TensorFlow models
- A practical example of ML + web integration
- A documented pipeline from training artifacts to inference

**NERV is NOT:**
- A production ML framework
- An AutoML tool
- A plug-and-play library

If you are learning how ML systems *actually live beyond notebooks*, this project is for you.

---

## Project Architecture (High Level)

NERV is intentionally split into two layers:

### 1. Training & Experimentation
All model training, preprocessing, and evaluation live here:

🔗 **Training Repository (TensorFlow-focused)**  
https://github.com/aypy01/tensorflow

This includes:
- Data preprocessing
- Model architectures
- Training strategies
- Evaluation metrics
- Saved `.keras` checkpoints

### 2. Application & Inference (This Repository)
NERV consumes those trained models and:
- Loads them as versioned artifacts
- Integrates them into a Django application
- Runs controlled inference
- Demonstrates real-world usage patterns

This separation mirrors how ML systems are structured in practice.

---

## Models Included

| Model | Task | Dataset | Accuracy |
|------|-----|--------|----------|
| `titanic.keras` | Binary classification | Titanic Survival | ~81% |
| `iris_species.keras` | Multiclass classification | Iris Dataset | ~70% |
| `cifar10.keras` (Oculus) | Image classification | CIFAR-10 | ~72% |
| `sentiments.keras` (Yapper) | Text classification | IMDb Reviews | **85.80%** |

📁 Model files are stored in:  
https://github.com/aypy01/nerv/tree/main/nerv/models
<br>
> Models are intentionally consumed through code, not as standalone downloads.


---

## Components Overview

- **Titanic Survival Prediction**  
  Classical tabular ML workflow with feature engineering.

- **Iris Species Classification**  
  Multiclass classification using dense networks.

- **Oculus (Computer Vision)**  
  CNN-based image classification on CIFAR-10.

- **Yapper (NLP)**  
  Sentiment analysis using embeddings and BiLSTM.

Each component demonstrates a different ML modality while following the same deployment discipline.

---

## Documentation

**Full Project Documentation:**  
https://aypy01.github.io/docs/nerv/nerv.html

The documentation explains:
- End-to-end training → inference flow
- Model design choices
- Integration decisions
- Common ML mistakes avoided

Think of the docs as a guided walkthrough, not just reference material.

---

## Tech Stack

- TensorFlow / Keras  
- Python 3  
- Django  
- HTML / CSS  
- JavaScript  

---


## Credits & Acknowledgements
- **Kiran Jain**  - My primary school homeroom teacher, whose early trust and encouragement shaped my confidence in learning and building.
- [David J. Malan](https://github.com/dmalan)   CS50 instructor
- [Brian Yu](https://github.com/brianyu28)   CS50 Web
- [TensorFlow](https://github.com/tensorflow/tensorflow)   Model training & inference
- [Django](https://github.com/django/django)   Backend & web integration
- [CS50](https://cs50.harvard.edu/)   Computer science foundations
- [scikit-learn](https://github.com/scikit-learn/scikit-learn)   Classical ML utilities
- [Google Colab](https://colab.research.google.com/)   Experimentation & prototyping
- ChatGPT   Debugging, documentation



---

## Note:

NERV is not about experimenting blindly.  
It is about **applying trained intelligence correctly**.

Models are treated as:
- Versioned artifacts
- Measurable components
- Replaceable, improvable systems

Training is iterative.  
Deployment is deliberate.

---

## Author
 <p align="left">
  Created and maintained by &nbsp;
  <a href="https://github.com/aypy01" target="_blank">
  <img src="https://img.shields.io/badge/Aaditya_Yadav-aypy01-e6770b?style=flat-square&logo=github&logoColor=00FF80&labelColor=765898" alt="GitHub Badge"/>
</a>
</p>
<p>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&duration=3000&pause=500&color=00FF80&background=765898&center=false&vCenter=false&width=440&lines=Break+Things+First%2C+Understand+Later;Built+to+Debug%2C+Not+Repeat;Learning+What+Actually+Sticks;Code.+Observe.+Refine." alt="Typing SVG" />
</p>

---

## License

This project is licensed under the [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT).
---
