from transformers import AutoTokenizer, AutoModelForCausalLM


class GPTModel:

    def __init__(self, model_path: str = 'sberbank-ai/rugpt3medium_based_on_gpt2'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForCausalLM.from_pretrained(model_path)

    def generate(self, text: str,
                 max_new_tokens: int = 20,
                 early_stopping: bool = True,
                 do_sample: bool = True,
                 temperature: float = 1.5):
        input_ids = self.tokenizer.encode(text, return_tensors='pt')
        output = self.model.generate(input_ids,
                                     max_new_tokens=max_new_tokens,
                                     early_stopping=early_stopping,
                                     do_sample=do_sample,
                                     pad_token_id=self.model.config.eos_token_id,
                                     temperature=temperature)
        return self.tokenizer.decode(output[0], skip_special_tokens=True)