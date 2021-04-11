import sentencepiece as spm
import io

model = io.BytesIO()
spm.SentencePieceTrainer.train(input='corpus.txt', model_prefix='m', vocab_size=10000, model_type="bpe", model_writer=model)

with open('out.model', 'wb') as f:
    f.write(model.getvalue())
