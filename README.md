# NERV - Neural Experiments & Real-world Validation
<p align="left">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&duration=3500&pause=500&color=00FF80&center=false&vCenter=false&width=520&lines=Titanic:+Predicts+Passenger+Survival;Iris:+Classifies+Species+from+4+Features;Oculus:+CNN+Across+10+CIFAR-10+Objects;Yapper:+NLP+Sentiment+Using+BiLSTM" alt="Typing SVG" />
</p>


NERV is an applied machine learning project that brings trained TensorFlow models into a practical, deployable workflow.  
This repository focuses on **using**, **integrating**, and **evaluating** models that were originally trained and validated in my dedicated TensorFlow learning repository.


---

## Model Lineage & Training Source

All core models used in this repository were trained in the following TensorFlow-focused repository:

🔗 **Training Repository (TensorFlow):**  
https://github.com/aypy01/tensorflow  

That repository documents:
- Data preprocessing
- Model architectures
- Training strategy
- Evaluation metrics
- Saved `.keras` checkpoints  

NERV consumes those trained models and applies them in a structured application context.

---

## Models Used in This Project

| Model File | Task | Dataset | Performance |
|------------|------|--------|-------------|
| `titanic.keras` | Binary Classification | Titanic Survival | ~81% Accuracy |
| `iris_species.keras` | Multiclass Classification | Iris Dataset | ~70% Accuracy |
| `cifar10.keras` (Oculus) | Image Classification | CIFAR-10 | ~72% Accuracy |
| `sentiments.keras` (Yapper) | Text Classification | IMDb Reviews | **85.80% Accuracy** |

> Model architecture, preprocessing, and training details are documented in the TensorFlow repo linked above.

---

## Project Components

> - **Titanic Survival Prediction**
> - **Iris Species Classification**
> - **Oculus (Computer Vision)**
> - **Yapper (NLP)**

These models demonstrate classical tabular ML workflows:
- Feature engineering
- Normalization
- Dense neural networks
- Proper train/test separation

---

### Oculus (Computer Vision)
- Uses the **CIFAR-10 CNN model**
- Focuses on image-based inference and integration
- Serves as the visual intelligence component of the system

---

### Yapper — Sentiment Analysis(NLP)
- Powered by `sentiments.keras`
- IMDb review classification
- Text vectorization + embedding-based neural network
- Designed for real-world text inference scenarios

---

## Tech Stack

- **TensorFlow / Keras**
- **Python 3**
- **Django** (application & integration layer)
- **HTML/CSS**
- **JavaScript**

---

## Attribution & Acknowledgements

This project would not exist without strong foundational learning resources.

- **TensorFlow & Google** — for the framework and tooling that made model training accessible and scalable  
- **CS50 (Harvard University)** — for instilling rigorous problem-solving and system-level thinking  
- **David J. Malan** — for teaching clarity, discipline, and respect for fundamentals in computer science
- brian yu CS50 Web
- google Colab
- ChatGpt
- Gemini

> Strong abstractions are built on strong fundamentals.  
> This repository is a direct outcome of learning things the *right* way.

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
