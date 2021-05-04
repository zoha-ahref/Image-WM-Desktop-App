from tkinter import *
import tkinter.filedialog as tk_fd
from PIL import Image, ImageTk, ImageDraw, ImageFont

image_path = ""
img_in = Image
logo_path = ""
final_img = Image

def open_image():
    global img_in, image_path

    image_path = tk_fd.askopenfilename()

    img_in = Image.open(image_path)
    render_user_img = ImageTk.PhotoImage(img_in.resize((500, 500), Image.ANTIALIAS))

    panel = Label(window, image=render_user_img)
    panel.image = render_user_img
    panel.grid(column=0, row=1)


def add_text():
    global image_path, final_img
    final_img = Image.open(image_path)
    watermark_text = text_input.get()
    drawing = ImageDraw.Draw(final_img)
    black_text = (3,8,12,128)
    font = ImageFont.truetype("arial.ttf", 25)
    drawing.text((20,20), watermark_text, fill=black_text, font=font)
    # photo.save(final_image_path)
    img = ImageTk.PhotoImage(final_img.resize((500,500), Image.ANTIALIAS))
    panel = Label(window, image=img)
    panel.image = img
    panel.grid(column=1, row=1)

def add_logo():
    global image_path, logo_path, final_img

    photo = Image.open(image_path)
    logo_path = tk_fd.askopenfilename()
    watermark_logo = Image.open(logo_path)
    # render_user_logo = ImageTk.PhotoImage()

    width, height = photo.size
    final_img = Image.new('RGBA', (width, height), (0,0,0,0))
    final_img.paste(photo, (0,0))
    final_img.paste(watermark_logo, (10,10), mask=watermark_logo)
    # trans_back_img.save(final_image_path)
    img = ImageTk.PhotoImage(final_img)
    panel = Label(window, image=img)
    panel.image = img
    panel.grid(column=1, row=1)

def save_image():
    global final_img, image_path
    image_name = image_path.split('/')[-1].split(".")[0] + "wm"

    final_img.save(f"/Users/zohakaukab/Desktop/{image_name}.png")



window = Tk(screenName="Image Watermarking")
window.title("Image Watermarking App")
window.config(bg="#a4ebf3")

window.geometry("1008x650")
window.maxsize(1008, 650)

text_input = Entry(width=50)
text_input.insert(0, "Text Watermark")
text_input.grid(column=0, row=0, columnspan= 2, pady=15)

# button_open_logo = Button(text="Select Logo", command=open_image)
# button_open_logo.grid(column=1, row=0)

Canvas(bg="#ccf2f4", width=500, height=500).grid(column=0, row=1)

Canvas(bg="#ccf2f4", width=500, height=500).grid(column=1, row=1)

select_image_button = Button(text="Select an image", command=open_image,highlightthickness=0)
select_image_button.grid(column=0, row=2, pady=10)

f1 = Frame(window, bg="#a4ebf3")
f1.grid(column=1, row=2, sticky="nsew")
f1.config()
apply_button_tw = Button(f1, text="Apply Text Watermark",command=add_text, highlightthickness=0)
# apply_button_tw.grid(column=1, row=2, pady=10)
apply_button_tw.pack(side="left", padx=40, pady=10)

apply_button_iw = Button(f1, text="Apply Image Watermark",command = add_logo, highlightthickness=0)
# apply_button_iw.grid(column=2, row=2, pady=10)
apply_button_iw.pack(side="left", padx=40, pady=10)

save_img_button = Button(text="Save Image", command=save_image, highlightthickness=0)
save_img_button.grid(column=0, row=3, columnspan=2, pady=15)

window.mainloop()