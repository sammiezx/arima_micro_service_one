# from PIL import Image
# import torch
# from torch import autocast
# from diffusers import StableDiffusionPipeline 

# # Define the prompt
# prompt = "A beautiful landscape with mountains and a lake"

# # Set up the StableDiffusionPipeline
# model_id = "CompVis/stable-diffusion-v1-4"
# device = torch.device("cpu")
# pipe = StableDiffusionPipeline.from_pretrained(model_id, revision="fp16", torch_dtype=torch.float32, use_auth_token="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") 
# pipe.to(device) 

# # Generate the image
# with autocast(device_type='cpu'):
#     image = pipe(prompt, guidance_scale=8.5).images[0]

# # Save the image as a file
# image.save("generated_image.png")

# print("Image saved successfully!")
