# Nazo Manga Maker (謎漫画メーカー)

[日本語](#日本語) | [English](#english)
<br><br>

# 日本語

# 概要

このプログラムは、指定したフォルダ内の画像ファイルからランダムに画像を選び、グリッド状の画像を作成します。出力画像の数、名前、フォーマット、品質、クロップ方式、グリッドサイズなどを設定できます。
<br><br>

# 遊び方

1. Stable Diffusion WebUI Automatic1111 等を使用して漫画のコマ風の画像を多数生成します。
2. 本プログラムを使用してランダムに画像をグリッド状に配置します。
3. 意味がよく分からない謎の漫画が出来上がります。
4. すごく楽しい！
   <br><br>

# 使い方

1. `inputs` フォルダに任意の画像ファイル (`png`、`jpg`、`jpeg`、`webp`、`bmp`、`gif`) を配置します。
2. プログラムを実行します。

   - Windows

     `nazo-manga-maker.bat` をダブルクリックします。

   - Linux, Mac 及び Windows のコマンドライン

     ```
     python nmm.py
     ```

3. `outputs` フォルダに画像が保存されます。
   <br><br>

# コマンドライン引数を指定する場合

- 以下の様に指定が可能です。

  ```
  python nmm.py [output_count] [output_name] [output_format] [quality] [crop_type] [grid_type]
  ```

- 使用例

  ```
  python nmm.py 3 output jpg 85 top-left 2x3
  ```

- 引数の説明
  - `output_count`: 生成する画像の数 (デフォルト: 3)
  - `output_name`: 出力ファイル名の一部 (デフォルト: 'output') (例:20240607-103250-output-00001.jpg)
  - `output_format`: 出力ファイルのフォーマット ('png', 'jpg', 'jpeg', 'webp', 'bmp', 'gif') (デフォルト: 'jpg')
  - `quality`: 出力ファイルの品質 (`jpg`および`webp`の場合) (0-100) (デフォルト: 85)
  - `crop_type`: 画像が正方形でない場合のクロップ方式 ('none', 'center', 'top-left', 'bottom-right', 'random') (デフォルト: 'top-left')
  - `grid_type`: '1x4' '2x2', '2x3', '2x4' (デフォルト: '2x3')
    <br><br>

# 動作環境

- Python3

- PIL

  PIL のインストール有無を確認する方法

  ```
  pip show Pillow
  ```

  PIL がない場合はインストールします。

  ```
  pip install Pillow
  ```

  <br>

# 設定

プログラムの設定は `--- config start ---` と `--- config end ---` の間で行います。

```python
# --- config start ---
input_folder = 'inputs'
output_folder = 'outputs'
input_extensions = ('png', 'jpg', 'jpeg', 'webp', 'bmp', 'gif')
output_count = 3
output_name = 'output'
output_format = 'jpg'
quality = 85
crop_type = 'top-left'
grid_type = '2x3'
# --- config end ---
```

- `input_folder`: 入力画像ファイルを格納するフォルダ
- `output_folder`: 出力画像ファイルを保存するフォルダ
- `input_extensions`: 入力画像ファイルの拡張子 (指定した拡張子が選択対象となります) サポート拡張子 ('png', 'jpg', 'jpeg', 'webp', 'bmp', 'gif') (大文字可)
- `output_count`: 生成する画像の数 (デフォルト: 3)
- `output_name`: 出力ファイル名の一部 (例:20240607-103250-output-00001.jpg)
- `output_format`: 出力ファイルのフォーマット ('png', 'jpg', 'jpeg', 'webp', 'bmp', 'gif') (デフォルト: 'jpg')
- `quality`: 出力ファイルの品質 (0-100) (デフォルト: 85)
- `crop_type`: 画像が正方形でない場合のクロップ方式 ('none', 'center', 'top-left', 'bottom-right', 'random') (デフォルト: 'top-left')
- `grid_type`: 画像の配置方法 ('1x4' '2x2', '2x3', '2x4') (デフォルト: '2x3')
  <br><br>

# クロップタイプ（画像の切り取り方法）

入力画像が正方形以外の場合は自動的に整形・クロップを行います。デフォルト値は'top-left'です。<br>
一コマのサイズは 512x512 です。入力画像が 512x512 未満の場合は 512x512 に引き伸ばされるため画質が劣化します。

- `none`: 入力画像のアスペクト比を無視して正方形に整形します。画像が変形するため非推奨。
- `center`: 中央を基準に正方形に切り取ります。
- `top-left`: 縦長画像の場合は上を基準に切り取ります。横長画像の場合は左を基準に切り取ります。
- `bottom-right`: 縦長画像の場合は下を基準に切り取ります。横長画像の場合は右を基準に切り取ります。
- `random`: 任意の位置を基準に切り取ります。
  <br><br>

# グリッドタイプ（画像の配置方法）

縦横の画像配置方法を設定できます。デフォルト値は'2x3'です。

- `1x4`: 横 1 コマ縦 4 コマ 512x2048 (いわゆる 4 コマ漫画)
- `2x2`: 横 2 コマ縦 2 コマ 1024x1024
- `2x3`: 横 2 コマ縦 3 コマ 1024x1536
- `2x4`: 横 2 コマ縦 4 コマ 1024x2048
  <br><br>

# 補足

- 推奨画像は 512x512 以上の正方形です。1024x1024 はもちろん OK です。
- 入力フォルダに必要な画像数が不足している場合、白い画像で補完します。
- 指定されたフォーマットやクロップタイプ、グリッドタイプが無効な場合、デフォルト値が使用されます。
  <br><br>

# 変更履歴

## [0.1.0] - 2024-06-07

### 追加

- 初回リリース
  <br><br>

# ライセンス

Copyright © 2024 Takenoko  
Released under the [MIT License](https://opensource.org/licenses/mit-license.php).
<br><br><br>

# English

# Overview

This program randomly selects images from a specified folder and creates a grid of images. You can configure the number of output images, their names, formats, quality, crop type, and grid type.

<br><br>

# How to Play

1. Use Stable Diffusion WebUI Automatic1111 or similar to generate many comic strip-style images.
2. Use this program to randomly arrange the images into a grid.
3. You'll get a mysterious and often nonsensical comic strip.
4. It's a lot of fun!

<br><br>

# Usage

1. Place the desired image files (`png`, `jpg`, `jpeg`, `webp`, `bmp`, `gif`) in the `inputs` folder.
2. Run the program.

   - On Windows

     Double-click `nazo-manga-maker.bat`.

   - On Linux, Mac, and Windows command line

     ```
     python nmm.py
     ```

3. The images will be saved in the `outputs` folder.

<br><br>

# Specifying Command Line Arguments

- You can specify arguments as follows:

  ```
  python nmm.py [output_count] [output_name] [output_format] [quality] [crop_type] [grid_type]
  ```

- Example:

  ```
  python nmm.py 3 output jpg 85 top-left 2x3
  ```

- Argument descriptions:
  - `output_count`: Number of images to generate (default: 3)
  - `output_name`: Part of the output file name (default: 'output') (e.g., 20240607-103250-output-00001.jpg)
  - `output_format`: Output file format ('png', 'jpg', 'jpeg', 'webp', 'bmp', 'gif') (default: 'jpg')
  - `quality`: Quality of the output file (for `jpg` and `webp`) (0-100) (default: 85)
  - `crop_type`: Crop type if the image is not square ('none', 'center', 'top-left', 'bottom-right', 'random') (default: 'top-left')
  - `grid_type`: '1x4', '2x2', '2x3', '2x4' (default: '2x3')

<br><br>

# Requirements

- Python3

- PIL

  To check if PIL is installed:

  ```
  pip show Pillow
  ```

  If PIL is not installed, install it using:

  ```
  pip install Pillow
  ```

<br>

# Configuration

The program's settings can be configured between `--- config start ---` and `--- config end ---`.

```python
# --- config start ---
input_folder = 'inputs'
output_folder = 'outputs'
input_extensions = ('png', 'jpg', 'jpeg', 'webp', 'bmp', 'gif')
output_count = 3
output_name = 'output'
output_format = 'jpg'
quality = 85
crop_type = 'top-left'
grid_type = '2x3'
# --- config end ---
```

- `input_folder`: Folder containing input image files
- `output_folder`: Folder to save output image files
- `input_extensions`: Extensions of input image files (specified extensions will be selected) Supported extensions ('png', 'jpg', 'jpeg', 'webp', 'bmp', 'gif') (case-insensitive)
- `output_count`: Number of images to generate (default: 3)
- `output_name`: Part of the output file name (e.g., 20240607-103250-output-00001.jpg)
- `output_format`: Output file format ('png', 'jpg', 'jpeg', 'webp', 'bmp', 'gif') (default: 'jpg')
- `quality`: Quality of the output file (0-100) (default: 85)
- `crop_type`: Crop type if the image is not square ('none', 'center', 'top-left', 'bottom-right', 'random') (default: 'top-left')
- `grid_type`: Image arrangement ('1x4', '2x2', '2x3', '2x4') (default: '2x3')

<br><br>

# Crop Types

If the input image is not square, it will be automatically cropped. The default value is 'top-left'.<br>
Each panel size is 512x512. If the input image is smaller than 512x512, it will be stretched to 512x512, resulting in reduced image quality.

- `none`: Ignores the aspect ratio of the input image and reshapes it to a square. Not recommended as it distorts the image.
- `center`: Crops to a square from the center.
- `top-left`: Crops from the top if the image is vertical, and from the left if horizontal.
- `bottom-right`: Crops from the bottom if the image is vertical, and from the right if horizontal.
- `random`: Crops from a random position.

<br><br>

# Grid Types

You can set the vertical and horizontal arrangement of the images. The default value is '2x3'.

- `1x4`: 1 panel horizontally and 4 panels vertically, 512x2048 (e.g., 4-panel comic strip)
- `2x2`: 2 panels horizontally and 2 panels vertically, 1024x1024
- `2x3`: 2 panels horizontally and 3 panels vertically, 1024x1536
- `2x4`: 2 panels horizontally and 4 panels vertically, 1024x2048

<br><br>

# Additional Notes

- Recommended images are at least 512x512 square; 1024x1024 is of course acceptable.
- If the required number of images is insufficient in the input folder, white images will be used as placeholders.
- If the specified format, crop type, or grid type is invalid, the default values will be used.

<br><br>

# Change Log

## [0.1.0] - 2024-06-07

### Added

- Initial release

<br><br>

# License

Copyright © 2024 Takenoko  
Released under the [MIT License](https://opensource.org/licenses/mit-license.php).
