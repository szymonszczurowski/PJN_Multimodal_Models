### PJN_Multimodal_Models

## Zbiór danych
Zbiór danych używany w tym projekcie to zmieniona wersja zbioru ChartQA: [ChartQA](https://huggingface.co/datasets/HuggingFaceM4/ChartQA).

## Modele
Wytrenowane modele na wyżej wymienionym zbiorze danych:

- [**Moondream2**](https://huggingface.co/vikhyatk/moondream2)
- [**SmolVLM-Base**](https://huggingface.co/HuggingFaceTB/SmolVLM-Base)
- [**Qwen2-VL-2d-Instruct**](https://huggingface.co/Qwen/Qwen2-VL-2B-Instruct)

### Fine-tuning
Fine-tuning został przeprowadzony na jedną epokę na zbiorze treningowym (1200 próbek).

Finetuned modele dostępne są tutaj:

- [**PJN_moondream**](https://huggingface.co/krowiemlekommm/PJN_moondream)
    -  GPU: NVIDIA L4
    -  ![Train Loss](images/moon_dream_2_loss.png "Moondream Train Loss")

- [**SmolVLM**](https://huggingface.co/Szczurek/smolvlm).
    -  GPU: NVIDIA L4
    -  ![Train Loss](images/smolvlm_loss.png "SmolvVLM Train Loss")
 
- [**PJN_Qwen_2b**](https://huggingface.co/krowiemlekommm/PJN_qwen_2b)
    -  GPU: NVIDIA L4
    - ![Train Loss](images/train_loss_qwen2b.png "Qwen_2B Train Loss")

