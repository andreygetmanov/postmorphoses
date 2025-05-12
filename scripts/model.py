from transformers import AutoTokenizer, AutoModelForCausalLM


class GPTModel:
    """
    Initializes and uses a pre-trained GPT model for text generation."""

    def __init__(self, model_path: str = "sberbank-ai/rugpt3medium_based_on_gpt2"):
        """
        Initializes the RuGPT3 model with a specified path.

            Args:
                model_path: The path to the pre-trained RuGPT3 model.
                    Defaults to 'sberbank-ai/rugpt3medium_based_on_gpt2'.

            Returns:
                None
        """
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForCausalLM.from_pretrained(model_path)

    def generate(
        self,
        text: str,
        max_new_tokens: int = 20,
        early_stopping: bool = True,
        do_sample: bool = True,
        temperature: float = 1.5,
    ):
        """
        Generates text based on a given prompt.

            Args:
                text: The input text to generate from.
                max_new_tokens: The maximum number of new tokens to generate. Defaults to 20.
                early_stopping: Whether to stop generation when the EOS token is reached. Defaults to True.
                do_sample: Whether to use sampling for generation. Defaults to True.
                temperature: The temperature value for sampling. Defaults to 1.5.

            Returns:
                str: The generated text.
        """
        input_ids = self.tokenizer.encode(text, return_tensors="pt")
        output = self.model.generate(
            input_ids,
            max_new_tokens=max_new_tokens,
            early_stopping=early_stopping,
            do_sample=do_sample,
            pad_token_id=self.model.config.eos_token_id,
            temperature=temperature,
        )
        return self.tokenizer.decode(output[0], skip_special_tokens=True)
