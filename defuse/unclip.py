import torch
from diffusers import DiffusionPipeline, StableDiffusionDepth2ImgPipeline
from diffusers.utils import load_image
from PIL import Image

model_id = "stabilityai/stable-diffusion-2-depth"

pipe = StableDiffusionDepth2ImgPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.to("cuda")


def generate(prompt: str) -> Image:
    # get image
    url = "https://cdn.discordapp.com/attachments/874586602201055252/1098489535253459005/ElfBro_dnd_changeling_thief_rogue_hooded_figure_dark_and_broodi_5607ecbb-0f62-46fc-a09b-705976d5ee9b.png"
    image = load_image(url)
    n_propmt = "bad, deformed, ugly, bad anotomy"
    return pipe(prompt=prompt, image=image, strength=0.7).images[0]
