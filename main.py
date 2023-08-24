import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont


class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermark App")
        self.image_path = ""

        # Create GUI components
        self.select_button = tk.Button(root, text="Select Image", command=self.load_image)
        self.watermark_entry = tk.Entry(root)
        self.watermark_button = tk.Button(root, text="Add Watermark", command=self.add_watermark)
        self.canvas = tk.Canvas(root)

        # Layout
        self.select_button.pack()
        self.watermark_entry.pack()
        self.watermark_button.pack()
        self.canvas.pack()

        # Disable the "Add Watermark" button initially
        self.watermark_button.config(state=tk.DISABLED)

        # Validate the entry whenever a character is typed
        self.watermark_entry.bind("<KeyRelease>", self.validate_input)

    def validate_input(self, event):
        if self.watermark_entry.get():
            self.watermark_button.config(state=tk.NORMAL)
        else:
            self.watermark_button.config(state=tk.DISABLED)

    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])
        if self.image_path:
            img = Image.open(self.image_path)
            img.thumbnail((400, 400))
            self.photo = ImageTk.PhotoImage(img)
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

    def add_watermark(self):
        if self.image_path:
            img = Image.open(self.image_path)

            # Get the watermark text from the Entry widget
            watermark_text = self.watermark_entry.get()
            font = ImageFont.load_default()
            draw = ImageDraw.Draw(img)
            draw.text((10, 10), watermark_text, fill=(255, 255, 255, 128), font=font)
            img.show()
            img.save("watermarked_image.jpg")


if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
