 
from PIL import Image, ImageDraw, ImageFont

def create_badge(winner_name):
    base = Image.open("badge_template.png")  # Use your badge design
    draw = ImageDraw.Draw(base)
    font = ImageFont.truetype("arial.ttf", 40)
    draw.text((200, 300), f"Winner: {winner_name}", font=font, fill="white")
    path = f"static/{winner_name}_badge.png"
    base.save(path)
    return path
