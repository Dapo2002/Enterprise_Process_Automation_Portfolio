 📸 Image Manipulation & Automation

A collection of Python scripts developed using the Pillow (PIL) library to automate image processing, searching, and document generation. These projects are part of a systematic journey to master file-system automation and computer vision basics.

---

 🛠️ Project Suite

 1. Identifying Photo Folders (`identifyingPhotoFoldersOnTheHardDrive.py`)
The Problem: Digital camera transfers often get lost in deep subdirectories.
The Solution: Scans the entire hard drive (or a specified path) to find "Photo Folders."
 Logic: Identifies a folder as a "Photo Folder" if more than 50% of the files are images (`.png`, `.jpg`) with dimensions greater than 500x500 pixels.
 Robustness: Handles system-level errors like `DecompressionBombError` and `PermissionError` during deep scans.

 2. Custom Seating Cards (`customSeatingCards.py`)
The Problem: Manually creating name cards for events is tedious.
The Solution: Reads names from `guests.txt` and generates a 4×5 inch (288×360 px) printable seating card for each.
 Features:
     Adds a black cutting guide border for physical printing.
     Pastes a decorative flower element on a red background.
     Uses Center-Middle (mm) anchoring to perfectly align guest names regardless of length.

 3. Smart Logo Watermarking (`extendingAndFixingTheResizeAndAddLogoProgram.py`)
The Problem: Small images look cluttered if a large logo is pasted on them.
The Solution: An enhanced version of the "Resize and Add Logo" program.
 Smart Scaling: The logo is only added if the target image is at least twice the width and height of the logo.
 Compatibility: Process images in a case-insensitive manner for `.jpg`, `.png`, `.gif`, and `.bmp`.

 4. Batch Resize and Logo (`resizeAndAddLogo.py`)
The Problem: Preparing images for web galleries requires uniform sizing.
The Solution: Resizes all images in a directory to fit within a 300x300 pixel square while maintaining the original aspect ratio.
 Automation: Automatically creates a `withLogo` output folder and batch-processes the entire working directory.

---

 🚀 Technical Concepts Mastered
 OS Module: Walking directory trees (`os.walk`), path joining, and directory creation.
 Pillow Library: Image resizing, coordinate geometry, transparency masks (RGBA), and text drawing with TrueType fonts.
 Error Handling: Implementing `try/except` blocks to prevent script crashes on corrupted or restricted system files.
 Logic Filters: Using counting variables (`numPhotoFiles`) to categorize data based on specific metadata criteria.

 📖 Setup
1. Install requirements: `pip install Pillow`
2. Ensure assets like `catlogo.png`, `flower.png`, and `guests.txt` are in the project folder.
3. Run the scripts via terminal: `python customSeatingCards.py`

---
Developed as part of the My_Python_for_Automation_Journey.