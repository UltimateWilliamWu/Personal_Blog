# Plant Leaf Disease Classification Using a Simplified 11-Layer Deep Neural Network

## Abstract

This paper presents a lightweight yet robust convolutional neural network (CNN) model for classifying plant leaf diseases using image data. The model is trained on a simplified version of the Mendeley Data dataset, where 39 original classes were consolidated into 16 for better generalization and reduced complexity. The proposed 11-layer CNN incorporates residual connections and attention modules and is trained using a combination of focal loss and label smoothing to address class imbalance and overconfidence. The model achieves over 96% validation accuracy while maintaining a compact architecture with ~1.18M parameters, making it well-suited for real-world agricultural applications.

**Keywords**: leaf disease, CNN, plant pathology, image classification, focal loss, label smoothing, deep learning

---

## I. Introduction

Leaf diseases significantly threaten global food security by reducing crop yield and quality. Traditional disease detection methods are labor-intensive, error-prone, and unsuitable for large-scale farming. With the rapid development of deep learning and computer vision, automated image-based plant disease classification systems have become viable alternatives.

This project introduces a custom-built 11-layer CNN optimized for classifying plant diseases. To enhance real-world usability, we simplified the dataset by merging visually similar diseases across crops. We also incorporated modern regularization strategies and loss functions to improve robustness and accuracy.

---

## II. Related Work

CNN-based classification models like AlexNet, VGGNet, and ResNet have been widely applied in plant disease detection. Mohanty et al. (2016) achieved >99% accuracy on PlantVillage using standard CNNs. Later research introduced attention mechanisms and transfer learning to improve interpretability and performance.

Nevertheless, many models overfit small, imbalanced datasets. Techniques such as focal loss (Lin et al., 2017), label smoothing (Müller et al., 2019), and class rebalancing have proven effective in addressing this issue. Our method integrates these improvements while simplifying class taxonomy for agricultural deployment.

---

## III. Methods

### 3.1 Model Architecture

We propose a custom 11-layer CNN designed to balance performance and efficiency. Key components include:

- **Residual Connections**: Mitigate vanishing gradients and enhance feature propagation.
- **Attention Modules**: Squeeze-and-Excitation blocks improve channel-wise focus.
- **Batch Normalization + Dropout**: Enhance convergence and reduce overfitting.
- **Adaptive Pooling**: Maintains fixed-size output for any input resolution.

The model contains ~1.18M parameters—small enough for fast training and low memory usage.

### 3.2 Loss Functions

To address class imbalance and model calibration, we employ:

- **Focal Loss**:
    

$$FocalLoss(pt)=−αt(1−pt)γ⋅log⁡(pt)\text{FocalLoss}(p_t) = -\alpha_t (1 - p_t)^\gamma \cdot \log(p_t)$$

Where γ=1.5, $\gamma$ = 1.5, $\alpha_t$ is the class-specific weight.

- **Label Smoothing Loss**:
    

Smoothed targets:

$$y~i=(1−ε)⋅yi+εK\tilde{y}_i = (1 - \varepsilon) \cdot y_i + \frac{\varepsilon}{K}$$

Loss:

$$Loss=−∑i=1Ky~i⋅log⁡(pi)\text{Loss} = -\sum_{i=1}^{K} \tilde{y}_i \cdot \log(p_i)$$

Both losses help address class imbalance and model overconfidence.

### 3.3 Dataset Simplification

The original dataset contains 39 classes with high imbalance. We manually grouped similar disease types into 16 plant-specific categories, e.g.,:

- Tomato: healthy vs. diseased  
- Apple: healthy vs. diseased  
- Background, orange disease, etc.

This not only reduces noise but also aligns with real-world decision-making scenarios.

---

## IV. Experiments

### 4.1 Dataset Description

We use the augmented Mendeley Data dataset (~54K images). After merging classes, the dataset is divided as follows:

| Split      | Samples | Proportion |
|------------|---------|------------|
| Training   | 43,058  | 70%        |
| Validation | 6,000   | 10%        |
| Testing    | 12,000  | 20%        |

Each image is labeled into one of the 16 consolidated categories.

### 4.2 Preprocessing and Augmentation

- Resize to 128×128 pixels  
- Color normalization  
- Training-only augmentations:
  - Random rotation, flip
  - Color jitter
  - Random erasing

### 4.3 Training Configuration

| Component     | Setting                      |
|---------------|------------------------------|
| Optimizer     | AdamW (lr = 1e-3)            |
| Weight Decay  | Weight Decay: 2 × 10⁻⁴       |
| Scheduler     | StepLR (γ = 0.7 every 5 epochs) |
| Epochs        | 15                           |
| Batch Size    | 64                           |
| Hardware      | CUDA (if available)          |

---

## V. Results

### 5.1 Quantitative Metrics

| Metric        | Value     |
|---------------|-----------|
| Best Val Acc  | **96.12%** |
| Final Val Acc | 95.87%    |
| Train Acc     | 99.10%    |
| Param/Sample  | ~27:1     |

The model achieves high accuracy with low overfitting, owing to the class merging, advanced loss functions, and data augmentation.

### 5.2 Comparison to Baselines

Compared to standard networks:

- **VGG11 / ResNet18**: ~11M parameters  
- **Ours**: ~1.18M parameters  
- **Training Speed**: 2–3× faster  
- **Memory Footprint**: significantly reduced  
- **Accuracy**: similar or better on the simplified dataset

---

## VI. Conclusion

### Strengths

- Lightweight and fast: ideal for edge deployment  
- Combined use of focal loss and label smoothing improves calibration  
- Residual and attention modules improve learning efficiency  
- Dataset restructuring enhances class balance and generalization  

### Limitations

- Manual class merging may lose semantic granularity  
- Slight performance drop on rare categories  
- Limited validation on real-world, in-field images

### Future Work

- Test on external datasets and field conditions  
- Add hierarchical classification (crop → disease type)  
- Incorporate explainability tools (e.g., Grad-CAM)  
- Optimize model for mobile devices (quantization, pruning)

---

## References

[1] Mohanty, S. P., Hughes, D. P., & Salathé, M. (2016). Using deep learning for image-based plant disease detection. *Frontiers in Plant Science*, 7, 251.  
[2] Lin, T. Y., et al. (2017). Focal loss for dense object detection. *ICCV*.  
[3] Müller, R., Kornblith, S., & Hinton, G. (2019). When does label smoothing help? *NeurIPS*, 32.  
[4] Ferentinos, K. P. (2018). Deep learning models for plant disease detection and diagnosis. *Computers and Electronics in Agriculture*, 145, 311–318.  
[5] Barbedo, J. G. A. (2019). Plant disease identification from individual lesions using deep learning. *Biosystems Engineering*, 180, 96–107.

