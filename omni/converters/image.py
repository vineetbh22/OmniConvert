# omni/converters/image.py
from PIL import Image, ImageOps, ImageEnhance
import os
import logging
import time
from omni.utils.format_size import _format_size
from omni.utils.format_time import _format_time

logging.basicConfig(level=logging.INFO)

IMAGE_FORMATS = {"png", "jpg", "jpeg", "webp", "bmp", "tiff", "ico"}

def convert_image(input_file: str, output_file: str, options: dict = None):
    if options is None:
        options = {}

    start_time = time.time()
    
    try:
        with Image.open(input_file) as img:
            # 1. Smart Orientation (Fixes sideways photos)
            img = ImageOps.exif_transpose(img)

            # 2. Smart Transparency handling
            # If target is JPEG and image has transparency, composite onto white background
            output_ext = os.path.splitext(output_file)[1][1:].lower()
            if output_ext in ["jpg", "jpeg"] and img.mode in ("RGBA", "LA", "P"):
                background = Image.new("RGB", img.size, (255, 255, 255))
                if img.mode == "P":
                    img = img.convert("RGBA")
                background.paste(img, mask=img.split()[3] if img.mode == "RGBA" else None)
                img = background
            elif img.mode == "RGBA" and output_ext not in ["png", "webp"]:
                # Fallback for other formats that don't support alpha
                img = img.convert("RGB")

            # 3. Smart Enhancement
            if options.get("enhance"):
                # a. Auto-Contrast (Better range)
                img = ImageOps.autocontrast(img)
                # b. Sharpness Boost (1.5 is a nice subtle boost, 1.0 is original)
                enhancer = ImageEnhance.Sharpness(img)
                img = enhancer.enhance(1.5)
                # c. Color Balance (Subtle saturation boost)
                color_enhancer = ImageEnhance.Color(img)
                img = color_enhancer.enhance(1.1)

            # 4. Smart Resizing
            if options.get("resolution"):
                try:
                    res_parts = options["resolution"].lower().split("x")
                    if len(res_parts) == 2:
                        target_width = int(res_parts[0])
                        target_height = int(res_parts[1])
                        # Thumbnail maintains aspect ratio within the bounds
                        img.thumbnail((target_width, target_height), Image.Resampling.LANCZOS)
                except Exception as e:
                    logging.warning(f"⚠️ Could not resize: {e}")

            # 4. Saving with optimization
            save_kwargs = {}
            if output_ext in ["jpg", "jpeg"]:
                save_kwargs["quality"] = int(options.get("quality", 85))
                save_kwargs["optimize"] = True
            elif output_ext == "webp":
                save_kwargs["quality"] = int(options.get("quality", 80))
                save_kwargs["method"] = 6  # Slowest but best compression

            img.save(output_file, **save_kwargs)

        end_time = time.time()
        duration = end_time - start_time
        file_size_bytes = os.path.getsize(output_file)

        print(f"\n🎉 Image Conversion Complete!")
        print(f"📁 File: {output_file}")
        print(f"📦 Size: {_format_size(file_size_bytes)}")
        print(f"🖼️ Dimensions: {img.width}x{img.height}")
        print(f"⏳ Time Taken: {_format_time(duration)}")

        return True

    except Exception as e:
        logging.error(f"❌ Image conversion failed: {e}")
        raise e
