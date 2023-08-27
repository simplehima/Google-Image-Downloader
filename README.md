# Image Downloader using Selenium and Requests

This Python script uses Selenium and Requests to download images from Google Images based on different categories. It automates the process of searching for images and downloading them to your local machine.

## Requirements

Make sure you have Python installed on your machine. You will also need the following Python packages:

- selenium
- requests
- ChromeDriver 

You can install these packages using the following command:


```bash
git clone https://github.com/simplehima/Google-Image-Downloader.git
```

```bash
pip install -r requirements.txt
```

## Setup

1- Clone this repository to your local machine or download the script directly.

2- Install the required Python packages using the provided requirements.txt file.

3- Download the appropriate ChromeDriver executable for your system and place it in the root directory of the project. Make sure the ChromeDriver version matches your Chrome browser version (`windows x64 is included`).

3.1- Download for Windows from here [here](https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/win64/chrome-win64.zip) and extrat it to the root of this project 'chrome-win64' 

4- Open the script (image_downloader.py) in a text editor.

5- Modify the chromedriver_path and chromepath variables in the script to match the paths of the ChromeDriver executable and Chrome browser on your machine.

6- Customize the categories list to include the categories you want to download images for.

7- Run the script using the following command:

```bash
python image_downloader.py
```

The script will automatically search for images for each category, scroll to load more images, and download them to a directory named image_download.

## License
MIT License

Copyright (c) [2023] [@simplehima]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


## Notes
The script may need adjustments over time if the structure of the Google Images page changes.

Use this script responsibly and respect copyright and usage rights of the downloaded images.

This script works based on the current state of the web as of my last update. If any changes occur in the future, the script might need to be modified accordingly.

Happy image downloading!
