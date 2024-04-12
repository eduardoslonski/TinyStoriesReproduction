# TinyStories Reproduction

Reproducing the Microsoft paper [TinyStories](https://arxiv.org/pdf/2305.07759.pdf) from scratch.

The primary contribution of the TinyStories paper is demonstrating that even small models can master coherent English and perform reasoning tasks.

### Model
- It is a GPT model with a modification from the original paper, using RoPE for positional information.
- All the code for the model was written from scratch, facilitating experiments on model architecture and performance.
- One improvement I implemented was modifying the tokenizer to reduce the embedding and unembedding sizes. This adjustment speeds up the training process and makes the model lighter without affecting performance.

### Training
- Initiate training with `python train/train.py`.
- The configuration files for both the model and training are located at [train/config.py](train/config.py).
- Monitor the training run and adjust its configuration using [Weights & Biases](https://wandb.ai/) at [train/trainer.py](train/trainer.py).
- Checkpoints are saved by setting a value for `checkpoint_every` in the configuration file.
- The trainer is compatible with any binary data file in `uint16` format with stacked samples.

### Data
- The original TinyStories dataset is available [here](https://huggingface.co/datasets/roneneldan/TinyStories).
- This reproduction includes data processing jobs in the [data_processing](/data_processing) folder.
- Download the processed and tokenized data directly from S3 using `python utils/download_data.py --object train.bin --file_path data/train.bin`, and similarly for `valid.bin`.
- `train.bin` consists of approximately 500 million tokens, and `valid.bin` contains 5 million (1%).
- The data was tokenized using the same tokenizer employed in the paper (GPT-Neo).

### Results
- The trained models replicate the losses reported in the paper. For instance, the final loss for a model with 512 hidden size and 8 layers is around 1.2, matching the reported loss for a model of the same size in the paper.
- The training process is stable, and the loss decreases as expected.

<img width="1426" alt="training_loss_tinystories" src="https://github.com/eduardoslonski/TinyStoriesReproduction/assets/121900778/88c785a2-97ae-4e62-b316-dbac198d67a9">


- Models demonstrate no further performance improvement beyond 80M parameters on the TinyStories dataset, highlighting the simplicity and limitations of the data.
- The generation capabilities also mirror those described in the paper and are equally impressive. For example, this completion from an 8M model for the prompt:

"Once upon a time there was a boy named Tim"

```Once upon a time there was a boy named Tim. Tim had a toy car that he loved to play with. One day, Tim's mom told him to clean his room. She said, "Tim, you need to clean your room." Tim did not want to clean his room. He wanted to play with his toys. So, he started to clean his room. He put his toys in the right place. He was very happy. But then, something unexpected happened. The toys started to talk! It said, "Thank you for cleaning me, Tim. I am a magic toy car. I will give you a wish." Tim was very surprised. He wished for a big, yummy cake to eat. Tim was very happy. He learned that sometimes, things are not what they seem. He learned that it is good to be kind and help others. And that is the moral of the story.<|endoftext|>```

Even models with significantly larger capacities, such as those with 100M parameters, trained on general data, do not achieve this level of coherence.
